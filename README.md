# FastAPI Vue3 Template

## 詳細實作

善用 Ctrl+F 搜尋各 Commit

### Commit-001

首先是 `Python` 的安裝與運作

這裡不單獨下載 `Python`

而是使用 `uv` 作為 `Python` 的管理工具

在 [uv 官網](https://docs.astral.sh/uv/) 按照裡面的說明安裝 `uv`

接著在合適的資料夾使用 `uv init` 建立新的 `Python` 專案

並使用 `uv run main.py` 測試 `uv` 與 `Python` 的運作狀況

### Commit-002

再來是 `FastAPI` 的實作

先使用 `uv add fastapi[all]` 加入相關依賴到 `Python` 專案

再來修改 [main.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/c910e1d94ce51504de4c8c11c12372384606ddab/main.py)

最後使用 `uv run main.py` (後面都是使用此命令運行伺服器，不再贅述) 運行 `uvicorn`

就會看到終端輸出啟動信息

瀏覽 [http://127.0.0.1:8000](http://127.0.0.1:8000) 會看到 `{"detail":"Not Found"}`

瀏覽 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 會看到 `Swagger UI`

### Commit-003

很多時候會需要將終端的信息備份成檔案

這邊透過 `logging` 的 `TimedRotatingFileHandler` 類實作這部分

為了後續方便，將功能分成對應的檔案

- 建立
    - [backend/util/uvicorn_log_override.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/9600e31a828b854105bb3b58afb63b04af4829a2/backend/util/uvicorn_log_override.py)
    - [backend/lifespan.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/9600e31a828b854105bb3b58afb63b04af4829a2/backend/lifespan.py)
    - [backend/app.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/9600e31a828b854105bb3b58afb63b04af4829a2/backend/app.py)
- 修改
    - [main.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/9600e31a828b854105bb3b58afb63b04af4829a2/main.py)

運行伺服器後會建立 `log/uvicorn.access.log`

且當 `FastAPI` 被瀏覽時，log 將會被寫入

並在每日午夜自動備份檔案

### Commit-004

來到網頁前端 `Vue3` 的部分

必須先安裝 [Node.js](https://nodejs.org/en/download)

接著在專案底下使用 `npm create vite`
- `Project name` 我都命名為 `frontend`
- `Framework` 選擇 `Vue`
- `Variant` 根據個人習慣使用 `JavaScript` 或 `TypeScript`，我選擇 `TypeScript`

然後使用 `cd frontend` (後續所有 `npm` 相關的命令都會在 `frontend/` 底下運行，不再贅述)

使用 `npm install` 安裝所需依賴 (當沒有 `frontend/node_modules/` 資料夾時都需先使用此命令)

然後就可以使用 `npm run dev` 進行 `Vue3` 的開發了

開發時都是瀏覽 [http://localhost:5173](http://localhost:5173) 進行除錯

且程式碼更新時，網頁會熱重載，大多數時候都不需要刷新網頁

### Commit-005

再來說說前端網頁的編譯與後端呈現前端的方法

編譯 `Vue3` 使用 `npm run build`

會看到 `frontend/` 裡面有 `dist/` 資料夾，裡面即是編譯出來的相關檔案

而讓 `FastAPI` 呈現 `frontend/dist/` 的方式為

修改 [backend/app.py](backend/app.py)

瀏覽 [http://127.0.0.1:8000](http://127.0.0.1:8000) 就會看到網頁內容
