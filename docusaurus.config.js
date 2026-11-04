// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// Usuario y repositorio de GitHub donde se publica el sitio.
const USUARIO = 'pesco13';
const REPO = 'Python-para-Quimica';

// Autoria del material.
const AUTOR = 'Paulina Escobar';
const CORREO = 'p.escobar@utp.edu.co';
const ORCID = 'https://orcid.org/0009-0009-1454-212X';

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
    autor: AUTOR,
  },

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  plugins: [
    [
      // En noviembre de 2026 las practicas se renumeraron para que el numero
      // coincidiera con el orden del curso. Estas redirecciones mantienen
      // vivos los enlaces anteriores.
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {from: '/practicas/03-moleculas-con-rdkit', to: '/practicas/06-moleculas-con-rdkit'},
          {from: '/practicas/04-pubchem-desde-python', to: '/practicas/07-pubchem-desde-python'},
          {from: '/practicas/05-similitud-y-espacio-quimico', to: '/practicas/08-similitud-y-espacio-quimico'},
          {from: '/practicas/06-estructuras-3d-y-conformeros', to: '/practicas/09-estructuras-3d-y-conformeros'},
          {from: '/practicas/07-primer-calculo-cuantico-pyscf', to: '/practicas/10-primer-calculo-cuantico-pyscf'},
          {from: '/practicas/08-graficas-para-quimica', to: '/practicas/03-graficas-para-quimica'},
          {from: '/practicas/09-calibracion-y-error', to: '/practicas/04-calibracion-y-error'},
          {from: '/practicas/10-cinetica-y-ajuste', to: '/practicas/05-cinetica-y-ajuste'},
        ],
      },
    ],
  ],

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
            title: 'Autoría',
            items: [
              {label: AUTOR, href: ORCID},
              {label: 'ORCID', href: ORCID},
              {label: 'Escribir', href: `mailto:${CORREO}`},
            ],
          },
          {
            title: 'Más',
            items: [
              {label: 'GitHub', href: `https://github.com/${USUARIO}/${REPO}`},
              {label: 'Cómo citar', href: `https://github.com/${USUARIO}/${REPO}/blob/main/CITATION.cff`},
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} ${AUTOR} · Código con licencia MIT, textos con CC BY 4.0 · Hecho con Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash'],
      },
    }),
};

export default config;
