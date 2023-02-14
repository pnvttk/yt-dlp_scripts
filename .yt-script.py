from textwrap import dedent
import subprocess

videosPATH = '~/Desktop/videos/'
dlFilePATH = '~/Desktop/videos/dl.txt'

def main():
    welcome = """
    Welcome to yt-dlp scripts.

    Please select you poison.
    1. Normal (best)
    2. Extract audio to wav
    3. Select Time of Video
    4. Multiple Video with file
    """
    print(dedent(welcome))

    dlCase_number = input('Select download case : ')

    if dlCase_number.isdigit():
        dlCase(int(dlCase_number))
    else:
        print('incorrect selected number')
        return main()

def timeToSecond(time):
    time = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time.split(":"))))
    return time

def normalDownload(url):
    subprocess.run(['yt-dlp', '-f', 'best', '-P', videosPATH, url], check=True)

def extractAudio(url):
    subprocess.run(['yt-dlp', '-f', 'bestaudio', '-x', '--audio-format', 'wav', '-P', videosPATH, url], check=True)

def selectTime(startTime,endTime,url):
    subprocess.run(['yt-dlp', '-f', '(best)[protocol!*=dash]', '--external-downloader', 'ffmpeg', '--external-downloader-args', f'ffmpeg_i:-ss {startTime} -to {endTime}', '-P', videosPATH, url], check=True)

def multiVideo():
    subprocess.run(['yt-dlp', '-f', 'best', '-P', videosPATH, '-a', dlFilePATH], check=True)

def dlCase(dlCase_number):
    match dlCase_number:
        case 1:
            url = input('Enter URL : ')
            return normalDownload(url)
        case 2:
            url = input('Enter URL : ')
            return extractAudio(url)
        case 3:
            start_time = input('Enter Start time : ')
            start_timeSecond = timeToSecond(start_time)
            end_time = input('Enter End time : ')
            end_timeSecond = timeToSecond(end_time)
            url = input('Enter URL : ')
            return selectTime(start_timeSecond,end_timeSecond,url)
        case 4:
            multiVideo_instruction = """
            befor process make sure
            - dl.txt is exist in ~/Desktop/videos
            """
            print(dedent(multiVideo_instruction))
            confirm = input(f" dl.txt is correct? (Y/N) ")
            if confirm.lower() != 'y':
                return main()
            return multiVideo()
        case _:
            print('incorrect selected number')        

main()
