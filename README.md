# Simulación del Flujo de Caja y Cálculo del Valor Presente Neto (VPN) para GF Auto Corporation

Este repositorio contiene un proyecto de simulación de flujos de caja para un nuevo modelo de auto de **GF Auto Corporation**, analizando su rendimiento financiero en los próximos 5 años. Se estima el Valor Presente Neto (VPN) de los flujos de caja después de impuestos, considerando distintas suposiciones de costos fijos y variables.

## Enunciado del Problema

GF Auto Corporation planea lanzar un auto compacto con un horizonte de ventas de 5 años. Los datos recopilados incluyen:

- **Costo de Desarrollo**: Se incurre al inicio del proyecto.
- **Margen de Ganancia**: La diferencia entre el precio de venta y el costo variable de producción (inicio en $4000, decremento de 4% anual).
- **Ventas Anuales**: Estimadas con distribución triangular (demanda inicial y decrecimiento anual).
- **Impuestos y Depreciación**: 40% de tasa corporativa e impuestos sobre depreciación lineal.
- **Tasa de Descuento**: 10%, que representa el costo de capital.

La simulación estima el **VPN** del proyecto bajo escenarios de costos fijos y variables y presenta un análisis de resultados con intervalos de confianza.

## Requisitos

A continuación se detallan las librerías necesarias para ejecutar el código.

| Librería          | Versión Requerida |
|-------------------|-------------------|
| Python            | 3.x               |
| NumPy             | Latest            |
| Matplotlib        | Latest            |
| Random            | Built-in          |
| Math              | Built-in          |

Puedes instalar las librerías con:
```bash
pip install numpy matplotlib
```

