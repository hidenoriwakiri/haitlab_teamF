# haitlab_teamF
HAIT LAB東京3期, チームFのリポジトリです.


※バグが多数あったので, 修正を行いました。**2020/4/1 19:00**以前にこのリポジトリを利用した方は、再度```git clone```してください。

私たちは, 丸亀製麺のメニュー判別を行うプロダクトを開発しました. 
 ```app```ではYOLOv3を ```app-tiny```ではYOLOv3-tinyを物体検出モデルとして使用しています.  
リポジトリの利用にあたり, 注意すべき点を挙げます.

1. ```download```でコードを取り込むとファイルの内容が一部変更され, うまくいかないことが確認されているので, 必ず```git clone```してください.
2. ```app```および```app-tiny```フォルダ内に```app.js```と```bill.py```というファイルがありますが, ```darknet```フォルダへのパスを記述するところがあるので, 忘れずに行なってください.
3. Webサーバーを起動するには, ```app(-tiny)```ディレクトリに移動した後, 
```
node app.js
```
と打ってください. そして, http://localhost:3000/ に移動すれば, Webページが開きます.
