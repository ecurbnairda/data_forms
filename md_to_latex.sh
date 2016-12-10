#!/bin/sh

echo '\documentclass[book.tex]{subfiles}\n' | cat - acknowledgments.tex > temp && mv temp acknowledgments.tex
pandoc --biblatex preface.md -o preface.tex
echo '\documentclass[book.tex]{subfiles}\n' | cat - preface.tex > temp && mv temp preface.tex
cd ch0_introduction/
pandoc --biblatex ch_introduction.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch1_learning/
pandoc --biblatex  ch_praxis.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch2_vector/
pandoc --biblatex ch_vector_space.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch3_curves/
pandoc --biblatex ch_curves_functions.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch4_probability/
pandoc --biblatex ch_naive_informed.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch5_dimensionality/
pandoc --biblatex ch_dimensional_exuberance.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch6_topologies/
pandoc --biblatex ch_genomic_topologies.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch7_subjects/
pandoc --biblatex ch_learning_subjects.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
cd ch8_conclusion/
pandoc --biblatex ch_conclusion.md -o ch.tex
echo '\documentclass[../book.tex]{subfiles}\n' | cat - ch.tex > temp && mv temp ch.tex
cd ..
