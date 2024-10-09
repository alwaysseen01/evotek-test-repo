from app.domain.models.models import AudioFilesURLs
from app.infrastructure.repository_interface import SQLAlchemyRepository


class AudioFilesURLsRepository(SQLAlchemyRepository):
    model = AudioFilesURLs
