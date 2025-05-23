#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v25
# autospec commit: 9594167
#
Name     : pypi-jupyterlab_widgets
Version  : 3.0.15
Release  : 49
URL      : https://files.pythonhosted.org/packages/b9/7d/160595ca88ee87ac6ba95d82177d29ec60aaa63821d3077babb22ce031a5/jupyterlab_widgets-3.0.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/7d/160595ca88ee87ac6ba95d82177d29ec60aaa63821d3077babb22ce031a5/jupyterlab_widgets-3.0.15.tar.gz
Summary  : Jupyter interactive widgets for JupyterLab
Group    : Development/Tools
License  : MIT
Requires: pypi-jupyterlab_widgets-data = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-license = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-python = %{version}-%{release}
Requires: pypi-jupyterlab_widgets-python3 = %{version}-%{release}
Requires: pypi(jupyter_packaging)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
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
%setup -q -n jupyterlab_widgets-3.0.15
cd %{_builddir}/jupyterlab_widgets-3.0.15
pushd ..
cp -a jupyterlab_widgets-3.0.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1746454578
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets
cp %{_builddir}/jupyterlab_widgets-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets/4bc698855139810986744237da220b75da688c7c || :
cp %{_builddir}/jupyterlab_widgets-%{version}/labextension/static/439.b350310d057b43cdd50f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_widgets/01ebbe688c25d738b9ee0e2de8113f7351c88e7a || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/327.d242f1a99504b2d5b629.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/420.23ab95819c045f6c36bc.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/439.b350310d057b43cdd50f.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/439.b350310d057b43cdd50f.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/446.f8696ce72124c78273da.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/586.085510630436c2e4273f.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/647.8458d9c331000024a14a.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/651.fe40a967a60b543cf15c.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/651.fe40a967a60b543cf15c.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/701.043aefe0b66133629348.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/722.53e4a64671c3c48de007.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/727.b26a6f3871012a0fd66a.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/898.db11fb1a7e18acb58b5b.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/remoteEntry.35b6c65bd99dab37b910.js
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
