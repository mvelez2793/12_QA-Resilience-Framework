# 🚀  Test Plan & Arquitectura QA


| Capa / Componente | Tecnologías | Propósito / Alcance |
| :--- | :--- | :--- |
| **🤖 Automatización E2E** | ![Python] ![Appium] ![Android] | Pruebas funcionales e integrales móviles automatizadas. |
| **📊 Performance & Stress** | ![Postman] | Ejecución de Postman Performance Runner con VUs concurrentes. |
| **🔒 Seguridad (DAST/MitM)** | ![Charles Proxy] | Validación de políticas TLS y bypass de SSL Pinning. |
| **📈 Observabilidad** | ![Grafana] | Telemetría integrada para monitoreo en tiempo real de Connection Pools. |
| **⚙️ Infraestructura** | ![Node.js] ![PostgreSQL] | Servidor de aplicación y capa de persistencia de datos analizada. |



---

## 1. Descripción del Proyecto
El presente documento detalla la estrategia, alcance y resultados de la auditoría técnica de Calidad y Seguridad (Caja Negra) 

La evaluación se centró en el flujo crítico de negocio (Autenticación / Inicio de Sesión), sometiendo a la aplicación a pruebas de automatización UI End-to-End (E2E), validación de resiliencia ante errores y análisis dinámico de seguridad de la red (DAST) para garantizar la integridad de los datos financieros del usuario.

---

## 2. Objetivos de la Auditoría

### 🎯 Objetivos de Negocio
* Garantizar que los usuarios legítimos puedan acceder a la plataforma sin fricciones (Happy Path).
* Validar que el sistema impida el acceso a credenciales no autorizadas sin exponer información sensible que facilite ataques de enumeración (Account Enumeration).

### ⚙️ Objetivos Técnicos
* Desarrollar un framework de automatización E2E escalable e **idempotente** (cero fugas de estado entre pruebas).
* Auditar la configuración de seguridad de red (Network Security Configuration) del cliente móvil.
* Evaluar el comportamiento de la infraestructura backend ante inyecciones automatizadas en ventanas de alta concurrencia.

---

## 3. Alcance y Límites (Scope & Boundaries)

Para mantener la precisión de la auditoría y cumplir con los tiempos de entrega, se delimitaron fronteras estrictas de prueba basadas en la gestión de riesgos.

| Categoría | Dentro del Alcance (In Scope) | Fuera del Alcance (Out of Scope) |
| :--- | :--- | :--- |
| **Entorno de Pruebas** | Android 12 (API 31) - Estrategia de compatibilidad *Legacy*. | iOS, Android 15 (API 35), Dispositivos físicos. |
| **Módulos App** | Pantalla de Onboarding, Login y validaciones de campos UI. | Transferencias, Registro completo, Dashboard interno. |
| **Tipos de Prueba** | Automatización E2E (UI), DAST (MitM), Negative Testing. | Pruebas de Carga/DDoS directas al servidor, Inyección SQL. |
| **Herramientas** | Appium 2, Python 3, UiAutomator2, Charles Proxy. | Appium Inspector nativo (solo usado para mapeo estático). |

---

## 4. Estrategia de Pruebas (Test Strategy)

El enfoque arquitectónico seleccionado fue la **Agrupación por Módulo (Feature-Based Grouping)**. La estrategia se dividió en tres capas fundamentales:

1. **Capa de Estabilidad (Idempotencia):** Uso de comandos nativos del SO (`mobile: clearApp`) en las fases de Teardown para destruir el caché y garantizar que cada prueba inicie en un entorno estéril.
2. **Capa de Resiliencia UI:** Implementación de selectores globales robustos (`XPath` por índices) respaldados por *Explicit Waits* (`WebDriverWait` de 15s) para tolerar latencias de red impredecibles.
3. **Capa de Seguridad (Shift-Left Testing):** Intercepción activa del tráfico HTTP/HTTPS mediante proxy inverso para validar las políticas de validación de certificados de la aplicación en tiempo de ejecución.
---
## 5. Instrucciones de Replicación (Setup & Execution)

Para garantizar la reproducibilidad de esta auditoría, el entorno debe configurarse siguiendo estos pasos:

## 🛠️ Stack Tecnológico de Auditoría
Para garantizar la reproducibilidad y el rigor técnico, se ha utilizado el siguiente ecosistema:
* **Automatización E2E:** Python 3, Appium 2, UiAutomator2.
* **Performance & Stress Testing:** Postman Performance Runner (VUs concurrentes).
* **Seguridad (DAST/MitM):** Charles Proxy (TLS/SSL Pinning validation).
* **Observabilidad:** Telemetría integrada con Grafana (Monitoreo de Connection Pools).
* **Infraestructura:** Node.js, PostgreSQL (Capa de persistencia).

### Instalación de Dependencias
```bash
# 1. Instalar el driver de UI Automator 2 en Appium
appium driver install uiautomator2

# 2. Instalar el cliente de Appium y Selenium para Python
pip install Appium-Python-Client selenium

# 1. Levantar el servidor de Appium (Asegurar que el emulador esté encendido)
appium --allow-cors

```
---

## 🧑‍💻 Perfil Técnico
**María Auxiliadora Vélez Mendoza** - *QA Engineer Full-Stack*

