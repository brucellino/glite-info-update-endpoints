# gLite Update Endpoints

## Information sources in a distributed infrastructure

This provides a means to update information sources (site-bdii endpoints),
from a central repository.
Once central repository per infrastructure is expected, _i.e._ the global
operations database for that infrastructure.
These databases contain an overall topology of endpoints in a distributed
computing platform, with each resource containing one information index.
Any application needing to consume these resources needs to know the full
list of endpoints, which are kept in a top-level BDII.

This repository contains the script necessary to create the list of endpoints
for populating the top-BDII.
It is written in python and is executed periodically as a cron job.
This should be installed and configured on top-bdiis.
This is not expected to be executed by users, but rather should run in the
background.

## Description

This consists of a single **executable python script** which reads a **configuration file** and writes a **local cache** of the list of
information indices.

### Configuration file

A typical configuration file can be found in `etc/glite-info-update-endpoints.conf`:

```
[configuration]
EGI  = True
OSG = True
certification_status =  Certified
manual = False
manual_file =
output_file = /var/cache/glite/top-urls.conf
cache_dir = /var/cache/glite/glite-info-update-endpoints
```

These variables describe the following:

- `EGI` (bool) - Should we get the topology of the EGI infrastructure?
- `OSG` (bool) - Should we get the topology of the Open Science Grid (OSG) infrastructure ?
- `certification_status` (string) - Sites in the EGI or OSG databases are tagged with a "certification      status". This variable is defaulted to "Certified", to get only the production-grade sites. Other       options are:
  - `Uncertified`
- `manual` (bool) - It is possible to create a list of information sources manually - _i.e._ without contacting the central database. This is only used in edge cases, and in conjunction with `manual_file`
- `manual_file` (string) - The path ot the file which contains the manually-selected
- `output_file` (string) - The path (directory and file name) of the configuration file that is generated. This will be used by the         top-bdii, so it shouldn't be changed.
- `cache_dir` (string) - The path to where the top-urls will be written. This will be used by the         top-bdii, so it shouldn't be changed.

### Edge Cases

There are very few edge cases we can describe.
These are cases where you would want to change the configuration slightly in order to tweak the behaviour
of the updater.
These are included for completeness, but are rarely used.

<!-- describe edge case configurations here -->

  1. Including uncertified sites
  2. Using manual configuration
  3. Adding a new infrastructure

## Requirements

<!-- What is required to run this  -->
In order to use this, you will need a Python2 runtime environment.