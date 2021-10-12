class DemoCustomValidator:
    INSTANCE = None

    def check_demo(self, obj):
        return obj == "Demo"

DemoCustomValidator.INSTANCE = DemoCustomValidator()
