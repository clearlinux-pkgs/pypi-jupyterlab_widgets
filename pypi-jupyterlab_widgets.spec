#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-jupyterlab_widgets
Version  : 3.0.7
Release  : 34
URL      : https://files.pythonhosted.org/packages/d4/68/ef3070afff437dc92562241294467112566d3b402d85bb9b32e3fd65352a/jupyterlab_widgets-3.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/68/ef3070afff437dc92562241294467112566d3b402d85bb9b32e3fd65352a/jupyterlab_widgets-3.0.7.tar.gz
Summary  : Jupyter interactive widgets for JupyterLab
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-jupyterlab_widgets-data = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-license = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-python = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-python3 = %{version}-%{release}
Requires: pypi(jupyter_packaging)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_packaging)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Widgets JupyterLab Extension
A JupyterLab 3.0 extension for Jupyter/IPython widgets.

%package data
Summary: data components for the pypi-jupyterlab_widgets package.
Group: Data

%description data
data components for the pypi-jupyterlab_widgets package.


%package license
Summary: license components for the pypi-jupyterlab_widgets package.
Group: Default

%description license
license components for the pypi-jupyterlab_widgets package.


%package python
Summary: python components for the pypi-jupyterlab_widgets package.
Group: Default
Requires: pypi-jupyterlab_widgets-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlab_widgets package.


%package python3
Summary: python3 components for the pypi-jupyterlab_widgets package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_widgets)

%description python3
python3 components for the pypi-jupyterlab_widgets package.


%prep
%setup -q -n jupyterlab_widgets-3.0.7
cd %{_builddir}/jupyterlab_widgets-3.0.7
pushd ..
cp -a jupyterlab_widgets-3.0.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680103287
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets
cp %{_builddir}/jupyterlab_widgets-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets/4bc698855139810986744237da220b75da688c7c || :
cp %{_builddir}/jupyterlab_widgets-%{version}/labextension/static/113.270dbb43db912c1b3723.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets/01ebbe688c25d738b9ee0e2de8113f7351c88e7a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/install.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/package.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/schemas/@jupyter-widgets/jupyterlab-manager/package.json.orig
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/schemas/@jupyter-widgets/jupyterlab-manager/plugin.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/113.270dbb43db912c1b3723.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/113.270dbb43db912c1b3723.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/134.402424ef4079078b2e0e.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/150.1a6d6a3a0542a41bec5a.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/291.0b98a9cbc7337e1749ed.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/291.0b98a9cbc7337e1749ed.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/345.03be96cd091aac4797a5.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/495.ea5e18a84b54f152ae61.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/595.b7741b41fd98f8f3d844.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/596.340cb969418e72309eb4.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/61.21f571face17e35076c2.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/644.7d1bff49f8e38fac4070.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/699.2ea6ecfcddb8f3bb4732.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/965.b0caf50c6bbde92efb37.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/remoteEntry.35e76720037cafa02724.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/style.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/third-party-licenses.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab_widgets/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
/usr/share/package-licenses/pypi-jupyterlab_widgets/4bc698855139810986744237da220b75da688c7c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
