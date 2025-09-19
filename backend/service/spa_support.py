from pathlib import Path
from shutil import copyfile

from fastapi.staticfiles import StaticFiles
from starlette.types import Scope


class SPA_Support(StaticFiles):
    def __init__(self, *, directory: str):
        if not Path(directory).exists():
            Path(directory).mkdir(
                parents=True,
                exist_ok=True,
            )

        if (Path(directory) / "index.html").exists():
            copyfile(Path(directory) / "index.html", Path(directory) / "404.html")

        super().__init__(directory=directory, html=True)

    async def get_response(self, path: str, scope: Scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404 and any(
            path.startswith(prefix)
            for prefix in [
                "about",
            ]
        ):
            response.status_code = 200
        return response
