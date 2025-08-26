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
        css_href = "/static/kolibri_angels4ed_theme/angels.css"
        icon512  = "/static/kolibri_angels4ed_theme/android-chrome-512x512.png"
        favicon  = "/static/kolibri_angels4ed_theme/favicon.ico"

        # Fallback: forcibly inject our <link> (works on all Kolibri versions)
        head_html = (
            f'<link rel="icon" type="image/x-icon" href="{favicon}"/>'
            f'<link rel="stylesheet" type="text/css" href="{css_href}"/>'
            # JS fallback: if not present, append again (defensive)
            f'<script>(function(){{var h=document.head;'
            f'if(!document.querySelector(\'link[href="{css_href}"]\')){{'
            f'var l=document.createElement("link");l.rel="stylesheet";l.href="{css_href}";h.appendChild(l);}}'
            f'}})();</script>'
        )

        return {
            "signIn": {
                "background": static(f"{APP}/kolibri_angels4ed_theme/background.jpeg"),
                "backgroundImgCredit": "Angels for Education",
                "topLogo": { "style": "padding-left:64px; padding-right:64px; margin:8px 0" },
                # The “title” key may be ignored in some builds; we handle it in CSS below.
            },
            "logos": [
                {"src": static(f"{APP}/kolibri_angels4ed_theme/favicon.ico"), "content_type": "image/vnd.microsoft.icon", "size": "48x48"},
                {"src": static(f"{APP}/kolibri_angels4ed_theme/android-chrome-192x192.png"), "content_type": "image/png", "size": "192x192"},
                {"src": static(f"{APP}/kolibri_angels4ed_theme/android-chrome-256x256.png"), "content_type": "image/png", "size": "256x256"},
                {"src": static(f"{APP}/kolibri_angels4ed_theme/android-chrome-512x512.png"), "content_type": "image/png", "size": "512x512"},
            ],
            # keep this for newer Kolibri versions (harmless if ignored)
            "styles": [css_href],
            # guaranteed injection for older versions
            "headHTML": head_html,
        }
