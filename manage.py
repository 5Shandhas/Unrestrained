#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from mainapp import app
from exts import db

manage = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

#增加迁移脚本的命令到manager中
manage.add_commend('db', MigrateCommand)

if __name__ == "__main__":
    manage.run()