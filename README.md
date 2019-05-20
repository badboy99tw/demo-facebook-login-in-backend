# [DEMO] Facebook login in backend

## Setup - Facebook Apps
* 到 [facebook for developers](https://developers.facebook.com/) 開一個 demo app，最好再從 demo app 開一個 test demo app。
* Facebook Apps 的 PRODUCTS 那邊新增 Facebook Login
* 把 test demo app 的 App ID 和 App Secret 填到 .env 檔案裡面

## Run
* 用 docker-compose 把 frontend 和 backend 都跑起來
```
make run
```
* 打開瀏覽器，前端網址是 http://localhost:5000
* 按下 LOGIN 按鈕！
