Name:		texlive-booklet
Version:	15878
Release:	2
Summary:	Aids for printing simple booklets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/booklet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pages of a document processed with the booklet package will be
reordered and scalled so that they can be printed as four pages
per physical sheet of paper, two pages per side. The resulting
sheets will, when folded in half, assemble into a booklet.
Instructions on producing the manual itself as a booklet are
included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/booklet/bkltprnt.sty
%{_texmfdistdir}/tex/latex/booklet/booklet.sty
%doc %{_texmfdistdir}/doc/latex/booklet/README
%doc %{_texmfdistdir}/doc/latex/booklet/booklet.pdf
#- source
%doc %{_texmfdistdir}/source/latex/booklet/booklet.dtx
%doc %{_texmfdistdir}/source/latex/booklet/booklet.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
