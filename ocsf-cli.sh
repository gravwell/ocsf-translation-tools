APP_HOME=/app
CLASSPATH=$APP_HOME/lib/*
JAVACMD=java
set -- \
        -classpath "$CLASSPATH" \
        io.ocsf.schema.cli.Main \
        "$@"

exec "$JAVACMD" "$@"