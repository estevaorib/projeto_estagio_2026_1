# 🏥 FilaSmart - Otimização de Filas Hospitalares

O **FilaSmart** é uma aplicação web desenvolvida com **Django** cujo objetivo é auxiliar instituições de saúde na **gestão e otimização do fluxo de atendimento**, reduzindo filas, tempos de espera e melhorando a experiência do paciente.

📱 **O projeto foi desenvolvido seguindo a abordagem _Mobile First_**, garantindo excelente usabilidade em dispositivos móveis desde o início e escalando progressivamente para tablets e desktops.

O sistema conta com uma **landing page institucional**, formulário de contato e um **painel administrativo** para gerenciamento das mensagens recebidas.

---

## 🎯 Proposta do Projeto

O FilaSmart foi pensado para:

- Apresentar uma solução de consultoria em gestão hospitalar
- Permitir que gestores entrem em contato via formulário
- Centralizar mensagens em um painel administrativo
- Possibilitar **visualização, edição e exclusão** das mensagens
- Garantir boa experiência visual com **Tailwind CSS**
- Aplicar boas práticas de organização e segurança em Django

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django**
- **HTML5**
- **Tailwind CSS (via CDN)**
- **Google Fonts**
- **SQLite**

---

## 📁 Estrutura do Projeto

```text
project_root/
│
├── manage.py
├── requirements.txt
│
├── core/                  # Configurações globais
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── contact/                 # App principal
│   ├── migrations/
│   ├── templates/
│   │       ├── base.html
│   │       ├── edit_contact.html
│   │       ├── landpage.html
│   │       ├── login.html
│   │       └── panel.html
│   │       └── thank_you.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│   └── forms.py
│
└── static/                   # Arquivos estáticos
│   └── landpage/
│           ├── images/
│           └── favicon/
```

## 🌐 Rotas da Aplicação

### Públicas

| Rota | Descrição |
|------|-----------|
| `/` | Landing page |
| `/login/` | Página de login |
| `/thank-you/` | Página exibida após envio do formulário |

### Administrativas

| Rota | Descrição |
|------|-----------|
| `/logout/` | Rota para fazer logout |
| `/panel/` | Painel de gerenciamento de mensagens |
| `/edit/<id>/` | Edição de mensagem |
| `/delete/<id>/` | Exclusão de mensagem |

> ⚠️ As rotas administrativas são protegidas por autenticação.

## 🚀 Como Rodar o Projeto Localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/estevaorib/projeto_estagio_2026_1.git
cd projeto_estagio_2026_1
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar as migrações
```bash
python manage.py migrate
```

### 5️⃣ Criar um superusuário
```bash
python manage.py createsuperuser
```

### 6️⃣ Iniciar o servidor
```bash
python manage.py runserver
```

### 🌐 Acesse no navegador
| Página | URL |
|------|-----------|
| Landing page | http://127.0.0.1:8000/ |
| Admin | http://127.0.0.1:8000/admin/ |
| Painel | http://127.0.0.1:8000/panel/ |

## 🎨 Interface e UX

- Design responsivo com **Mobile First**
- Layout limpo e moderno
- Tipografia consistente
- Feedback visual para ações (hover, focus, active)
- Componentes reutilizáveis
- Boa legibilidade em qualquer tamanho de tela

## 👨‍💻 Autor

**Estevão Ribeiro Santos**  
Estudante de Ciência da Computação — IFNMG Montes Claros  
