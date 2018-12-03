# exodus

Build a Genealogy site from your Rootsmagic Database.

## Name

Names are one of the hardest things to come up with, and in the age of Google,
most of the simple and short ones have already been taken (as this one has
too). Anyway, the idea is this program serves to take your genelogy data,
currently captive on your local machine, and take it to the promised land of
sharing!

## Prior Art, Other Resources

- [Awesome GEDCOM](https://github.com/todrobbins/awesome-gedcom) -- a
  collection of Gedcom resources
- [Surnames with Places](https://ancestry.dandyer.co.uk/public/surnames/) -- a
  surname list that also shows where that surname was in use. This seems
  exceedingly helpful in trying to determine if someone's information is about
  *your* family. The rest of the site seems to be password controlled. The
  format is a listing of surnames, with places (as the country flag, and then
  the county/state, and then the village) next to it; multiple places can be
  listed for a surname.
- [rosetta](https://github.com/OpenGenOrg/rosetta) -- this is designed to
  provide an intermediate data format for moving data between genealogy
  programs. In theory, this could be very helpful to gather the information out
  of my RootsMagic file and then serve it up to my website generator.
  Unfortunately, it seems to be somewhere between an alpha-level project, and a
  proof-of-concept. As well, it's being written in C#, so the code may not be
  of much immediate use. However, there appear to be some [breakdown of the
  RootsMagic database
  format](https://github.com/OpenGenOrg/rosetta/tree/master/analysis), which
  will likely be helpful.
- "[TimeNets](http://vis.stanford.edu/papers/timenets)" -- this is a research
  paper that discribles one way to show the temporal coincidence of people in
  your genealogy file. I think this would be very helpful, either in just
  showing parents and their children, or maybe even a pedigree.
- [gedcom2html](https://github.com/picnicprojects/gedcom2html) -- takes a
  Gedcom file and turns it into [a rather good looking
  site](https://picnicprojects.com/gedcom2html/dutchroyalfamily/I1208_Willem-Alexander.html).
  I'm not sure I understand the navigator though.
- [python-gedcom](https://github.com/nickreynke/python-gedcom) -- most of the
  Python Gedcom pharsers I've found trace back to a BYU class assignment from
  appoximately 2005. However, none of them seem to have reached production
  level code quality. That said, this fork seems to be the most active (last
  update 5 days ago), the most developed, and it's available on
  [PyPI](https://pypi.org/project/python-gedcom/).
  