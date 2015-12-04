from remote_api import env,run
import private

env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

with cd("~"):
    print(run("ls -l"))