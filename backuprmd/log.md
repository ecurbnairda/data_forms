

## Tue May 10 10:38:02 BST 2016

- fixing up the bibliography; modified the zotero export to exclude large fields (like notes, abstract); modifying mybook package to suppress other fields
- struggling with 'last accessed' field -- that needs to be 'by type'. 
- sorted this out by adding stuff to 'mybook.sty' --\clearfield(urlyear},etc. A bit of pfaff and took me all morning, but references are now much cleaner. 
- will go through rest of reference list adding page numbers, etc. 



## Thu May 12 13:14:42 BST 2016

- reading conclusion (crap!) + intro to see how they map onto each other. Not too much at th e moment
- adding new index entries into index on a couple of docs. 

## Fri May 13 23:06:35 BST 2016
- finally managed to read intro and conclusion. Started work on glossary and fixed googletrends code.
- collated some Domingos quotes in a notes file

## Mon May 16 16:20:54 BST 2016

- read chapter 1 on diagramming -- quite a bit of reasonable stuff in there, but its too vague in its claims;
- did quite a bit of work getting some foucault quotes, and hyperobjects descriptions. 
- considering whether to reoroder the chapter to start with NAND function, program it and then learn it. We get from NAND to perceptron via rosenblatt, and then programs, and then their formalization as a machine learner; and this machine learner is just one of many that might be constructed. We get sense of their plenitude, their accumulation in learning machine learning, in seeing who is machine learning, in seeing the practice of machine learning in code, and in the archives of contemporary knowledge production. 

## Mon May 16 17:06:57 BST 2016
- getting glossaries to work -- seems to be ok. 
- also played with separate bibliographies for primary and 2ndary sources -- sample code is in testbib in latex folder; instructions on how to do this are in glossaries how to pdf in latex folder



## Tue May 17 13:49:05 BST 2016
- read 1/3 ch2 on vector space -- doesn't seem too bad. Still need to spend quite a bit of work to get it clearer.
- sorting references into primary and 2ndary -- found Hansen on Faucault and media; worth reading perhaps -- in archive
- read rest of ch2 -- its ok -- needs quite a bit of tightening, and not sure hw well the code vectorisation stuff fits. Needs to be also be understood as a topos, or some other threshold thing. 


## Wed May 18 09:27:26 BST 2016

- reading ch4 -- ok so far. Not sure of what the hook is: slippage between different senses of function (superimposed thresholds!) or something else
- need to resize tables, so did that by adding lines to mybook.sty; trying to rebuild with that. ; ok, worked by putting size in the xtable options at beginning of knitr code. Need to put this across all the chapters. 
- got 10 pages into chapter, but still no strong hook -- optimisation is what I want to get to -- to say that the threshold that has been crossed is one in which learning == optimisation, and optimisation is a kind of searching

## Thu May 19 16:24:19 BST 2016

- got a fair ways  through ch4 on curves -- learning is still struggling to get through -- so complicated to disentangle all the functions
- also played with building everything on hp machine -- didn#t go so well. Some missing dependencies?
- talked to press about deadline -- mid-July -- need to work back from that ... 


## Wed May 25 11:30:41 BST 2016
- got through chapter 5 -- feels like quite a lot needed on it -- some diagrams too would help
- starting chapter 6
- install mlxtend to help plot decision boundaries and put some code in chapter 5 area to plot decision boundary for naive bayes on iris. Could replace this with the enron data?
- also looked at R code to do the decision boundary -- its there on stackexchange ..

## Thu May 26 09:33:57 BST 2016
- finding it hard to start today -- did a lot yesterdy on ch 6, trying to iron out different terminologies -- enunciative function, enunciative modality, statement, discourse, discursive formation, archive, archaeology ... Feel a bit better about these, but still not sure what the main point of the chapter is. Something about pattern, and the difference between sparsity and abundance, a few things that stand out versus a mass of things. ... 
- after lunch, reached last 10 pages, but horrible conceptual work around statements still needs to be done. 
- finished ch6 -- thinking about main point -- it should really be about how to think about differences; changed title to reflect this: 'patterns and differences in ml'
- also looked at how to fix code listings -- use 'minted' package - can label all code listings using that. 
- been adding many glossary entries -- might need to sub-divide glossaries to separate technical and critical entries. 


