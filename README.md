# 🛡️ Cyber Roadmap — From Developer to Security Engineer

> A structured, hands-on path for developers transitioning into cybersecurity. Built on the belief that the best security professionals are those who understand how things are *built* — and therefore how they *break*.

---

## 📋 Table of Contents

- [Philosophy](#philosophy)
- [Phase 1 — Foundations (Months 1–4)](#phase-1--foundations-months-14)
  - [Module 1.1 — TCP/IP, OSI & DNS](#module-11--tcpip-osi--dns)
  - [Module 1.2 — Cryptography in Practice](#module-12--cryptography-in-practice)
  - [Module 1.3 — Linux Beyond `cd` and `ls`](#module-13--linux-beyond-cd-and-ls)
- [Phase 2 — Offensive Skills (Months 4–9)](#phase-2--offensive-skills-months-49)
  - [Module 2.1 — Web Security](#module-21--web-security)
  - [Module 2.2 — Binary Exploitation](#module-22--binary-exploitation)
  - [Module 2.3 — Active Directory](#module-23--active-directory-the-windows-world)
- [Phase 3 — Expert Maturity (Month 9 onward)](#phase-3--expert-maturity-month-9-onward)
  - [Module 3.1 — Mastering the Craft](#module-31--mastering-the-craft)
  - [Module 3.2 — Threat Hunting & Defense](#module-32--threat-hunting--defense)
  - [Module 3.3 — The Real Senior](#module-33--the-real-senior)
- [Ship's Log](#ships-log)

---

## Philosophy

Most people enter security by memorizing tools. This roadmap takes the opposite approach: **understand the fundamentals, build things by hand, then break them**. Every module follows the same loop:

```
Learn the theory → Capture/observe it in practice → Implement it in code → Attack it
```

If you already know how to code, you have a massive head start. Use it.

---

## Phase 1 — Foundations (Months 1–4)

> **Goal:** Understand the substrate everything else runs on — networks, cryptography, and the operating system.

---

### Module 1.1 — TCP/IP, OSI & DNS

**Book:** [Computer Networking: A Top-Down Approach](https://www.cs.sjtu.edu.cn/~linghe.kong/CS339/Download/ComputerNetworking.pdf) — Kurose & Ross

**Labs (Wireshark):**
- Download the [Kurose Wireshark Lab workbook](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- Capture your own traffic. Filter it. Follow TCP streams.
- **See the Three-Way Handshake happen in real time.** Watch DNS queries. Visualize the TLS handshake byte by byte.

**Code it (Python + Scapy):**
1. Write a packet sniffer that captures DNS requests on your network.
2. Write a program that captures TCP SYN packets and logs the source/destination.
3. **Write an ARP Spoofing script** that poisons your own router's ARP table — in an isolated lab VM only. Build it packet by packet. This alone will teach you more TCP/IP than any course.

**Why this matters:** You can't attack or defend a network you don't truly understand. Tools like Wireshark make the invisible visible.

---

### Module 1.2 — Cryptography in Practice

**Course:** [Cryptography I — Dan Boneh (Stanford/Coursera)](https://www.coursera.org/learn/crypto)
Hardcore. Mathematical. Perfect for developers. Focus on the attack sections against ciphers and protocols.

**Challenges (CryptoPals):** [cryptopals.com](https://cryptopals.com)
- Work through the sets in any language you prefer.
- You'll implement AES in ECB mode, then **break it**. You'll execute a Padding Oracle attack from scratch.
- This is the perfect bridge between software development and applied cryptography.

**Why this matters:** Almost every major breach in history has a cryptographic component. Understanding crypto failures from the inside out is non-negotiable.

---

### Module 1.3 — Linux Beyond `cd` and `ls`

**Goal:** Go from user to sysadmin who understands hardening at the OS level.

**Reading:**
- [The Linux Command Line](https://linuxcommand.org/tlcl.php) — William Shotts (master the shell)
- *UNIX and Linux System Administration Handbook* — Evi Nemeth et al. (understand how it really works)

**The Painful VM Exercise:**
Install Arch Linux (or Gentoo) in a VM. **No GUI. Terminal only.**
Configure the network, bootloader, and kernel from scratch. It will hurt. That's the point — you'll understand every layer of the OS when you're done.

**Hardening Lab:**
1. Spin up a web server on your Arch VM.
2. Apply a hardening guide (e.g., [CIS Benchmark](https://www.cisecurity.org/cis-benchmarks)).
3. Disable unnecessary services, configure `iptables`, audit `chmod 700` file permissions.
4. **Now try to break into it from a second VM.** Defend and attack the same machine.

---

## Phase 2 — Offensive Skills (Months 4–9)

> **Goal:** Learn to break what you know how to build.

---

### Module 2.1 — Web Security

**Goal:** You already know how to build web apps. Now learn how to break them.

**Platform:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) — Free, created by the makers of Burp Suite. The single best resource for developers entering security.

**Roadmap:**
1. Read the theory for each topic **before** attempting the lab.
2. Work through all labs in this order: **SQL Injection → XSS → CSRF → Authentication flaws**
3. Each lab gives you a live vulnerable application to exploit — no simulations.
4. As a developer, the epiphany hits fast: *"I've made this exact mistake in production."*

**Why this matters:** Web vulnerabilities are the most commonly exploited attack surface in real-world breaches. Your dev background makes this click faster than for anyone else.

---

### Module 2.2 — Binary Exploitation

**Goal:** Get inside the machine's mind. Step fully outside the developer comfort zone.

**Prerequisite:** Learn x86-64 Assembly.
The [Intro to x86 Assembly Language](https://opensecuritytraining.info/IntroX86.html) playlist on OpenSecurityTraining.info is the right starting point.

**Practice Platforms:**

| Platform | What You'll Learn |
|---|---|
| [pwn.college](https://pwn.college) | Progressive CTF from zero — CLI to kernel exploitation, built by a security professor |
| [Exploit Education / Protostar](https://exploit.education) | Download the VMs and corrupt stacks, jump to memory addresses, and execute shellcode |

**Why this matters:** This is where you understand what a buffer overflow *actually is* — not as a concept, but as bytes overwriting a return address. This separates security engineers from script kiddies.

---

### Module 2.3 — Active Directory (The Windows World)

**Goal:** Learn how most corporate environments are actually compromised.

**Platform:** [TryHackMe](https://tryhackme.com) — subscribe to the premium plan.

**Roadmap:**
- Follow the **"Offensive Pentesting"** and **"Cyber Defense"** learning paths.
- Focus on Active Directory rooms: *Attacktive Directory*, *Post-Exploitation Basics*, *Breaching AD*.
- You'll use real tools in a live Windows network environment:
  - **BloodHound** — AD relationship graph mapping
  - **Mimikatz** — credential extraction
  - **Impacket** — network protocol suite

**Why this matters:** Active Directory is the backbone of nearly every enterprise network. Knowing how to attack it is essential for red teaming, and knowing how to defend it is critical for blue teams.

---

## Phase 3 — Expert Maturity (Month 9 onward)

> **Goal:** Depth, specialization, and research. Stop being a tool user — become an engineer who builds the tools.

---

### Module 3.1 — Mastering the Craft

**Platform:** [Hack The Box (HTB)](https://www.hackthebox.com) — VIP subscription.
The professional playground. No hand-holding. You get an IP and a blank page.

**Strategy:**
- Work through retired machines, then watch write-ups by **IppSec** on YouTube.
- Focus on internalizing **methodology**: How do you enumerate? What do you look for first? How do you pivot between hosts?
- Build a personal note system (Obsidian, Notion) that captures your enumeration checklists and attack patterns.

**Certification (Optional, but career-defining):**
**OSCP (Offensive Security Certified Professional)** — the gold standard for proving hands-on skill. The course is PEN-200. Attempt after HTB gives you confidence.

---

### Module 3.2 — Threat Hunting & Defense

**Goal:** Know what the attacker does so you can hunt them.

**Home SIEM Lab:**
1. Install a free SIEM: [Wazuh](https://wazuh.com) or [Elastic Security](https://www.elastic.co/security)
2. Ingest logs from your machine, your router, your VMs.
3. **Create detection rules for the attacks you run in your HTB lab.**
4. The goal: detect your own attack. Be both the attacker and the defender simultaneously.

**Framework:** Study [MITRE ATT&CK](https://attack.mitre.org).
For every HTB machine you complete, map each step of your attack to an ATT&CK technique.

> Example: `T1003.001 — OS Credential Dumping: LSASS Memory`

This practice transforms you from a pentester into a **Threat Intelligence professional**.

---

### Module 3.3 — The Real Senior

This phase has no end date. It's a continuous discipline.

**Read RFCs:** Want to truly master a protocol? Read the original RFC. No summary, no tutorial. The source.
- [RFC 793](https://datatracker.ietf.org/doc/html/rfc793) — TCP
- [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035) — DNS
- [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) — TLS 1.3

**Read Source Code:** Don't just use Ghidra. Pull the source of `netcat`, study Linux kernel internals, read a cryptography library implementation.

**Build and Ship:**
- Automate an attack technique you've executed manually — build a Python tool for it.
- Publish it on GitHub with documentation.
- Contribute to open-source security projects.

**Your GitHub is your portfolio.** Every tool you build, every technique you document, every CTF write-up you publish compounds into a reputation.

---

## Ship's Log

Progress notes, weekly reflections, and lab write-ups.

| Entry | Link |
|---|---|
| Week 1 | [github.com/ppfuark/cyber_roadmap/semana_1](https://github.com/ppfuark/cyber_roadmap/semana_1) |

---

<div align="center">

**Built in public. Learned the hard way.**

*The best security engineers are the ones who built things first.*

</div>


# 🛡️ Cyber Roadmap — De Desenvolvedor a Engenheiro de Segurança

> Um caminho estruturado e hands-on para desenvolvedores que estão migrando para cibersegurança. Construído na crença de que os melhores profissionais de segurança são os que entendem como as coisas são *construídas* — e portanto como elas *quebram*.

---

## 📋 Índice

- [Filosofia](#filosofia)
- [Fase 1 — Fundamentos (Meses 1–4)](#fase-1--fundamentos-meses-14)
  - [Módulo 1.1 — TCP/IP, OSI e DNS](#módulo-11--tcpip-osi-e-dns)
  - [Módulo 1.2 — Criptografia na Prática](#módulo-12--criptografia-na-prática)
  - [Módulo 1.3 — Linux Além do `cd` e `ls`](#módulo-13--linux-além-do-cd-e-ls)
- [Fase 2 — Habilidades Ofensivas (Meses 4–9)](#fase-2--habilidades-ofensivas-meses-49)
  - [Módulo 2.1 — Segurança Web](#módulo-21--segurança-web)
  - [Módulo 2.2 — Exploração Binária](#módulo-22--exploração-binária)
  - [Módulo 2.3 — Active Directory](#módulo-23--active-directory-o-mundo-windows)
- [Fase 3 — Maturidade do Especialista (Mês 9 em diante)](#fase-3--maturidade-do-especialista-mês-9-em-diante)
  - [Módulo 3.1 — Domínio do Ofício](#módulo-31--domínio-do-ofício)
  - [Módulo 3.2 — Threat Hunting e Defesa](#módulo-32--threat-hunting-e-defesa)
  - [Módulo 3.3 — O Verdadeiro Senior](#módulo-33--o-verdadeiro-senior)
- [Diário de Bordo](#diário-de-bordo)

---

## Filosofia

A maioria das pessoas entra em segurança memorizando ferramentas. Este roadmap segue o caminho oposto: **entender os fundamentos, construir as coisas à mão, depois quebrá-las**. Cada módulo segue o mesmo ciclo:

```
Aprenda a teoria → Observe na prática → Implemente em código → Ataque
```

Se você já sabe programar, tem uma vantagem enorme. Use-a.

---

## Fase 1 — Fundamentos (Meses 1–4)

> **Meta:** Entender o substrato em que tudo roda — redes, criptografia e o sistema operacional.

---

### Módulo 1.1 — TCP/IP, OSI e DNS

**Livro:** [Computer Networking: A Top-Down Approach](https://www.cs.sjtu.edu.cn/~linghe.kong/CS339/Download/ComputerNetworking.pdf) — Kurose & Ross

**Laboratórios (Wireshark):**
- Baixe o [livro de exercícios práticos do Kurose](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- Capture seu próprio tráfego. Filtre. Siga streams TCP.
- **Veja o Three-Way Handshake acontecer em tempo real.** Observe pacotes DNS. Visualize o TLS handshake byte a byte.

**Programe (Python + Scapy):**
1. Escreva um sniffer que capture requisições DNS na sua rede.
2. Escreva um programa que capture pacotes TCP SYN e logue origem/destino.
3. **Escreva um script de ARP Spoofing** que envenene a tabela ARP do seu próprio roteador — somente em uma VM isolada. Construa pacote por pacote. Isso sozinho vai te ensinar mais TCP/IP do que qualquer curso.

**Por que isso importa:** Você não consegue atacar ou defender uma rede que não entende de verdade. Ferramentas como o Wireshark tornam o invisível visível.

---

### Módulo 1.2 — Criptografia na Prática

**Curso:** [Cryptography I — Dan Boneh (Stanford/Coursera)](https://www.coursera.org/learn/crypto)
Hardcore. Matemático. Perfeito para desenvolvedores. Foque nas seções de ataques a cifras e protocolos.

**Desafios (CryptoPals):** [cryptopals.com](https://cryptopals.com)
- Faça os sets na linguagem de sua preferência.
- Você vai implementar AES no modo ECB e depois **quebrá-lo**. Vai executar um ataque de Padding Oracle do zero.
- É a ponte perfeita entre desenvolvimento de software e criptografia aplicada.

**Por que isso importa:** Quase toda grande brecha de segurança da história tem um componente criptográfico. Entender falhas de cripto por dentro é inegociável.

---

### Módulo 1.3 — Linux Além do `cd` e `ls`

**Meta:** Ir de usuário a administrador que entende hardening no nível do SO.

**Leituras:**
- [The Linux Command Line](https://linuxcommand.org/tlcl.php) — William Shotts (dominar o shell)
- *UNIX and Linux System Administration Handbook* — Evi Nemeth et al. (entender como realmente funciona)

**O Exercício Doloroso da VM:**
Instale o Arch Linux (ou Gentoo) em uma VM. **Sem GUI. Só terminal.**
Configure a rede, o bootloader e o kernel do zero. Vai doer. Esse é o ponto — quando terminar, você vai entender cada camada do SO.

**Lab de Hardening:**
1. Suba um servidor web na sua VM Arch.
2. Aplique um guia de hardening (ex: [CIS Benchmark](https://www.cisecurity.org/cis-benchmarks)).
3. Desabilite serviços desnecessários, configure o `iptables`, audite permissões com `chmod 700`.
4. **Agora tente invadir a VM a partir de uma segunda VM.** Defenda e ataque a mesma máquina.

---

## Fase 2 — Habilidades Ofensivas (Meses 4–9)

> **Meta:** Aprender a quebrar o que você sabe construir.

---

### Módulo 2.1 — Segurança Web

**Meta:** Você já sabe construir aplicações web. Agora vai aprender a quebrá-las.

**Plataforma:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) — Grátis, criado pelos criadores do Burp Suite. O melhor recurso do mundo para desenvolvedores entrando em segurança.

**Roteiro:**
1. Leia a teoria de cada tópico **antes** de fazer o laboratório.
2. Percorra todos os labs nessa ordem: **SQL Injection → XSS → CSRF → Falhas de Autenticação**
3. Cada lab te dá uma aplicação vulnerável real para explorar — sem simulações.
4. Como desenvolvedor, o estalo vem rápido: *"Cara, eu cometi exatamente esse erro em produção."*

**Por que isso importa:** Vulnerabilidades web são a superfície de ataque mais explorada em brechas do mundo real. Seu background de dev faz isso clicar mais rápido do que para qualquer outra pessoa.

---

### Módulo 2.2 — Exploração Binária

**Meta:** Entrar na mente da máquina. Sair completamente da zona de conforto do desenvolvedor.

**Pré-requisito:** Aprenda Assembly x86-64.
A playlist [Intro to x86 Assembly Language](https://opensecuritytraining.info/IntroX86.html) no OpenSecurityTraining.info é o ponto de partida certo.

**Plataformas de Prática:**

| Plataforma | O que você vai aprender |
|---|---|
| [pwn.college](https://pwn.college) | CTF progressivo do zero — CLI até exploração de kernel, criado por um professor de segurança |
| [Exploit Education / Protostar](https://exploit.education) | Baixe as VMs e corrompa stacks, pule para endereços de memória e execute shellcode |

**Por que isso importa:** É aqui que você entende o que é um buffer overflow *de verdade* — não como conceito, mas como bytes sobrescrevendo um endereço de retorno. Isso separa engenheiros de segurança de script kiddies.

---

### Módulo 2.3 — Active Directory (O Mundo Windows)

**Meta:** Aprender como a maioria dos ambientes corporativos é comprometida.

**Plataforma:** [TryHackMe](https://tryhackme.com) — assine o plano premium.

**Roteiro:**
- Siga as trilhas **"Offensive Pentesting"** e **"Cyber Defense"**.
- Foque nas salas de Active Directory: *Attacktive Directory*, *Post-Exploitation Basics*, *Breaching AD*.
- Você vai usar ferramentas reais em um ambiente de rede Windows ao vivo:
  - **BloodHound** — mapeamento de relações no AD
  - **Mimikatz** — extração de credenciais
  - **Impacket** — suite de protocolos de rede

**Por que isso importa:** O Active Directory é a espinha dorsal de quase toda rede corporativa. Saber atacá-lo é essencial para red teams, e saber defendê-lo é crítico para blue teams.

---

## Fase 3 — Maturidade do Especialista (Mês 9 em diante)

> **Meta:** Profundidade, especialização e pesquisa. Deixar de ser um usuário de ferramentas — tornar-se um engenheiro que as constrói.

---

### Módulo 3.1 — Domínio do Ofício

**Plataforma:** [Hack The Box (HTB)](https://www.hackthebox.com) — assinatura VIP.
O playground dos profissionais. Sem passo a passo. Você recebe um IP e uma página em branco.

**Estratégia:**
- Resolva máquinas aposentadas, depois assista write-ups do **IppSec** no YouTube.
- Foque em internalizar **metodologia**: Como enumerar? O que olhar primeiro? Como pivotar entre hosts?
- Construa um sistema pessoal de notas (Obsidian, Notion) com seus checklists de enumeração e padrões de ataque.

**Certificação (Opcional, mas que consolida a carreira):**
**OSCP (Offensive Security Certified Professional)** — o padrão ouro para provar habilidade prática. O curso é o PEN-200. Tente após o HTB te dar confiança suficiente.

---

### Módulo 3.2 — Threat Hunting e Defesa

**Meta:** Saber o que o atacante faz para poder caçá-lo.

**Lab de SIEM em Casa:**
1. Instale um SIEM gratuito: [Wazuh](https://wazuh.com) ou [Elastic Security](https://www.elastic.co/security)
2. Injete logs do seu PC, do seu roteador, das suas VMs.
3. **Crie regras de detecção para os ataques que você executa no seu lab HTB.**
4. O objetivo: detectar seu próprio ataque. Ser atacante e defensor ao mesmo tempo.

**Framework:** Estude o [MITRE ATT&CK](https://attack.mitre.org).
Para cada máquina do HTB que você completar, mapeie cada etapa do ataque a uma técnica do ATT&CK.

> Exemplo: `T1003.001 — OS Credential Dumping: LSASS Memory`

Essa prática te transforma de pentester em profissional de **Threat Intelligence**.

---

### Módulo 3.3 — O Verdadeiro Senior

Essa fase não tem data de fim. É uma disciplina contínua.

**Leia RFCs:** Quer realmente dominar um protocolo? Leia a RFC original. Sem resumo, sem tutorial. A fonte.
- [RFC 793](https://datatracker.ietf.org/doc/html/rfc793) — TCP
- [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035) — DNS
- [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) — TLS 1.3

**Leia Código-Fonte:** Não use só Ghidra. Puxe o código do `netcat`, estude os internals do kernel Linux, leia a implementação de uma biblioteca de criptografia.

**Construa e Publique:**
- Automatize uma técnica de ataque que você executou manualmente — construa uma ferramenta Python para isso.
- Publique no GitHub com documentação.
- Contribua com projetos open-source de segurança.

**Seu GitHub é seu portfólio.** Cada ferramenta construída, cada técnica documentada, cada write-up de CTF publicado compõe uma reputação ao longo do tempo.

---

## Diário de Bordo

Notas de progresso, reflexões semanais e write-ups de laboratório.

| Entrada | Link |
|---|---|
| Semana 1 | [github.com/ppfuark/cyber_roadmap/semana_1](https://github.com/ppfuark/cyber_roadmap/semana_1) |

---

<div align="center">

**Construído em público. Aprendido da forma difícil.**

*Os melhores engenheiros de segurança são os que construíram coisas primeiro.*

</div>
