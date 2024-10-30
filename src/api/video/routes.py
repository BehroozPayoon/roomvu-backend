import os

from fastapi import APIRouter
from moviepy.editor import ImageClip, TextClip, CompositeVideoClip

router = APIRouter(prefix="/video")


@router.post("/")
async def create_video():
    background_image_path = f"{_get_assets_path()}/images/background_image.jpg"
    background = ImageClip(background_image_path).set_duration(5)

    # Define the text
    text = ("The IFA doesn’t offer separate down payment assistance (DPA) programs for first-time homebuyers, but "
            "rather, assistance in conjunction with the FirstHome and Homes for Iowans programs.")

    # Create a text clip
    font_path = f"{_get_assets_path()}/fonts/font.ttf"
    txt_clip = TextClip(text, fontsize=60, color='black',
                        font=font_path)
    txt_clip = txt_clip.set_position((50, 150)).set_start(1).set_duration(4)

    # Overlay the text on the background
    video = CompositeVideoClip([background, txt_clip])
    video.set_duration(5)
    video.write_videofile(f"{_get_assets_path()}/output_video.avi", fps=30,
                          codec='mpeg4',
                          audio=False,
                          preset='medium',
                          ffmpeg_params=["-crf", "18"])

    return "OK"


def _get_assets_path():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "assets")
