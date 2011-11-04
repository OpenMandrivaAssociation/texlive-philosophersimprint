# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/philosophersimprint
# catalog-date 2008-08-23 00:06:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-philosophersimprint
Version:	1.0
Release:	1
Summary:	Typesetting articles for "Philosophers' Imprint"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/philosophersimprint
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
In its mission statement we read "Philosophers' Imprint is a
refereed series of original papers in philosophy, edited by
philosophy faculty at the University of Michigan, with the
advice of an international Board of Editors, and published on
the World Wide Web by the University of Michigan Digital
Library. The mission of the Imprint is to promote a future in
which funds currently spent on journal subscriptions are
redirected to the dissemination of scholarship for free, via
the Internet". The journal used to accept manuscripts in Rich
Text Format only. However, for many authors, especially from
the field of logic, TeX seems to be a better choice. The author
was commissioned to write a LaTeX class for the journal. The
class helps authors to typeset their own articles in 'Web-
ready' format. No assumption is made about the fonts available
to the author: the class uses freely available and freely
distributed fonts, only.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/philosophersimprint/philosophersimprint.bib
%{_texmfdistdir}/tex/latex/philosophersimprint/philosophersimprint.cls
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/README
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/philosophersimprint.pdf
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/sample.pdf
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/philosophersimprint/Makefile
%doc %{_texmfdistdir}/source/latex/philosophersimprint/philosophersimprint.dtx
%doc %{_texmfdistdir}/source/latex/philosophersimprint/philosophersimprint.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
