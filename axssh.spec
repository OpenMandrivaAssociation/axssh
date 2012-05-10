Name:         axssh
License:      GPL
Group:        Communications
Version:      0.4
Release:      1
Summary:      Secure login with linemode and ssh
Source0:      axssh-%{version}.tar.gz
Url:	      http://tools.assembla.com/svn/hamradio	      

%description
Axssh is a linemode wrapper for SSH via 
Amateur Packet Radio links

Authors:
--------
    Jörg Reuter <jreuter@yaina.de>

%prep
%setup -q -n axssh-%{version}

%build
%make

%install
install -d -m 755 %{buildroot}/%{_bindir}
install -d -m 755 %{buildroot}/%{_docdir}/%{name}
install -s -m 755 axssh %{buildroot}/%{_bindir}/
install -m 644 README %{buildroot}/%{_docdir}/%{name}

%files
%doc README
%{_bindir}/axssh
