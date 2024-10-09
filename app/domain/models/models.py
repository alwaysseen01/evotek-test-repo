from sqlalchemy import MetaData, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

metadata = MetaData()

class Base(DeclarativeBase):
    metadata = metadata


class AudioFilesURLs(Base):
    __tablename__ = 'audio_files_urls'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(2048), nullable=False)
