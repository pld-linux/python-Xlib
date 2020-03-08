#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (SECURITY test seem to fail)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	Xlib

Summary:	X client library for Python 2
Summary(pl.UTF-8):	Biblioteka klienta X dla Pythona 2
Name:		python-%{module}
Version:	0.26
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
#Source0Download: https://github.com/python-xlib/python-xlib/releases
Source0:	https://github.com/python-xlib/python-xlib/releases/download/%{version}/python-xlib-%{version}.tar.bz2
# Source0-md5:	678871a692c5409a6d6b5aaaf7f6e60d
URL:		https://github.com/python-xlib/python-xlib
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools >= 30.3.0
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-six >= 1.10.0
BuildRequires:	xorg-xserver-Xvfb
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools >= 30.3.0
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-nose
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	xorg-xserver-Xvfb
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	texi2html
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python X Library is intended to be a fully functional X client
library for Python programs. It is written entirely in Python, in
contrast to earlier X libraries for Python (the ancient X extension
and the newer plxlib) which were interfaces to the C Xlib.

%description -l pl.UTF-8
Python X Library (biblioteka X dla Pythona) ma być w pełni
funkcjonalną biblioteką kliencką X dla programów w Pythonie. Jest
napisana całkowicie w Pythonie, w przeciwieństwie do poprzednich
bibliotek X dla Pythona (starego rozszerzenia X i nowszej plxlib),
które były interfejsami do Xlib w C.

%package -n python3-%{module}
Summary:	X client library for Python 3
Summary(pl.UTF-8):	Biblioteka klienta X dla Pythona 3
Group:		Development/Languages/Python
Requires:	python3-devel >= 1:3.3

%description -n python3-%{module}
The Python X Library is intended to be a fully functional X client
library for Python programs. It is written entirely in Python, in
contrast to earlier X libraries for Python (the ancient X extension
and the newer plxlib) which were interfaces to the C Xlib.

%description -n python3-%{module} -l pl.UTF-8
Python X Library (biblioteka X dla Pythona) ma być w pełni
funkcjonalną biblioteką kliencką X dla programów w Pythonie. Jest
napisana całkowicie w Pythonie, w przeciwieństwie do poprzednich
bibliotek X dla Pythona (starego rozszerzenia X i nowszej plxlib),
które były interfejsami do Xlib w C.

%package apidocs
Summary:	API documentation for Python Xlib module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Xlib
Group:		Documentation

%description apidocs
API documentation for Python Xlib module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Xlib.

%prep
%setup -q -n python-xlib-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} runtests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} runtests.py
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/python,%{__python},' \
	-e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.py
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__sed} -i -e '1s,/usr/bin/python,%{__python3},' \
	-e '1s,/usr/bin/env python,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/*.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rst TODO
%{py_sitescriptdir}/Xlib
%{py_sitescriptdir}/python_xlib-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rst TODO
%{py3_sitescriptdir}/Xlib
%{py3_sitescriptdir}/python_xlib-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.html
%endif
