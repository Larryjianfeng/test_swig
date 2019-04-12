ps aux | grep z_server.py | awk '{print $2}' | xargs kill -9
ps aux | grep z_proxy.py | awk '{print $2}' | xargs kill -9
ps aux | grep client.py | awk '{print $2}' | xargs kill -9

sleep 1s

python z_proxy.py &

for i in `seq 1 3 `
    do
        python z_server.py $i &
    done


python client.py
