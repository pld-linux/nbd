Summary:	Tools for using the Network Block Device
Summary(pl):	Narz�dzia do u�ywania Network Block Device
Name:		nbd
Version:	2.8.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/nbd/%{name}-%{version}.tar.bz2
# Source0-md5:	2a911e6499d9281b34ff904a446b1049
Patch0:		%{name}-types.patch
Patch1:		%{name}-gznbd.patch
URL:		http://nbd.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
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

%description -l pl
nbd zawiera narz�dzia potrzebne do wyeksportowania i u�ywania
sieciowego urz�dzenia blokowego (Network Block Device). Modu� do nbd
jest w j�drze 2.2 i p�niejszych.

Je�eli masz kernel z odpowiedni� �at�, mo�esz u�ywa� sieciowego
urz�dzenia blokowego do swapowania przez sie� - jest to przydatne w
przypadku stacji bezdyskowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-lfs

%{__make}

cd gznbd

%{__cc} %{rpmldflags} %{rpmcflags} -DMY_NAME='"gznbd"' -Wall -o gznbd gznbd.c -lz

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gznbd/gznbd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nbd-server
%attr(755,root,root) %{_sbindir}/nbd-client
%attr(755,root,root) %{_sbindir}/gznbd
%{_mandir}/man[18]/*
