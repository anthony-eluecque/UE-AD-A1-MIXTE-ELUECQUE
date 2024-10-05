from typing import TypedDict, Optional

class MutationResponse(TypedDict):
    success : bool
    error :  Optional[str]
