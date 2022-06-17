#!/bin/sh

if [ $# -ne 1 ]; then
    echo "./build.sh version"
    ./gen.py
    exit 1
fi

rm -rf ClickHouse.docset ClickHouse.tgz

cp -r ClickHouse.docset-tmpl/ ClickHouse.docset
sed -i "" -e "s/VERSION/$1/g" ClickHouse.docset/Contents/Info.plist
cp -r Documents/$1 ClickHouse.docset/Contents/Resources/Documents/
./gen.py $1
mv docSet.dsidx ClickHouse.docset/Contents/Resources/

tar zcf ClickHouse.tgz ClickHouse.docset
