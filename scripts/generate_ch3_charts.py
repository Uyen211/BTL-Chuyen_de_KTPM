import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("docs/figures", exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.dpi": 180,
})

COLORS = {
    "mono": "#2B5B84",
    "mod": "#2E8B57",
    "ms": "#D95F02",
    "accent": "#7570B3",
    "gray": "#666666",
}


def chart_1_faustino():
    tasks = ["Source\nListing", "Fragment\nListing", "Interpretation\nView", "Assisted\nOrdering"]
    lat_100 = {
        "Monolith": [17, 103, 29, 137],
        "Modular Monolith": [22, 61, 24, 165],
        "Microservices": [438, 725, 155, 886],
    }
    lat_720 = {
        "Monolith": [61, 350, 25, 3801],
        "Modular Monolith": [629, 1095, 37, 12295],
        "Microservices": [4317, 5715, 140, 11444],
    }

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)
    x = np.arange(len(tasks))
    w = 0.25

    for ax, data, title in [
        (axes[0], lat_100, "(a) Mức tải dữ liệu nhỏ: 100 fragments"),
        (axes[1], lat_720, "(b) Mức tải dữ liệu lớn: 720 fragments"),
    ]:
        b1 = ax.bar(x - w, data["Monolith"], w, label="Monolith", color=COLORS["mono"])
        b2 = ax.bar(x, data["Modular Monolith"], w, label="Modular Monolith", color=COLORS["mod"])
        b3 = ax.bar(x + w, data["Microservices"], w, label="Microservices", color=COLORS["ms"])
        ax.set_yscale("log")
        ax.set_ylim(10, 30000)
        ax.set_xticks(x)
        ax.set_xticklabels(tasks)
        ax.set_title(title)
        ax.set_ylabel("Độ trễ trung bình (ms, thang log)" if ax == axes[0] else "")
        for bars in (b1, b2, b3):
            for bar in bars:
                h = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    h * 1.08,
                    f"{int(h)}",
                    ha="center",
                    va="bottom",
                    fontsize=7.5,
                    rotation=0,
                )

    axes[0].legend(loc="upper left", frameon=True)
    fig.suptitle(
        "Hình 3.1. Độ trễ trung bình giữa Monolith, Modular Monolith và Microservices (LdoD Archive)",
        fontsize=12,
        fontweight="bold",
        y=0.98,
    )
    fig.text(
        0.5,
        0.01,
        "Nguồn: Faustino et al. (2022). Điều kiện đo: Java/Spring Boot, Docker (Intel i7 6C, 16GB RAM), JMeter 50 requests tuần tự (+1 warm-up).",
        ha="center",
        fontsize=8.5,
        color=COLORS["gray"],
    )
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    plt.savefig("docs/figures/fig3_1_faustino_latency.png")
    plt.close()


