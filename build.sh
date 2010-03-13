#!/bin/sh
export SMARTY_VERSION=$1
echo "Publishing Smarty version ${SMARTY_VERSION} to pearfarm..."
dlfile="Smarty-${SMARTY_VERSION}.tgz"
dlurl="http://www.smarty.net/do_download.php?download_file=Smarty-${SMARTY_VERSION}.tar.gz"
[ -f $dlfile ] || curl -q -L -o $dlfile $dlurl
if [ ! -f $dlfile ]; then
    echo "Couldn't download file $dlurl"
    exit 1;
fi
mkdir -p smarty-to-package
tar -zxf $dlfile -C smarty-to-package --wildcards "Smarty-*/libs/*"
pearfarm build
