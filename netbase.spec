#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netbase
Version  : 5.6
Release  : 20
URL      : https://mirrors.kernel.org/debian/pool/main/n/netbase/netbase_5.6.tar.xz
Source0  : https://mirrors.kernel.org/debian/pool/main/n/netbase/netbase_5.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: netbase-data = %{version}-%{release}
Requires: netbase-license = %{version}-%{release}
Patch1: 0001-Add-a-Makefile-to-the-package.patch
Patch2: 0002-Use-rpcbind-for-sunrpc-services.patch

%description
No detailed description available

%package data
Summary: data components for the netbase package.
Group: Data

%description data
data components for the netbase package.


%package license
Summary: license components for the netbase package.
Group: Default

%description license
license components for the netbase package.


%prep
%setup -q -n netbase-5.6
cd %{_builddir}/netbase-5.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604085120
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604085120
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/netbase
cp %{_builddir}/netbase-5.6/debian/copyright %{buildroot}/usr/share/package-licenses/netbase/473b4254e3bb9789f056d2ffbf21b5a855813f2a
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/protocols
/usr/share/defaults/etc/services

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/netbase/473b4254e3bb9789f056d2ffbf21b5a855813f2a
