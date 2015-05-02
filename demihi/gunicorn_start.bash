#!/bin/bash

NAME="demihi"                                                               # Name of the application
DJANGODIR=/home/ekaradon/demihi                                             # Django project directory
SOCKFILE=/home/ekaradon/run/gunicorn.sock                                   # we will communicate using this unix socket
USER=ekaradon                                                               # the user to run as
NUM_WORKERS=3                                                               # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=demihi.settings.production                           # which settings file should Django use
DJANGO_WSGI_MODULE=demihi.wsgi                                              # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../p3/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ekaradon/p3/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-