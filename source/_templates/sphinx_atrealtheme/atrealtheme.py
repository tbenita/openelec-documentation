# Parametrage de sphinx
language = 'fr'
today_fmt = '%d / %m / %Y'

# Parametrage du theme sphin.atrealtheme pour le rendu html
html_theme = 'sphinx_atrealtheme'
html_theme_path = ["_templates"]

# Logo de l'aplication
#html_logo = '_static/<votre_image>.png' #Exemple pour plone

html_static_path = ['_static']
html_use_index = True

# Parametrage du Header et Footer d'atReal pour le rendu pdf (latex)
latex_logo = '_templates/sphinx_atrealtheme/static/logo_entete_atreal.png'
latex_additional_files = ['_templates/sphinx_atrealtheme/static/latex_footer_atreal.png']
latex_show_pagerefs = False
latex_domain_indices = True
latex_use_modindex = True

# Nom de votre documentation
#latex_document_name = "<nom_documentation>"

atrealtableofcontents ='''

\\begin{flushleft}{
    \\fontsize{9}{0} 
    \\fontfamily{verdana}
    \\selectfont
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\ \\linebreak \\ \\linebreak
    \\includegraphics{latex_footer_atreal.png}
    \\textbf{atReal SARL} - SIRET 44470817600011 \\linebreak Code APE 6202A - TVA FR 23444708176 - RC 
    \\linebreak 113 bd de Pont de Vivaux 13010 Marseille
}
\\end{flushleft}
\\ \\linebreak
\\begin{flushright}{
    \\fontsize{9}{0} 
    \\fontfamily{verdana}
    \\selectfont
    http://www.atreal.fr/ \\linebreak contact@atreal.fr \\linebreak Tel : 04 91 29 42 81 - Fax : 04 91 29 42 82
}
\\end{flushright}
\\ \\linebreak
\\begin{center}{
    \\fontsize{9}{0} 
    \\fontfamily{verdana}
    \\selectfont
    \\textcolor{Lightgray}{
        \\copyright \\ atReal tous droits de reproduction ou de diffusion r\\'{e}serv\\'{e}s
    } 
}
\\end{center}

\\textcolor{Black}{}

\\maketitle \\clearpage
\\tableofcontents \\clearpage

'''

atrealpreamble ='''
\\usepackage{color}
\\usepackage[T1]{fontenc}
\\definecolor{Gray}{RGB}{102,102,102}
\\definecolor{Lightgray}{RGB}{179,179,179}
\\definecolor{Black}{RGB}{0,0,0}
\\definecolor{White}{RGB}{255,255,255}
\\usepackage{hyperref}
\\hypersetup{
    colorlinks,breaklinks,
    urlcolor=Gray,
    linkcolor=Gray
}

\\fancypagestyle{plain}{
\\fancyhf{}
\\textheight = 640pt
\\fancyhead[L]{{
	\\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\includegraphics{logo_entete_atreal.png}
}}

\\fancyfoot[LO]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\thepage} }
}}
\\fancyfoot[RO]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\nouppercase\\leftmark} }
}}

\\fancyfoot[RE]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\thepage} }
}}
\\fancyfoot[LE]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\nouppercase\\rightmark} }
}}

\\renewcommand{\\headrulewidth}{0.4pt}
\\renewcommand{\\footrulewidth}{0.4pt}
}


\\fancypagestyle{normal}{
\\fancyhf{}
\\textheight = 640pt
\\fancyhead[L]{{
	\\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\includegraphics{logo_entete_atreal.png}
}}

\\fancyfoot[LO]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\thepage} }
}}
\\fancyfoot[RO]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\nouppercase\\leftmark} }
}}

\\fancyfoot[RE]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\thepage} }
}}
\\fancyfoot[LE]{{
        \\fontsize{9}{0} \\fontfamily{verdana}\\selectfont \\textcolor{Black}{ \\textbf{\\nouppercase\\rightmark} }
}}

\\renewcommand{\\headrulewidth}{0.4pt}
\\renewcommand{\\footrulewidth}{0.4pt}
}

'''
