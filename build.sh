#!/bin/sh
version=$1
echo "Publishing Smarty version ${version} to pearfarm..."
dlfile="Smarty-${version}.tgz"
dlurl="http://www.smarty.net/do_download.php?download_file=Smarty-${version}.tar.gz"
[ -f $dlfile ] || curl -v -L -o $dlfile $dlurl
if [ ! -f $dlfile ]; then
    echo "Couldn't download file $dlurl"
    exit 1;
fi
mkdir -p smarty-to-package
tar -zxf $dlfile -C smarty-to-package --wildcards "Smarty-*/libs/*"

