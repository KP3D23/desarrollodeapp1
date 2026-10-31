# Primeros pasos en la creación de mi Aplicación Web

**Autor:** Carlos Andrade  
**Subproyecto:** Desarrollo de Aplicaciones I (Módulo I)  

---

## Metodología de Desarrollo en V: Fase de Verificación (Rama Descendente)

Este proyecto se desarrolla bajo los principios de la **Metodología de Desarrollo en V**, un modelo secuencial y estructurado que garantiza la trazabilidad, verificación y validación constante entre las fases de planificación y construcción del software. A continuación, se detalla la **Rama Descendente (Fase de Verificación)**, la cual funge como nuestra hoja de ruta arquitectónica y funcional:

### 1. Análisis de Requisitos (Requirement Gathering)
* **Descripción:** Fase inicial donde se identifican y documentan las necesidades de los usuarios finales, así como las restricciones y funcionalidades globales del sistema.
* **Objetivo:** Definir con precisión el alcance operativo del software y los servicios que ofrecerá a los distintos tipos de usuarios.
* **Entregable:** Especificación formal de requisitos funcionales y no funcionales.

### 2. Análisis del Sistema (System Analysis)
* **Descripción:** Traducción de los requisitos de negocio en especificaciones técnicas estructuradas. Se define el comportamiento general del software y su arquitectura funcional.
* **Objetivo:** Modelar las reglas del negocio, el flujo de información y la interacción entre los componentes del sistema.

### 3. Diseño de Software / Arquitectura (Software Design)
* **Descripción:** Establecimiento de la estructura macro del sistema, seleccionando componentes, interfaces y el stack tecnológico idóneo.
* **Stack Tecnológico Seleccionado:**
  * **Lenguaje Backend:** Python
  * **Framework Backend:** Django
  * **Frontend & Estilos:** HTML5, CSS3, JavaScript (Vite.js) y Bootstrap 5
  * **Contenedor e Infraestructura:** Docker
  * **Control de Versiones:** Git y GitHub

### 4. Diseño de Módulos (Module Design)
* **Descripción:** Desglose detallado de la lógica interna, algoritmos y modelado de datos específicos para cada módulo funcional de la aplicación web.
* **Objetivo:** Estructurar componentes clave como el subsistema de autenticación, control de perfiles, gestión de bases de datos y jerarquía de permisos.

### 5. Punto de Inflexión
* **Descripción:** Hito crítico que marca la culminación de la fase de diseño e ingeniería descendente, validando que la planificación esté lista para dar paso a la construcción tangible del sistema.

### 6. Codificación (Coding)
* **Descripción:** Fase de ejecución donde las especificaciones técnicas y los diseños modulares se traducen en código fuente ejecutable.
* **Actividades implementadas en el proyecto:** 
  * Configuración del entorno de desarrollo mediante Docker.
  * Inicialización y control de versiones en el repositorio de GitHub.
  * Instalación y configuración del framework Django y librerías complementarias (*crispy-bootstrap5*).
  * Creación del backend y la aplicación modular de gestión de cuentas (*accounts*) con control de acceso basado en roles (*RBAC*): **Administrador, Gestor, Usuario y Visitante**.
  * Configuración avanzada del panel de control nativo (*Django Admin*).

---
