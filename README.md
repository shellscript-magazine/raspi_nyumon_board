シェルスクリプトマガジンとビット・トレード・ワンで共同制作したラズパイ用拡張ボード「ラズパイ入門ボード」で動作するサンプルアプリを公開しています。ラズパイ入門ボードは、小型コンピュータボード「Raspberry Pi」のプログラミングを学習できるハードウエアです。

## choucho.py  
圧電スピーカーで童謡「ちょうちょ」を演奏するアプリです。次のように実行してください。  

$ sudo apt-get update  
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio pigpio python-pigpio python3-pigpio  
$ sudo pigpiod  
$ python choucho.py  

## entryboard.py, initial.py
ラズパイ入門ボードを初期化するプログラムです。次のように実行してください。

$ sudo apt-get update  
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio  
$ python initial.py

written by Jiro Aso
