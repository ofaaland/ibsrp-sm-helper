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
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: systemd
Requires: opensm

%description
IBSRP SM helper starts an SM on each port used for SRP, which is required for the ibsrp kernel driver to communicate with the attached storage controller.

%prep
%setup -n %{name}-%{version}-%{release}

#%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/ibsrp-sm-helper
%{_mandir}/man8/ibsrp-sm-helper.8.gz

%changelog
* Thu Mar 16 2017 Olaf Faaland <faaland1@llnl.gov> - 0.1-0ch6
- ibsrp-sm-helper initial version
