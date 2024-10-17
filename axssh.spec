Summary:	Secure login with linemode and ssh
Name:		axssh
Version:	0.4
Release:	3
License:	GPLv2+
Group:		Communications
Url:		https://tools.assembla.com/svn/hamradio
Source0:	axssh-%{version}.tar.gz
Requires:	openssh-clients

%description
Axssh is a linemode wrapper for SSH via Amateur Packet Radio links.

%files
%doc README
%{_bindir}/axssh

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
install -d -m 755 %{buildroot}/%{_bindir}
install -d -m 755 %{buildroot}/%{_docdir}/%{name}
install -m 755 axssh %{buildroot}/%{_bindir}/
install -m 644 README %{buildroot}/%{_docdir}/%{name}

