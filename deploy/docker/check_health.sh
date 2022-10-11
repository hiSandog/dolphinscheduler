#!/bin/bash

worker_name="node2_dolphinscheduler-worker_1"
docker_dir="/opt/dolphin3.0.1/docker/node2"
log_dir="/opt/dolphin3.0.1/log"


curr_date=$(date "+%Y%m%d%H%M%S")
restart_master=0
restart_worker=0

worker_id=$(docker ps | grep dolphinscheduler-worker | awk '{print $1}')
master_id=$(docker ps | grep dolphinscheduler-master | awk '{print $1}')

worker_unhealthy=$(docker ps | grep dolphinscheduler-worker | grep unhealthy)
master_unhealthy=$(docker ps | grep dolphinscheduler-master | grep unhealthy)

if [ "$worker_id" ]
    then
    if [ "$worker_unhealthy" ]
        then
            echo "docker stop worker"
            docker stop "$worker_id"
            touch "$log_dir"/stop_worker_"$curr_date"
            restart_worker=1
    fi
    else
    restart_worker=1
fi

if [ "$master_id" ]
    then
    if [ "$master_unhealthy" ]
        then
            echo "docker stop master"
            docker stop "$master_id"
            touch "$log_dir"/stop_master_"$curr_date"
            restart_master=1
    fi
    else
    restart_master=1
fi

cd "$docker_dir"
pwd

if [ $restart_master -eq 1 -o $restart_worker -eq 1 ]
    then
        echo "docker-compose up -d"
        docker-compose up -d
        touch "$log_dir"/docker_compose_up_"$curr_date"
fi

if [ $restart_worker -eq 1 ]
    then
        echo "restart worker"
        docker exec -it $worker_name sh /deploy_script/worker_deploy.sh
        touch "$log_dir"/restart_worker_"$curr_date"
fi
