%include	/usr/lib/rpm/macros.python

%define         module Xlib

Summary:	X client library for Python
Summary(pl):	Biblioteka klienta X dla Pythona
Name:		python-%{module}
Version:	0.12
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/python-xlib/python-xlib-%{version}.tar.gz
# Source0-md5:	83b294f34876c06b1a7697227249cb83
URL:		http://python-xlib.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python X Library is intended to be a fully functional X client
library for Python programs. It is written entirely in Python, in
contrast to earlier X libraries for Python (the ancient X extension
and the newer plxlib) which were interfaces to the C Xlib.

This is possible to do since X client programs communicate with the X
server via the X protocol. The communication takes place over TCP/IP,
Unix sockets, DECnet or any other suitable streaming network protocol.
The C Xlib is merely an interface to this protocol, providing
functions suited for a C environment.

There are three advantages of choosing to implement a pure Python
library:
- Integration: The library can make use of the wonderful object system
  in Python, providing an easy-to-use class hierarchy.
- Portability: The library will be usable on (almost) any computer
  which have Python installed. A C interface could be problematic to
  port to non-Unix systems, such as MS Windows or OpenVMS.

%prep
%setup -q -n python-xlib-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

find $RPM_BUILD_ROOT%{py_sitedir}/%{module}/ -name \*.py | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%{py_sitedir}/%{module}/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
