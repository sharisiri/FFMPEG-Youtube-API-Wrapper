import argparse
import subprocess


parser = argparse.ArgumentParser()

parser.add_argument('-img', 
                    required=True, 
                    dest='img',
                    help="Input the relative path to your album cover image")
parser.add_argument('-audio', 
                    required=True, 
                    dest='audio', 
                    help="Input the relative path to your audio file")

parser.add_argument('-title', 
                    required=True, 
                    dest='title', 
                    help="Input the relative path to your video title")

parser.add_argument('-description', 
                    required=False, 
                    dest='description',
                    help="Input the relative path to your video description")

args = parser.parse_args()

def generate_video(video,audio):
    command = "ffmpeg -loop 1 \
            -i {video} \
            -i {audio} \
            -c:v libx264 \
            -vf 'scale=w=1920:h=1080:force_original_aspect_ratio=1,pad=1920:1080:(ow-iw)/2:(oh-ih)/2' \
            -tune stillimage \
            -c:a aac \
            -strict experimental \
            -b:a 192k \
            -pix_fmt yuv420p \
            -shortest out.mp4".format(video=video, audio=audio)
    subprocess.call(command,shell=True)

generate_video(args.img, args.audio)

process = subprocess.run(['python3', 'upload_video.py', '--file', 'out.mp4', \
                    '--title', args.title, \
                    '--description', '', \
                    '--category', '10', \
                    '--privacyStatus', 'unlisted'], input=None)
