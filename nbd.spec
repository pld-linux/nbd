Summary:	Tools for using the Network Block Device
Summary(pl.UTF-8):	Narzędzia do używania Network Block Device
Name:		nbd
Version:	3.14
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/nbd/%{name}-%{version}.tar.xz
# Source0-md5:	fa29f57ca752e363edc15f0e35f0a95f
Source1:	nbd@.service.tmpl
Patch0:		%{name}-gznbd.patch
URL:		http://nbd.sourceforge.net/
BuildRequires:	docbook-dtd45-sgml
BuildRequires:	docbook-utils
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.26.0
Obsoletes:	nbd-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
nbd contains the tools needed to export a network block device and to
use a network block device. The nbd module is part of the 2.2 kernels
and higher.

If you have a kernel patched for it, you can use the network block
device to swap over the net, which is particularly useful for diskless
workstations.

%description -l pl.UTF-8
nbd zawiera narzędzia potrzebne do wyeksportowania i używania
sieciowego urządzenia blokowego (Network Block Device). Moduł do nbd
jest w jądrze 2.2 i późniejszych.

Jeżeli masz kernel z odpowiednią łatą, możesz używać sieciowego
urządzenia blokowego do swapowania przez sieć - jest to przydatne w
przypadku stacji bezdyskowych.

%prep
%setup -q
%patch0 -p1

test ! -f systemd/nbd@.service.tmpl
cp %{SOURCE1} systemd

%build
%configure \
	--enable-gznbd \
	--enable-lfs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/nbd-server

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/gznbd
%attr(755,root,root) %{_bindir}/nbd-server
%attr(755,root,root) %{_bindir}/nbd-trdump
%attr(755,root,root) %{_sbindir}/nbd-client
%dir %{_sysconfdir}/nbd-server
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nbd-server/config
%{_mandir}/man1/nbd-server.1*
%{_mandir}/man1/nbd-trdump.1*
%{_mandir}/man5/nbd-server.5*
%{_mandir}/man5/nbdtab.5*
%{_mandir}/man8/nbd-client.8*
