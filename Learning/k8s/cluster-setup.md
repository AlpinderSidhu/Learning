# Cluster Setup (CRI-O)

<!--ts-->

- Setup Steps
  - [Prerequisites](#prerequisites)
  - [Initialize VM](#initialize-vm)
  - [Install Container Runtime](#install-container-runtime)

<!--te-->

### Prerequisites

Check Latest Instruction [here](https://kubernetes.io/docs/setup/production-environment/)

- A compatible Linux host. The Kubernetes project provides generic instructions for Linux distributions based on Debian and Red Hat, and those distributions without a package manager.
- 2 GB or more of RAM per machine (any less will leave little room for your apps).
- 2 CPUs or more.
- Full network connectivity between all machines in the cluster (public or private network is fine).
- Unique hostname, MAC address, and product_uuid for every node. See here for more details.
- Certain ports are open on your machines. See here for more details.
- Swap disabled. You MUST disable swap in order for the kubelet to work properly.
  For example, `sudo swapoff -a` will disable swapping temporarily. To make this change persistent across reboots, make sure swap is disabled in config files like `/etc/fstab`, `systemd.swap`, depending how it was configured on your system.

### Initialize VM

Initialize 3 VMs and assign static IPs to them

1. External (Master)

#### Master

> ```
> gcloud compute instances create kubemaster --project=temporal-kube-393320 --zone=us-central1-a --machine-type=e2-medium --network-interface=network-tier=PREMIUM,private-network-ip=10.128.0.2,stack-type=IPV4_ONLY,subnet=default --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=542149362096-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=kubemaster1,image=projects/centos-cloud/global/images/centos-7-v20230711,mode=rw,size=20,type=projects/temporal-kube-393320/zones/us-central1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any
> ```

2. Internal (Nodes/Minions)

#### Node 1

> ```
> gcloud compute instances create kubenode1 --project=temporal-kube-393320 --zone=us-central1-a --machine-type=e2-medium --network-interface=private-network-ip=10.128.0.7,stack-type=IPV4_ONLY,subnet=default,no-address --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=542149362096-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=kubemaster1,image=projects/centos-cloud/global/images/centos-7-v20230711,mode=rw,size=20,type=projects/temporal-kube-393320/zones/us-central1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any
> ```

#### Node 2

> ```
> gcloud compute instances create kubenode2 --project=temporal-kube-393320 --zone=us-central1-a --machine-type=e2-medium --network-interface=private-network-ip=10.128.0.8,stack-type=IPV4_ONLY,subnet=default,no-address --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=542149362096-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=kubemaster1,image=projects/centos-cloud/global/images/centos-7-v20230711,mode=rw,size=20,type=projects/temporal-kube-393320/zones/us-central1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any
> ```

Upon creating nodes. Go to `VPC Networks` to create the `static` IP addresses.

#### Create NAT

NAT is required to connect the internal VMs to the internet to download the container runtime. To create NAT.

- Navigate to `Cloud NAT` service
- Click on `CREATE CLOUD NAT GATEWAY` and add the required details.

### Install Container Runtime (CRI-O)

In this we are insalling the CRI-O on CENT OS. However, kubernetes support various container runtimes:

- containerd
- CRI-O
- Docker Engine
- Mirantis Container Runtime

1. Install container runtime on each node of the cluster. To install CRI-O, execute following commands.

```
sudo -i
export OS=CentOS_7
export VERSION=1.27
echo $OS
echo $VERSION
```

```
curl -L -o /etc/yum.repos.d/devel:kubic:libcontainers:stable.repo https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/devel:kubic:libcontainers:stable.repo --verbose
curl -L -o /etc/yum.repos.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.repo https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable:cri-o:$VERSION/$OS/devel:kubic:libcontainers:stable:cri-o:$VERSION.repo --verbose
yum install cri-o
```
