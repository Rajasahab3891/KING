from King.core.bot import Alone
from King.core.dir import dirr
from King.core.git import git
from King.core.userbot import Userbot
from King.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Alone()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
