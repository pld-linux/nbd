Summary:	Tools for using the Network Block Device
Summary(pl):	Narzêdzia do u¿ywania Network Block Device
Name:		nbd
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/nbd/%{name}-%{version}.tar.gz
# Source0-md5:	8364e916d4464fbec2132709c67b868c
URL:		http://nbd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nbd contains the tools needed to export a network block device and to
use a network block device. The nbd module is part of the 2.2 kernels
and higher.

If you have a kernel patched for it, you can use the network block
device to swap over the net, which is particularly useful for diskless
workstations.

%description -l pl
nbd zawiera narzêdzia potrzebne do wyeksportowania i u¿ywania
sieciowego urz±dzenia blokowego (Network Block Device). Modu³ do nbd
jest w j±drze 2.2 i pó¼niejszych.

Je¿eli masz kernel z odpowiedni± ³at±, mo¿esz u¿ywaæ sieciowego
urz±dzenia blokowego do swapowania przez sieæ - jest to przydatne w
przypadku stacji bezdyskowych.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

db2man nbd-client.8.sgml
db2man nbd-server.1.sgml

cd gznbd

%{__cc} %{rpmldflags} %{rpmcflags} -Wall -o gznbd gznbd.c -lz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir},%{_mandir}/man{1,8}}

install nbd-client $RPM_BUILD_ROOT/sbin
install nbd-server $RPM_BUILD_ROOT%{_sbindir}
install gznbd/gznbd $RPM_BUILD_ROOT%{_sbindir}

install NBD-CLIENT.8 $RPM_BUILD_ROOT%{_mandir}/man8/nbd-client.8
install NBD-SERVER.1 $RPM_BUILD_ROOT%{_mandir}/man1/nbd-server.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/nbd-client
%attr(755,root,root) %{_sbindir}/nbd-server
%attr(755,root,root) %{_sbindir}/gznbd
%{_mandir}/man[18]/*
