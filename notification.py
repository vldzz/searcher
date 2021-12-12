from plyer import notification


def notify(title, body):
    notification.notify(
        title=title,
        message=body,
        app_name='',
        app_icon='',
        timeout=1
    )
