#!/usr/bin/env bash

usage () {
  echo "Event Email Platform Liquibase";
  echo "===============================================================================";
  echo "usage: liquibase [-e] [-h]";
  echo "[mandatory] -e --env     <value>    Environment [unittest|local]";
  echo "[optional]  -s --seeder             Use seeder";
  echo "[optional]  -h --help               Help";
}

for arg in "$@"; do
  shift
  case "$arg" in
    "--env"       ) set -- "$@" "-e";;
    "--seeder"    ) set -- "$@" "-s";;
    "--help"      ) set -- "$@" "-h";;
    *             ) set -- "$@" "$arg"
  esac
done

changelog="event_email"
env="local"
use_seeder="false"

while getopts e:sh option; do
  case $option in
    (e)
      env=$OPTARG;;
    (s)
      use_seeder="true";;
    (h)
      usage;
      exit;;
    (*)
      echo "unknown option: "$option;
      usage;
      exit;;
  esac
done

docker run --rm -v $(pwd)/migrations/changelog:/liquibase/changelog -v $(pwd)/migrations/config:/liquibase/config \
  --link=postgres --entrypoint=/liquibase/liquibase liquibase/liquibase --logLevel=debug \
  --changeLogFile=changelog/"$changelog".postgres.sql --defaultsFile=/liquibase/config/"$env" \
  --defaultSchemaName="$changelog" update

if [ "$use_seeder" == "true" ]
  then
    docker run --rm -v $(pwd)/migrations/seed:/liquibase/seed -v $(pwd)/migrations/config:/liquibase/config \
      --link=postgres --entrypoint=/liquibase/liquibase liquibase/liquibase --logLevel=debug \
      --changeLogFile=seed/"$changelog".seeder.postgres.sql --defaultsFile=/liquibase/config/"$env" \
      --defaultSchemaName="$changelog" update
  fi
