Name:       htop
Summary:    htop - interactive processes viewer
Version:    2.0.1
Release:    1
Group:      Utilities
License:    GNU/GPL
Requires:   ncurses
BuildRequires:  ncurses-devel

%description
Htop is an ncursed-based process viewer similar to top, but it
allows one to scroll the list vertically and horizontally to see
all processes and their full command lines.

Tasks related to processes (killing, renicing) can be done without
entering their PIDs.

%build
./configure --enable-cgroup --enable-taskstats --enable-linux-affinity --enable-proc --disable-unicode
make

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/icons/hicolor/86x86/apps/
cp -a htop %{buildroot}/usr/bin/
cp rpm/htop.desktop %{buildroot}/usr/share/applications/htop.desktop
cp rpm/htop.png     %{buildroot}/usr/share/icons/hicolor/86x86/apps/htop.png

%files
%defattr(-,root,root,-)
/usr/bin/htop
/usr/share/applications/htop.desktop
/usr/share/icons/hicolor/86x86/apps/htop.png
