Summary:        Code coverage measurement for Python.
Name:           python3-coverage
Version:        5.3
Release:        3%{?dist}
License:        Apache 2.0
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/coverage
Source0:        https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
%define         sha1 coverage=0931102f6bfdfd021f9c0488a88950721d9a111b

BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with_check}
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
BuildRequires:  iana-etc
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  python3-pytest
BuildRequires:  python3-six
%endif

%description
Code coverage measurement for Python.
Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

%prep
%autosetup -n coverage-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
LANG=en_US.UTF-8 tox -e py36

%files
%defattr(-,root,root)
%{python3_sitelib}/*
%{_bindir}/coverage
%{_bindir}/coverage3
%{_bindir}/coverage-%{python3_version}

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 5.3-3
-   Bump up to compile with python 3.10
*   Tue Sep 29 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 5.3-2
-   openssl 1.1.1
*   Mon Sep 21 2020 Gerrit Photon <photon-checkins@vmware.com> 5.3-1
-   Automatic Version Bump
*   Wed Aug 26 2020 Gerrit Photon <photon-checkins@vmware.com> 5.2.1-1
-   Automatic Version Bump
*   Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 4.5.1-3
-   Mass removal python2
*   Mon Oct 21 2019 Shreyas B. <shreyasb@vmware.com> 4.5.1-2
-   Fixed makecheck errors.
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 4.5.1-1
-   Updated to 4.5.1
*   Thu Aug 10 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.4-5
-   Fixed make check errors
*   Fri Jul 07 2017 Chang Lee <changlee@vmware.com> 4.3.4-4
-   Add python-xml and pyhton3-xml to  Requires.
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.4-3
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 4.3.4-2
-   Packaging python2 and oython3 scripts in bin directory
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.4-1
-   Initial packaging for Photon
