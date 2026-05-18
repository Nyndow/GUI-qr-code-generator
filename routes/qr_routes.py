from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from models.qr import QR
from services.qr_services import qr_service

router = APIRouter(prefix="/qr", tags=["QR Codes"])


class QRBody(BaseModel):
    size: Optional[int] = None
    content: Optional[str] = None
    path: Optional[str] = None


@router.post("/", response_model=QR, status_code=status.HTTP_201_CREATED)
def create_qr(body: QRBody) -> QR:
    return qr_service.create(size=body.size, content=body.content, path=body.path)


@router.get("/", response_model=list[QR])
def list_qr() -> list[QR]:
    return qr_service.get_all()


@router.get("/{qr_id}", response_model=QR)
def get_qr(qr_id: str) -> QR:
    qr = qr_service.get_by_id(qr_id)
    if qr is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR '{qr_id}' not found.")
    return qr


@router.patch("/{qr_id}", response_model=QR)
def update_qr(qr_id: str, body: QRBody) -> QR:
    qr = qr_service.update(qr_id, size=body.size, content=body.content, path=body.path)
    if qr is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR '{qr_id}' not found.")
    return qr


@router.delete("/{qr_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_qr(qr_id: str) -> None:
    if not qr_service.delete(qr_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR '{qr_id}' not found.")