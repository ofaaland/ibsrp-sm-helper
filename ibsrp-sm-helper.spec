##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##

Name: ibsrp-sm-helper
Summary: IBSRP SM helper
Version: 0.1
Release: 0%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Helper to start an SM on IB interfaces using SRP
URL: https://github.com/ofaaland/ibsrp-sm-helper
Packager: Olaf Faaland <faaland1@llnl.gov>
Source: %{name}-%{version}-%{release}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: systemd
Requires: opensm

%description
IBSRP SM starts an instance of OpenSM on each port used for SRP, which is
required for the ibsrp kernel driver to communicate with the attached storage
controller.

%prep
%setup -n %{name}-%{version}-%{release}

%install
rm -rf %{buildroot}
mkdir %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}/
mkdir -p %{buildroot}/%{_mandir}/man8/
mkdir -p %{buildroot}/%{_unitdir}/
cp -a ibsrp-sm-helper         %{buildroot}/%{_sbindir}/
cp -a ibsrp-sm-helper.8.gz    %{buildroot}/%{_mandir}/man8/
cp -a ibsrp-sm-helper.service %{buildroot}/%{_unitdir}/

%clean
rm -rf %{buildroot}

%post
/bin/systemctl enable ibsrp-sm-helper > /dev/null 2>&1 ||:

%preun
if [ "$1" = 0 ]; then
  systemctl stop ibsrp-sm-helper >/dev/null 2>&1 || :
  systemctl disable ibsrp-sm-helper > /dev/null 2>&1 || :
fi

%postun
if [ "$1" -ge 1 ]; then
  systemctl try-restart ibsrp-sm-helper >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%{_sbindir}/ibsrp-sm-helper
%{_mandir}/man8/ibsrp-sm-helper.8.gz
%{_unitdir}/ibsrp-sm-helper.service

%changelog
* Thu Mar 16 2017 Olaf Faaland <faaland1@llnl.gov> - 0.1-0ch6
- ibsrp-sm-helper initial version
- adapted from pragmatic-infiniband-utilities written by Ira Weiny
