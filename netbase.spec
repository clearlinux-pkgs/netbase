Name:           netbase
Version:        5.3
Release:        7
License:        GPL-2.0
Summary:        Basic TCP/IP networking support
Url:            http://packages.debian.org/netbase
Group:          base
Source0:        ftp://ftp.debian.org/debian/pool/main/n/netbase/netbase_5.3.tar.xz
BuildRequires:  filesystem >= 3.0.14-44
Requires:       filesystem >= 3.0.14-44
Requires:       nss-altfiles

%description
Basic TCP/IP networking support.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/defaults%{_sysconfdir}
install -m 0644 etc-protocols %{buildroot}%{_datadir}/defaults%{_sysconfdir}/protocols
install -m 0644 etc-services %{buildroot}%{_datadir}/defaults%{_sysconfdir}/services

%files
%{_datadir}/defaults%{_sysconfdir}/*
