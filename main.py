from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

import onetimepass as otp


class OnetimepassExtension(Extension):

    def __init__(self):
        super(OnetimepassExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        data = event.get_argument()

        providers = extension.preferences['onetimepass_providers'].split(' ')

        for provider in providers:
            if data:
                if data not in provider:
                    continue

            secrets = provider.split("=")
            name = secrets[0]
            secret = secrets[1] + '=' * ((8 - len(secrets[1])) % 8)
            token = str(otp.get_totp(secret)).zfill(6)

            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s' % token,
                                             description='%s' % name,
                                             on_enter=CopyToClipboardAction(token)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    OnetimepassExtension().run()
