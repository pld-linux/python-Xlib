
%define		module	Xlib

Summary:	X client library for Python
Summary(pl):	Biblioteka klienta X dla Pythona
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
BuildRequires:	rpm-pythonprov
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

%description -l pl
Python X Library (biblioteka X dla Pythona) ma byæ w pe³ni
funkcjonaln± bibliotek± klienck± X dla programów w Pythonie. Jest
napisana ca³kowicie w Pythonie, w przeciwieñstwie do poprzednich
bibliotek X dla Pythona (starego rozszerzenia X i nowszej plxlib),
które by³y interfejsami do Xlib w C.

Jest to mo¿liwe do zrobienia poniewa¿ programy klienckie X komunikuj±
siê z X serwerem za pomoc± protoko³u X. Komunikacja odbywa siê poprzez
TCP/IP, gniazda uniksowe, DECnet lub dowolny inny strumieniowy
protokó³ sieciowy. Biblioteka Xlib w C jest jedynie interfejsem do
tego protoko³u, dostarczaj±c funkcje odpowiednie dla ¶rodowiska C.

S± trzy zalety wyboru implementacji jako czysto pythonowej biblioteki:
- integracja: biblioteka mo¿e u¿ywaæ cudownego systemu obiektowego
  Pythona, dostarczaj±c ³atw± w u¿yciu hierarchiê klas
- przeno¶no¶æ: biblioteka bêdzie u¿yteczna na (prawie) ka¿dym
  komputerze z zainstalowanym Pythonem. Interfejs w C móg³by byæ
  problematyczny do sportowania na systemy nieuniksowe, jak na
  przyk³ad MS Windows czy OpenVMS.

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
