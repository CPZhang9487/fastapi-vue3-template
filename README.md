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

再來修改 [main.py](main.py)

最後使用 `uv run main.py` (後面都是使用此命令運行伺服器，不再贅述) 運行 `uvicorn`

就會看到終端輸出啟動信息

瀏覽 [http://127.0.0.1:8000](http://127.0.0.1:8000) 會看到 `{"detail":"Not Found"}`

瀏覽 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 會看到 `Swagger UI`

### Commit-003

很多時候會需要將終端的信息備份成檔案

這邊透過 `logging` 的 `TimedRotatingFileHandler` 類實作這部分

為了後續方便，將功能分成對應的檔案

- 建立
    - [backend/util/uvicorn_log_override.py](backend/util/uvicorn_log_override.py)
    - [backend/lifespan.py](backend/lifespan.py)
    - [backend/app.py](backend/app.py)
- 修改
    - [main.py](main.py)

運行伺服器後會建立 `log/uvicorn.access.log`

且當 `FastAPI` 被瀏覽時，log 將會被寫入

並在每日午夜自動備份檔案
