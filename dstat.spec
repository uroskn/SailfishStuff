Name:       dstat
Summary:    Versatile resource statistics tool 
Version:    0.7.2
Release:    1
Group:      Utilities
License:    GNU/GPL
BuildArch:  noarch
Requires:   python >= 2.6.6

%description
Dstat is a versatile replacement for vmstat, iostat and ifstat. Dstat
overcomes some of the limitations of these programs and adds some
extra features.

%build

%install
mkdir -p %{buildroot}/usr/bin/
cp -a dstat %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/dstat