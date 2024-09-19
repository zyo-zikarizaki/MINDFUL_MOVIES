
window.addEventListener("load", function() {
    let today = new Date();
    let year = String(today.getFullYear());
    let month = ("0" + String(today.getMonth() + 1)).slice(-2);
    let day = ("0" + String(today.getDate())).slice(-2);
    let hours = ("0" + String(today.getHours())).slice(-2);
    let minutes = ("0" + String(today.getMinutes())).slice(-2);

    let date = year + "-" + month + "-" + day + "T" + hours + ":" + minutes;

    let config_date = {
        locale: "ja",
        dateFormat: "Y-m-d H:i", // 日付と時間のフォーマット
        enableTime: true,        // 時間選択を有効にする
        time_24hr: true,         // 24時間制を使用する
        defaultDate: new Date()  // デフォルトの日付
    };

    flatpickr("[name='deadline']", config_date);

    console.log(events);

    const calendar_elem = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendar_elem, {
        initialView: 'dayGridMonth',
        locale: 'ja',
        editable: true,
        events: events,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        views: {
            dayGridMonth: {
                titleFormat: { year: 'numeric', month: 'long' }
            },
            timeGridWeek: {
                titleFormat: { year: 'numeric', month: 'long', day: 'numeric' }
            },
            timeGridDay: {
                titleFormat: { year: 'numeric', month: 'long', day: 'numeric' }
            }
        },
        customButtons: {
            today: {
                text: '今日',
                click: function() {
                    calendar.today();
                }
            },
            dayGridMonth: {
                text: '月',
                click: function() {
                    calendar.changeView('dayGridMonth');
                }
            },
            timeGridWeek: {
                text: '週',
                click: function() {
                    calendar.changeView('timeGridWeek');
                }
            },
            timeGridDay: {
                text: '日',
                click: function() {
                    calendar.changeView('timeGridDay');
                }
            }
        },
        eventClick: function(info) {
            console.log('Event: ' + info.event.id);
            const target = document.getElementById("todo_" + info.event.id);
            target.scrollIntoView({
                behavior: 'smooth',
            });
        },
        eventDrop: function(info) {
            updateEvent(info.event);
        },
        eventResize: function(info) {
            updateEvent(info.event);
        }
    });

    calendar.render();

    function updateEvent(event) {
        fetch('/update-event/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                id: event.id,
                start: event.start.toISOString(),
                end: event.end ? event.end.toISOString() : null
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert('Event updated successfully!', 'success');
            } else {
                showAlert('Error updating event', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('Error updating event', 'danger');
        });
    }

    function showAlert(message, type) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.role = 'alert';
        alert.innerHTML = `${message}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>`;
        document.body.prepend(alert);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});



