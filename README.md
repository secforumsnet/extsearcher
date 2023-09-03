# extsearcher



</head>
<body>

<h1>Web Crawler and File Search</h1>

<p>This Python script allows you to crawl a website, search for specific words, and find files with given extensions. It's a versatile tool for exploring websites and extracting useful information.</p>

![screenshot](https://github.com/secforumsnet/extsearcher/assets/143932328/c5231880-4a09-44a8-aa5e-7bf177e85203)
![screenshot](https://github.com/secforumsnet/extsearcher/assets/143932328/2a899546-d419-456a-9328-0460faa614dd)



<h2>Features</h2>

<ul>
    <li>Crawl a website and search for specific words.</li>
    <li>Find files with specified extensions.</li>
    <li>Print matching files in green for easy identification.</li>
    <li>Recursively explore subdirectories on the website.</li>
    <li>Handle various errors and exceptions gracefully.</li>
</ul>

<h2>Requirements</h2>

<p>Before using the script, make sure you have the following Python libraries installed:</p>

<ul>
    <li><b>requests:</b> For making HTTP requests to the website.</li>
    <li><b>beautifulsoup4:</b> For parsing HTML content.</li>
    <li><b>colorama:</b> For colored console output (install using pip: <code>pip install colorama</code>).</li>
</ul>

<h2>How to Use</h2>

<ol>
    <li>Clone or download this repository to your local machine.</li>
    <li>Open your terminal or command prompt.</li>
    <li>Navigate to the directory where the script is located.</li>
    <li>Run the script by executing the following command:</li>
</ol>

<pre><code>python extsearcher.py</code></pre>

<li>Follow the on-screen prompts:</li>

<ul>
    <li>Enter the website URL you want to crawl (e.g., https://example.com).</li>
    <li>Specify the file extensions you want to search for (comma-separated, e.g., .pdf, .txt).</li>
</ul>

<li>The script will start crawling the website and searching for files. Matching files will be displayed in green in the terminal.</li>


