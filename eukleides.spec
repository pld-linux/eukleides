# TODO:
# - the scripts move to subpackages ?
#
Summary:	Eukleides is a computer language devoted to elementary plane geometry
Name:		eukleides
Version:	1.5.0
Release:	0.1
License:	GPL v3
Group:		Applications/Science
Source0:	http://www.eukleides.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9bd6958fdb7fa0aee7cb9a0ccff016e1
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile-destdir.patch
URL:		http://www.eukleides.org/
BuildRequires:	/usr/bin/pdflatex
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRequires:	texlive-latex-ae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eukleides is a computer language devoted to elementary plane geometry.
It aims to be a fairly comprehensive system to create geometric
figures, either static or dynamic. Eukleides allows to handle basic
types of data: numbers and strings, as well as geometric types of
data: points, vectors, sets (of points), lines, circles and conics.

%package -n texlive-latex-eukleides
Summary:	Eukleides LaTeX style
Group:		Applications/Publishing/TeX

%description -n texlive-latex-eukleides
Eukleides LaTeX style.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i "s,ginstall-info,install-info,g" doc/Makefile

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/*.pdf doc/manual
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/%{name}.info*

%files -n texlive-latex-eukleides
%defattr(644,root,root,755)
%dir %{_datadir}/texmf-dist/tex/latex/eukleides
%{_datadir}/texmf-dist/tex/latex/eukleides/*
