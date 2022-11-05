import os
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction


class KillOnClick(Extension):
    def __init__(self):
        super(KillOnClick, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="Kill window",
                on_enter=ExtensionCustomAction("kill", keep_app_open=False),
            )
        )

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):

        os.system(f"bash -c 'xkill'")


if __name__ == "__main__":
    KillOnClick().run()
