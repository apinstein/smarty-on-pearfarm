#!/bin/sh
export SMARTY_VERSION=$1
if [ -z $SMARTY_VERSION ]; then
    echo "Usage: build.sh X.Y.ZZZ\n You must pass in the desired smarty version."
    exit 1
fi
echo "Publishing Smarty version ${SMARTY_VERSION} to pearfarm..."
dlfile="Smarty-${SMARTY_VERSION}-source.tgz"
dlurl="http://www.smarty.net/do_download.php?download_file=Smarty-${SMARTY_VERSION}.tar.gz"
[ -f $dlfile ] || curl -q -L -o $dlfile $dlurl
if [ ! -f $dlfile ]; then
    echo "Couldn't download file $dlurl"
    exit 1;
fi
rm -rf "smarty-to-package"
mkdir -p smarty-to-package
tar -zxf $dlfile -C smarty-to-package --wildcards "Smarty-*/libs/*"
cp pearfarm.spec "smarty-to-package/Smarty-${SMARTY_VERSION}/libs"
pushd "smarty-to-package/Smarty-${SMARTY_VERSION}/libs"
pearfarm build
pearfarm push
popd
