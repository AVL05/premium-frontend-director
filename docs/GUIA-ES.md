# Instalación y uso — Guía rápida en español

La skill **Premium Frontend Director** funciona en Codex y Claude Code. Sirve para planificar, implementar y revisar interfaces frontend con dirección artística coherente. **No requiere pagar ni instalar otras skills**, aunque algunas pueden aportar más criterio visual.

## 1. ¿Qué perfil elijo?

| Perfil | Instala | Cuándo |
| --- | --- | --- |
| **Core** | Premium Frontend Director | Quieres una instalación ligera, sin complementos |
| **Premium (recomendado)** | **Core + UI UX Pro Max + Taste Skill + Impeccable + Web Design Guidelines** | Landing pages, portfolios, marcas creativas y webs con mayor ambición visual |
| **Studio** | **Todas las de Premium + Design System Patterns**; añade **Vercel React Best Practices** si usas React/Next.js; **Responsive Design**, **Accessibility Compliance** y **Tailwind Design System** solo si lo necesitas | SaaS, dashboards, aplicaciones complejas y sistemas de diseño extensos |

**Importante:** Studio *no* significa instalar absolutamente todas las skills disponibles. Elige las que correspondan a tu stack y al objetivo. No se gana calidad por cantidad. Todos los complementos son opcionales.

## Elige también el nivel de ambición creativa

**No es lo mismo que el perfil de skills.** `Core / Premium / Studio` selecciona herramientas; `Refined / Expressive / Immersive` define el nivel de transformación artística.

| Ambición | Qué significa |
| --- | --- |
| **Refined** | Pulido editorial, legibilidad y composición controlada |
| **Expressive** | Cambio estructural reconocible e interacción original |
| **Immersive** | Escena o experiencia cinematográfica con profundidad y transición distintiva; WebGL solo si aporta valor |

Para un archivo fotográfico experimental, prueba **Premium + Immersive**. El agente **debe implementar y revisar primero un prototipo real** de la portada y una transición; comparar antes/después en el mismo viewport y pasar **G11 Visual Ambition**. Si solo cambió márgenes, colores o fuentes ante una petición radical, **G11 FAIL**, aunque los tests técnicos estén verdes. También debe construir un fallback de reducción de movimiento, sin WebGL y compatible con móvil.

**Ejemplo de prompt:** «Usa premium-frontend-director con perfil Premium y ambición Immersive. Quiero un rediseño estructural, no un retoque de tipografía. Antes de cambiar todas las rutas, implementa una portada inmersiva funcional, compara capturas a 375 y 1440 px y verifica la interacción. Si G11 falla, itera antes de continuar. Conserva accesibilidad, contratos y rendimiento».

## 2. Qué necesitas antes de instalar

- **Codex o Claude Code** actualizado, con soporte de Agent Skills.
- **Node.js 22 o posterior y npm/npx**, recomendado si vas a usar Premium o Studio (Taste Skill requiere Node 22+).
- **Python 3**, para los scripts de búsqueda de UI UX Pro Max. Compruébalo con `python --version` en Windows o `python3 --version` en macOS/Linux.
- **Chrome, Edge o Chromium**, para funciones visuales de Taste y el navegador de revisión. Si usas el script de auditoría integrado, instala **Playwright** en el proyecto donde se ejecutará.
- Un proyecto frontend con su runtime habitual. Puedes instalar las skills de forma global o solo para un proyecto; no mezcles ambas modalidades sin necesidad.

Comprueba tus herramientas:

```bash
node --version
npm --version
python --version
```

En macOS/Linux, el último comando puede ser `python3 --version`. Si falta algo, instálalo desde su fuente oficial antes de seguir. **No ejecutes comandos de instalación de terceros sin revisar sus permisos y procedencia.**

## 3. CORE — la instalación más sencilla

Ejecuta en una terminal dentro de tu proyecto:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

