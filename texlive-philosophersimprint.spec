Name:		texlive-philosophersimprint
Version:	56954
Release:	2
Summary:	Typesetting articles for "Philosophers' Imprint"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/philosophersimprint
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philosophersimprint.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/philosophersimprint
%doc %{_texmfdistdir}/doc/latex/philosophersimprint
#- source
%doc %{_texmfdistdir}/source/latex/philosophersimprint

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
