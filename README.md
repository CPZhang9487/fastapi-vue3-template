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

修改 [backend/app.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/89f2eb962f58b0b91d676abee3f71d3bcfb7ae39/backend/app.py)

瀏覽 [http://127.0.0.1:8000](http://127.0.0.1:8000) 就會看到網頁內容

### Commit-006

介紹一下 `Python` 的一個依賴 `orjson`

這是一個使用 `Rust` 重寫的 `json` 庫

且效率快了 `Python` 自帶的 `json` 庫好幾倍

運行 [other/json_orjson_compare.py](https://github.com/CPZhang9487/fastapi-vue3-template/blob/4026d88d60e69b636ea02c4ee54aa1ab14425097/other/json_orjson_compare.py) 來測試 `json` 與 `orjson` 的運行速度

而 `FastAPI` 預設大多數回應都是使用 `json` 轉換格式

我們可以簡單的增加幾行程式碼讓 `FastAPI` 使用 `orjson`

修改 [backend/app.py](backend/app.py)

### Commit-007

`Vite` 在建立 `Vue3` 專案時可以選擇模板 `Official Vue Starter ↗`

推薦初學者選擇所有功能並在 `frontend/src/` 查看範例程式碼

`frontend/src/` 底下的結構為
- `assets/`
- `components/`
- `router/`
- `stores/`
- `views/`
- `App.vue`
- `main.ts`

而剛剛選取的功能當中，較為重要的是
- `Router`
    - 用於建立 `SPA (單頁應用程式)`
    - 使用官方路由庫 `vue-router`
    - 對應的資料夾為 `router/`
- `Pinia`
    - 用於管理網頁狀態
    - 使用官方狀態庫 `pinia`
    - 對應的資料夾為 `stores/`

推薦學習 `Vue3` 語法後接著研究上述兩個功能

編譯官方範例後運行 `FastAPI` 並瀏覽 [http://127.0.0.1:8000](http://127.0.0.1:8000) 會發現

點擊 `About` 按鈕後會跳至 [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)

再點擊 `Home` 按鈕就會跳回 [http://127.0.0.1:8000](http://127.0.0.1:8000)

但當你在 `about` 頁面刷新瀏覽器，卻會跳出 `{"detail":"Not Found"}`

這是因為目前 `FastAPI` 尚未實作 `SPA` 的相關功能

- 建立
    - [backend/service/SPA_support.py](backend/service/SPA_support.py)
- 修改
    - [backend/app.py](backend/app.py)

當前端的路由做更改時

後端再修改 `SPA_Support.get_response` if 判斷式 (後續不再贅述)

至於 `404 Not Found` 頁面則可以這麼做

- 建立
    - [frontend/src/views/NotFound.vue](frontend/src/views/NotFound.vue)
- 修改
    - [frontend/src/router/index.ts](frontend/src/router/index.ts)

這樣瀏覽像是 [http://127.0.0.1:8000/test](http://127.0.0.1:8000/test) 這種沒有實作的頁面

就會出現 `404 Not Found`
