#file---features/environment

def before_all(context):
    context.hostname=context.config.userdata.get("hostname")
    context.username=context.config.userdata.get("username")
    context.key_filename=context.config.userdata.get("key_filename")
