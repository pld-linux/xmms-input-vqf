Summary:	VQF plugin for xmms
Summary(pl):	Wtyczka odtwarzaj±ca pliki VQF dla xmms
Name:		xmms-input-vqf
Version:	0.9
Release:	2
Group:		X11/Applications/Multimedia
License:	GPL
Source0:	http://www.csn.ul.ie/~mel/projects/linux/vqfplugin/vqfplugin-%{version}.tar.gz
Patch0:		vqfplugin-gtkconfig.patch
Patch1:		vqfplugin-DESTDIR.patch
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This plugin allows xmms to play VQF files.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê w formacie VQF.

%prep
%setup -q -n vqfplugin-%{version}
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure 

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf AUTHORS ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Input/*
