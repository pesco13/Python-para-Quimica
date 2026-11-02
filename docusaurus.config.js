// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// Usuario y repositorio de GitHub donde se publica el sitio.
const USUARIO = 'pesco13';
const REPO = 'Python-para-Quimica';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Python para Química',
  tagline: 'Prácticas de Python aplicado a la química',
  favicon: 'img/logo.svg',

  future: {
    v4: true,
  },

  url: `https://${USUARIO}.github.io`,
  baseUrl: `/${REPO}/`,
  organizationName: USUARIO,
  projectName: REPO,
  trailingSlash: false,

  onBrokenLinks: 'throw',

  customFields: {
    usuario: USUARIO,
    repo: REPO,
  },

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  themes: [
    [
      // Buscador que funciona sin cuenta de Algolia: construye el indice
      // durante el build y lo sirve como un archivo estatico mas.
      require.resolve('@easyops-cn/docusaurus-search-local'),
      /** @type {import('@easyops-cn/docusaurus-search-local').PluginOptions} */
      ({
        hashed: true,
        language: ['es'],
        indexBlog: false,
        docsRouteBasePath: '/',
      }),
    ],
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          editUrl: `https://github.com/${USUARIO}/${REPO}/tree/main/`,
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        respectPrefersColorScheme: true,
      },
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      navbar: {
        title: 'Python para Química',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg',
          srcDark: 'img/logo-oscuro.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Contenido',
          },
          {
            to: '/entregables',
            label: 'Entregables',
            position: 'left',
          },
          {
            href: `https://github.com/${USUARIO}/${REPO}`,
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Curso',
            items: [
              {label: 'Inicio', to: '/'},
              {label: 'Prácticas', to: '/practicas'},
              {label: 'Entregables', to: '/entregables'},
            ],
          },
          {
            title: 'Herramientas',
            items: [
              {label: 'Google Colab', href: 'https://colab.research.google.com'},
              {label: 'RDKit', href: 'https://www.rdkit.org'},
              {label: 'PubChem', href: 'https://pubchem.ncbi.nlm.nih.gov'},
              {label: 'PySCF', href: 'https://pyscf.org'},
            ],
          },
          {
            title: 'Más',
            items: [
              {label: 'GitHub', href: `https://github.com/${USUARIO}/${REPO}`},
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} · Licencia MIT · Hecho con Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash'],
      },
    }),
};

export default config;