def chart_2_tofan():
    scenarios = ["S1 (50 users)", "S2 (200 users)", "S3 (500 users)"]
    x = np.arange(len(scenarios))
    w = 0.28

    p90_mono = [131.35, 492.70, 1217.60]
    p90_ms = [171.38, 608.11, 1534.50]
    p95_mono = [140.85, 505.15, 1252.80]
    p95_ms = [175.50, 664.72, 1574.56]

    tp_mono = [429.89, 432.49, 438.25]
    tp_ms = [332.38, 338.07, 343.24]

    ram_mono = [75.00, 85.94, 95.31]
    ram_ms_prod = [73.25, 82.36, 120.78]
    ram_ms_order = [146.53, 178.51, 218.01]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5.0))

    # Panel A: Tail Latency P90 & P95
    ax = axes[0]
    ax.plot(x, p90_mono, "o-", color=COLORS["mono"], label="Monolith P90", linewidth=2)
    ax.plot(x, p95_mono, "s--", color=COLORS["mono"], alpha=0.6, label="Monolith P95")
    ax.plot(x, p90_ms, "o-", color=COLORS["ms"], label="Microservices P90", linewidth=2)
    ax.plot(x, p95_ms, "s--", color=COLORS["ms"], alpha=0.6, label="Microservices P95")
    for i in range(3):
        ax.annotate(f"{p90_mono[i]:.0f}", (x[i], p90_mono[i]), textcoords="offset points", xytext=(0, -12), ha="center", fontsize=8, color=COLORS["mono"])
        ax.annotate(f"{p95_ms[i]:.0f}", (x[i], p95_ms[i]), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8, color=COLORS["ms"])
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios)
    ax.set_ylim(20, 1750)
    ax.set_ylabel("Độ trễ (ms)")
    ax.set_title("(a) Tail Latency (P90 & P95)")
    ax.legend(fontsize=8, loc="upper left")

    # Panel B: Throughput
    ax = axes[1]
    b1 = ax.bar(x - w / 2, tp_mono, w, label="Monolith", color=COLORS["mono"])
    b2 = ax.bar(x + w / 2, tp_ms, w, label="Microservices", color=COLORS["ms"])
    for bars in (b1, b2):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 6, f"{h:.1f}", ha="center", va="bottom", fontsize=8)
    ax.set_ylim(0, 520)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios)
    ax.set_ylabel("Thông lượng (req/s)")
    ax.set_title("(b) Thông lượng (Throughput)")
    ax.legend(fontsize=8, loc="upper right")

    # Panel C: Peak RAM
    ax = axes[2]
    b1 = ax.bar(x - w, ram_mono, w, label="Monolith (2 CPU / 512 MB)", color=COLORS["mono"])
    b2 = ax.bar(x, ram_ms_prod, w, label="MS: product-service (256 MB)", color="#F4A261")
    b3 = ax.bar(x + w, ram_ms_order, w, label="MS: order-service (256 MB)", color=COLORS["ms"])
    for bars in (b1, b2, b3):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 4, f"{h:.0f}", ha="center", va="bottom", fontsize=7.5)
    ax.annotate(
        "Tổng MS đỉnh đồng thời\ntại S3: 319.43 MiB (3.35x)",
        xy=(2 + w, 218),
        xytext=(0.70, 215),
        arrowprops=dict(arrowstyle="->", color=COLORS["gray"]),
        fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFF8E7", ec=COLORS["ms"], alpha=0.95),
    )
    ax.set_ylim(0, 345)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios)
    ax.set_ylabel("Peak RAM (MiB)")
    ax.set_title("(c) Tiêu thụ RAM đỉnh từng container")
    ax.legend(fontsize=7.5, loc="upper left")

    fig.suptitle(
        "Hình 3.2. Hiệu năng đuôi, thông lượng và bộ nhớ dưới giới hạn Docker công bằng (2 CPU / 512 MB)",
        fontsize=12,
        fontweight="bold",
        y=0.98,
    )
    fig.text(
        0.5,
        0.01,
        "Nguồn: Tofan (2026). Điều kiện đo: Node.js v18 + MariaDB 10.11, Ryzen 5 2400GE, JMeter 5.6.3 POST /orders (FOR UPDATE), lặp 20 lần (p < 0.0001).",
        ha="center",
        fontsize=8.5,
        color=COLORS["gray"],
    )
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    plt.savefig("docs/figures/fig3_2_tofan_tail_latency_ram.png")
    plt.close()


