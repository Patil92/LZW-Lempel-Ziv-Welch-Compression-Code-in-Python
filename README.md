# LZW-Lempel-Ziv-Welch-Compression-Code-in-Python
Lempel–Ziv–Welch implementation using Python

 A drawback of Huffman’s code is that it requires simple probabilities. For real time applications, Huffman encoding becomes impractical as a source statistics are not always known apriori. A code that might be more efficient to use statistical interdependence of the letters in the alphabet along with their individual probabilities of occurrences is the Lempel-ziv algorithm. This algorithm belongs to the class of universal source coding algorithms.

The logic behind Lempel-ziv universal coding is as follows:

* The compression of an arbitrary binary sequence is possible by coding a series of zeros and ones as some previous such string (prefix string) + one new bit.

* The new string formed by such parsing becomes a potential prefix, string for future strings.
   These variables are called phrases (sub sequences). The phrases are listed in a dictionary or code book which stores the existing phrases and their locations. In encoding a new phrase be specified the location of the existing phrase in the code book and append the new letter.
   
  for more Information About Algorithm,
    https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
    http://www.electronicsandcommunications.com/2012/07/lempel-ziv-algorithm-with-example.html
    
