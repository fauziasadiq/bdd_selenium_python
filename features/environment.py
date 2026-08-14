import os
from utils.driver_factory import create_driver
from utils.config_reader import load_config


def before_all(context):
    context.config_data = load_config()

    context.driver = create_driver(
        context.config_data["browser"],
        context.config_data["headless"]
    )

    context.driver.implicitly_wait(
        context.config_data["implicit_wait"]
    )


def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        context.driver.save_screenshot(
            f"{screenshot_dir}/{step.name}.png"
        )


def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()