from pydantic import BaseModel


class TTSSynthesizeRequest(BaseModel):
    """
    Contains: 'text' (str), 'voice' (str), 'role' (str), 'speed' (str), 'filename' (str).
    """
    tts_text: str
    voice: str
    role: str
    speed: float
    new_file_name: str


class AudioFilesURLsResponse(BaseModel):
    """
    Contains: 'id' (int), 'file_name' (str), 'file_path' (str).
    """
    id: int
    file_name: str
    file_path: str

    class Config:
        orm_mode = True
