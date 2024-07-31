# ocsf-translation-tools
This repo builds off of the [official OCSF Java Tools](https://github.com/ocsf/ocsf-java-tools) repo to allow the ocsf-cli to run in a standalone docker container.

## Using the Docker Container
If you have already cloned the repository, you can build the docker image with:

```
sudo docker build -t ocsf-cli .
```

Note: If you have Java installed, feel free to modify the code that performs the translations. Once you are done making changes be sure to run `./gradlew build` and then rebuild the container with the command above.


The `data/` folder contains sample, anonymized Office365 and Box logs. You can use Docker volumes to store and translate logs. Run

```
sudo docker run -d -v data-volume:/data --name temp ubuntu
```

This starts a temporary container  with a volume named data-volume. Next copy data into the volume using 

```
sudo docker cp data/o365 temp:/data && sudo docker cp data/box temp:/data
```

Now we can use the volume with our ocsf-cli container. Run the below command to open a bash shell in the container. 

```
sudo docker run -it -v data-volume:/app/data ocsf-cli /bin/bash
```

Try simply running ocsf-cli in the shell to see the usage info. To convert the O365 logs run:

```
ocsf-cli -s lib/schema.json -R data/o365/ -r rule.json data/o365/logs/ > data/o365/o365_translated.json
```
The -R parameter specifies the directory of the translation rule while -r specifies the name of the rule file (rule.json in this case). 

Run the below python script to format the result so each log entry is on its own line.

```
python3 singleLine.py data/o365/o365_translated.json data/  o365_ocsf.json
```

To copy the translated file to your local, first run `exit`. Then run `sudo docker ps -a` and get the container id for the ocsf-cli image. Then run

```
sudo docker cp <ContainerID>:/app/o365_ocsf.json 
```





