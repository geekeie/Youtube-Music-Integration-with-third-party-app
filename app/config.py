import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'your-youtube-api-key')
