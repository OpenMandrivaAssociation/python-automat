Summary:	Python library for finite-state machines
Name:		python-automat
Version:	25.4.16
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/Automat/
Source0:	https://files.pythonhosted.org/packages/source/a/automat/automat-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-m2r
BuildRequires:	python-pip python-wheel
BuildRequires:	python3dist(tomli)
BuildArch:	noarch

%description
Python library for finite-state machines

%prep
%autosetup -p1 -n automat-%{version}

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/automat
%{py_sitedir}/*.dist-info
%{_bindir}/automat-visualize
