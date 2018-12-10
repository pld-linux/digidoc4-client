# TODO
# - obsolete qesteidutil?
Summary:	DigiDoc4 Client
Name:		digidoc4-client
Version:	4.2.0.43
Release:	0.1
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://github.com/open-eid/DigiDoc4-Client/releases/download/v4.2.0/qdigidoc4_%{version}.orig.tar.xz
# Source0-md5:	69008db6002270e981b0685e4330511c
Patch0:		cmake.patch
Patch1:		LibDigiDocpp-required.patch
URL:		https://github.com/open-eid/DigiDoc4-Client
BuildRequires:	Qt5ScriptTools-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	libdigidocpp-devel >= 3.13.8
BuildRequires:	pcsc-lite-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DigiDoc4 Client is an application for digitally signing and encrypting
documents; the software includes functionality to manage Estonian
ID-card - change pin codes, update certificates etc.

%prep
%setup -qc
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.md RELEASE-NOTES.md
%attr(755,root,root) %{_bindir}/qdigidoc4
%{_mandir}/man1/qdigidoc4.1*
%{_desktopdir}/qdigidoc4.desktop
%{_iconsdir}/hicolor/*/apps/qdigidoc4.png
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.etsi.asic-e+zip.png
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.etsi.asic-s+zip.png
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.lt.archyvai.adoc-2008.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-cdoc.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-ddoc.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-p12d.png
%{_datadir}/mime/packages/qdigidoc4.xml
