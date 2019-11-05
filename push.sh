#!/bin/bash

mdbook clean
python3 build.py

git add .
git commit -m "$1"
git push origin master


rm bench.fut
rm poly
futhark c poly.hs
touch bench.fut

echo "-- Polynomial Expansion"
echo "-- =="

for degree in `seq 1 9` \
                  `seq 10 10 99` \
                  `seq 100 100 999` \
                  `seq 1000 1000 9999` \
                  `seq 10000 10000 99999`
do
    for n in $(echo 1024 | bc) \
        $(echo 8 \*1024 | bc) \
        $(echo 16 \*1024 | bc) \
        $(echo 32 \*1024 | bc) \
        $(echo 64 \*1024 | bc) \
        $(echo 128 \*1024 | bc) \
             $(echo 256 \*1024 | bc) \
             $(echo 512 \*1024 | bc) \
             $(echo 1024 \*1024 | bc) \
             $(echo 8 \*1024 \*1024 | bc) \
                 $(echo 16 \*1024 \*1024 | bc) \
                 $(echo 32 \*1024 \*1024 | bc) \
                 $(echo 64 \*1024 \*1024 | bc) \
                 $(echo 128 \*1024 \*1024 | bc) \
                     $(echo 256 \*1024 \*1024 | bc) \
                     $(echo 512 \*1024 \*1024 | bc) \
                     $(echo 1024 \*1024 \*1024 | bc)
                         do
                                            out=$(echo $n $degree | ./poly)
                                    echo "-- compiled input { $n $degree } output { $out } "
                         done
done

cat ./poly.hs