# CMPS 2200 Recitation 6
## Answers

**Name:** Ella Moses


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

| filename     |   fixed-length-cost |   huffman-cost |   ratio |
|--------------|---------------------|----------------|---------|
| alice29.txt  |             1039367 |         676374 |   1.537 |
| asyoulik.txt |              876253 |         606448 |   1.445 |
| f1.txt       |                1340 |            826 |   1.622 |
| fields.c     |               78050 |          56206 |   1.389 |
| grammar.lsp  |               26047 |          17356 |   1.501 |

The compression ratios fall between 1.38 and 1.63. This means that the huffman cost is lower than the fixed cost for all of these files. The ratio depends on how uniform the character frequencies are. When the character frequencies are less uniform, the compression ratio is higher than when the frequencies are similar across characters.


- **e.**
The cost of the huffman encoding is calculated by multiplying the frequeny of a character by the length of the encoding and adding this result across all characters. If all the frequencies are the same, then the length of the encoding can be found by calculating log_2(n) where n is the number of characters. So the cost can be calculated by calculating nf * log_2(n). This formula is the same across documents as long as f is the same for each character. The result will differ if n and f are different for other documents. 