def chart_3_krzyszton():
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.0))

    # Panel A: Communication mechanism
    threads = ["10", "100", "200", "400"]
    x = np.arange(len(threads))
    rt_inmem = [31, 215, 438, 866]
    rt_mod_rmq = [66, 661, 1333, 2680]
    rt_ms_rmq = [64, 662, 1343, 2678]

    ax = axes[0]
    ax.plot(x, rt_inmem, "o-", color=COLORS["mod"], linewidth=2.2, label="Modular Monolith + In-memory queue (449 rps @ 400t)")
    ax.plot(x, rt_mod_rmq, "s--", color=COLORS["mono"], linewidth=2.0, label="Modular Monolith + RabbitMQ (147 rps @ 400t)")
    ax.plot(x, rt_ms_rmq, "^:", color=COLORS["ms"], linewidth=2.0, label="Microservices + RabbitMQ (147 rps @ 400t)")
    for i in range(len(threads)):
        off = (14, -6) if i == 0 else (0, -14)
        ax.annotate(f"{rt_inmem[i]}", (x[i], rt_inmem[i]), textcoords="offset points", xytext=off, ha="center", fontsize=8, color=COLORS["mod"])
        ax.annotate(f"{rt_ms_rmq[i]}", (x[i], rt_ms_rmq[i]), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8, color=COLORS["ms"])
    ax.set_xticks(x)
    ax.set_xticklabels([f"{t} threads" for t in threads])
    ax.set_ylabel("Thời gian phản hồi trung bình (ms)")
    ax.set_ylim(-120, 3100)
    ax.set_title("(a) Tác động của cơ chế hàng đợi liên thành phần")
    ax.legend(fontsize=8, loc="upper left")

    # Panel B: Selective scaling at 400 threads
    ax = axes[1]
    labels = [
        "Modular\n(1 inst)",
        "Modular\n(3 inst)",
        "Modular\n(6 inst)",
        "MS Base\n(1 inst)",
        "MS Scale\nProducts (3/6)",
        "MS Scale\nDiscounts (3)",
        "MS Scale\nDiscounts (6)",
    ]
    vals = [2637, 1215, 902, 2679, 2704, 1233, 1023]
    bar_colors = [
        COLORS["mod"], COLORS["mod"], COLORS["mod"],
        COLORS["ms"], "#888888", "#F4A261", COLORS["ms"],
    ]
    bars = ax.bar(np.arange(len(labels)), vals, color=bar_colors, width=0.6)
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 45, f"{h}", ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Thời gian phản hồi trung bình (ms)")
    ax.set_ylim(0, 3100)
    ax.set_title("(b) Mở rộng chọn lọc ở mức tải 400 threads × 250 reqs")

    fig.suptitle(
        "Hình 3.3. So sánh cơ chế giao tiếp và mở rộng chọn lọc trên .NET 8 (Modular Monolith vs. Microservices)",
        fontsize=12,
        fontweight="bold",
        y=0.98,
    )
    fig.text(
        0.5,
        0.01,
        "Nguồn: Krzysztoń et al. (>=2024). Điều kiện đo: .NET 8, Docker Swarm (Ryzen 9 7945HX, 40GB RAM, không giới hạn CPU/RAM container), tắt Gateway/Consul ở Exp 2–3.",
        ha="center",
        fontsize=8.5,
        color=COLORS["gray"],
    )
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    plt.savefig("docs/figures/fig3_3_krzyszton_comm_scaling.png")
    plt.close()


def chart_4_waseem():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.2))

    # Panel A: Waseem 2021 Practitioner Challenges (N=106)
    items_2021 = [
        "Xác định ranh giới dịch vụ (Design)",
        "Thu thập log/metrics từ container (Mon)",
        "Tạo kiểm thử thủ công (Test)",
        "Truy vết phân tán (Mon)",
        "Kiểm thử tích hợp (Test)",
        "Gỡ lỗi trên container (Test)",
        "Quá nhiều thành phần giám sát (Mon)",
        "Giám sát hiệu năng (Mon)",
        "Phát hiện vùng lỗi (Mon)",
    ][::-1]
    pct_2021 = [69.8, 54.7, 50.0, 45.3, 43.4, 42.5, 41.5, 40.6, 34.0][::-1]
    colors_2021 = [
        COLORS["accent"] if "(Design)" in s else (COLORS["mono"] if "(Mon)" in s else COLORS["ms"])
        for s in items_2021
    ]

    ax = axes[0]
    y = np.arange(len(items_2021))
    bars = ax.barh(y, pct_2021, color=colors_2021, height=0.62)
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 1.0, bar.get_y() + bar.get_height() / 2, f"{w:.1f}%", va="center", fontsize=8.5)
    ax.set_yticks(y)
    ax.set_yticklabels(items_2021, fontsize=8.5)
    ax.set_xlim(0, 82)
    ax.set_xlabel("Tỷ lệ chuyên gia gặp thách thức (%)")
    ax.set_title("(a) Thách thức Thiết kế, Giám sát & Kiểm thử (N=106)")

    # Panel B: Waseem 2023/2025 GitHub Issues (2,698 instances)
    cats_2025 = [
        "Technical Debt",
        "CI/CD (Deploy, K8s, Docker)",
        "Exception Handling",
        "Service Exec & Comm",
        "Security",
        "Build Issue",
        "Configuration Issue",
        "Monitoring Issue",
        "Testing Issue",
    ][::-1]
    pct_2025 = [25.46, 11.60, 8.45, 8.11, 7.89, 7.78, 4.48, 3.29, 2.85][::-1]

    ax = axes[1]
    y2 = np.arange(len(cats_2025))
    bars2 = ax.barh(y2, pct_2025, color=COLORS["mod"], height=0.62)
    for bar in bars2:
        w = bar.get_width()
        ax.text(w + 0.5, bar.get_y() + bar.get_height() / 2, f"{w:.2f}%", va="center", fontsize=8.5)
    ax.set_yticks(y2)
    ax.set_yticklabels(cats_2025, fontsize=8.5)
    ax.set_xlim(0, 31)
    ax.set_xlabel("Tỷ trọng trong 2.698 sự cố thực tế (%)")
    ax.set_title("(b) Phân bố 2.698 sự cố từ 15 dự án GitHub OSS")

    fig.suptitle(
        "Hình 3.4. Bằng chứng thực nghiệm về độ phức tạp vận hành trong hệ thống Microservices",
        fontsize=12,
        fontweight="bold",
        y=0.98,
    )
    fig.text(
        0.5,
        0.01,
        "Nguồn: (a) Waseem et al. (2021), khảo sát N=106 chuyên gia; (b) Waseem et al. (2023/2025), khai phá 2.641 closed issues từ 15 dự án OSS.",
        ha="center",
        fontsize=8.5,
        color=COLORS["gray"],
    )
    plt.tight_layout(rect=[0, 0.04, 1, 0.93])
    plt.savefig("docs/figures/fig3_4_waseem_operational_challenges.png")
    plt.close()


