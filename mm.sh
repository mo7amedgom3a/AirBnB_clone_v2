# Remove extraneous web_static dir
#!/bin/bash
ssh ubuntu@54.236.48.164 -i ~/.ssh/school "sudo rm -rf /data/web_static/releases/web_static_20240404200135/web_static"
ssh ubuntu@3.84.158.242 -i ~/.ssh/school "sudo rm -rf /data/web_static/releases/web_static_20240404200135/web_static"

# Delete pre-existing sym link
ssh ubuntu@54.236.48.164 -i ~/.ssh/school "sudo rm -rf /data/web_static/current"
ssh ubuntu@3.84.158.242 -i ~/.ssh/school "sudo rm -rf /data/web_static/current"

# Re-establish symbolic link
ssh ubuntu@3.84.158.242 -i ~/.ssh/school "sudo ln -s /data/web_static/releases/web_static_20240404200135/ /data/web_static/current"
ssh ubuntu@54.236.48.164 -i ~/.ssh/school "sudo ln -s /data/web_static/releases/web_static_20240404200135/ /data/web_static/current"
