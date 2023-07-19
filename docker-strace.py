import docker
import sys
import subprocess

# Requires installing the 'docker' package

args = sys.argv[1:]
container_name = args[0]

client = docker.from_env()
container = client.containers.get(container_name)

# Second element of the array is the host pid
pids = [proc[1] for proc in container.top()['Processes']]

pid_arg = ' '.join(pids)

strace_cmd = ['strace', '-p', pid_arg]
strace_cmd += args[1:]

subprocess.run(strace_cmd)