def chart_5_dapper():
    rates = ["1/1\n(100%)", "1/2\n(50%)", "1/4\n(25%)", "1/8\n(12.5%)", "1/16\n(6.25%)", "1/1024\n(0.1%)"]
    lat_overhead = [16.3, 9.40, 6.38, 4.12, 2.12, -0.20]
    tp_impact = [-1.48, -0.73, -0.30, -0.23, -0.08, -0.06]
    x = np.arange(len(rates))

    fig, ax1 = plt.subplots(figsize=(9.5, 4.6))
    bars = ax1.bar(x, lat_overhead, width=0.45, color=COLORS["ms"], alpha=0.85, label="Tăng độ trễ trung bình (%)")
    ax1.axhline(0, color="black", linewidth=0.8)
    for bar in bars:
        h = bar.get_height()
        va = "bottom" if h >= 0 else "top"
        offset = 0.4 if h >= 0 else -0.6
        ax1.text(bar.get_x() + bar.get_width() / 2, h + offset, f"{h:+.2f}%", ha="center", va=va, fontsize=8.5, color=COLORS["ms"], fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(rates)
    ax1.set_ylabel("Thay đổi độ trễ trung bình (%)", color=COLORS["ms"])
    ax1.set_ylim(-2.5, 19.5)

    ax2 = ax1.twinx()
    ax2.plot(x, tp_impact, "o-", color=COLORS["mono"], linewidth=2.2, label="Thay đổi thông lượng (%)")
    for i, v in enumerate(tp_impact):
        ax2.annotate(f"{v:+.2f}%", (x[i], v), textcoords="offset points", xytext=(0, -14), ha="center", fontsize=8, color=COLORS["mono"])
    ax2.set_ylabel("Thay đổi thông lượng (%)", color=COLORS["mono"])
    ax2.set_ylim(-2.0, 0.5)
    ax2.grid(False)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", frameon=True)

    fig.suptitle(
        "Hình 3.5. Chi phí hiệu năng của Distributed Tracing theo tỷ lệ lấy mẫu (Google Dapper)",
        fontsize=12,
        fontweight="bold",
        y=0.97,
    )
    fig.text(
        0.5,
        0.01,
        "Nguồn: Sigelman et al. (2010), Table 2. Điều kiện đo: Web search cluster sản xuất tại Google (sai số thực nghiệm ±2.5% latency, ±0.15% throughput).",
        ha="center",
        fontsize=8.5,
        color=COLORS["gray"],
    )
    plt.tight_layout(rect=[0, 0.04, 1, 0.92])
    plt.savefig("docs/figures/fig3_5_dapper_tracing_overhead.png")
    plt.close()


if __name__ == "__main__":
    chart_1_faustino()
    chart_2_tofan()
    chart_3_krzyszton()
    chart_4_waseem()
    chart_5_dapper()
    print("Generated 5 charts in docs/figures/")
