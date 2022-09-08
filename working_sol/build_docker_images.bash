podman build . -f generator/Dockerfile -t quay.io/gary_crowe/generator:0.1
podman build . -f client/Dockerfile -t quay.io/gary_crowe/bingo:0.1
