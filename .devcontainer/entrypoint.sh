#!/bin/sh

NONROOT_USER=dist

sudoIf() { 
    if [ "$(id -u)" -ne 0 ]
      then
        sudo "$@"
      else
        "$@"
    fi
}

SOCKET_GID=$(stat -c '%g' /var/run/docker.sock) 

if [ "${SOCKET_GID}" != '0' ]
  then
    if [ "$(cat /etc/group | grep :${SOCKET_GID}:)" = '' ]
      then 
        sudoIf groupadd --gid ${SOCKET_GID} docker-host; 
    fi 

    if [ "$(id $NONROOT_USER | grep -E "groups=.*(=|,)${SOCKET_GID}\(")" = '' ]
      then
        sudoIf usermod -aG ${SOCKET_GID} $NONROOT_USER
    fi
fi
exec "$@"
