# 📱 Appium iOS Test – TestApp Demo

## ✅ App
**Nombre:** TestApp (Appium iOS Test App)  
**Propósito:** Validar que la app muestra una alerta al presionar un botón mediante una prueba automatizada ca# Appium iOS Test – TestApp

## App usada
**Nombre:** TestApp (demo oficial de Appium)  
**Motivo:** La usé porque es liviana, fácil de compilar y pensada para hacer pruebas rápidas de UI. Ideal para este tipo de challenge.

---

## Entorno de prueba
- Dispositivo: Simulador iPhone 16
- Versión de iOS: 18.5
- Sistema operativo: macOS + Xcode
- Appium: v2
- Lenguaje: Python 3.13
- Librería usada: Appium-Python-Client 3.1.1
- Driver: `xcuitest`

---

## Qué hace el test
1. Abre la app `TestApp.app` en el simulador.
2. Toca el botón `"show alert"`.
3. Espera que aparezca una alerta con el botón `"OK"`.
4. Toma una captura de pantalla y guarda el archivo como `screenshot.png`.

---

## Resultado
✅ El test pasó correctamente.  
🖼️ La captura se generó como `screenshot.png` (está incluida).

---

## Decisiones del test
Elegí esta app porque no necesitaba instalar nada extra ni configurar una app real desde cero. Me permitió probar una interacción de usuario muy básica (tap + validación de alerta), que era justo lo que se pedía.

---

## Matriz de dispositivos (`device_matrix.txt`)
```txt
Android:
- Pixel 6 (Android 14): siempre tiene la última versión del sistema, lo uso como base.
- Samsung Galaxy A52 (Android 12): gama media muy común, especialmente fuera de EE.UU.

iOS:
- iPhone 13 (iOS 17): muy popular, ideal para validar UI moderna.
- iPhone SE (iOS 15): pantalla más chica, útil para validar layouts responsivos.on Appium y Python en iOS.

---

## 🧪 Dispositivo y entorno
- Simulador: iPhone 16
- Versión iOS: 18.5
- Plataforma: macOS + Xcode 15+
- Appium: v2
- Lenguaje: Python 3.13
- Librería: Appium-Python-Client 3.1.1
- Driver: `xcuitest`

---

## 🔍 Pasos del test
1. Inicia la app `TestApp.app` en el simulador iOS.
2. Toca el botón `"show alert"` en la pantalla principal.
3. Verifica que aparece una alerta con el botón `"OK"`.
4. Toma una captura de pantalla (`screenshot.png`) al final de la interacción.

---

## ✅ Resultado final
- **Resultado:** ✔️ Test PASÓ
- **Captura:** [`screenshot.png`](./screenshot.png)

---

## 💡 Diseño del test
Elegí `TestApp.app` porque es una app simple y pensada para pruebas UI. Sirve bien para probar interacciones sin tener que configurar algo más complejo.
La interacción con `"show alert"` permite validar fácilmente la aparición de elementos visibles tras una acción del usuario, ideal para una prueba simple y efectiva.

---

## 📱 (Bonus) Matriz de Dispositivos (`device_matrix.txt`)
```txt
Android:
- Pixel 6 (Android 14): dispositivo moderno y muy utilizado
- Samsung Galaxy A52 (Android 12): gama media con alta distribución global

iOS:
- iPhone 13 (iOS 17): referencia moderna y con gran base instalada
- iPhone SE (iOS 15): pantalla más pequeña, útil para validar layout adaptativo