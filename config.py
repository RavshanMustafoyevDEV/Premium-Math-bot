from environs import Env
env = Env()
env.read_env()


TOKEN = env("token")
ADMINS = ['1947186487', '5744389492']
