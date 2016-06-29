Name:       nmon
Summary:    nmon - performance monitoring tool for Linux
Version:    3.9.8
Release:    1
Group:      Utilities
License:    GNU/GPL
Requires:   ncurses
BuildRequires:  ncurses-devel

%description
nmon is a systems administrator, tuner, benchmark tool.
It can display the CPU, memory, network, disks (mini graphs or numbers),
file systems, NFS, top processes, resources (Linux version & processors) and
on Power micro-partition information.

Data is displayed on the screen and updated once every two seconds, using a
dumb screen. However, you can easily change this interval to a longer or
shorter time period.

The nmon tool can also capture the same data to a text file for later analysis
and graphing for reports. The output is in a spreadsheet format (.csv).

%build
gcc -g -D JFS -D GETUSER -Wall -D LARGEMEM -D POWER -D KERNEL_2_6_18 lmon16f.c -o nmon -lcurses -lm

%install
mkdir -p %{buildroot}/usr/bin/
cp -a nmon %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/nmon