## Fri May 27 13:35:51 BST 2016
- startgin ch7 -- seems to be on the referential. But is that really what I want to talk about here? It seems a pretty obscure concept. Chapter is meant to be about the ways that machine learning brings new kinds of things into existence, so that would be ok. 
- ok, had a good idea to intensify the referential as the collective pre-individual reserve, the hyperobject for machine learning; there are a number of these -- images (faces-things-places), genome, social media, market-entanglements, network-states, epidemics ... 

## Mon May 30 16:33:44 BST 2016
- got through ch7 -- feels like a the hyperobject chapter really is a hyperobject. Do I characterise the hyperobject clearly enough? Felt that maybe the MF material on referentials, positivity, is a really a bit arcane. 
- starting ch8 -- the neural net stuff is ok so far. 

## Thu Jun 23 15:56:25 BST 2016
- been working a lot on chapters on paper -- now on ch7 again -- still dealing with referentials, but trying to capture the somewhat excessive aspect of it more, to see what happens to it under mlr conditions. 


## Tue Jun 28 14:21:34 BST 2016
- think I've finished the chapters now. Can either redo conclusion or start adding corrections, or both. 

## Wed Jun 29 18:25:23 BST 2016
- starting working on the conclusion; got the RNN in. 

## Thu Jun 30 12:47:49 BST 2016

- put main summary of chapters and the bigger argument about technologies of self into conclusion; going ok, although not especially scintillating. 

## Sun Jul  3 22:35:16 BST 2016

- almost finished intro rev

## Wed Jul  6 22:43:53 BST 2016
- lot of revisions on ch1 and ch2. Almost on schedule



## Mon  5 Dec 14:47:17 GMT 2016

- addressing image permissions for openscikit image and american statistical association journal. Figures 4.1 and 6.2
- scikit-learn image is here http://scikit-learn.org/stable/tutorial/machine_learning_map/ It is under BSD Licence, which I read to mean that a copyright notice needs to accompany the figure. i.e. **Copyright** (c) 2010 - 2016, scikit-learn developers, (see https://en.wikipedia.org/wiki/BSD_licenses) for details.   
- american statist: probably will need to use copyright clearance centre http://www.amstat.org/ASA/Copyright.aspx has the details. 



## Tue Dec  6 14:57:30 GMT 2016
- requested prices from RightsLink for figure 6.2 -- waiting for Taylor & Francis to get back to me
- TODO: look at rest of queries on size, etc


## Sat Dec 10 12:50:32 GMT 2016
- had conniptions over versions, but checking branch history and merges, it seems ok
- using bookdown to build gh-pages html version of the book, following instructions in ~/archive/hui_20106_bookdown.pdf
- quite tricky to set up -- updated R packages, updated Pandoc, trying now to run render_book
- spent most of the afternoon on this -- found configuration difficult to do. Went best after total rename of files; managed to get the references in; 
- turning into an epic slog - 9pm at night still working on getting the images in. Have managed to get the chapters showing ok, altho the numbers are wrong. still no glossary, index, reference list. 


## Sun Dec 11 15:16:08 GMT 2016

- experimenting with bookdown to get images showing. Working ok on test files. But will need to go through an convert everything to the format \@ref(fig:x). 


## Mon Dec 12 14:36:51 GMT 2016
- feeling better now that images are starting to show. Had to do a lot of subheading fixing. Undoing latex stuff with simpler bookdown. 
- working on a script to change all the references: this one is ok for images:
    sed 's/\\ref{fig:\(\w*\)}/\\@ref(fig:\1)/' 03_praxis.rmd|grep '\\@'

## Sun Dec 18 10:16:28 GMT 2016
- ran the sed script to convert images links
- then did the tables:
sed -i 's/\\ref{tab:\(\w*\)}/\\@ref(tab:\1)/' *.rmd 
- still need to do chapter references
    sed -i 's/\\ref{ch:\(\w*\)}/\\@ref(ch:\1)/' *.rmd 

## Mon Dec 19 08:55:58 GMT 2016
- spent quite a long time on the sed expression to change all chunk labels to use hyphens instead of underscores. Wish I knew about that little requirement earlier. 
    sed  's/`{r \([[:alnum:]]*\)_?\([[:alnum:]]*\)/```{r \1-\2/' *.rmd|grep '{r \w*'
- it doesn't work properly, not sure why -- oh, ok, begin to see why -- groupings are not right. 
- giving up on this for the moment -- could probably just get it done manually ... 