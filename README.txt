Steps to setup auzre Virtual Machines and measure bandwidth:
Measured 3 scenarios:
1) default : Standard_F2s_v3 - 2vcpus and 8GiB Memory - In same virtual Network in same regions
2) default : Standard_F2s_v3 - 2vcpus and 8GiB Memory - In differenct virtual Network in same regions
3) default : Standard_F2s_v2 - 2vcpus and 8GiB Memory - In differenct virtual Network in different regions
Considering Standard_F2s_v2:
	1) create VM in Azure portal
		- give password as security
		- enable SSH, HTTP, and HTTPS connections
    - give option to allow in bound ports for TCP on 8080 for all virtual machines.
	2) conect to VM in Mac( command prompt ) and Windows ( Putty ):
		Server and client:
			ssh <username>@<ipaddress>
	4) install all iperf3 in both server and clent:
		sudo apt-get update -y
		sudo apt-get install -y iperf3
	5) run below commands:
		server : iperf3 -s -p 8080 > {outputfile name} &
		client : iperf3 -c {ip address of server} -p 8080 -bidir -i 1 -t 5 >> {outputfile name} &    --- For 5 seconds streams of iperf test
             iperf3 -c {ip address of server} -p 8080 -bidir -i 1 -t 10 >> {outputfile name} &    --- For 10 seconds streams of iperf test
                  Run below python file in client to achieve sleep of 30 seconds in between
             python run_iperf.py
	6) run the clent command to save all bandwith values in background


Latency measurement:

For running tcp dump
client:
sh measure_latency.sh &
Server we are suming iperf is running
leter once you get the data after the above command completes, run below python file to get average of all latency in milliseconds
python measure_latency.py

To extract all the values for graphs run below python files
python measure_bandwidth.py
python measure_retranmissions.py



Below is the table mapping for output filenames and secraios:

For 5 seconds streams of iperf test 

Scenario -> File name
Client side output log - Same Region and Same Vnet -> SameVnetClient.txt
Client side output log - Same Region and Different Vnet -> DiffVnetClient.txt
Client side output log - Different Region and Different Vnet -> DiffVnetRegionClient.txt
Server side output log - Same Region and Same Vnet -> SameVnetServer.txt
Server side output log - Same Region and Different Vnet -> DiffVnetServer.txt
Server side output log - Different Region and Different Vnet -> DiffVnetRegionServer.txt



For 10 seconds streams of iperf test 

Scenario -> File name
Client side output log - Same Region and Same Vnet -> f_client_same_vnet.txt
Client side output log - Same Region and Different Vnet -> f_client_diff_vnet.txt
Client side output log - Different Region and Different Vnet -> f_client_diff_region.txt
Server side output log - Same Region and Same Vnet -> f_server_same_vnet.txt
Server side output log - Same Region and Different Vnet -> f_server_diff_vnet.txt
Server side output log - Different Region and Different Vnet -> f_server_diff_vnet_diff_region.txt


