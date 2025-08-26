from django.templatetags.static import static
from kolibri.core import theme_hook
from kolibri.plugins import KolibriPluginBase
from kolibri.plugins.hooks import register_hook

APP = "kolibri_angels4ed_theme"

class Angels4EdThemePlugin(KolibriPluginBase):
    pass

@register_hook
class Angels4EdThemeHook(theme_hook.ThemeHook):
    @property
    def theme(self):
        return {
            "signIn": {
                "background": static(f"{APP}/background.jpeg"),
                "backgroundImgCredit": "Angels for Education",
                "topLogo": {
                    "style": "padding-left:64px; padding-right:64px; margin:8px 0",
                },
            },
            "logos": [
                {"src": static(f"{APP}/favicon.ico"), "content_type": "image/vnd.microsoft.icon", "size": "48x48"},
                {"src": static(f"{APP}/android-chrome-192x192.png"), "content_type": "image/png", "size": "192x192"},
                {"src": static(f"{APP}/android-chrome-256x256.png"), "content_type": "image/png", "size": "256x256"},
                {"src": static(f"{APP}/android-chrome-512x512.png"), "content_type": "image/png", "size": "512x512"},
            ],
            # Load your custom stylesheet (with app prefix)
            "styles": [static(f"{APP}/angels.css")],
        }
