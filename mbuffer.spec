Name:       mbuffer
Summary:    tool for buffering data streams
Version:    20160228
Release:    1
Group:      Utilities
License:    GNU/GPL

%description
The mbuffer tool is used to buffer data streams and show the I/O rate and
summary to the user.  It is especially useful for writing backups to
fast tape drives or streaming them over the network.  If used correctly,
it can prevent buffer underruns and speed up the whole backup or
transfer process.

%build
./configure --disable-md5
make 
 
%install
mkdir -p %{buildroot}/usr/bin/
cp -a mbuffer %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/mbuffer