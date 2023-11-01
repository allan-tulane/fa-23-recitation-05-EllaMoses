# CMPS 2200 Recitation 6
## Answers

**Name:** Ella Moses


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

| filename     |   fixed-length-cost |   huffman-cost |   ratio |
|--------------|---------------------|----------------|---------|
| alice29.txt  |             1039367 |         676374 |   0.651 |
| asyoulik.txt |              876253 |         606448 |   0.692 |
| f1.txt       |                1340 |            826 |   0.616 |
| fields.c     |               78050 |          56206 |   0.720 |
| grammar.lsp  |               26047 |          17356 |   0.666 |

The ratio of huffman-cost to fixed-length-cost seems to be between 0.6 and 0.7. This means that the huffman cost is constistantly lower than the fixed cost and the ratio is approximately the same regardless of file size. 




- **e.**
If we use huffman encoding on a file and every character has the same frequency f, then the length would be equal to f + 2f + 3f + ... + (n-1)f + nf + nf, where n equals the number of characters. Regardless of the document, if each character has the same frequency nf + f * ((n+1)/2)

