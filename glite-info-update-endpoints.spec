Name:		glite-info-update-endpoints
Version:	2.0.14
Release:	1%{?dist}
Summary:	Updates LDAP endpoins for EGI and OSG
Group:		Development/Libraries
License:	ASL 2.0
URL:		https://github.com/EGI-Foundation/glite-info-update-endpoints
Source:		%{name}-%{version}.src.tgz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Updates LDAP endpoins for EGI and OSG

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%post
if [ ! -f /var/cache/glite/top-urls.conf ]; then
   /usr/bin/glite-info-update-endpoints -c /etc/glite/glite-info-update-endpoints.conf > /var/log/glite/glite-info-update-endpoints.log 2>&1
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /etc/glite/
%dir /var/log/glite/
%dir /var/cache/glite/
%dir /usr/share/doc/glite-info-update-endpoints
%config(noreplace) /etc/glite/glite-info-update-endpoints.conf
/usr/bin/glite-info-update-endpoints
/etc/cron.hourly/glite-info-update-endpoints
/var/cache/glite/glite-info-update-endpoints
%doc /usr/share/doc/glite-info-update-endpoints/README.md
%doc /usr/share/doc/glite-info-update-endpoints/AUTHORS
%doc /usr/share/doc/glite-info-update-endpoints/COPYRIGHT
%doc /usr/share/doc/glite-info-update-endpoints/LICENSE.txt

%changelog

* Mon Aug 27 2018 Baptiste Grenier <baptiste.grenier@egi.eu> - 2.0.14-1
- Updated OSG URL (vokac)
- Bug GitHub #1: Silent fail on CentOS 7 when not able to validate GOCDB certificate (vokac)
- Update build, documetation and link to new GitHub repository (Baptiste Grenier)

* Thu Aug 01 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.13-1
- Updated URL
- BUG #99322: Error when manual file does not exist

* Wed Apr 24 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.12-2
- Added Source URL information

* Wed Nov 21 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.12-1
- BUG #98983: Improve error handling in glite-info-update-endpoints 

* Tue Sep 11 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.11-1
- BUG #96484: Fixed post install actions
- BUG #97395: Fixed rpmlint errors

* Mon May 25 2012 Laurence Field <laurence.field@cern.ch> - 2.0.10-1
- Changed the location of top-urls.conf to address GGUS #73823

* Mon Apr 19 2012 Laurence Field <laurence.field@cern.ch> - 2.0.9-1
- Added random sleep to cronjob to address GGUS #81404 

* Mon Mar 28 2011 Laurence Field <laurence.field@cern.ch> - 2.0.8-1
- Addressed IS-228

* Fri Aug 20 2010 Laurence Field <laurence.field@cern.ch> - 2.0.3-1
- Refactored version that queries the GOCs directly
