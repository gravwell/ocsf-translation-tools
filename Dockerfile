FROM openjdk:11
WORKDIR /app
LABEL org.opencontainers.image.source=https://github.com/gravwell/ocsf-translation-tools
LABEL org.opencontainers.image.title=ocsf-cli
LABEL org.opencontainers.image.documentation=https://github.com/gravwell/ocsf-translation-tools/blob/main/README.md
LABEL org.opencontainers.image.description="Provides a container of the OCSF CLI used to translate source data into the OCSF format"
RUN mkdir lib
COPY ocsf-cli/build/libs/ /app/lib
COPY ocsf-parsers/build/libs/ /app/lib
COPY ocsf-schema/build/libs/ /app/lib
COPY ocsf-translator/build/libs/ /app/lib
COPY ocsf-utils/build/libs/ /app/lib
COPY log4j-core-2.23.1.jar /app/lib
COPY log4j-api-2.23.1.jar /app/lib
COPY ocsf-cli.sh /app/lib
COPY schema.json /app/lib
COPY data/singleLine.py /app
RUN chmod +x /app/lib/ocsf-cli.sh
RUN echo "alias ocsf-cli=/app/lib/ocsf-cli.sh" >> ~/.bashrc



