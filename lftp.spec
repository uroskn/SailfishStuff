Name:       lftp
Summary:    lftp - a file retrieving tool 
Version:    4.7.1
Release:    1
Group:      Utilities
License:    GNU/GPL
Requires:   ncurses 
Requires:   readline
Requires:   zlib
Requires:   openssl
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel 
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  bison
BuildRequires:  gettext

%description
Lftp is a file retrieving tool that supports FTP, HTTP, FISH, SFTP, HTTPS,
FTPS and BitTorrent protocols under both IPv4 and IPv6. Lftp has an amazing
set of features, while preserving its interface as simple and easy as possible.

%build
./configure --without-gnutls --with-openssl --prefix=/usr --sysconfdir=/etc \
            --with-pager=/usr/bin/less
make all
 
%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/lftp/
cp -a src/lftp %{buildroot}/usr/bin/
cp -a src/{convert-mozilla-cookies,xdg-move,import-netscape,import-ncftp,verify-file} %{buildroot}/usr/share/lftp

%files
%defattr(-,root,root,-)
/usr/bin/lftp
/usr/share/lftp/convert-mozilla-cookies
/usr/share/lftp/xdg-move
/usr/share/lftp/import-netscape
/usr/share/lftp/import-ncftp
/usr/share/lftp/verify-file