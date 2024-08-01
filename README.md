# ocsf-translation-tools
This repo builds off of the [official OCSF Java Tools](https://github.com/ocsf/ocsf-java-tools) repo to allow the ocsf-cli to run in a standalone docker container.

## Using the Docker Container
If you have already cloned the repository, you can build the docker image with:

```
sudo docker build -t ocsf-cli .
```

Note: If you have Java installed, feel free to experiment with the parsers in in the ocsf-parsers folder to try; to modify or make your own parers. Once you are done making changes be sure to run `./gradlew build` and then rebuild the container with the command above.


The `data/` folder contains sample, anonymized Office365 and Box logs. In this example, these logs will be converted into the File Hosting Activity OCSf class. See the rule.json files within the `data/` folder that specify the mapping from source to the OCSF standard. 

You can use Docker volumes to store and translate logs. First run

```
sudo docker run -d -v data-volume:/data --name temp ubuntu
```

This starts a temporary container with a volume named data-volume. Next copy data into the volume using 

```
sudo docker cp data/o365 temp:/data && sudo docker cp data/box temp:/data
```

Now we can use the volume with our ocsf-cli container. Run the below command to open a bash shell in the container. 

```
sudo docker run -it -v data-volume:/app/data ocsf-cli /bin/bash
```

Try simply running `ocsf-cli` in the shell to see the usage info. To convert the O365 logs run:

```
ocsf-cli -s lib/schema.json -R data/o365/ -r rule.json data/o365/logs/ > data/o365/o365_translated.json
```
The `-R` parameter specifies the directory of the translation rule while `-r` specifies the name of the rule file (rule.json in this case). 

Run the below python script to format the result so each log entry is on its own line.

```
python3 singleLine.py data/o365/o365_translated.json data/  o365_ocsf.json
```

To copy the translated file to your local, first run `exit`. Then run `sudo docker ps -a` and get the container id for the ocsf-cli image. Then run

```
sudo docker cp <ContainerID>:/app/o365_ocsf.json 
```

Now the o365_ocsf.json file is ready to be uploaded into Gravwell or another SIEM for analysis. Note that all of fields to be queried are now specified by the File Hosting Activity OCSF class.

## Updating this project
The dockerfile for this project first copies the .jar files from the ocsf-cli, ocsf-parers, ocsf-schema, ocsf-translator and ocsf-utils folders. In the ocsf-cli.sh script, allof these .jars are added to the Java classpath, allowing the ocsf-cli to be invoked.

If the code in any of these folders is changed, then the project must be rebuit with `./gradlew build` and the docker container must also be rebuilt.

The upstream repository for this project is the [official OCSF Java Tools](https://github.com/ocsf/ocsf-java-tools). The upstream repository should periodically be merged into this project.