Selecciona Codex o Claude Code si el instalador te pregunta. Reinicia la sesión del agente y confirma que aparece `premium-frontend-director` entre sus skills.

**Alternativa para Claude Code:** dentro de Claude Code:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

Utiliza **uno** de estos métodos para evitar duplicados.

## 4. PREMIUM — el perfil que recomiendo

Instala **Core** y después estos **cuatro complementos**:

**A. UI UX Pro Max — biblioteca de sistemas visuales**

En un proyecto con Codex:

```bash
npx ui-ux-pro-max-cli init --ai codex
```

En un proyecto con Claude Code, utiliza **en su lugar**:

```bash
npx ui-ux-pro-max-cli init --ai claude
```

Si quieres inspeccionar cambios antes de instalarlos:

```bash
npx ui-ux-pro-max-cli init --ai codex --dry-run
```

Requiere Python 3 para las búsquedas. El comando instala archivos propios del proveedor, no solo un `SKILL.md`.

**B. Taste Skill — dirección artística**

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
```

Taste Skill necesita Node.js 22+ y un navegador Chrome/Edge/Chromium para sus scripts.

**C. Impeccable — crítica y acabado**

```bash
npx impeccable install
```

Elige tu agente y ámbito de instalación; habilita el hook de diseño si lo deseas. En Codex también puede requerir aprobar el hook desde `/hooks`.

**D. Web Design Guidelines — revisión de interfaz**

```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

Reinicia Codex o Claude Code y verifica que reconoce las skills. La instalación correcta de un CLI no significa por sí sola que se haya activado la integración.

## 5. STUDIO — complementos para proyectos grandes

Instala **Premium** y añade:

**Design System Patterns — recomendado para Studio**

```bash
npx skills add wshobson/agents --skill design-system-patterns
```

**Según el tipo de proyecto**, utiliza solo las necesarias:

```bash
# Solo React / Next.js
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices

# Layouts responsive especialmente complejos
npx skills add wshobson/agents --skill responsive-design

# Revisión de accesibilidad más profunda
npx skills add wshobson/agents --skill accessibility-compliance

# Si tu proyecto usa Tailwind
npx skills add wshobson/agents --skill tailwind-design-system
```

Confirma el nombre y la disponibilidad de cada skill opcional en el repositorio original antes de instalarla. No todas las herramientas son necesarias en todos los proyectos.

**Herramienta opcional para inspeccionar el navegador (no es una skill):**

```bash
npm install -g agent-browser
agent-browser install
```

No sustituye automáticamente al script interno `visual-audit.mjs`, que necesita Playwright.

## Especializaciones opcionales — cuándo añadirlas

El conjunto **Premium sigue teniendo cinco skills**. Estas especializaciones no se instalan por defecto y tampoco son requisitos del modo Immersive.

