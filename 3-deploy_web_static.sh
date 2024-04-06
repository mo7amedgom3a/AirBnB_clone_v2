#!/bin/bash

# Set variables
ARCHIVE_PATH=$(do_pack)
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Define function to create tar gzipped archive
do_pack() {
    dt=$(date -u +"%Y%m%d%H%M%S")
    file="versions/web_static_${dt}.tgz"
    if [ ! -d "versions" ]; then
        mkdir -p versions || return 1
    fi
    if ! tar -cvzf "$file" web_static; then
        return 1
    fi
    echo "$file"
}

# Define function to deploy archive
do_deploy() {
    archive_path="$1"
    if [ ! -f "$archive_path" ]; then
        return 1
    fi
    file=$(basename "$archive_path")
    name=$(basename "$archive_path" .tgz)

    if ! scp -i ~/.ssh/school "$archive_path" ubuntu@54.236.48.164:/tmp/"$file"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "rm -rf /data/web_static/releases/$name/"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "mkdir -p /data/web_static/releases/$name/"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "tar -xzf /tmp/$file -C /data/web_static/releases/$name/"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "rm /tmp/$file"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "mv /data/web_static/releases/$name/web_static/* /data/web_static/releases/$name/"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "rm -rf /data/web_static/releases/$name/web_static"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "rm -rf /data/web_static/current"; then
        return 1
    fi
    if ! ssh -i ~/.ssh/school ubuntu@54.236.48.164 "ln -s /data/web_static/releases/$name/ /data/web_static/current"; then
        return 1
    fi
    return 0
}

# Define function to deploy
deploy() {
    file=$(do_pack)
    if [ -z "$file" ]; then
        return 1
    fi
    if ! do_deploy "$file"; then
        return 1
    fi
    return 0
}

# Execute deployment
deploy

