%define	api	0.0
%define major	0
%define	libname	%mklibname	zapojit %{api} %{major}
%define	girname	%mklibname	zapojit-gir %{api} 
%define	devname	%mklibname	zapojit	-d

Summary:	GLib/GObject wrapper for Skydrive and Hotmail
Name:		libzapojit
Version:	0.0.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://gnome.org	
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.0/%{name}-%{version}.tar.xz

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
%{_libdir}/girepository-1.0/Zpj-0.0.typelib

%files -n %{devname}
%dir %{_includedir}/libzapojit-%{api}
%dir %{_includedir}/libzapojit-%{api}/zpj
%{_includedir}/libzapojit-%{api}/zpj/*
%doc %{_datadir}/doc/%{name}/*
%{_datadir}/gtk-doc/html/libzapojit-%{api}/*
%{_datadir}/gir-1.0/Zpj-0.0.gir
%{_libdir}/libzapojit-%{api}.so
%{_libdir}/pkgconfig/*



%changelog
* Tue Oct 16 20012 Arkady L. Shane <ashejn@rosalab.ru> 0.0.2-1
- update to 0.0.2

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.1-1
+ Revision: 801478
- imported package libzapojit

