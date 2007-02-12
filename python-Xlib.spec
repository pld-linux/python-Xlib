
%define		module	Xlib

Summary:	X client library for Python
Summary(pl.UTF-8):   Biblioteka klienta X dla Pythona
Name:		python-%{module}
Version:	0.12a
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/python-xlib/python-xlib-%{version}.tar.gz
# Source0-md5:	4edc71320669e99ad874094bff44f4f8
URL:		http://python-xlib.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
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

%description -l pl.UTF-8
Python X Library (biblioteka X dla Pythona) ma być w pełni
funkcjonalną biblioteką kliencką X dla programów w Pythonie. Jest
napisana całkowicie w Pythonie, w przeciwieństwie do poprzednich
bibliotek X dla Pythona (starego rozszerzenia X i nowszej plxlib),
które były interfejsami do Xlib w C.

Jest to możliwe do zrobienia ponieważ programy klienckie X komunikują
się z X serwerem za pomocą protokołu X. Komunikacja odbywa się poprzez
TCP/IP, gniazda uniksowe, DECnet lub dowolny inny strumieniowy
protokół sieciowy. Biblioteka Xlib w C jest jedynie interfejsem do
tego protokołu, dostarczając funkcje odpowiednie dla środowiska C.

Są trzy zalety wyboru implementacji jako czysto pythonowej biblioteki:
- integracja: biblioteka może używać cudownego systemu obiektowego
  Pythona, dostarczając łatwą w użyciu hierarchię klas
- przenośność: biblioteka będzie użyteczna na (prawie) każdym
  komputerze z zainstalowanym Pythonem. Interfejs w C mógłby być
  problematyczny do sportowania na systemy nieuniksowe, jak na
  przykład MS Windows czy OpenVMS.

%prep
%setup -q -n python-xlib-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/ -name \*.py | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%{py_sitescriptdir}/%{module}
%{_examplesdir}/%{name}-%{version}
