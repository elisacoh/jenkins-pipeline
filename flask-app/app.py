import docker
from flask import Flask, jsonify

client = docker.from_env()

app = Flask(__name__)

"""
talks to the local docker engine and gets the list of running containers
"""
@app.route("/containers")
def get_running_containers():
    try:
        containers = client.containers.list()
    except docker.errors.DockerException as err:
        return {"error": str(err)}, 500
    return [{"name": c.name, "status": c.status, "id": c.short_id} for c in containers]

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run()