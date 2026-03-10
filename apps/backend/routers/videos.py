from fastapi import APIRouter, UploadFile, HTTPException
from ..services.pipeline import analyse_video

router = APIRouter()

ALLOWED_VIDEO_TYPES = ["video/mp4", "video/avi", "video/quicktime"]


@router.post("/videos/uploadfile/")
async def create_upload_file(file: UploadFile):
    if file.content_type not in ALLOWED_VIDEO_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. upload a video file"
        )
    contents = await file.read()

    result = analyse_video(contents)
    return {"result": result}