| Si el proyecto necesita... | Repositorio | Aporta |
| --- | --- | --- |
| Animaciones complejas con GSAP / ScrollTrigger | [GreenSock GSAP Skills](https://github.com/greensock/gsap-skills) | Timelines, scroll y limpieza de animaciones |
| Diagnosticar Core Web Vitals o Lighthouse | [Web Quality Skills](https://github.com/addyosmani/web-quality-skills) | Medición y análisis reales del rendimiento |
| Una escena espacial con Three.js/WebGL | [Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | Escenas 3D, renderizado y fallbacks |

**Solo tras inspeccionar el stack**, puedes consultar las skills disponibles en cada repositorio:

```powershell
npx skills add greensock/gsap-skills
npx skills add addyosmani/web-quality-skills
npx skills add CloudAI-X/threejs-skills
```

Estos comandos son una **selección interactiva** de un repositorio, no una orden para instalar todo. Elige la skill específica y el ámbito **project/local**. Revisa su `SKILL.md`, dependencias y licencia antes de aceptar. No los ejecutes todos juntos: un proyecto sin WebGL no necesita Three.js Skills.

**Para RAW.VIVES:** si el prototipo usa GSAP y una escena Three.js real, pueden contribuir los especialistas correspondientes. Web Quality se invoca para métricas comprobables, no para declarar el rendimiento óptimo sin mediciones. Playwright o navegador real y G11 siguen siendo obligatorios para validar el impacto artístico.

## 6. ¿Cómo usarla después de instalar?

Abre **tu proyecto frontend** en Codex o Claude Code (no el repositorio de la skill) y pega uno de estos mensajes. Cambia el perfil a Core, Premium o Studio.

### Ejemplo — web con diseño premium

```text
Usa premium-frontend-director con el perfil Premium.
Analiza mi proyecto y las skills que tienes realmente disponibles.
Quiero una identidad visual memorable y profesional, adaptada a mi público,
sin gradientes, tarjetas ni layouts genéricos por defecto.

Propón tres conceptos distintos y elige el más coherente si no hace falta
mi aprobación. Define design.md, implementa el diseño, revisa la interfaz
real en móvil, tablet y escritorio, solicita una crítica visual con Impeccable
si está disponible y corrige las deficiencias. No inventes imágenes,
métricas, pruebas ni resultados. Indica qué integraciones se han usado,
cuáles faltan y cuáles no se han podido ejecutar.
```

### Ejemplo — SaaS complejo

```text
Usa premium-frontend-director con el perfil Studio.
Mantén mi arquitectura y mis flujos de negocio.
Crea una identidad visual y un sistema de componentes y tokens
consistentes; activa solamente las skills apropiadas para mi stack.
Incluye estados vacíos, carga, errores y navegación accesible.
Valida layout, funcionalidad y rendimiento en un navegador real;
documenta evidencia y limitaciones.
```

## 7. ¿Cómo comprobar que funciona?

1. Pide al agente que enumere las skills que **puede invocar realmente**. No basta con que haya carpetas en el disco.
2. Comprueba que entrega **tres direcciones visuales**, genera/actualiza `design.md` e implementa cambios reales.
3. Revisa las capturas de móvil y escritorio y que la navegación y los formularios funcionan.
4. Exige un informe de gates **PASS / FAIL / NOT RUN**. Si no pudo abrir el navegador, no debe afirmar que superó la prueba visual.
5. Para comprobar todos los métodos de instalación, sigue la [matriz de aceptación](manual-testing.md).

Los **tests automáticos de GitHub** validan el paquete y un ejemplo de Chromium, pero no garantizan un diseño excelente ni certifican la ejecución de las skills en tu ordenador.

## 8. Problemas comunes

| Problema | Solución |
| --- | --- |
| El agente no ve la skill | Reinicia la sesión y comprueba que la instalaste para el agente correcto |
| UI UX Pro Max no ejecuta búsquedas | Verifica Python 3 y el `--ai` elegido |
| Taste Skill no ejecuta scripts | Verifica Node.js 22+ y Chrome/Edge/Chromium |
| Impeccable no aplica hooks | Revisa la instalación, los permisos y `/hooks` en Codex |
| No hay capturas | Instala y configura Playwright o utiliza otra herramienta de navegador compatible |
| Un complemento no está disponible | Continúa con los recursos internos de Premium Frontend Director; las dependencias externas no son obligatorias |

## 9. Enlaces originales

- [Premium Frontend Director](https://github.com/AVL05/premium-frontend-director)
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Taste Skill](https://github.com/Leonxlnx/taste-skill)
- [Impeccable](https://github.com/pbakaus/impeccable)
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [Wshobson Agent Skills](https://github.com/wshobson/agents)
- [Agent Browser](https://github.com/vercel-labs/agent-browser)

La compatibilidad real en tu instalación concreta de Codex/Claude Code **sigue pendiente de tus pruebas**. Las instalaciones de terceros pueden evolucionar; utiliza las instrucciones oficiales actuales si alguna cambia.
