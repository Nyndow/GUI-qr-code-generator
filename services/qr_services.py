from typing import Optional

from models.qr import QR


_store: dict[str, QR] = {}


class QRService:

    def create(self, size: int, content: str, path: str) -> QR:
        qr = QR(size=size, content=content, path=path)
        _store[qr.id] = qr
        return qr

    def get_by_id(self, qr_id: str) -> Optional[QR]:
        return _store.get(qr_id)

    def get_all(self) -> list[QR]:
        return list(_store.values())

    def update(self, qr_id: str, size: Optional[int] = None, content: Optional[str] = None, path: Optional[str] = None) -> Optional[QR]:
        qr = _store.get(qr_id)
        if qr is None:
            return None
        changes = {k: v for k, v in {"size": size, "content": content, "path": path}.items() if v is not None}
        updated = qr.model_copy(update=changes)
        _store[qr_id] = updated
        return updated

    def delete(self, qr_id: str) -> bool:
        if qr_id not in _store:
            return False
        del _store[qr_id]
        return True


qr_service = QRService()