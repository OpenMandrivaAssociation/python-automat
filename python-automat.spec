Summary:	Python library for finite-state machines
Name:		python-automat
Version:	0.7.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/Automat/
Source0:	https://files.pythonhosted.org/packages/4a/4f/64db3ffda8828cb0541fe949354615f39d02f596b4c33fb74863756fc565/Automat-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	python-m2r
BuildRequires:	python2-m2r
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
