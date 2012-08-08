# revision 26831
# category Package
# catalog-ctan /macros/latex/contrib/philosophersimprint
# catalog-date 2012-06-03 22:54:07 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-philosophersimprint
Version:	1.2
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In its mission statement we read "Philosophers' Imprint is a
refereed series of original papers in philosophy, edited by
philosophy faculty at the University of Michigan, with the
advice of an international Board of Editors, and published on
the World Wide Web by the University of Michigan Digital
Library. The mission of the Imprint is to promote a future in
which funds currently spent on journal subscriptions are
redirected to the dissemination of scholarship for free, via
the Internet". The class helps authors to typeset their own
articles in "Web-ready" format. No assumption is made about the
fonts available to the author: the class itself is restricted
to freely available and freely distributed fonts, only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/philosophersimprint/philosophersimprint.cls
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/Makefile
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/README
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/philosophersimprint.bib
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/philosophersimprint.pdf
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/sample.pdf
%doc %{_texmfdistdir}/doc/latex/philosophersimprint/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/philosophersimprint/philosophersimprint.dtx
%doc %{_texmfdistdir}/source/latex/philosophersimprint/philosophersimprint.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
