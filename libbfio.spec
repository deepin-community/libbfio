Name: libbfio
Version: 20160108
Release: 1
Summary: Library to support (abstracted) basic file IO
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libbfio/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
          
          

%description
libbfio is a library to support (abstracted) basic file IO

%package devel
Summary: Header files and libraries for developing applications for libbfio
Group: Development/Libraries
Requires: libbfio = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libbfio.

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir}
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libbfio.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
* Fri Jan  8 2016 Joachim Metz <joachim.metz@gmail.com> 20160108-1
- Auto-generated

