import os

from moviepy.editor import ImageClip, TextClip, CompositeVideoClip


class VideoService:

    def generate_video(self):
        background_image_path = f"{self._get_assets_path()}/images/background_image.jpg"
        background = ImageClip(background_image_path).set_duration(5)

        text = ("The IFA doesn’t offer separate down payment assistance (DPA) programs for first-time homebuyers, but "
                "rather, assistance in conjunction with the FirstHome and Homes for Iowans programs.")

        font_path = f"{self._get_assets_path()}/fonts/font.ttf"
        txt_clip = TextClip(text, fontsize=60, color='black',
                            font=font_path)
        txt_clip = txt_clip.set_position(
            (50, 150)).set_start(1).set_duration(4)

        video = CompositeVideoClip([background, txt_clip])
        video.set_duration(5)
        video.write_videofile(f"{self._get_assets_path()}/output_video.avi", fps=30,
                              codec='mpeg4',
                              audio=False,
                              preset='medium',
                              ffmpeg_params=["-crf", "18"])

    def _get_assets_path(self):
        return os.path.join(os.path.dirname(__file__), "..", "..", "..", "assets")
