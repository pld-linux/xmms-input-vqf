Summary:	VQF plugin for xmms
Summary(pl):	Wtyczka odtwarzaj±ca pliki VQF dla xmms
Name:		xmms-input-vqf
Version:	0.9
Release:	7
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.csn.ul.ie/~mel/projects/linux/vqfplugin/vqfplugin-%{version}.tar.gz
# Source0-md5:	7153736f375ff34819c8b2bc7b503972
Patch0:		vqfplugin-gtkconfig.patch
Patch1:		vqfplugin-DESTDIR.patch
Patch2:		vqfplugin-compile.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows xmms to play VQF files.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê w formacie VQF.

%prep
%setup -q -n vqfplugin-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{xmms_input_plugindir}/*
