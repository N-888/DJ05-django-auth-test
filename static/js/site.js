// Ждем полной загрузки HTML-страницы.
document.addEventListener("DOMContentLoaded", () => {
    // Получаем все alert-сообщения на странице.
    const alerts = document.querySelectorAll(".alert");

    // Если сообщений нет, прекращаем выполнение.
    if (!alerts.length) {
        return;
    }

    // Через несколько секунд автоматически закрываем сообщения.
    setTimeout(() => {
        // Перебираем все найденные сообщения.
        alerts.forEach((alert) => {
            // Проверяем, доступен ли Bootstrap Alert.
            if (window.bootstrap && bootstrap.Alert) {
                // Создаем или получаем существующий экземпляр alert.
                const alertInstance = bootstrap.Alert.getOrCreateInstance(alert);
                // Закрываем сообщение.
                alertInstance.close();
            }
        });
    }, 5000);
});