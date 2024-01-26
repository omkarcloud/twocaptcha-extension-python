from chrome_extension_python import Extension

class TwoCaptcha(Extension):
    def __init__(self, api_key):
        super().__init__(
            extension_id="ifibfemgeogfhoebkmokieepdoobkbpo",
            extension_name="2captcha",
            api_key=api_key,
        )

    def update_files(self, api_key):
        def update_config_contents(content):
            key_replaced = content.replace("apiKey: null,", f'apiKey: "{api_key}",')
            return key_replaced
        self.get_file("/common/config.js").update_contents(update_config_contents)