# Auditoría de Resiliencia y Seguridad

### 🛠️ Stack Tecnológico Utilizado

| Capa / Componente | Tecnologías | Propósito / Alcance |
| :--- | :--- | :--- |
| **🤖 Automatización E2E** | ![Python](https://shields.io) ![Appium](https://shields.io) ![Android](https://shields.io) | Pruebas funcionales e integrales móviles automatizadas. |
| **📊 Performance & Stress** | ![Postman](https://shields.io) | Ejecución de Postman Performance Runner con VUs concurrentes. |
| **🔒 Seguridad (DAST/MitM)** | ![Charles Proxy](https://shields.io) | Validación de políticas TLS y bypass de SSL Pinning. |
| **📈 Observabilidad** | ![Grafana](https://shields.io) | Telemetría integrada para monitoreo en tiempo real de Connection Pools. |
| **⚙️ Infraestructura** | ![Node.js](https://shields.io) ![PostgreSQL](https://shields.io) | Servidor de aplicación y capa de persistencia de datos analizada. |


**Versión:** 1.0.0 | **Estado:** Hallazgo Crítico Detectado

## 1. Resumen Ejecutivo
Auditoría técnica orientada a evaluar la resiliencia del endpoint de autenticación bajo condiciones de estrés. El análisis revela una brecha crítica de infraestructura donde la ausencia de segmentación de tráfico (Throttling) permite que ráfagas masivas de peticiones comprometan la disponibilidad del servicio y agoten los recursos de persistencia (Connection Pool).

## 2. Matriz de Resultados (Auditoría de Resiliencia)
| Escenario de Prueba | Objetivo | Hallazgo Principal | Estatus |
| :--- | :--- | :--- | :--- |
| **Stress Test (Carga)** | Validar contención (Throttler) | Saturación total del Connection Pool | 🔴 CRÍTICO |
| **IP Spoofing** | Validar filtrado de origen | Inconcluso (requiere Throttler activo) | 🟡 PENDIENTE |

## 3. Análisis Forense: Causa Raíz
La telemetría de **Grafana** confirma un **Efecto Cascada**:
1. El API Gateway permite el paso del 100% del tráfico abusivo.
2. El microservicio de autenticación, ante la falta de una política de *Rate Limiting*, intenta validar cada petición contra PostgreSQL.
3. El motor de base de datos alcanza el límite estático de `max_connections`, resultando en un error de **"Too many clients already"** y la caída del servicio.

## 4. Evidencias Técnicas


*(Aquí insertarás tus capturas: `01_stress_standard_metrics.png`, `01_stress_standard_grafico.png`)*.
* **Observación:** Las trazas demuestran que el sistema no está diferenciando entre tráfico legítimo y malicioso, degradando la experiencia del usuario final a través de una denegación de servicio no intencional.

## 5. Hoja de Ruta de Recomendaciones (Remediación)
* **Prioridad Alta (Infraestructura):** Implementación inmediata de *Rate Limiting* en el API Gateway sobre el endpoint.
* **Prioridad Media (Seguridad):** Configuración de validación de *IP Sockets* en el middleware de autenticación para mitigar técnicas de suplantación (Spoofing).
* **Prioridad Baja (Resiliencia):** Optimización del *Connection Pool* de PostgreSQL y revisión de la política de *Auto-scaling* de los servicios de autenticación.


---
## 🧑‍💻 Perfil Técnico
**María Auxiliadora Vélez Mendoza** - *QA Engineer Full-Stack*