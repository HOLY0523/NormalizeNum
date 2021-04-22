#!/bin/sh
sed -i -e 's/ゼロ/〇/g' $1
sed -i -e 's/零/〇/g' $1
sed -i -e 's/０/〇/g' $1
sed -i -e 's/１/一/g' $1
sed -i -e 's/２/二/g' $1
sed -i -e 's/３/三/g' $1
sed -i -e 's/４/四/g' $1
sed -i -e 's/５/五/g' $1
sed -i -e 's/６/六/g' $1
sed -i -e 's/７/七/g' $1
sed -i -e 's/８/八/g' $1
sed -i -e 's/９/九/g' $1
python3 ks2k.py txtmp $1
mv -f txtmp $1
sed -i -e 's/〇千//g' $1
sed -i -e 's/一千/千/g' $1
sed -i -e 's/〇百//g' $1
sed -i -e 's/一百/百/g' $1
sed -i -e 's/〇十//g' $1
sed -i -e 's/一十/十/g' $1
sed -i -e 's/十〇/十/g' $1
sed -i -e 's/百〇/百/g' $1
sed -i -e 's/千〇/千/g' $1
