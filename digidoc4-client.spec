# TODO
# - obsolete qesteidutil?
#
# Conditional build:
%bcond_without	kde			# Install KDE service menu
%bcond_without	nautilus	# Build Nautilus extension

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
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5ScriptTools-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.5
BuildRequires:	libdigidocpp-devel >= 3.13.8
BuildRequires:	pcsc-lite-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DigiDoc4 Client is an application for digitally signing and encrypting
documents; the software includes functionality to manage Estonian
ID-card - change pin codes, update certificates etc.

%package kde
Summary:	KDE service menu
Group:		X11/Applications
BuildArch:	noarch

%description kde
KDE service menu.

%package -n nautilus-extension-%{name}
Summary:	Nautilus extension
Group:		X11/Applications
BuildArch:	noarch

%description -n nautilus-extension-%{name}
Nautilus extension.

%prep
%setup -qc
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	-DENABLE_KDE=%{!?with_kde:OFF}%{?with_kde:ON} \
	-DENABLE_NAUTILUS_EXTENSION=%{!?with_nautilus:OFF}%{?with_nautilus:ON} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with nautilus}
%find_lang nautilus-qdigidoc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database

%postun
%update_icon_cache hicolor
%update_mime_database

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

%if %{with kde}
%files kde
%defattr(644,root,root,755)
%{_datadir}/kde4/services/qdigidoc-signer.desktop
%endif

%if %{with nautilus}
%files -n nautilus-extension-%{name} -f nautilus-qdigidoc.lang
%defattr(644,root,root,755)
%{_datadir}/nautilus-python/extensions/nautilus-qdigidoc.py
%endif
