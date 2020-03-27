'use strict';

const execSync = require('child_process').execSync;

const express = require('express');

const multer = require('multer');

const storage = multer.diskStorage({

destination: function (req, file, cb) {
cb(null, './');
},

filename: function (req, file, cb) {
cb(null, file.originalname);
}

});

const upload = multer({storage: storage});

const app = express();

app.use(express.static(__dirname));


// darknetを導入したディレクトリ(必要に応じて書き換えてください)
const dnDir = '~/Desktop/haitlab/YOLO/2class/darknet';

// HTMLを表示
app.get('/', (req, res) => res.sendFile('./index.html'));

// 画像アップロードをPOSTで受け付け
app.post('/', upload.single('input-img'), (req, res) => {

console.log('[done] Image upload');

console.log(req.file);

// darknetを導入したディレクトリに移動し、
// darknetを実行する。するとpredictions.pngというファイルが出力されるので、
// それをウェブサーバのディレクトリまでコピーしてくる
//
// 注意：この方法だと複数のユーザから同時にアップロードされた場合対応できないので
// 別の方法を考える必要がある。

execSync(`cd ${dnDir} && ./darknet detector test cfg/obj.data cfg/yolov3-voc_test.cfg backup/yolov3-voc_10000.weights data/images/${req.file.filename} && cp predictions.jpg ${__dirname}/predictions.jpg`);
console.log('Darknet done.');

// 画像ファイルのパスをJSONで返す

res.type('application/json');

res.send(JSON.stringify({
"path": "predictions.jpg"
}));

res.end();

});

 

// listenを開始する

app.listen(3000);