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
        css_href = static(f"{APP}/kolibri_angels4ed_theme/angels.css")  # note the app-prefixed subfolder
        icon512  = static(f"{APP}/kolibri_angels4ed_theme/android-chrome-512x512.png")
        favicon  = static(f"{APP}/kolibri_angels4ed_theme/favicon.ico")

        # fallback injection: add <link> directly into <head>
        head_html = (
            f'<link rel="stylesheet" type="text/css" href="{css_href}"/>'
            f'<link rel="icon" type="image/x-icon" href="{favicon}"/>'
        )

        return {
            "signIn": {
                "background": static(f"{APP}/kolibri_angels4ed_theme/background.jpeg"),
                "backgroundImgCredit": "Angels for Education",
                "topLogo": {
                    "src": icon512,
                    "alt": "Angels for Education",
                    "style": "width:120px; height:auto; margin: 12px auto;"
                },
                "title": "Angels for Education",
            },
            "logos": [
                {"src": favicon, "content_type": "image/vnd.microsoft.icon", "size": "48x48"},
                {"src": icon512, "content_type": "image/png", "size": "512x512"},
            ],

            # keep this for newer Kolibri (harmless if ignored)
            "styles": [css_href],

            # add explicit head HTML for older versions
            "headHTML": head_html,
        }
