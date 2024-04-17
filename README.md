# Documentación de CI/CD para API REST

Este documento describe el proceso de Integración Continua y Despliegue Continuo (CI/CD) para una API REST utilizando GitHub, Jenkins, DockerHub, y ArgoCD corriendo en un clúster de Amazon EKS.

![alt text](image/process.png)

## Descripción General

El flujo de CI/CD está diseñado para automatizar la construcción, y despliegue de la API REST. Se utiliza un pipeline multibranch en Jenkins para gestionar los procesos de CI.

### Herramientas Utilizadas

- **Jenkins**: Automatiza la construcción y prueba del proyecto.
- **Docker Hub**: Repositorio para almacenar las imágenes de Docker construidas.
- **GitHub**: Almacena el código fuente y los manifiestos de Kubernetes.
- **ArgoCD**: Automatiza el despliegue en el clúster de Amazon EKS.

## Proceso de CI/CD

### 1. Integración Continua (CI)

#### Paso 1: Trigger en Jenkins

- **Trigger**: Cada `push` en la rama `main` activa el pipeline de Jenkins.
  
#### Paso 2: Clonación del Repositorio

- **Clonación**: Jenkins clona la última versión del repositorio.

#### Paso 3: Construcción de la Imagen

- **Construcción**: Se construye la imagen de Docker de la API.
- **Etiquetado**: La imagen se etiqueta con el ultimo TAG.

#### Paso 4: Push a Docker Hub

- **Autenticación**: Jenkins se autentica en Docker Hub.
- **Push**: La imagen se sube a Docker Hub.

### 2. Despliegue Continuo (CD)

#### Paso 1: Actualización de Manifiestos en GitHub

- **Actualización**: Los manifiestos de Kubernetes en GitHub se actualizan con la nueva imagen.

#### Paso 2: Despliegue con ArgoCD en EKS

- **Creación Cluster EKS**: Levantamos nuestro Cluster de EKS, siguiendo estos pasos:




- **Sincronización**: ArgoCD, instalado en el clúster de EKS, detecta los cambios en los manifiestos.
- **Despliegue**: ArgoCD despliega la nueva versión de la API en el clúster de EKS.

## Consideraciones Finales

Este pipeline asegura que cualquier cambio en `main` se prueba, construye, y despliega automáticamente, manteniendo la integridad y disponibilidad de la aplicación.

## Configuraciones y Scripts

> Nota: Asegúrate de configurar las credenciales y permisos adecuados en Jenkins, Docker Hub, GitHub y EKS.
> Nota: modificar aca