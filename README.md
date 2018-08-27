# glite-info-update-endpoints

This component is used with Top BDII and is intented to update LDAP endpoits for EGI and OSG.
BDII documentation is available here: https://gridinfo-documentation.readthedocs.io/

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:
- rpm-build
- make
- rsync

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/glite-info-update-endpoints.git
cd glite-info-update-endpoints
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

### Building a deb

**This is _not working_ as there is no debian directory.**

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/glite-info-update-endpoints.git
cd glite-info-update-endpoints
git checkout X.X.X
mkdir -p ~/debs/xenial
# Building in a container using the source files
docker run --rm -v $(pwd):/source -it ubuntu:xenial
apt update
apt install -y dpkg-dev make rsync
cd /source && make deb
```

## Installing from source

This procedure is not recommended for production deployment, please consider using packages.

Get the source by cloning this repo and do a `make install`.

## History

This work started under the EGEE project, and was hosted and maintained for a long time by CERN.
This is now hosted here on GitHub, maintained by the BDII community with support of members of the EGI Federation.
