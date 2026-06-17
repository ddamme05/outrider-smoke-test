from pydantic import BaseModel, Field


class PageParams(BaseModel):
    limit: int = Field(default=50, ge=1, le=100)
    offset: int = Field(default=0, ge=0)


def apply_page(items: list[object], params: PageParams) -> list[object]:
    return items[params.offset : params.offset + params.limit]
