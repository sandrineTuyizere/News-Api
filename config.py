import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=266885d5426a4c5ab4444c5aa64f079f'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=266885d5426a4c5ab4444c5aa64f079f'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}

