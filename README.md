## omron_envsensor - オムロン環境センサ受信スクリプトライブラリ

### 取り扱い方

omron_envsensorは、pythonスクリプト内からインポートするもしくはrun.py、cat_csv.pyファイルを用いて活性化してください。これらにはroot権限が必要です。
活性化する際には、必須パッケージをインストールした状態のraspberryPi3もしくはraspberryPiZero内から使用しなければなりません。
必須パッケージのインストールについては **補遺1** を参照してください。


### 概要

omron_envsensorは、およそ6つのファイルからなるpython言語で書かれた[オムロン環境センサ](http://www.omron.co.jp/ecb/product-info/sensor/iot-sensor/environmental-sensor)受信スクリプトです。
活性化されると機器のBluetooth機能よりパケットを傍受し、特定の機器のパケットをパースして返します。

omron_envsensorの活性化には特定のパッケージがインストールされていないと、通常のpython言語のエラーメッセージと共に動作を停止します。
使用するpythonは2,3どちらでも構いません。

このライブラリは[OmronMicroDevices/envsensor-observer-py](https://github.com/OmronMicroDevices/envsensor-observer-py)を参考に作られています。


### 補遺1 必須パッケージのインストール

``` shell
sudo apt-get install -y libperl-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libglib2.0
sudo apt-get install -y libbluetooth-dev libreadline-dev
sudo apt-get install -y libboost-python-dev libboost-thread-dev libboost-python-dev

sudo pip3 install pybluez
sudo pip3 install pygattlib

```
