%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	0.0
%define major	0
%define	libname	%mklibname	zapojit %{api} %{major}
%define	girname	%mklibname	zapojit-gir %{api}
%define	devname	%mklibname	zapojit	-d
%define _disable_rebuild_configure 1

Summary:	GLib/GObject wrapper for Skydrive and Hotmail
Name:		libzapojit
Version:	 0.0.3
Release:	11
License:	GPLv2+
Group:		System/Libraries
Url:		http://gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libzapojit/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(rest-0.7)

%description
Libzapojit is a GLib/GObject wrapper for Skydrive and Hotmail.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Libzapojit is a GLib/GObject wrapper for Skydrive and Hotmail.

This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains files needed for development with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libzapojit-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Zpj-%{api}.typelib

%files -n %{devname}
%dir %{_includedir}/libzapojit-%{api}
%dir %{_includedir}/libzapojit-%{api}/zpj
%{_includedir}/libzapojit-%{api}/zpj/*
%doc %{_datadir}/doc/%{name}/*
%{_datadir}/gtk-doc/html/libzapojit-%{api}/*
%{_datadir}/gir-1.0/Zpj-%{api}.gir
%{_libdir}/libzapojit-%{api}.so
%{_libdir}/pkgconfig/*

