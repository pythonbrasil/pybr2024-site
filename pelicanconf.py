from util.jinja_filters import get_by_slug


SITEYEAR = 2023
SITEURL = ''

AUTHOR = 'Python Brasil'
SITENAME = 'Python Brasil 2023'
THEME = 'theme' 
PATH = 'content'
TIMEZONE = 'America/Bahia'
DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA_FILTERS = {
    "get_by_slug": get_by_slug,
}

PLUGINS = []

MENU = [
    ('#inicio', 'Início', False),
    ('#evento', 'Sobre o evento', False),
    ('#keynotes', 'Keynotes', False),
    ('#programacao', 'Programação', False),
    ('#patrocinadores', 'Patrocinadores', False),
    ('#faq', 'FAQ', False),
    ('#footer', 'Site Map', False),
]

SOCIAL = {
    'twitter':'https://twitter.com/pythonbrasil',
    'instagram':'https://instagram.com/pythonbrasil',
    'linkedin':'https://www.linkedin.com/company/apyb/',
    'youtube':'https://www.youtube.com/c/pythonbrasiloficial',
    'facebook':'https://www.facebook.com/pythonbrasil',
    'flickr':'https://www.flickr.com/pythonbrasil',
    'telegram':'https://t.me/pythonbrasil',
    'email':'mailto:eventos@python.org.br',
}

DEFAULT_PAGINATION = False
SITE_META_KEYWORDS = f"Python Brasil, Python Brasil {SITEYEAR}, evento python, comunidade, evento, Programação, Python"
SITE_META_DESCRIPTION = "Python Brasil é o maior evento sobre linguagem de programação Python do Brasil. Feito pela comunidade para a comunidade, tem o objetivo de difundir a linguagem, promover a troca de experiências e manter a comunidade crescendo igualmente em público e impacto social."

EVENTO = {
    'inscricao':'',
    'submissao':'',
    'data_evento': '',
    'cidade': ''
}

PLANOS = {
    'pt_br':'',
    'en':'',
}

GUIA = {
    'pt_br':'',
}
