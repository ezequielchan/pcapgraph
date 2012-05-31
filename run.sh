#/bin/bash

python run.py

mscgen -i  salida.msc -T png -o out.png

#cat salida.msc
eog out.png

