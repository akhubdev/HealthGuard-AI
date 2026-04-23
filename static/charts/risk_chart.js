

document.addEventListener("DOMContentLoaded", function () {

    const gauge = document.getElementById("riskGauge");

    if (gauge) {

        const ctx = gauge.getContext("2d");

        new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: ["Low Risk", "Medium Risk", "High Risk"],
                datasets: [{
                    data: [33, 33, 34],
                    backgroundColor: [
                        "#00C853",
                        "#FFD600",
                        "#D50000"
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                circumference: 180,
                rotation: 270,
                cutout: "70%",
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });

    }

});