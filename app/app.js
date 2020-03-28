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
const dnDir = '~/Desktop/darknet';

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
//岩切用メモ: 重み変更する必要あり
execSync(`cd ${dnDir} && ./darknet detector test cfg/obj.data cfg/yolov3-voc_test.cfg backup/yolov3-voc_10000.weights -thresh 0.3 ${__dirname}/${req.file.filename} && cp predictions.jpg ${__dirname}/predictions.jpg`);
execSync(`python bill.py`);
execSync(`python convert_to_html.py`);

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
