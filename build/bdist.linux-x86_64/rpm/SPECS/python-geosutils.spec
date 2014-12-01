%define name python-geosutils
%define version 0.0.8
%define unmangled_version 0.0.8
%define unmangled_version 0.0.8
%define release 1

Summary: GeosUtils
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Lou Markovski <lou.markovski@gmail.com>
BuildRequires: rpm-build >= 4.8.0 python-sphinx10 = 1.0.8 python-unittest2 = 0.5.1 python-nose1.1 = 1.1.2 python-coverage = 4.0a0 python-GeographicLib == 1.38

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
/usr/bin/python setup.py build

%install
/usr/bin/python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
