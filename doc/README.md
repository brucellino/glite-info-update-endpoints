
glite-info-update-endpoints is a cron job that runs every hour to download
the list of site BDII URLs that are going to be used by the top level
BDII to publish their resources.

The script uses the /etc/glite/glite-info-update-endpoints.conf file which 
by default is configured to use the EGI and OSG list of site BDIIs. 
The list of site BDIIs is taken from the EGI and OSG GOCDBs.
