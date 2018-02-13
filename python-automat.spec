Summary:	Python library for finite-state machines
Name:		python-automat
Version:	0.6.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/Automat/
Source0:	https://files.pythonhosted.org/packages/de/05/b8e453085cf8a7f27bb1226596f4ccf5cc9e758377d60284f990bbdc592c/Automat-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Python library for finite-state machines

%package -n python2-automat
Summary:	Python 2.x library for finite-state machines
Group:		Development/Python

%description -n python2-automat
Python 2.x library for finite-state machines

%prep
%setup -qn Automat-%{version}
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/automat
%{py_sitedir}/*.egg-info
%{_bindir}/automat-visualize

%files -n python2-automat
%{py2_puresitedir}/automat
%{py2_puresitedir}/*.egg-info
