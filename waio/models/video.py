from typing import Dict
from typing import Optional
from typing import Union

import ujson


class VideoModel:
    def __init__(self, url: str, caption: Optional[str] = None):
        self.type = "video"
        self.url = url
        self.caption = caption

    def dict(self) -> Dict[str, Union[str, None]]:
        return {
            "type": self.type,
            "url": self.url,
            "caption": self.caption,
        }

    def json(self) -> str:
        return ujson.dumps(self.dict(), indent=2)
