# 🧠 Wiki-Agéntica: Protocolo Maestro de Gestión del Conocimiento

Este archivo define la constitución, la estructura y las reglas de operación para cualquier Agente de IA que actúe sobre esta base de conocimiento. El Agente es el mantenedor proactivo; el Usuario es el estratega.

# 1. 📂 Mapa del Proyecto (Estructura de Directorios)

Cualquier agente debe respetar estrictamente esta jerarquía para garantizar la integridad del sistema:

* /.agentic/ (El Cerebro): Instrucciones de bajo nivel para el agente.
  * skills/: Capacidades lógicas y reglas de procesamiento específicas.
  * workflows/: Algoritmos secuenciales para tareas complejas (ej. inicialización, ingesta).
  * templates/: Esquemas YAML y Markdown para la estandarización de notas.
* /doc/ (Contexto Humano): Documentación de referencia, guías de usuario y arquitectura.
* /raw/ (Entrada - Inmutable): Material bruto original. Prohibido modificar o borrar.
* /wiki/ (Salida - Grafo de Conocimiento): El producto destilado y estructurado.
  * fuentes/: Resúmenes de materiales originales y perfiles de autores/creadores.
  * entidades/: Objetos con nombre propio (personas, herramientas, organizaciones).
  * conceptos/: Ideas abstractas, métodos, teorías y modelos mentales.
  * registros/: Diario de operaciones (log) y estados del sistema.
* /scripts/ (Las Manos): Herramientas de soporte y scripts de automatización.

1. 🤖 Protocolo de Descubrimiento (AI-First)

Al iniciar una sesión o tarea, el Agente debe seguir este orden de lectura:

1. Consultar este archivo RULES.md para entender el entorno.
2. Localizar el flujo de trabajo correspondiente en /.agentic/workflows/.
3. Cargar las reglas lógicas necesarias de /.agentic/skills/.
4. Prioridad de Verdad: Las instrucciones en /.agentic/ tienen prioridad sobre la documentación en /doc/.

# 3. 🛠 Reglas Operativas Core

## 3.1. Ingesta y Síntesis (Filtro MVC)

El Agente debe priorizar la densidad de información sobre el volumen de archivos:

* MVC (Mínimo Valor de Conocimiento): Solo se crea una nota atómica en /wiki/ si la información nueva aporta al menos 3 puntos de datos o ideas sustanciales. De lo contrario, la información se integra en la nota de la fuente.

* Contexto Temporal: Es obligatorio registrar la fecha de procesamiento y, si existe, la fecha de creación del material original.

* Multimodalidad: Cualquier contenido visual en /raw/assets/ debe ser descrito textualmente en la wiki para asegurar su indexabilidad semántica.

## 3.2. Gestión de la Información

* Propiedad: El Agente responde a consultas basándose exclusivamente en el contenido procesado en `/wiki/` . La carpeta `/raw/` es material de trabajo, no de consulta directa para el usuario.

* Inmutabilidad: Los archivos en `/raw/` no se modifican bajo ninguna circunstancia.

## 3.3. Integridad del Grafo (Conectividad)

* Bidireccionalidad: Si una Nota A enlaza a [[Nota B]], el agente debe asegurar que la Nota B tenga un enlace de retorno en su sección de relacionados.

* Detección de Menciones: Al crear o actualizar contenido, el agente debe identificar términos clave que ya existan en la wiki y transformarlos en enlaces activos ([[wikilinks]]).

# 4. 📊 Estándar de Metadatos (YAML)

Todas las notas en la `/wiki/` deben seguir una estructura de metadatos estricta. Se diferencia el uso de etiquetas de clasificación (en el YAML) de las etiquetas de contexto (en el cuerpo del texto).

## 4.1. Bloque de Metadatos (YAML)

Ubicado al inicio de cada nota. Se utiliza para definir la naturaleza del archivo y permitir consultas con plugins como Dataview.

YAML
---

title: "Título de la Nota"
aliases: [Sínonimo1, Sinonimo2]
type: [entidad | concepto | fuente | registro]
tags: [clase/subclase] # Uso de taxonomía jerárquica
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

## 4.2. Reglas de Sintaxis para Tags

Para mantener un grafo limpio y evitar duplicidades, el Agente debe aplicar estas reglas:

* Formato: Uso estricto de kebab-case (ej. #inteligencia-artificial en lugar de #IA o #Inteligencia_Artificial).
* Singularidad: Las etiquetas se definen siempre en singular (ej. #empresa, no #empresas).
* Jerarquía: Siempre que sea posible, usar tags anidados para agrupar temas (ej. #metodología/agéntica).

## 4.3. Estrategia de Etiquetado Mixto

* Tags de YAML (Clasificación): Definen qué es la nota. Son etiquetas estructurales que no cambian (ej. tags: [fuente/video]).
* Tags en Línea (Contexto): Se insertan en el cuerpo del texto para marcar temas específicos, riesgos o atributos cualitativos. Estos permiten al usuario humano rastrear conceptos transversales en el Graph View de Obsidian (ej. "Esta tesis presenta un alto #riesgo-regulatorio").

## 4.4. Enlazado vs. Etiquetado

Usar [[Enlace Bidireccional]] para Entidades o Conceptos que tienen (o deben tener) su propia nota en la wiki.

Usar `#Etiqueta` para Atributos o Temáticas que no requieren una página independiente pero deben ser agrupables.

1. 🔍 Mantenimiento y Calidad

El Agente es responsable de realizar validaciones lógicas tras cada operación:

* Resolución de Conflictos: Si un nuevo dato contradice contenido existente, se debe marcar con un bloque > [!CAUTION] Contradicción indicando ambas versiones.

* Saneamiento: Identificar y proponer la fusión de notas que traten el mismo tema bajo nombres distintos (alias).

* Consistencia: Asegurar que el archivo de índice general refleja siempre la estructura actual de la wiki.

Última actualización: 2026-04-23
Estado: Operativo
