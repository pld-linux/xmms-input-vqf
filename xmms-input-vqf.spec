Summary:	VQF plugin for XMMS
Summary(pl):	Wtyczka wej�ciowa dla XMMS-a odtwarzaj�ca pliki VQF
Name:		xmms-input-vqf
Version:	0.94
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.csn.ul.ie/~mel/projects/linux/vqfplugin/vqfplugin-%{version}.tar.gz
# Source0-md5:	ce4f77b94303db473cc15aabf91649b5
Patch1:		vqfplugin-DESTDIR.patch
URL:		http://www.csn.ul.ie/~mel/projects/linux/vqfplugin/
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
Ta wtyczka pozwala XMMS-owi odtwarza� muzyk� w formacie VQF.

%prep
%setup -q -n vqfplugin-%{version}
%patch1 -p1

%build
echo "#" > vqfinfo/Makefile.am
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	CC="%{__cc}"

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
