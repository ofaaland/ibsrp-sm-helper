##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##

Name: srp_sm_helper
Summary: SRP SM helper
Version: 0.1
Release: 0%{?dist}
BuildArch: noarch
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Helper to start an SM on IB interfaces using SRP
URL: https://github.com/ofaaland/srp_sm_helper
Packager: Olaf Faaland <faaland1@llnl.gov>
Source: %{name}-%{version}-%{release}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: systemd
Requires: opensm

%description
srp_sm_helper starts an instance of OpenSM on each IB port used for SRP, which
is required for the ib_srp kernel driver to communicate with the attached
storage controller.

%prep
%setup -n %{name}-%{version}-%{release}

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_sbindir}/
install -d %{buildroot}/%{_mandir}/man8/
install -d %{buildroot}/%{_unitdir}/
install -m 755 srp_sm_helper         %{buildroot}/%{_sbindir}/
install -m 644 srp_sm_helper.8.gz    %{buildroot}/%{_mandir}/man8/
install -m 644 srp_sm_helper.service %{buildroot}/%{_unitdir}/

%clean
rm -rf %{buildroot}

%post
/bin/systemctl enable srp_sm_helper > /dev/null 2>&1 ||:

%preun
if [ "$1" = 0 ]; then
  systemctl stop srp_sm_helper >/dev/null 2>&1 || :
  systemctl disable srp_sm_helper > /dev/null 2>&1 || :
fi

%postun
if [ "$1" -ge 1 ]; then
  systemctl try-restart srp_sm_helper >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%{_sbindir}/srp_sm_helper
%{_mandir}/man8/srp_sm_helper.8.gz
%{_unitdir}/srp_sm_helper.service

%changelog
* Thu Mar 16 2017 Olaf Faaland <faaland1@llnl.gov> - 0.1-0ch6
- srp_sm_helper initial version
- adapted from pragmatic-infiniband-utilities written by Ira Weiny
