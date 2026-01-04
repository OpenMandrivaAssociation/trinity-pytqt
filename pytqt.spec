%bcond clang 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_pkg pytqt
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	3.18.1
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TQt bindings for Python
Group:		Development/Libraries/Python
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/dependencies/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

Obsoletes:		trinity-PyQt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-python-qt3 < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-python-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-python-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	tqt3-apps-devel >= 3.5.0
BuildRequires:	libtqt4-devel >= %{?epoch:%{epoch}:}4.2.0
BuildRequires:	trinity-filesystem >= %{tde_version}
BuildRequires:	sip4-tqt-devel >= %{?epoch:%{epoch}:}4.10.5
BuildRequires:	libtqscintilla-devel >= %{?epoch:%{epoch}:}1.7.1

%{!?with_clang:BuildRequires:	gcc-c++}

# PYTHON support
%if "%{python}" == ""
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel
%endif

# MESA support
BuildRequires:  pkgconfig(glu)

# XMU support
BuildRequires:  pkgconfig(xmu)

%description
Python binding module that allows use of TQt X Window toolkit v3.
You can use it to create portable graphics-capable scripts.

At this moment pytqt offers a vast subset of TQt API. There are
some minor issues related to the differences between C++ and Python
(types, etc), but usually you'll be able to write code pretty much the
same way in both languages (with syntax differences, of course)

##########

%package -n pytqt
Summary:	TQt bindings for Python
Group:		Development/Libraries/Python
Requires:	trinity-filesystem >= %{tde_version}
Requires:	sip4-tqt >= %{?epoch:%{epoch}:}4.10.5
Requires:	libtqt4 >= %{?epoch:%{epoch}:}4.2.0
Obsoletes:	python-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt
Python binding module that allows use of TQt X Window toolkit v3.
You can use it to create portable graphics-capable scripts.

At this moment pytqt offers a vast subset of TQt API. There are
some minor issues related to the differences between C++ and Python
(types, etc), but usually you'll be able to write code pretty much the
same way in both languages (with syntax differences, of course)

%files -n pytqt
%defattr(-,root,root,-)
%doc NEWS README
%dir %{python_sitearch}/PyTQt
%{python_sitearch}/PyTQt/__init__.py*
%{python_sitearch}/PyTQt/tqt.so
%{python_sitearch}/PyTQt/tqtcanvas.so
%{python_sitearch}/PyTQt/tqtnetwork.so
%{python_sitearch}/PyTQt/tqtsql.so
%{python_sitearch}/PyTQt/tqttable.so
%{python_sitearch}/PyTQt/tqtui.so
%{python_sitearch}/PyTQt/tqtxml.so

##########

%package -n pytqt-gl
Summary:	TQt OpenGL bindings for Python
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	python-tqt-gl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-gl = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-gl
Python binding module that allows use of the OpenGL facilities
offered by the TQt X Window toolkit v3. You can use it to create
portable graphics-capable scripts.

%files -n pytqt-gl
%defattr(-,root,root,-)
%{python_sitearch}/PyTQt/tqtgl.so

##########

%package -n pytqt-tqtext
Summary:	TQtext extensions for pytqt
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	python-tqt-tqtext < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-tqtext = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-tqtext
pytqt Extensions. Contains:

* TQScintilla: a featureful TQt source code editing component based
              on Scintilla.

%files -n pytqt-tqtext
%defattr(-,root,root,-)
%{python_sitearch}/PyTQt/tqtext.so

##########

%package -n trinity-pytqt-tools
Summary:	Pyuic and pylupdate for TQt
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-pytqt-tools
pyuic is the PyQt counterpart for TQt's uic. It takes an XML
user interface file and generates Python code.

pylupdate is the counterpart for TQt's lupdate. It updates TQt
Linguist translation files from Python code.

%files -n trinity-pytqt-tools
%defattr(-,root,root,-)
%{tde_prefix}/bin/pytqlupdate
%{tde_prefix}/bin/pytquic

##########

%package -n pytqt-devel
Summary:	TQt bindings for Python - Development files
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-pytqt-tools = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt4-devel >= %{?epoch:%{epoch}:}4.2.0
Obsoletes:	python-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-devel
Development .sip files with definitions of PyQt classes. They
are needed to build PyQt, but also as building blocks of other
packages based on them, like PyTDE.

%files -n pytqt-devel
%defattr(-,root,root,-)
%{python_sitearch}/PyTQt/pytqtconfig.py*
%dir %{_datadir}/sip
%{_datadir}/sip/tqt/

%prep
%autosetup -p1 -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"

mkdir build
cd build

echo yes | %__python ../configure.py \
	-c -n %{_includedir}/tqt3 \
	-g %{_includedir}/tqt3 \
	-q %{_datadir}/tqt3 \
	-y tqt-mt \
	-o %{_libdir} -u -j 10 \
	-d %{python_sitearch}/PyTQt \
	-v %{_datadir}/sip/tqt \
	-b %{tde_prefix}/bin \
	-w \
	CXXFLAGS_RELEASE="" CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt" STRIP=""

# %__make


%install
%__make install DESTDIR=%{?buildroot} -C build

%__install -d %{?buildroot}%{_datadir}/sip/
%__cp -rf sip/* %{?buildroot}%{_datadir}/sip/tqt/

