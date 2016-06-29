Name:       netcat
Summary:    TCP/IP Swiss Army Knife 
Version:    1.10.41
Release:    1
Group:      Utilities
License:    GNU/GPL

%description
A simple Unix utility which reads and writes data across network
connections using TCP or UDP protocol. It is designed to be a reliable
"back-end" tool that can be used directly or easily driven by other
programs and scripts. At the same time it is a feature-rich network
debugging and exploration tool, since it can create almost any kind
of connection you would need and has several interesting built-in
capabilities.

%build
make clean
make linux DFLAGS='-DLINUX -DTELNET -DGAPING_SECURITY_HOLE -DIP_TOS -DDEBIAN_VERSION=\"1.10-41\"'

%install
mkdir -p %{buildroot}/usr/bin/
cp -a nc %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/nc