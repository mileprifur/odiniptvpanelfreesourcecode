# Odin IpTV Panel Free Source Code
Require python 3.10+ and python requests module
For install python 3.10+

This installer works on Ubuntu, CentOS, Fedora and Debian all stable versions maintained.

The installer is still in development.
Please wait for this message to be erased
or install at your own risk and danger.

## Ubuntu 24.04 Support

```
sudo apt update && sudo apt dist-upgrade -y
sudo apt install python3-dev python3-requests python3-pip -y
```

## Ubuntu 22.04

```
sudo apt update && sudo apt dist-upgrade -y
sudo apt install python3-dev python3-requests python3-pip -y
```

## Ubuntu 20.04 use ppa

```
sudo apt update && sudo apt dist-upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.10-dev -y
wget https://bootstrap.pypa.io/get-pip.py -O $HOME/get-pip.py
sudo python3.10 $HOME/get-pip.py
sudo sed -i 's|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin|Defaults    secure_path = /usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin|' /etc/sudoers
sudo pip3.10 install --upgrade pip setuptools wheel
sudo pip3.10 install requests
```

For Fedora 37/38/39 and 40

```
sudo dnf -y install python3.10-devel
wget https://bootstrap.pypa.io/get-pip.py -O $HOME/get-pip.py
sudo python3.10 $HOME/get-pip.py
sudo sed -i 's|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin|Defaults    secure_path = /usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin|' /etc/sudoers
sudo pip3.10 install --upgrade pip setuptools wheel
sudo pip3.10 install requests
```

manual build for Centos

```
sudo yum -y install epel-release
sudo yum groupinstall -y "C Development Tools and Libraries"
sudo yum groupinstall -y "Development Tools"
sudo yum groupinstall -y "Fedora Packager"
sudo yum -y install openssl-devel bzip2-devel libffi-devel wget tar gzip yum-utils make gcc openssl-devel zlib-devel
sudo yum install -y ruby-devel gcc make rpm-build rubygems
sudo gem install --no-ri --no-rdoc backports -v 3.21.0
sudo gem install --no-ri --no-rdoc fpm -v 0.4.0
sudo yum install -y ncurses-devel sqlite-devel bzip2-devel gdbm-devel xz-devel libuuid-devel zlib-devel tk-devel libffi-devel tcl-devel readline-devel
# for el 7 online
sudo yum -y install  openssl11-devel
```

or for Ubuntu 18.04/Debian

```
sudo apt update && sudo apt dist-upgrade -y
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

python3.10 build

```
cd
rm -rf Python*
wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
tar -xzf Python-3.10.13.tgz
cd Python-3.10.13
# for el 7 online
sed -i 's/PKG_CONFIG openssl /PKG_CONFIG openssl11 /g' configure
sudo ./configure
sudo sed -i 's|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin|Defaults    secure_path = /usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin|' /etc/sudoers
sudo make -j ${nproc}
sudo make altinstall
cd
rm -rf Python*
sudo pip3.10 install --upgrade pip setuptools wheel
sudo pip3.10 install requests
```

To start installer for main or sub

```
sudo wget -O /root/install.py3  https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/install.py3 && sudo python3 /root/install.py3
```

Silent installer for main (recommended)

```
sudo wget -O /root/install-silent.py3  https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/install-silent.py3 && sudo python3 /root/install-silent.py3
```

Debug service not starting - stop all and check problem

```
# stop all
sudo kill $(ps aux | grep 'xtreamcodes' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 1
sudo kill $(ps aux | grep 'xtreamcodes' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sudo kill $(ps aux | grep 'xtreamcodes' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 1
sudo kill $(ps aux | grep 'xtreamcodes' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 1
# restart mariadb (use systemctl on Ubuntu 24.04+)
systemctl restart mariadb 2>/dev/null || service restart mariadb
# check php work
sudo -u xtreamcodes /home/xtreamcodes/iptv_xtream_codes/php/bin/php --version
# check nginx and nginx_rtmp
/home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx -version
/home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp -version
```

If error: sudo: /home/xtreamcodes/iptv_xtream_codes/php/bin/php: command not found

Full binary rebuild required

```
wget https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/depbuild.sh -O /root/depbuild.sh
bash /root/depbuild.sh
wget https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/php7.2rebuild.sh -O /root/php7.2rebuild.sh
bash /root/php7.2rebuild.sh
/home/xtreamcodes/iptv_xtream_codes/start_services.sh
```

If nginx and nginx_rtmp error - minimal rebuild required

```
wget https://github.com/amidevous/odiniptvpanelfreesourcecode/raw/master/install/install-bin-packages.sh -O /root/install-bin-packages.sh
bash /root/install-bin-packages.sh
/home/xtreamcodes/iptv_xtream_codes/start_services.sh
```

## Changes for Ubuntu 24.04

The codebase has been updated to support Ubuntu 24.04 with the following changes:

1. **Python 2→3 Migration**: All Python scripts now use Python 3 syntax (print function, urllib.request, base64 module, zip instead of izip)
2. **OpenSSL 3.x Support**: Nginx and PHP compilation scripts now detect Ubuntu 24.04 and use OpenSSL 3.0.x instead of 1.1.1h
3. **Systemd Compatibility**: Service management scripts now detect systemd and use systemctl commands where appropriate
4. **Docker Support**: Added `Dockerfile_Ubuntu-24.04` for containerized deployment
5. **Package Updates**: Updated package names for Ubuntu 24.04 (e.g., libcurl3→libcurl4, python-paramiko→python3-paramiko)
6. **Updated Dependencies**: All dependencies updated to versions compatible with Ubuntu 24.04's newer libraries