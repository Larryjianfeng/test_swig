ps aux | grep z_server.py | awk '{print $2}' | xargs kill -9
ps aux | grep z_proxy.py | awk '{print $2}' | xargs kill -9

python z_proxy.py &

for i in `seq 1 3 `
    do
        python z_server.py &
    done


python client.py &
python client2.py & 

