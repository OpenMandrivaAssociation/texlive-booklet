# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/booklet
# catalog-date 2009-09-02 11:33:10 +0200
# catalog-license lppl1.3
# catalog-version 0.7b
Name:		texlive-booklet
Version:	0.7b
Release:	6
Summary:	Aids for printing simple booklets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/booklet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booklet.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7b-2
+ Revision: 749835
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7b-1
+ Revision: 717966
- texlive-booklet
- texlive-booklet
- texlive-booklet
- texlive-booklet
- texlive-booklet

