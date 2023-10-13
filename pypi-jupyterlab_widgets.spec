#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-jupyterlab_widgets
Version  : 3.0.9
Release  : 37
URL      : https://files.pythonhosted.org/packages/74/21/6d8a2353ed57b431d8a23925006f03bb119d0c36c2e08b2c3becd8db479b/jupyterlab_widgets-3.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/21/6d8a2353ed57b431d8a23925006f03bb119d0c36c2e08b2c3becd8db479b/jupyterlab_widgets-3.0.9.tar.gz
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
BuildRequires : pypi(jupyterlab)
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
%setup -q -n jupyterlab_widgets-3.0.9
cd %{_builddir}/jupyterlab_widgets-3.0.9
pushd ..
cp -a jupyterlab_widgets-3.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694622083
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
cp %{_builddir}/jupyterlab_widgets-%{version}/labextension/static/113.e4cfda62b59ddbe550d3.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets/01ebbe688c25d738b9ee0e2de8113f7351c88e7a || :
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
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/113.e4cfda62b59ddbe550d3.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/113.e4cfda62b59ddbe550d3.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/134.a63a8d293fb35a52dc25.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/291.cff5ef71b29e18850479.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/291.cff5ef71b29e18850479.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/336.ebc7a55ea1768712771f.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/345.17494fea1ff555b26294.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/495.79062b4ce5ec7920dcb1.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/595.74686e2543ce21f10975.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/596.df8214a14175baf1ee16.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/61.21f571face17e35076c2.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/644.558670f1aa9ae5791769.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/699.e966b1425a7d4e8c3f4e.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/965.9a2bfc1116cea35345ca.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/remoteEntry.a37e37c87d212fe85e13.js
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
