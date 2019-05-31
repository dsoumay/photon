Summary:        Platform-neutral API
Name:           nspr
Version:        4.21
Release:        1%{?dist}
License:        MPLv2.0
URL:            http://ftp.mozilla.org/pub/mozilla.org
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://ftp.mozilla.org/pub/nspr/releases/v%{version}/src/%{name}-%{version}.tar.gz
%define sha1    nspr=0ae8c710a52775e209b96aa6220362837b79b6c3

%description
Netscape Portable Runtime (NSPR) provides a platform-neutral API
for system level and libc like functions.

%prep
%setup -q
cd nspr
sed -ri 's#^(RELEASE_BINS =).*#\1#' pr/src/misc/Makefile.in
sed -i 's#$(LIBRARY) ##' config/rules.mk

%build
cd nspr
%configure \
    --with-mozilla \
    --with-pthreads \
    $([ $(uname -m) = x86_64 ] && echo --enable-64bit) \
    --disable-silent-rules
make %{?_smp_mflags}

%install
cd nspr
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datarootdir}/aclocal/*

%changelog
*   Fri May 31 2019 Michelle Wang <michellew@vmware.com> 4.21-1
-   Upgrade to 4.21 for nss upgrade to 3.44
*   Tue Jun 20 2017 Xiaolin Li <xiaolinl@vmware.com> 4.15-1
-   Upgrade to 4.15.
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 4.12-2
-   GA - Bump release of all rpms
*   Thu Feb 25 2016 Kumar Kaushik <kaushikk@vmware.com> 4.12-1
-   Updated to version 4.12
*   Thu Jan 21 2016 Xiaolin Li <xiaolinl@vmware.com> 4.11-1
-   Updated to version 4.11
*   Fri May 29 2015 Alexey Makhalov <amakhalov@vmware.com> 4.10.8-1
-   Version update. Firefox requirement.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 4.10.3-1
-   Initial build. First version
