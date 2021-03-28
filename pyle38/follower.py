from typing import Literal
from typing import Optional
from typing import Union

from .client import Client
from .client import Command
from .client import SubCommand
from .commands.get import Get
from .errors import Tile38Error
from .responses import BoundsResponse
from .responses import ChansResponse
from .responses import ConfigGetResponse
from .responses import ConfigKeys
from .responses import HooksResponse
from .responses import JSONGetResponse
from .responses import JSONResponse


class Follower(Client):
    client: Client

    def __init__(self, url: str) -> None:
        if not url:
            raise Tile38Error("No Tile38 follower uri set")
        super().__init__(url)

        self.client = Client(url)

    async def bounds(self, key: str) -> BoundsResponse:
        return BoundsResponse(**(await self.client.command(Command.BOUNDS, [key])))

    async def chan(self, pattern: str = "*") -> ChansResponse:
        return ChansResponse(**(await self.client.command(Command.CHANS, [pattern])))

    async def config_get(self, name: ConfigKeys) -> ConfigGetResponse:
        return ConfigGetResponse(
            **(await self.client.command(Command.CONFIG, [Command.GET, name]))
        )

    async def config_set(
        self, name: ConfigKeys, value: Union[str, int, float]
    ) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [Command.SET, name, value]))
        )

    async def config_rewrite(self) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [SubCommand.REWRITE]))
        )

    async def gc(self) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.GC)))

    def get(self, key: str, id: str) -> Get:
        return Get(self.client, key, id)

    async def hooks(self, pattern: str = "*") -> HooksResponse:
        return HooksResponse(**(await self.client.command(Command.HOOKS, [pattern])))

    async def jget(
        self,
        key: str,
        id: str,
        path: Optional[str] = None,
        mode: Optional[Literal["RAW"]] = None,
    ) -> JSONGetResponse:
        return JSONGetResponse(
            **(
                await self.client.command(
                    Command.JGET,
                    [key, id, *([path] if path else []), *([mode] if mode else [])],
                )
            )
        )
