# Network Delay Measurement Tool

## 📌 Overview

This project measures and analyzes network delay (latency) between hosts using **Mininet** and **Software Defined Networking (SDN)**.

It uses the **ping command (ICMP protocol)** to calculate **RTT (Round Trip Time)** and demonstrates delay variation using network emulation.

---

## 🎯 Objectives

* Measure delay using ping
* Record RTT values
* Compare network behavior
* Analyze delay variations

---

## 🛠️ Technologies Used

* Python
* Mininet
* POX Controller
* OpenFlow
* Linux (Debian)

---

## 🧠 Concepts Used

* SDN (Software Defined Networking)
* Control Plane vs Data Plane
* Flow Tables (Match-Action)
* ICMP Protocol
* RTT (Round Trip Time)
* Packet-In Mechanism
* Network Emulation (tc netem)

---

## 🏗️ Network Topology

* 3 Hosts: h1, h2, h3
* 1 Switch: s1
* Remote Controller

---

## ⚙️ Setup & Execution

### 1. Start Controller

cd ~/pox
python3 pox.py forwarding.l2_learning

### 2. Start Mininet

sudo mn --topo single,3 --controller=remote

### 3. Measure Delay (Baseline)

h1 ping -c 5 h2

### 4. Introduce Artificial Delay

sh tc qdisc add dev s1-eth1 root netem delay 100ms

### 5. Measure Delay Again

h1 ping -c 5 h2

### 6. View Flow Table

sudo ovs-ofctl dump-flows s1

---

## 📊 Results

### 🔹 Network Topology

![Topology](screenshots/topology.png)

---

### 🔹 Ping Output (Baseline)

![Ping](screenshots/ping.png)

---

### 🔹 Delay After Adding Network Latency

![Delay Added](screenshots/delay_added.png)

---

### 🔹 Flow Table (SDN Rules)

![Flow Table](screenshots/flow_table.png)

---

## 📌 Key Observations

* The **first packet shows higher delay** due to controller interaction
* After flow rules are installed, **subsequent packets are faster**
* Artificial delay increased RTT from ~3 ms to ~100 ms
* Flow table confirms SDN-based forwarding

---

## 🧠 Explanation

* **Ping uses ICMP** to measure network delay
* **RTT** represents time taken for packet round trip
* In SDN:

  * First packet → sent to controller
  * Controller installs flow rule
  * Next packets → directly forwarded

---

## 🏁 Conclusion

This project demonstrates how network delay can be measured using RTT and how SDN dynamically controls packet forwarding. It also shows how network conditions impact latency.

---

## 👩‍💻 Author

Aarushi Singh
