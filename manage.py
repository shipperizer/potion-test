from flask import url_for
from flask_migrate import MigrateCommand
from flask_script import Manager

from potion_test.app import create_app, init_app


app = init_app(create_app())

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def list_routes():
    import urllib.parse
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(str(arg))

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
