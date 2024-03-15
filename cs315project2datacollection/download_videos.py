import pyktok as pyk
import logging

def download_tiktok_mp4s(urls):
    logger = logging.getLogger()
    file_handler = logging.FileHandler('download_failures.log')
    logger.addHandler(file_handler)

    pyk.specify_browser('chrome')
    for url in urls:
        try:
            pyk.download_tiktok_video(url)
        except Exception as exc:
            logger.warn("error while processing item: %s", exc)

    return True

if __name__ == "__main__":
    download_tiktok_mp4s(['https://www.tiktok.com/@comedicpill/video/7318066454983740715'])