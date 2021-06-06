from flaskr import launcher

application = launcher.create_app()

if __name__ == '__main__':
    application.run()