#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-screenshot
Version  : 3.30.0
Release  : 9
URL      : https://download.gnome.org/sources/gnome-screenshot/3.30/gnome-screenshot-3.30.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-screenshot/3.30/gnome-screenshot-3.30.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-screenshot-bin
Requires: gnome-screenshot-data
Requires: gnome-screenshot-license
Requires: gnome-screenshot-locales
Requires: gnome-screenshot-man
BuildRequires : appstream-glib-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)

%description
GNOME Screenshot
================
GNOME Screenshot is a small utility that takes a screenshot of the whole
desktop; the currently focused window; or an area of the screen.

%package bin
Summary: bin components for the gnome-screenshot package.
Group: Binaries
Requires: gnome-screenshot-data
Requires: gnome-screenshot-license
Requires: gnome-screenshot-man

%description bin
bin components for the gnome-screenshot package.


%package data
Summary: data components for the gnome-screenshot package.
Group: Data

%description data
data components for the gnome-screenshot package.


%package license
Summary: license components for the gnome-screenshot package.
Group: Default

%description license
license components for the gnome-screenshot package.


%package locales
Summary: locales components for the gnome-screenshot package.
Group: Default

%description locales
locales components for the gnome-screenshot package.


%package man
Summary: man components for the gnome-screenshot package.
Group: Default

%description man
man components for the gnome-screenshot package.


%prep
%setup -q -n gnome-screenshot-3.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536125033
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-screenshot
cp COPYING %{buildroot}/usr/share/doc/gnome-screenshot/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-screenshot

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-screenshot

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-screenshot.convert
/usr/share/applications/org.gnome.Screenshot.desktop
/usr/share/dbus-1/services/org.gnome.Screenshot.service
/usr/share/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
/usr/share/metainfo/org.gnome.Screenshot.metainfo.xml

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-screenshot/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/gnome-screenshot.1

%files locales -f gnome-screenshot.lang
%defattr(-,root,root,-)

