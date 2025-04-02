from pydantic import BaseModel

class RecommendedLunch(BaseModel):
    name: str
    main_menu: str
    address: str
    map_url: str
