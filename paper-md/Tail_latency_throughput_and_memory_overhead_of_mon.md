# Tail latency, throughput, and memory overhead of monolithic and microservices architectures in resource-constrained docker deployments

Yoga Ari Tofan <sup>*</sup> 

Department of Informatics, Universitas Pembangunan Nasional Veteran Jawa Timur, Surabaya 60294, Indonesia 

## ARTICLE INFO

Keywords: Docker Load testing Microservices Monolithic architecture Resource utilization 

* Corresponding author: yoga.if@upnjatim.ac.id 

Article history: Received: Apr 16<sup>th</sup>, 2026 Revised: May 15<sup>th</sup>, 2026 Accepted: Jun 18<sup>th</sup>, 2026 Available online: Jul 15<sup>th</sup>, 2026 

## ABSTRACT

Software architecture selection directly impacts system performance and resource efficiency. This motivates controlled comparisons to make pragmatic deployment decisions. This study compares the implementation of the same backend system, Node.js/Express and MariaDB, in a monolithic and microservices architecture with the same Docker resource allocation, 2 CPUs and 512 MB RAM per architecture, except database containers. The load test was carried out with Apache JMeter 5.6.3 with three levels of concurrency (50, 200, 500 users). Each scenario was performed 20 times within 60 s. The main metrics were response time P90, P95, throughput, error rate, CPU/RAM utilization. The monolithic implementation performed better than the microservices at all load levels. The monolith reached P90 131.35 ms and 429.89 req/s versus microservices P90 171.38 ms and 332.38 req/s at 50 users, and P90 1217.60 ms and 438.25 req/s versus 1534.50 ms and 343.24 req/s at 500 users. Statistical analysis All differences were statistically significant (Mann– Whitney U, p < 0.0001, |δ| = 1.000). For both architectures, the throughput plateaued at load levels. The most operationally significant difference in resource usage was in memory overhead at 500 users, the monolith used 95.31 ± 1.99 MiB compared to 319.43 MiB aggregate for microservices (3.35x higher). CPU utilization was broadly comparable across architectures.The results presented here are specific to this experimental configuration, i.e. a single-machine Docker deployment, two-service decomposition, and synchronous HTTP/ REST communication, and should not be generalized to monolithic and microservices architectures in general. 

## 1. Introduction

Software architecture decisions are fundamental because they influence performance and computational resource efficiency, particularly in backend systems that must handle concurrent requests reliably. Despite the growing adoption of microservices in modern backend development, empirical evidence comparing their performance against monolithic architectures under constrained infrastructure conditions remains limited. In this study, the monolithic implementation is deployed as a single application container, while the microservices implementation is divided into multiple service containers, such as a product service and an order service. Both architectures get the same total application-layer resource budget, without the database containers. This comparison addresses a practical issue: although microservices are often associated with large deployments, many teams work under stringent Docker CPU/RAM constraints and cannot rely on abundant infrastructure. Controlling for application layer resource allocation ensures performance differences are due to architectural characteristics rather than hardware differences. Our comparison is directly applicable for teams facing similar deployment constraints. 

Related work has demonstrated that microservices may add additional overhead compared to monoliths, usually because of passing of requests and communication between services. Therefore, monoliths could outperform microservices on a single machine [1], [2], [3]. At the same time, this body of evidence is context-dependent: studies may not enforce identical resource caps across architectures and may emphasize averages instead of tailoriented percentiles, which can limit how directly results map to percentile-based QoS goals [4]. In the Indonesian context, architecture and deployment considerations for medium-scale services also matter for teams who must run on constrained infrastructure, as reflected in recent local work such as [5]. 

Accordingly, this paper is motivated by three practical gaps that directly inform the experimental design. First, there is limited empirical evidence comparing monolithic and microservices performance under identical, measurable Docker resource limits within a controlled, containerized environment. Second, many comparisons rely on average response time or throughput-only evaluation, while robust performance characterization for userperceived quality requires tail-oriented percentile response time (P90/P95) [1], [4]. Third, medium-scale system developers need evidence-based guidance for choosing an architecture based on available hardware and explicit resource constraints, especially when infrastructure budgets are limited. 

To address these gaps, this study has two overarching objectives: (i) to analyze and compare monolithic and microservices performance using P90 response time, throughput, and error rate under three concurrent user scenarios implemented via controlled load testing, and (ii) to measure and compare CPU and RAM utilization under identical, constrained Docker resource allocations at the application layer. These objectives are complemented by the paper’s contribution to actionable decision support for architecture selection in resource-constrained environments by relating observed performance outcomes to observed resource footprints under high concurrency. 

The remainder of this paper is organized as follows. Section 2 reviews related literature on software architecture comparisons, containerization, inter-service communication, and performance metrics. Section 3 describes the experimental methodology, including the system implementation, Docker resource allocation, load-testing scenarios, and statistical analysis. Section 4 presents the empirical results. Section 5 discusses the findings, including the hypothesized mechanisms behind observed differences, limitations, and practical implications for Indonesian medium-scale system deployments. Section 6 concludes and outlines directions for future work. 

## 2. Related work

## 2.1. Software architecture

Monolithic and microservices architectures are commonly contrasted in terms of communication locality, deployment granularity, and scaling mechanisms, with latency and resource trade-offs often tied to how much work is executed in-process versus across service boundaries [3], [6]. Monolithic systems are frequently characterized as benefiting from in-process communication and more predictable latency behavior, which can make them suitable for tightly coupled transactional workloads where communication overhead must be minimized [6]. By contrast, microservices architectures emphasize independent scaling, fault isolation, and deployment flexibility, bu decomposition typically implies additional runtime instances and network-mediated calls that can introduce new overheads and performance bottlenecks [6]. Empirical and performance-engineering perspectives further suggest that architectural suitability is workload-dependent rather than universal, because the dominant bottleneck (e.g., database-dominated versus application-layer processing) can determine whether distributed decomposition helps or harms outcomes such as throughput and latency [6]. This conditional framing is consistent with comparative studies describing microservices as advantageous for handling dynamic user demand at high load while acknowledging that monoliths can deliver lower latency under conditions where fewer network calls and fewer distributed dependencies are beneficial [3]. 

## 2.2. Empirical comparisons

A recurring empirical observation is that monolithic deployments can outperform microservices on a single machine because microservices add request-passing and inter-service communication overheads that do not exist in an in-process monolith [1]. Blinowski, Ojdowska, and Przybyłek explicitly report that on a single machine a monolith performs better than its microservice-based counterpart and attribute the difference to overhead from passing requests between microservice components [1]. Jatkiewicz and Okrój similarly report that in almost all cases the monolithic architecture proved to be more efficient, based on an experimental study where applications were tested using prepared test cases across local and Azure environments and results were collected with JMeter [2]. These findings align with workload characterization evidence (Acme Air) showing a significant overhead due to the microservice architecture, where microservice performance can be substantially lower than the monolithic version on the same hardware configuration, alongside runtime-level evidence of increased processing time in the Node.js libraries for the microservice version [7]. 

At the same time, other empirical comparisons emphasize that microservices may deliver benefits under highload scenarios or when scalability and operational flexibility are primary objectives, even while acknowledging inherent overheads [3]. Horváth, Sakhnenko, and Gurbál report experiments using Apache JMeter and Locust and frame results as showing performance benefits of microservices in managing high-load scenarios, while also stating that monoliths offer lower latency due to fewer network calls, making the comparison explicitly a scalability-latency trade-off [3]. This mixed but context-dependent pattern is also compatible with studies treating architecture choice as a function of the dominant bottleneck, concluding that microservices can be effective when application-layer processing is the primary bottleneck, whereas monolithic deployments remain more efficient when constraints are dominated by database-layer contention [6]. 

Methodologically, comparative studies vary substantially in the environments and metrics they emphasize, which affects how directly they generalize to resource-constrained container deployments and percentile-based latency objectives [1], [4]. Recent studies further illustrate this variation, comparing Java Spring Boot containerized deployments [8], edge computing environments [9], and Python asynchronous frameworks [10]. For example, Blinowski et al. narrow assessment toward throughput and explicitly note the absence of response time and CPU utilization metrics, which limits alignment with tail-latency evaluation [1]. In addition, Jagiełło et al. examine response times and transaction rates in ways that expand comparison beyond pure performance rather than establishing percentile latency metrics as the primary lens [11]. 

Several studies incorporate containerization in their experimental design, yet containerization is treated differently across papers, ranging from containers-versus-KVM comparisons to Docker versus non-Docker measurement schemes, which can change where overhead is attributed and how strong the experimental control is [12], [13]. Tapia et al. compare KVM-based monolithic execution against containerized microservices with similar hardware resources, while Dirgantara et al. show that performance outcomes can reverse depending on whether Docker and an API gateway are included, indicating that deployment tooling interacts with architecture performance results [12], [13]. 

Taken together, the empirical evidence supports the practical framing for this study: decomposition overhead and additional network calls are repeatedly implicated as mechanisms that degrade latency or efficiency in microservices, especially on a single machine or when distributed dependencies are not amortized by scale [1], [14]. Additionally, because studies differ in whether they focus on throughput, average response time, resilience, or high-load scalability, comparisons intended for constrained deployments benefit from reporting both throughput and percentile response time while holding resource allocations constant [1], [4]. 

Docker-based experimentation provides reproducibility and isolation benefits, but containerization research cautions that benchmarking can have a measurable and non-constant influence on outcomes [15], [16]. Measurement tooling also shapes what is being claimed under Docker: Casalicchio and Perciballi note that cAdvisor/mpstat and docker stats can reflect different notions of CPU usage (effective workload vs CPU requested), implying that tooling choices can affect conclusions about resource efficiency [17]. Finally, container networking can materially shape microservices performance through network virtualization and container boundary effects, as reflected in network performance trade-offs reported by Amaral et al. and the non-negligible performance impact discussed by Ueda et al. [7], [18]. Recent Indonesian work further emphasizes that architecture trade-offs in practice must consider deployment realities under resource constraints [5]. 

## 2.3. Inter-service communication

The overhead of microservices is often blamed on inter-service communication and the increased coordination effort that accompanies decomposition. Replacing a monolithic in-process function call with a network request between containers adds serialization, transmission, and deserialization costs for each operation, which accumulate under concurrent load. Studies clearly mention the overhead of service decomposition in terms of inter-service communication, which impacts performance, and the impact of decomposition on performance can be either positive or negative, depending on the decomposition strategy, concurrency, and the number of service calls [14]. Jayasinghe et al. analyze these effects by identifying the key determinants, including number of service calls, demand for services, concurrency level, and decomposition strategy. Their experimental evaluation is complemented with queueing-theoretic models that closely match observed experimental trends [14]. 

The inter-service communication literature also provides evidence-based mitigation strategies relevant to reducing overhead under strict CPU/RAM budgets [19], [20]. Weerasinghe and Perera compare HTTP, WebSocket and gRPC using an industry-standard benchmark load test, observing that gRPC consistently outperforms HTTP and WebSocket in both response time and throughput [20]. These protocol-level performance differences are further corroborated by additional REST/gRPC comparative evaluations and RPC framework studies, indicating that transport and framework choices can meaningfully shift the overhead profile of microservices deployments [21] [22], [23]. Taken together, this body of evidence motivates treating HTTP/REST as a representative and widelydeployed baseline in the present study, while reserving deeper protocol-level comparisons for future work [19]. 

## 2.4. Performance metrics

Tail-oriented response-time percentiles are motivated in QoS literature as more suitable than averages under heavy-tailed latency behavior, since average response time can be significantly distorted by a small number of extreme outliers that disproportionately affect user-perceived performance. Fiedler and Plattner investigate whether the 95th, 98th, and 99th latency percentiles are more suitable statistics than average-like moment statistics, arguing that these percentiles are more robust precisely because they do not depend on the extreme tail of the latency distribution [4]. This perspective is consistent with performance-engineering arguments in enterprise settings, where percentile-based latency objectives such as P90 and P99 are considered critical because even a small fraction of delayed requests can violate SLAs and degrade user experience [6]. Accordingly, this study adopts P90 and P95 as the primary latency metrics, aligning the evaluation with tail-oriented service quality indicators that reflect realistic worst-case conditions under concurrent load rather than relying on averages alone. 

In load-testing literature, increasing concurrency is a common pattern to identify failure points or performance limits, and studies often report throughput and summary timing statistics that provide operational signals but may miss tail behavior; for example, Suryadevara and Ali report increasing users and calculating throughput and average median response time [24]. More broadly, Golo highlights how load stress patterns affect timing distributions [25]. Several studies incorporate containerization, yet the variety of experimental environments and measurement choices can limit direct applicability to controlled, resource-constrained container deployments; moreover, many comparative studies focus on averages or median response time rather than tail-oriented percentiles (P90/P95) [4]. 

This study addresses these three gaps simultaneously by (i) enforcing identical, measurable Docker CPU/RAM allocations at the application layer, (ii) reporting both throughput and percentile response time (P90/P95), and (iii) providing repeated-measurement data with formal statistical testing to support quantitative architecture selection guidance for medium-scale systems under explicit resource constraints. 

## 2.5. Research gap

The reviewed studies predominantly report average or median response time, while QoS literature argues that percentile-based metrics are more appropriate for heavy-tailed latency behavior [4]. In addition, empirical comparisons often do not enforce identical, measurable resource caps across architectures, which makes it difficult to attribute observed differences to architectural decomposition rather than to uneven resource allocation [1]. Finally, Docker containerization can affect measurement outcomes in a non-constant way, and tooling choices (e.g., docker stats) may bias CPU-related conclusions, which motivates careful control and explicit reporting [17]. 


Table 1. Hardware server specification.


<table><tr><td>Component</td><td>Specification</td><td>Details</td></tr><tr><td>Processor</td><td>AMD Ryzen 5 2400GE</td><td>4 Core / 8 Thread, Max 3,2 GHz, x86_64</td></tr><tr><td>RAM</td><td>14 GB DDR4</td><td>Approximately ~12 GB available during testing</td></tr><tr><td>Operating System</td><td>Ubuntu 22.04 LTS</td><td>Jammy Jellyfish, kernel 5.15</td></tr><tr><td>Network</td><td>Tailscale VPN</td><td>WireGuard-based and used consistently for all test scenarios</td></tr><tr><td>Storage</td><td>SSD</td><td>Used for Docker volume (MariaDB data)</td></tr></table>


Table 2. Software specifications and versions.


<table><tr><td>Component</td><td>Version</td><td>Description</td></tr><tr><td>Node.js</td><td>v18 (Alpine)</td><td>JavaScript runtime used for both architectures</td></tr><tr><td>Express.js</td><td>v4.18.2</td><td>HTTP server framework</td></tr><tr><td>MariaDB</td><td>10.11</td><td>Relational database using the InnoDB engine</td></tr><tr><td>mysql2</td><td>v3.9.1</td><td>Node.js connector library to MariaDB</td></tr><tr><td>Docker Engine</td><td>24.0.9</td><td>Container runtime</td></tr><tr><td>Docker Compose Plugin</td><td>v2.24.7</td><td>Multi-container orchestration (Compose plugin)</td></tr><tr><td>Apache JMeter</td><td>5.6.3</td><td>Load testing tool executed from Mac Mini M-series</td></tr><tr><td>Java (JMeter runtime)</td><td>OpenJDK 17.0.18</td><td>JMeter runtime (via Homebrew)</td></tr></table>

## 3. Methodology

## 3.1. Research design

This study applies a quantitative experimental method using controlled load testing to compare two software architectures (monolithic versus microservices) under a standardized and isolated testing environment. The experimental design follows a two-group comparative structure in which the independent variable is the architecture type, while the dependent variables are performance metrics (P90 response time, throughput, error rate) and resource utilization (CPU and RAM). To avoid resource interference between the two systems, experiments were executed sequentially: the monolithic architecture was tested first for all workload scenarios, after which the monolithic containers were fully stopped before running and testing the microservices architecture. This sequential execution ensures that only one architecture runs at a time, preventing resource competition between the compared systems during measurement. 

## 3.2. Testing environment

All experiments were conducted on a single physical server, and Table 1 summarizes the hardware configuration used in this study. The load generator (Apache JMeter) was executed from a separate machine (Mac Mini M-series), and network connectivity during testing was consistently provided via Tailscale VPN, so both architectures were evaluated under the same network conditions for all workloads. Table 2 lists all software components and versions used to implement and test both architectures. 

## 3.3. System implementation

Both architectures were implemented using Node.js/Express as the HTTP framework and MariaDB as the relational database, following a design pattern representative of production-style Node.js backend services [26]. Both were deployed in Docker containers to support a controlled comparison under fixed resource allocations. Fig. 1 is intended to show that the monolithic deployment runs as a single application process on port 3010, while the microservices deployment decomposes the application into separate services running on ports 3011 and 3012 with inter-service HTTP/REST communication using JSON. 

In both architectures, the evaluated workload targets a transactional ordering flow to stress concurrent readmodify-write behavior against a relational database. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/de7ba192820f8deb40abb77001cad08b9d6c96c36751b457ddc9435108ec7c7c.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/1e71b44d6afbcac97dc6385f46264179c54e87a123fab8e048073416679f3050.jpg)



(b)



Fig. 1. System architecture diagram: (a) monolithic (b) microservices.


## A. Monolithic architecture

The monolithic system is implemented as a single Node.js/Express application running on port 3010, containing two functional domains (Product and Order) within the same codebase and runtime instance. Both domains share a single database connection pool to the same MariaDB instance. The primary endpoint used for load testing is POST /orders, which executes the order flow atomically within a single database transaction: (1) retrieving product data using a row-level lock via SELECT ... FOR UPDATE, (2) validating stock availability, (3) decrementing the product stock, and (4) inserting a new order record. This atomic transaction design is explicitly intended to preserve data integrity under concurrent write operations during stress testing. 

## B. Microservices architecture

The microservices system decomposes the same business functionality into two independent services running on separate ports. The Product Service runs on port 3011 and manages product data, including PATCH / products/:id/stock for validating and decrementing stock atomically using a database transaction. The Order Service runs on port 3012 and handles POST /orders as the entry point for order creation. When the Order Service receives POST /orders, it issues an HTTP call to the Product Service for stock checking and stock decrement, and only after that does it store the order record in its own database context. Inter-service communication uses HTTP/ REST with JSON payloads, which means each end-to-end order request crosses Docker container boundaries rather than using in-process calls. This design introduces additional overhead (inter-service latency) because each POST / orders request in microservices requires at minimum two network round-trips between Docker containers. 

We intentionally select HTTP/REST as the protocol baseline for this study for two reasons. First, HTTP/REST with JSON is the most representative industry baseline for Node.js microservices, enabling comparability with prior comparative work that used similar HTTP/REST request-passing mechanisms [1], [2], [3]. Second, HTTP/REST remains aligned with the inter-service communication evaluation literature that documents measurable protocollevel differences and motivates protocol-aware overhead interpretation (including the role of gRPC advantages documented in [20]), while reserving a dedicated gRPC evaluation to future work so that this paper can isolate architectural overhead from protocol-level overheads [19], [21], [22], [23]. 

## 3.4. Docker resource allocation

Explicit Docker resource limits were configured for each container to ensure a fair comparison, and Table 3 details the CPU and memory constraints applied in both architectures. These constraints enforce that the total application-layer allocation (excluding database containers) is identical between the two architectures, enabling a controlled comparison under a fixed resource budget of 2 CPU and 512 MB RAM per architecture for the application layer. As shown in Table 3, the total resource allocation for the application layer (excluding the database) is identical between monolithic and microservices architectures (2 CPU and 512 MB RAM). In the monolithic case, the entire application-layer budget is assigned to a single container, while in the microservices case it is split evenly into 1 CPU and 256 MB RAM per service container. This equalization is crucial for ensuring the validity of the comparison because it prevents performance differences from being explained by different resource allocations rather than by architectural decomposition. 


Table 3. Docker resource allocation per container.


<table><tr><td>Architecture</td><td>Container</td><td>CPU Limit</td><td>RAM Limit</td><td>Total (App Layer)</td></tr><tr><td>Monolithic</td><td>monolith-api</td><td>2.0 CPU</td><td>512 MB</td><td>2 CPU / 512 MB</td></tr><tr><td>Monolithic</td><td>monolith-db (MariaDB)</td><td>0.5 CPU</td><td>256 MB</td><td>Separate</td></tr><tr><td>Microservices</td><td>product-service</td><td>1.0 CPU</td><td>256 MB</td><td rowspan="2">2 CPU / 512 MB (combined)</td></tr><tr><td>Microservices</td><td>order-service</td><td>1.0 CPU</td><td>256 MB</td></tr><tr><td>Microservices</td><td>microservices-db (MariaDB)</td><td>0.5 CPU</td><td>256 MB</td><td>Separate</td></tr></table>


Table 4. Load testing scenarios.


<table><tr><td>Scenario</td><td>Label</td><td>Concurrent Users</td><td>Ramp-up (s)</td><td>Duration (s)</td><td>Repetitions</td></tr><tr><td>S1</td><td>Light Load</td><td>50</td><td>10</td><td>60</td><td>20x (averaged)</td></tr><tr><td>S2</td><td>Medium Load</td><td>200</td><td>10</td><td>60</td><td>20x (averaged)</td></tr><tr><td>S3</td><td>Stress Test</td><td>500</td><td>10</td><td>60</td><td>20x (averaged)</td></tr></table>

## 3.5. Testing procedure and scenarios

Three workload scenarios were designed to evaluate system behavior across increasing concurrency levels, and Table 4 presents the configuration for each scenario. Each scenario uses the same ramp-up and duration settings and is repeated twenty times, with results summarized as averages across runs to minimize the influence of transient anomalies such as brief spikes from background operating system processes. 

## A. Test duration and steady-state justification

The evaluation uses a 60-second measurement window per run with a 10-second ramp-up, with the rationale that throughput becomes stable after ramp-up and that the subsequent 50 seconds reflect steady-state behavior under controlled load. This steady-state framing is consistent with prior load-testing studies that use similar controlled durations and user ramps to capture stable performance signals, including Suryadevara and Ali and methodological guidance emphasizing stable emulation conditions [24], [25]. Longer-duration evaluation is left for future work to observe additional drift effects that can appear in long-running deployments. 

## B. JMeter configuration

For all scenarios, the target endpoint is POST /orders with JSON body {"product_id": 1, "quantity": 1}, to standardize the transaction workload and ensure comparable request semantics across architectures. JMeter was executed in CLI mode using jmeter -n to avoid GUI overhead that could affect measurement accuracy during testing. JMeter produces .jtl log files, which were post-processed using a custom Python script to extract P90, P95, throughput, and error rate for analysis. 

## C. Testing procedure

Each scenario followed a standardized reset-and-run procedure to minimize the carryover effects of previous runs and to maintain a consistent starting state for the database and containers, as shown in Fig. 2. The procedure begins by stopping all containers using docker compose down -v to remove existing data volumes and then rebuilding and starting containers using docker compose up --build -d so that the database is re-seeded with the initial product dataset. Before each test, endpoint health is verified using curl /health to ensure that the system is ready to accept load. Resource monitoring is started using monitor-resources.sh in a separate terminal prior to running the load test so that CPU and RAM utilization are captured during the same time window as the performance measurement. The monitoring and load execution steps are repeated twenty times per scenario to obtain repeated measurements for averaging. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/99b48bde2da467f0b8c63a84ae30c9e5ad78743f7be39469eca3841f3cf581cc.jpg)



Fig. 2. Testing procedure.


## D. Statistical analysis approach

Mann-Whitney U is used for hypothesis testing because the experimental per-run sample size (n=20 for monolith; n=16 for S1 MS, n=18 for S2 and S3 MS, after exclusion of anomalous runs) violates practical assumptions required by parametric tests for normality of response-time distributions [4]. Cliff’s delta is computed as a non-parametric effect size to quantify the magnitude of distribution shift; in this study, the delta values provide a directionally consistent summary of performance differences. Because the reported |�|=1.00 corresponds to perfect rank separation across the small sample, it should be interpreted as evidence of strong separation within this experimental n rather than a universal population-level effect size. The final dataset comprises n=20 runs for the monolith and n=16–18 runs for microservices after exclusion of anomalous runs. For the microservices group, four runs were excluded from S1 (yielding n=16) and two runs were excluded from each of S2 and S3 (yielding n=18 each). Exclusion was applied to runs in which the order-service container exhibited a markedly elevated P90 response time (exceeding three standard deviations above the within-scenario mean) coinciding with anomalou RAM spikes recorded by docker stats, which are consistent with transient garbage-collection or container scheduling events rather than steady-state behavior. No monolith runs were excluded because no equivalent outlier pattern was observed. The direction and magnitude of all pairwise performance comparisons remain unchanged after exclusion: 


Table 5. Evaluation metrics and operational definitions.


<table><tr><td>Metric</td><td>Unit</td><td>Description</td></tr><tr><td>P90 Response Time</td><td>ms</td><td>90% of requests completed within this time; described as more valid than average due to reduced outlier influence.</td></tr><tr><td>P95 Response Time</td><td>ms</td><td>95% of requests completed within this time; used as additional validation.</td></tr><tr><td>Throughput</td><td>req/s</td><td>Number of successful requests processed per second during the test duration.</td></tr><tr><td>Error Rate</td><td>%</td><td>Percentage of failed requests (non-2xx or timeout) out of total requests.</td></tr><tr><td>Peak CPU</td><td>%</td><td>Highest per-container CPU utilization during testing, recorded via docker stats.</td></tr><tr><td>Peak RAM</td><td>MiB</td><td>Highest per-container memory consumption during testing, recorded via docker stats.</td></tr></table>


Table 6. Peak CPU and RAM utilization per container.


<table><tr><td>Scenario</td><td>Architecture</td><td>Container</td><td>Peak CPU (%)</td><td>Peak RAM (MiB)</td></tr><tr><td rowspan="3">S1 (50 users)</td><td>Monolithic</td><td>monolith-api</td><td>91.65 ± 10.95</td><td>75.00 ± 0.66</td></tr><tr><td>Microservices</td><td>product-service</td><td>72.25 ± 4.13</td><td>73.25 ± 0.48</td></tr><tr><td>Microservices</td><td>order-service</td><td>95.59 ± 11.67</td><td>146.53 ± 12.93</td></tr><tr><td rowspan="3">S2 (200 users)</td><td>Monolithic</td><td>monolith-api</td><td>103.24 ± 16.46</td><td>85.94 ± 9.14</td></tr><tr><td>Microservices</td><td>product-service</td><td>85.02 ± 6.41</td><td>82.36 ± 3.74</td></tr><tr><td>Microservices</td><td>order-service</td><td>100.12 ± 8.30</td><td>178.51 ± 4.44</td></tr><tr><td rowspan="3">S3 (500 users)</td><td>Monolithic</td><td>monolith-api</td><td>102.38 ± 16.52</td><td>95.31 ± 1.99</td></tr><tr><td>Microservices</td><td>product-service</td><td>85.67 ± 8.06</td><td>120.78 ± 18.62</td></tr><tr><td>Microservices</td><td>order-service</td><td>101.13 ± 7.16</td><td>218.01 ± 7.64</td></tr></table>


Mean ± SD; n=20 for monolith, n=16 for S1 MS, n=18 for S2 and S3 MS, after exclusion of anomalous runs 


the monolith outperforms microservices on all three metrics (P90, P95, throughput) in all three scenarios, and the statistical conclusions $( \mathrm { p } < 0 . 0 0 0 1$ and $| \delta | = 1 . 0 0 )$ hold under the cleaned dataset. 

## 3.6. Evaluation metrics

Performance evaluation is based on six metrics covering latency, throughput, reliability, and resource utilization, and Table 5 provides the operational definitions used in this study. P90 response time is selected as the primary latency metric, and P95 is included as a secondary validation metric. 

## 3.7. Resource monitoring

CPU and RAM utilization was monitored in real time during each load test run using docker stats with a twosecond logging interval, capturing per-container resource consumption throughout the duration of each scenario. The monitoring process ran in parallel with JMeter via a custom shell script in a separate terminal session, writing output continuously to a CSV file without interrupting the load test execution. The recorded CSV format includes timestamp, container name, CPU percentage, memory usage, memory limit, and memory percentage, providing a complete per-container resource trace for each run. Peak values were then extracted from each run’s CSV output and aggregated across repetitions to produce the mean and standard deviation figures reported in the results. 

For each scenario, Peak CPU and Peak RAM values were extracted from each of the twenty repetitions by identifying the maximum observed value per container per run (excluding idle rows where CPU was 0.00%). The reported values in Table 6 represent the mean and standard deviation (SD) of these twenty per-run peaks, providing a distributional summary rather than a single-run snapshot. Peak CPU values are interpreted using Docker’s percore reporting scale, where 100% corresponds to one fully utilized CPU core; therefore, a 2-CPU limit corresponds to a 200% ceiling on Docker’s scale for the monolithic application container. Performance metrics were extracted from JMeter .jtl logs using a custom Python script to compute P90, P95, throughput, and error rate for each run and scenario, enabling consistent post-processing across both architectures and all repetitions. 

To assess whether the observed performance differences between architectures are statistically significant beyond descriptive mean ± SD comparisons, a Mann-Whitney U test was applied to per-run P90 response time, P95 response time, and throughput values (n = 20 for monolith; n = 16 for S1 MS, n = 18 for S2 and S3 MS, after exclusion of anomalous runs). The Mann–Whitney U test was selected over a parametric t-test because the per-run sample sizes (n = 16-20 per group) preclude reliable verification of normality assumptions, and response time data from load testing is generally non-normally distributed [4]. Cliff’s delta (�) was computed as a non-parametric effect size measure, with thresholds of |�| < 0.147 (negligible), 0.147–0.330 (small), 0.330–0.474 (medium), and > 0.474 (large). Statistical analysis was implemented using the SciPy library (v1.13.1) in Python. The same Mann–Whitney U procedure was applied to Peak CPU and Peak RAM values, comparing the monolith-api container against each microservices container (product-service and order-service) separately, since the two architectures have different containerization topologies and a direct single-container comparison is not structurally possible. 

## 3.8. Validity controls

Several validity controls were applied to reduce confounding factors and support internal and external validity in the architecture comparison. Internal validity is supported by enforcing identical Docker resource limits between architectures so that measured performance differences are attributable to architectural differences rather than to different resource allocations. Reliability is supported by repeating each scenario twenty times and averaging results to reduce the influence of transient anomalies, such as background operating system activity spikes. Isolation is supported by running only one architecture at a time during testing, preventing resource competition between the compared systems. External validity is bounded by the workload and system characteristics, and generalization is most appropriate for systems with similar relational database transactions and concurrent write patterns, while generalization to architectures with different communication patterns (e.g., event-driven or message queues) requires further study. The study also excludes security, authentication, and public-cloud performance testing, which further constrains generalizability to these dimensions. 

## 4. Result and discussion

This section reports the comparative results for a monolithic versus microservices implementation of the same Node.js/Express + MariaDB application deployed in Docker under equalized application-layer resource limits (2 CPU and 512 MB RAM per architecture, excluding database containers). The evaluation uses controlled load testing with Apache JMeter 5.6.3 in three concurrency scenarios (50, 200, and 500 users), with twenty repetitions per scenario and 60-second duration per run, and reports percentile-based latency (P90/P95), throughput, error rate, and CPU/RAM utilization. 

## 4.1. Response time performance

Table 7 summarizes the average response time and throughput across twenty repetitions for each scenario. Across all scenarios, the monolithic implementation achieves lower tail latency than the microservices implementation, as shown by consistently smaller P90 and P95 values in Table 7. Under light load (S1), the monolith records P90 = 131.35 ms, whereas microservices records P90 = 171.38 ms, which corresponds to a  30.5% higher P90 for microservices under the same workload semantics and total application-layer resource budget. This pattern is consistent with the study’s architectural mechanism: in microservices, each end-to-end POST /orders request requires an inter-service HTTP call from Order Service to Product Service, introducing additional latency from network round trips across Docker container boundaries and message processing overhead (e.g., JSON handling). 

The P95 results corroborate the P90 trend across all three load scenarios, indicating that the latency penalty of microservices is not limited to a small subset of outliers but affects the upper tail more broadly. Reporting both P90 and P95 is consistent with QoS literature arguing that percentile metrics provide distribution-sensitive service quality indicators that are less distorted by extreme-tail behavior than average-like statistics [4]. This is further aligned with industry practice, where percentile-based response-time objectives have become standard precisely because even a small fraction of slow requests can violate SLAs and degrade user experience [6]. Together, the consistency between P90 and P95 findings strengthens the conclusion that the observed latency differences reflect a systematic architectural characteristic of the evaluated configurations rather than statistical noise or isolated extreme values. 


Table 7. Average response time and throughput across load scenarios.


<table><tr><td>Scenario</td><td>Architecture</td><td>Avg RT (ms)</td><td>P90 (ms)</td><td>P95 (ms)</td><td>Throughput (req/s)</td></tr><tr><td rowspan="2">S1 (50 users)</td><td>Monolithic</td><td>106.88</td><td>131.35</td><td>140.85</td><td>429.89</td></tr><tr><td>Microservices</td><td>138.63</td><td>171.38</td><td>175.50</td><td>332.38</td></tr><tr><td rowspan="2">S2 (200 users)</td><td>Monolithic</td><td>426.12</td><td>492.70</td><td>505.15</td><td>432.49</td></tr><tr><td>Microservices</td><td>545.75</td><td>608.11</td><td>664.72</td><td>338.07</td></tr><tr><td rowspan="2">S3 (500 users)</td><td>Monolithic</td><td>1057.67</td><td>1217.60</td><td>1252.80</td><td>438.25</td></tr><tr><td>Microservices</td><td>1338.67</td><td>1534.50</td><td>1574.56</td><td>343.24</td></tr></table>


mean of n=20 monolith runs; n=16 MS runs for S1, n=18 for S2 and S3, after exclusion of anomalous runs 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/fe2d76d30931ecea5b88e0552b4149acd069769fabd48b4b23b004be02d3af44.jpg)



Fig. 3. P90 response time: monolithic vs microservices.


A useful additional interpretation is to compare the internal consistency of the latency distribution via the P90– P95 spread within each architecture (e.g., P95 minus P90). Under S1, the monolith’s P90–P95 spread is 9.5 ms (131.35 to 140.85), whereas the microservices spread is 4.12 ms (171.38 to 175.50), suggesting more stable tail behavior for the monolith at light load under the given constraints. Because this study’s workload is a transactional, database-backed endpoint that performs a read–modify–write sequence guarded by SELECT ... FOR UPDATE, increasing load can shift the dominant contributor to tail latency toward database contention and queueing at the connection pool and lock layer, which can reduce the relative salience of inter-service overhead while still preserving a consistent absolute penalty for cross-service communication. Fig. 3 visualizes the P90 response time comparison across the three load scenarios. 

## 4.2. Throughput and error rate

Table  8 presents throughput and error rate across all scenarios. Throughput is defined as the number of successful requests processed per second, while error rate is the percentage of failed requests (non-2xx or timeout). The monolithic architecture exhibits higher throughput than microservices in all tested scenarios in Table  8, including under light load where the monolith achieves 429.89 req/s compared to 332.38 req/s for microservices [1]. This outcome is consistent with the same structural mechanism that affects latency: microservices introduces extra work per logical request due to inter-service communication and orchestration, whereas the monolith executes the same workflow in-process within a single runtime boundary. The results also align with empirical observations from prior comparative studies that report that microservices can incur additional overhead due to request passing between components, particularly when deployed on a single machine where the decomposition overhead is not offset by independent scaling across multiple hosts. Both implementations maintained zero error rates across all tested scenarios, indicating functional stability within the tested resource budget and test duration. This stability is consistent with the atomic transaction design used in both architectures: each POST /orders request is executed within a single database transaction guarded by SELECT ... FOR UPDATE, which enforces data integrity under concurrent writes without producing application-level errors in these controlled conditions. 


Table 8. Average throughput and error rate across load scenarios.


<table><tr><td>Metric</td><td>Scenario</td><td>S1 (50 users)</td><td>S2 (200 users)</td><td>S3 (500 users)</td></tr><tr><td rowspan="2">Throughput (req/s)</td><td>Monolithic</td><td>429.89</td><td>432.49</td><td>438.25</td></tr><tr><td>Microservices</td><td>332.38</td><td>338.07</td><td>343.24</td></tr><tr><td rowspan="2">Error rate (%)</td><td>Monolithic</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Microservices</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>


mean of n=20 monolith runs; n=16 MS runs for S1, n=18 for S2 and S3, after exclusion of anomalous runs 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/54ab998a5da1ffe9c51d52beedb2a650881ad5fda106a383bdb6884e3dc91751.jpg)



Fig. 4. Throughput: monolithic vs microservices.


A further interpretation concerns the apparent throughput stability pattern across scenarios for each architecture, which can be connected to workload characteristics rather than purely to CPU capacity. Since the tested endpoint is a transactional ordering flow that performs row-level locking and state changes under concurrent writes, a plausible throughput ceiling is imposed by database transaction serialization and lock contention, which may dominate both architectures and thereby limit throughput growth with higher concurrency even when CPU utilization is not at the hard limit. In microservices, this database contention is compounded by the fact that the request path includes at least one additional synchronous service call, adding latency and increasing in-flight work at the same throughput level, which can reduce effective throughput under strict resource limits. Fig. 4 compares the achieved throughput of the monolithic and microservices implementations across load scenarios. 

Table 9 presents the Mann–Whitney U test results for P90 response time, P95 response time, and throughput across all three load scenarios, comparing the twenty per-run observations for the monolithic architecture against those of the microservices architecture (n = 20 for monolith; n = 16 for S1 MS, n = 18 for S2 and S3 MS). All nine comparisons are statistically significant $( \mathrm { p } < 0 . 0 5 )$ , with Cliff’s delta of |�| = 1.00 across every metric and scenario, indicating a large effect size and complete separation between the two distributions, no single monolith run overlaps with any microservices run for any metric. This perfect separation reflects the high within-architecture consistency (low SD) relative to the between-architecture differences, and supports the conclusion that the observed performance gaps are not attributable to random run-to-run variation. The negative delta values for response time metrics confirm that monolith values are systematically lower (better), while the positive delta for throughput confirms that monolith values are systematically higher across all tested scenarios. However, the interpretation of | �| = 1.00 requires an important caveat: this value indicates perfect rank separation within the specific experimental samples evaluated here, meaning that every monolith run outperformed every microservices run on each metric in each scenario. It does not imply that the population effect size is exactly 1.00, nor does it generalize to monolithic and microservices architectures in all deployment contexts. The result is specific to this Node.js/Express + MariaDB implementation, the two-service decomposition evaluated, the tested concurrency levels (50–500 users), and the single-machine Docker environment with equalized resource constraints. Larger and more diverse samples across different technology stacks, decomposition strategies, and deployment environments would be necessary to establish broader generalizability. 


Table 9. Mann–Whitney U test results: monolithic vs microservices.


<table><tr><td>Scenario</td><td>Metric</td><td>Mono (mean ± SD)</td><td>MS (mean ± SD)</td><td>p-value</td><td><eq>\delta</eq></td></tr><tr><td rowspan="3">S1 (50)</td><td>P90 (ms)</td><td>131.35 ± 3.25</td><td>171.38 ± 0.62</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>P95 (ms)</td><td>140.85 ± 2.03</td><td>175.50 ± 1.26</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>Throughput (req/s)</td><td>429.89 ± 3.77</td><td>332.38 ± 11.33</td><td>&lt;0.0001*</td><td>+1.000</td></tr><tr><td rowspan="3">S2 (200)</td><td>P90 (ms)</td><td>492.70 ± 3.95</td><td>608.11 ± 2.22</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>P95 (ms)</td><td>505.15 ± 3.88</td><td>664.72 ± 8.10</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>Throughput (req/s)</td><td>432.49 ± 4.00</td><td>338.07 ± 1.75</td><td>&lt;0.0001*</td><td>+1.000</td></tr><tr><td rowspan="3">S3 (500)</td><td>P90 (ms)</td><td>1217.60 ± 9.63</td><td>1534.50 ± 12.51</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>P95 (ms)</td><td>1252.80 ± 15.64</td><td>1574.56 ± 14.67</td><td>&lt;0.0001*</td><td>-1.000</td></tr><tr><td>Throughput (req/s)</td><td>438.25 ± 3.47</td><td>343.24 ± 13.77</td><td>&lt;0.0001*</td><td>+1.000</td></tr></table>


n=20 for monolith, n=16 for S1 MS, n=18 for S2 and S3 MS, after exclusion of anomalous runs 


## 4.3. Resource utilization

Table 6 presents peak CPU and RAM utilization per container, recorded via docker stats with a two-second interval, and reported as the mean ± SD of per-run peak values across twenty repetitions $( n = 2 0 )$ for each scenario. The most pronounced resource difference is in memory consumption at high load, where the monolithic application container reaches a peak RAM of $9 5 . 3 1 \pm 1 . 9 9$ MiB under the 500-user scenario, while the microservices application layer reaches a substantially higher total memory footprint (319.43 MiB) when summing product-service and orderservice at the same scenario, corresponding to a 3.4x $( 3 1 9 . 4 3 / 9 5 . 3 1 \approx 3 . 3 5 \mathrm { x } )$ increase. This pattern supports the practical concern that microservices can multiply runtime overhead because each service runs its own separate language runtime instance and supporting framework stack, whereas the monolith incurs that baseline overhead once for the whole application. The container-level breakdown also indicates that the microservices order-service is the dominant memory consumer, rising to $2 1 8 . 0 1 \pm 7 . 6 4 \mathrm { M i B }$ and reaching approximately 86% of its configured 256 MB memory limit at the 500-user scenario. Under strict memory budgets, such a high fraction of the container memory limit suggests an elevated risk of instability if concurrency is increased beyond the current stress test or if the service experiences memory fragmentation and GC pressure under sustained load, which makes RAM headroom a key operational constraint for microservices in limited environments. 

CPU utilization differences are more nuanced because the two architectures have different containerization topologies under equalized total application-layer CPU budgets: the monolith uses one container with a 2 CPU limit (interpreted as a 200% ceiling in Docker’s per-core reporting scale), while microservices uses two 1 CPU service containers (each with a 100% ceiling). Consequently, the monolith’s peak CPU of $1 0 2 . 3 8 \pm 1 6 . 5 2 \%$ at S3 remains below the 200% ceiling, whereas microservices shows service-specific saturation behavior (e.g., product-service reaching $8 5 . 6 7 \pm 8 . 0 6 \%$ , indicating that service-level CPU ceilings can become binding earlier even when the total budget is equalized. This distinction is important because it illustrates an architectural interaction between decomposition and resource limits: splitting a fixed CPU budget across services can produce local saturation hotspots that do not occur when the same budget is pooled in a single process boundary. The low standard deviations for RAM (≤ 5.03 MiB for application containers) indicate high measurement stability across runs, while CPU variability is higher (SD up to 20.50%), consistent with the bursty nature of CPU scheduling under containerized workloads. 

Finally, it is important to interpret these resource measurements with awareness that monitoring tools characterize different notions of CPU usage, and that Docker-based benchmarking can have non-trivial measurement effects. Prior work notes that docker stats measures CPU requested by threads running inside the container, which may differ from effective CPU used, and that containerization can have a measurable and non-constant influence on measurement outcomes, motivating careful interpretation when attributing observed utilization patterns to architectural causes alone. Fig. 5 shows the peak RAM usage distribution per container for the monolithic and microservices architectures under the three load scenarios. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/9bb61a21-a0ae-47b2-b1f9-c399a604b0ce/dcdad52c2ef2ed774ced64db4c87021110efcfe8343f7545885686eabed1c94f.jpg)



Fig. 5. Peak RAM usage: monolithic vs microservices (per container).



Table 10. Mann–Whitney U Test: peak RAM (MiB) per container.


<table><tr><td>Scenario</td><td>Mono Peak RAM (MiB)</td><td>MS Container</td><td>MS Peak RAM (MiB)</td><td>p-value</td><td><eq>\delta</eq></td></tr><tr><td rowspan="2">S1 (50 users)</td><td rowspan="2">75.00 ± 0.66</td><td>product-service</td><td>73.25 ± 0.48</td><td>&lt;0.001*</td><td>+0.994</td></tr><tr><td>order-service</td><td>146.53 ± 12.93</td><td>&lt;0.001*</td><td>-1.000</td></tr><tr><td rowspan="2">S2 (200 users)</td><td rowspan="2">85.94 ± 9.14</td><td>product-service</td><td>82.36 ± 3.74</td><td>0.0013*</td><td>+0.614</td></tr><tr><td>order-service</td><td>178.51 ± 4.44</td><td>&lt;0.001*</td><td>-1.000</td></tr><tr><td rowspan="2">S3 (500 users)</td><td rowspan="2">95.31 ± 1.99</td><td>product-service</td><td>120.78 ± 18.62</td><td>&lt;0.001*</td><td>-0.967</td></tr><tr><td>order-service</td><td>218.01 ± 7.64</td><td>&lt;0.001*</td><td>-1.000</td></tr></table>


<sup>*</sup> p < 0.05. � = Cliff’s delta; |�| > 0.474 = large. n = 20 (monolith); n = 16 (S1 MS), n = 18 (S2, S3 MS), after exclusion of anomalous runs. 



Table 11. Mann–Whitney U Test: peak CPU (%) per container.


<table><tr><td>Scenario</td><td>Mono Peak CPU (%)</td><td>MS Container</td><td>MS Peak CPU (%)</td><td>p-value</td><td><eq>\delta</eq></td></tr><tr><td rowspan="2">S1 (50 users)</td><td rowspan="2">91.65 ± 10.95</td><td>product-service</td><td>72.25 ± 4.13</td><td>&lt;0.001*</td><td>+0.994</td></tr><tr><td>order-service</td><td>95.59 ± 11.67</td><td>0.5774</td><td>-0.113</td></tr><tr><td rowspan="2">S2 (200 users)</td><td rowspan="2">103.24 ± 16.46</td><td>product-service</td><td>85.02 ± 6.41</td><td>&lt;0.001*</td><td>+0.722</td></tr><tr><td>order-service</td><td>100.12 ± 8.30</td><td>0.7367</td><td>+0.067</td></tr><tr><td rowspan="2">S3 (500 users)</td><td rowspan="2">102.38 ± 16.52</td><td>product-service</td><td>85.67 ± 8.06</td><td>0.0022*</td><td>+0.583</td></tr><tr><td>order-service</td><td>101.13 ± 7.16</td><td>0.3726</td><td>-0.172</td></tr></table>


<sup>*</sup> p < 0.05. � = Cliff’s delta; |�| > 0.474 = large. n = 20 (monolith); n = 16 (S1 MS), n = 18 (S2, S3 MS), after exclusion of anomalous runs. 


Table 10 shows that RAM differences are statistically significant for order-service across all scenarios (p ≤ 0.012, � = −1.00), confirming that the memory gap is not attributable to run-to-run variation. The RAM difference between monolith-api and product-service is significant only at S1 $( \mathrm { p } = 0 . 0 1 2 )$ but not at S2 and S3, where both containers converge toward similar values. Table  11 shows that CPU differences are significant at S2 for both containers and for product-service at S3, while all S1 comparisons are non-significant, consistent with the high within-architecture CPU variability at light load (monolith-api $\mathrm { S D } = 2 0 . 5 0 \% )$ . 

## 4.4. Discussion

The overall pattern of results, monolith showing lower tail latency and higher throughput under a singlemachine, containerized deployment, matches a recurring conclusion in comparative literature that monoliths can perform better than microservices on a single machine [1], [2] due to additional overhead from request passing and inter-service communication in microservices. The experimental mechanism described in this study is directly aligned with that literature: microservices must cross service boundaries via HTTP/REST and JSON for each POST / orders request, whereas the monolith performs the equivalent logic in-process, avoiding container-to-container round trips. Literature focusing explicitly on decomposition similarly states that service decomposition introduces additional overhead [1], [2] due to inter-service communication that impacts performance, and identifies concurrency and number of service calls as key determinants, which is consistent with the tested workload where each order request requires an orchestration call under concurrent load. 

At the same time, the literature also indicates that microservices can offer advantages when scalability and operational flexibility are primary concerns, especially under high-load scenarios [3] where independent scaling can become valuable. This study’s design, however, intentionally holds the total application-layer resources constant and runs both systems on a single physical server to represent a constrained deployment scenario typical for mediumscale systems with limited infrastructure budgets. Under this constraint, microservices cannot realize its primary benefit of independent scaling across additional hosts, but it still incurs the decomposition costs of additional runtime instances and network-mediated calls. The most distinctive empirical contribution of these results within the paper’s framing is the magnitude of memory overhead under strict constraints: a 3.4x (319.43 / 95.31 ≈ 3.35x) higher RAM footprint for microservices at the 500-user scenario, with one service approaching its configured memory limit. This observation supports the paper’s practical conclusion that architecture selection for constrained environments must account not only for latency and throughput but also for memory headroom, because limited memory can cause instability and limit achievable concurrency even when CPU is not fully saturated. 

Finally, the throughput stability pattern observed across scenarios can be consistent with a database-driven bottleneck under concurrent writes. A plausible mechanism consistent with these observations is contention at the row-level lock acquired by SELECT ... FOR UPDATE under concurrent writes, which can cap throughput growth even when CPU utilization is not at the hard limit. This mechanism was not measured directly in this study; alternative or co-occurring mechanisms such as connection-pool saturation, MariaDB internal queue dynamics, or the Node.js event-loop saturation [26] cannot be ruled out without dedicated instrumentation (e.g., MariaDB slow query logs, connection pool telemetry, eBPF tracing), and we leave such mechanism-level investigation to future work. 

## 4.5. Limitations

Three structural constraints of this study require explicit acknowledgment before interpreting the results. First, the evaluation uses a single application workload: the transactional endpoint POST /orders, which performs an atomic read-modify-write sequence with row-level locking. Workloads with different access patterns, such as read-heavy queries, stateless request handling, or batch processing, may produce substantially different relative performance between architectures, and the findings here should not be extrapolated to such cases without additional experimentation. Second, the technology stack is specific to Node.js (v18, Alpine), Express.js (v4.18.2), and MariaDB (10.11) with the InnoDB engine. Performance characteristics of other runtimes (e.g., Java Spring Boot, Python/FastAPI, Go), other databases (e.g., PostgreSQL, MongoDB), or other inter-service communication patterns (e.g., gRPC, message queues, event-driven) may differ, and results from this stack may not transfer directly. Third, the microservices architecture is deliberately simplified to two services (Product and Order) communicating synchronously over HTTP/REST. Real-world microservices deployments typically involve more services, API gateways, service meshes, and asynchronous communication, all of which can alter the decomposition overhead in either direction. 

The load-testing setup uses Apache JMeter with a finite-user concurrency model (50, 200, 500 users), and the study acknowledges that workload emulation assumptions influence what latency percentiles mean in practice, since modern web traffic can be asynchronous and driven by unknown numbers of users. Resource utilization metrics (Peak CPU and Peak RAM) are reported as the mean and standard deviation across all twenty repetitions, which strengthens distributional interpretation. Formal Mann–Whitney U tests with Cliff’s delta effect sizes were applied to all primary metrics: performance metrics (P90, P95, throughput) are reported in Table 9, while resource utilization comparisons (Peak RAM and Peak CPU per container) are reported in Table 10 and Table 11 respectively. 

However, the small sample size (n = 20) reduces the precision of effect size estimates across all tests, and the observed perfect separation (� = ±1.00) reflects perfect rank separation within this small sample rather than a population-level claim about the underlying effect magnitude. The final dataset uses n=20 runs for the monolith and n=16–18 runs for microservices after excluding anomalous runs, which strengthens statistical precision relative to a minimal pilot while remaining a moderate sample size; future replications with larger and fully symmetric n are recommended to further tighten confidence intervals around the reported effect sizes. 

For performance interpretation, the 60-second measurement window is also shorter than typical long-running production observation. The steady-state behavior is argued to be reached after the 10-second ramp-up based on the stable throughput across the remaining 50 seconds of the run; this steady-state framing is consistent with prior controlled comparative studies. Extended-duration evaluation is left for future work to capture additional drift effects that may appear under longer production lifetimes. For resource utilization specifically, three non-significant comparisons $( \mathrm { p } > 0 . 0 5 )$ in Table 11 should be interpreted in light of measurement characteristics rather than as evidence of no architectural effect: the non-significant CPU comparisons for order-service reflect high withinarchitecture variability and near-equal values between the two architectures, which reduces statistical power at this sample size. Additionally, the non-significant RAM difference between monolith-api and product-service at S2 and S3 (see Table 10) reflects genuine convergence in memory usage between those two specific containers at higher loads, not absence of an overall RAM difference. 

## 4.6. Practical implications

For medium-scale systems deployed under explicit Docker CPU/RAM caps with a synchronous, transactional workload profile similar to the one evaluated here, these results suggest that a monolithic deployment may offe a pragmatic performance and memory advantage, as it avoids inter-service communication overhead and reduces runtime duplication under strict resource constraints. This implication is directly relevant to teams operating with limited infrastructure, since microservices success stories are often realized under substantial infrastructure budgets that may not match typical constrained server environments. Microservices remains a plausible choice when independent scalability, fault isolation, and deployment flexibility are prioritized, but the results indicate that the infrastructure must provide sufficient memory headroom to absorb the runtime and communication overhead of multiple services. Under the present configuration, the order-service reaches approximately 86% of its memory limit in the 500-user scenario, suggesting that memory constraints could become a binding factor earlier than CPU in scaling this microservices deployment within fixed budgets. 

These findings are especially relevant in the Indonesian context, where medium-scale information systems such as local government information systems (regional public service portals), university academic information systems, regional e-commerce / UMKM platforms, and BUMDes / village-level enterprise platforms are often hosted on a single VPS or on co-located servers with tight CPU/RAM caps [9]. In such settings, a  3.4x RAM overhead can translate directly into higher infrastructure cost, reduced headroom, and greater operational risk when concurrency increases. This local relevance is consistent with the deployment considerations discussed in [5]. Under resource-constrained deployments with workload characteristics similar to those evaluated in this study, practitioners may benefit from architecture selection that accounts for both performance objectives (e.g., P90/P95) and memory headroom, as the results suggest that memory constraints can become a binding factor before CPU saturation under this type of transactional load. 

## 5. Conclusion

This study compared a monolithic and a microservices implementation of the same backend system under identical application-layer Docker resource allocations, using a single transactional endpoint (POST /orders) as the evaluation workload across three concurrency levels with twenty repetitions per scenario. The monolithic implementation consistently outperformed microservices across all tested load levels in both tail latency and throughput. At 50 users, the monolith achieved P90 131.35 ms and 429.89 req/s versus microservices P90 171.38 ms and 332.38 req/s; at 500 users, P90 1217.60 ms and 438.25 req/s versus 1534.50 ms and 343.24 req/s. All differences were statistically significant across all scenarios (Mann-Whitney U, p < 0.0001, |δ| = 1.000). 

In terms of resource consumption, CPU utilization was about the same across the architectures, but memory overhead varied greatly at 500 users, the monolith used 95.31 ± 1.99 MiB compared to 319.43 MiB aggregate for microservices (3.35x higher), due to runtime duplication inherent to the two-service Node.js/Express decomposition. The differences in performance and memory are caused by the inter-service HTTP / REST communication path of the microservices implementation. Each POST /orders request requires at least two container-to-container network round trips that are not present in the in-process execution path of the monolith. 

These findings directly address the study’s motivating concerns: equal resource allocation eliminates hardware confounds, percentile-based metrics (P90/P95) provide distribution-sensitive latency indicators, and the quantitative results offer actionable evidence for teams selecting architectures under constrained infrastructure budgets. Within this specific experimental configuration, the monolithic architecture demonstrated better performance efficiency and substantially lower memory overhead, making it the more suitable choice for single-machine Docker deploy ments with strict CPU/RAM caps and synchronous HTTP workloads at the tested scale. The evaluation is bounded to a single transactional endpoint, a two-service decomposition, and synchronous HTTP/REST communication, which limits generalizability. Future work should evaluate additional endpoints and workload types, test alternative communication patterns such as event-driven and message-queue-based designs, explore asymmetric resource allocation strategies, and extend the evaluation to public-cloud environments to broaden external validity. 

## CRediT authorship contribution statement

Y. A. Tofan: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data Curation, Writing – Original Draft, Writing – Review & Editing, Visualization, Supervision, Project Administration. 

## Declaration of competing interest

The author declares that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## Acknowledgement

This research was conducted independently without external funding. The computing infrastructure was selfprovisioned. 

## Data availability

The data used to support the findings of this study (JMeter results and Docker container resource monitoring logs) are available from the corresponding author upon reasonable request. 

## Declaration of generative AI and AI-assisted technologies in the writing process

During the preparation of this work, the author used Elicit.ai and Claude (Anthropic) for literature search and synthesis, translating and improving the English manuscript, assisting with statistical computation of resource utilization metrics, and suggesting Typst formatting improvements. The author reviewed and edited the content as needed and takes full responsibility for its accuracy and integrity. 

## ORCID

Y. A. Tofan: https://orcid.org/0009-0002-1531-1365 

## References



[1] G. Blinowski, A. Ojdowska, and A. Przybyłek, “Monolithic vs. Microservice Architecture: A Performance and Scalability Evaluation,” IEEE Access, vol. 10, pp. 20357–20374, 2022, doi: 10.1109/ACCESS.2022.3152803. 





[2] P. Jatkiewicz and S. Okrój, “Differences in Performance, Scalability, and Cost of Using Microservice and Monolithic Architecture,” in Proceedings of the 38th ACM/SIGAPP Symposium on Applied Computing, in SAC '23. New York, NY, USA: Association for Computing Machinery, Jun. 2023, pp. 1038-1041.doi: 10.1145/3555776.3578725 





[3] M. Horváth, V. Sakhnenko, and F. Gurbál̆<sup>l̆</sup>, “Comparison of Scalability and Performance in Microservices and Monolithic Architectures,” in 2024 IEEE 17th International Scientific Conference on Informatics (Informatics), Nov. 2024, pp. 82–87. doi: 10.1109/Informatics62280.2024.10900892. 





[4] U. Fiedler and B. Plattner, “Using Latency Quantiles to Engineer QoS Guarantees for Web Services,” in Quality of Service — IWQoS 2003, K. Jeffay, I. Stoica, and K. Wehrle, Eds., Berlin, Heidelberg: Springer, 2003, pp. 345–362. doi: 10.1007/3-540-44884-5_19. 





[5] B. Susanto, E. Atmadji, and L. Hakim, “The Performance of Hotel Management System Using Microservices and Containerization Technology,” Jan. 2024, Accessed: Jun, 02, 2026, [Online]. Available: https://eudl.eu/doi/10.4108/eai,18-11-2023.2342548 





[6] P. Kumar, “Performance-Driven Evaluation of Monolithic and Microservice Architectures for Enterprise Cloud Applications: A Scalability, Latency, and Cost Perspective,” International Journal of Science and Research (IJSR), vol. 15, no. 1, pp. 333–343, Jan. 2026, doi: 10.21275/SR26104211700. 





[7] T. Ueda, T. Nakaike, and M. Ohara, “Workload Characterization for Microservices,” in 2016 IEEE International Symposium on Workload Characterization (IISWC), Sep. 2016, pp. 1–10. doi: 10.1109/IISWC.2016.7581269. 





[8] S. Gangarapu, “A Security and Performance Comparative Study of Monolithic and Microservices Architectures in Java Spring Boot Applications with Containerized Distributed Deployment,” Computer Fraud and Security, Feb. 2024, doi: 10.52710/cfs.1049. 





[9] N. Rathore and A. Rajavat, “Evaluating the Performance of Monolithic and Microservices Architectures in an Edge Computing Environment,” International Journal of Fog Computing (IJFC), vol. 5, no. 1, pp. 1–18, 2022, doi: 10.4018/IJFC.309139. 





[10] M. A. Ala'anzy and Z. Yeshpatov, “A Performance and Scalability Evaluation of Monolithic (Django) vs. Microservice (FastAPI) Architectures for Asynchronous API Workloads in Python,” in 2026 18th International Conference on Electronics, Computer, and Computation (ICECCO), Apr. 2026, pp. 1–6. doi: 10.1109/ICECCO67619.2026.11488798. 





[11] M. Jagiełło, M. Rusek, and W. Karwowski, “Performance and Resilience to Failures of an Cloud-Based Application: Monolithic and Microservices-Based Architectures Compared,” in Computer Information Systems and Industrial Management, K. Saeed, R. Chaki, and V. Janev, Eds., Cham: Springe International Publishing, 2019, pp. 445–456. doi: 10.1007/978-3-030-28957-7_37. 





[12] F. Tapia, M. Á. Mora, W. Fuertes, H. Aules, E. Flores, and T. Toulkeridis, “From Monolithic Systems to Microservices: A Comparative Study of Performance,” Applied Sciences, vol. 10, no. 17, p. 5797, Jan. 2020, doi: 10.3390/app10175797. 





[13] D. P. Dirgantara, D. S. Kusumo, and R. G. Utomo, “Docker-based Monolithic and Microservices Architecture Performance Comparison,” Jurnal Teknik Informatika (Jutif), vol. 5, no. 2, pp. 357–365, Apr. 2024, doi: 10.52436/1.jutif.2024.5.2.1338. 





[14] M. Jayasinghe, J. Chathurangani, G. Kuruppu, P. Tennage, and S. Perera, “An Analysis of Throughput and Latency Behaviours Under Microservice Decomposition,” in Web Engineering, M. Bielikova, T. Mikkonen, and C. Pautasso, Eds., Cham: Springer International Publishing, 2020, pp. 53–69 doi: 10.1007/978-3-030-50578-3_5. 





[15] S. Giallorenzo, J. Mauro, M. G. Poulsen, and F. Siroky, “Virtualization Costs: Benchmarking Containers and Virtual Machines Against Bare-Metal,” SN Computer Science, vol. 2, no. 5, p. 404, Aug. 2021, doi: 10.1007/s42979-021-00781-8. 





[16] S. Kaiser, A. şaman Tosun, and T. Korkmaz, “Benchmarking Container Technologies on ARM-Based Edge Devices,” IEEE Access, vol. 11, pp. 107331– 107347, 2023, doi: 10.1109/ACCESS.2023.3321274. 





[17] E. Casalicchio and V. Perciballi, “Measuring Docker Performance: What a Mess!!!,” in Proceedings of the 8th ACM/SPEC on International Conference on Performance Engineering Companion, in ICPE '17 Companion. New York, NY, USA: Association for Computing Machinery, Apr. 2017, pp. 11–16. doi: 10.1145/3053600.3053605. 





[18] M. Amaral, J. Polo, D. Carrera, I. Mohomed, M. Unuvar, and M. Steinder, “Performance Evaluation of Microservices Architectures Using Containers,” in 2015 IEEE 14th International Symposium on Network Computing and Applications, Sep. 2015, pp. 27–34. doi: 10.1109/NCA.2015.49. 





[19] A. Bhole, “Reducing Inter-Service Communication Latency in Microservices,” International Journal of Scientific Research in Engineering and Management, vol. 8, pp. 1–6, Dec. 2024, doi: 10.55041/IJSREM39350. 





[20] L. Weerasinghe and I. Perera, “Evaluating the Inter-Service Communication on Microservice Architecture,” in 2022 7th International Conference on Information Technology Research (ICITR), Dec. 2022, pp. 1–6. doi: 10.1109/ICITR57877.2022.9992918. 





[21] M. Bolanowski et al., “Eficiency of REST and gRPC Realizing Communication Tasks in Microservice-Based Ecosystems,” in Frontiers in Artificia Intelligence and Applications, H. Fujita, Y. Watanobe, and T. Azumi, Eds., IOS Press, 2022. doi: 10.3233/FAIA220242. 





[22] T. Vairam, V. K, K. T, S. E. T., and M. E, “An Empirical Evaluation of gRPC and REST Communication Patterns in Microservice Architectures,” in 2026 Second International Conference on Intelligent Systems for Communication, IoT and Security (ICISCoIS), Jan. 2026, pp. 1–6. doi: 10.1109 ICISCoIS62701.2026.11448051. 





[23] Ritu, S. Arora, A. Bhardwaj, A. Kukkar, and S. Kaur, “A Comparative Analysis of Communication Efficiency: REST vs. gRPC in Microservice- Based Ecosystems,” in 2024 International Conference on Emerging Innovations and Advanced Computing (INNOCOMP), May 2024, pp. 621–626. doi: 10.1109/INNOCOMP63224.2024.00107. 





[24] S. Suryadevara and S. Ali, “Preperformance Testing of A Website,” in Computer Science & Information Technology, AIRCC Publishing Corporation, Jun. 2020, pp. 33–52. doi: 10.5121/csit.2020.100703. 





[25] H. D. Golo and A. Osei-Owusu, “Performing Load Capacity Test for Web Applications,” International Journal of Innovation and Scientific Research, vol. 17, no. 1, pp. 51–68, Aug. 2015, Accessed: Apr. 03, 2026. [Online]. Available: http://www.ijisr.issr-journals.org/abstract.php?article=IJISR-15- 076-02 





[26] M. D. I. Sakti, D. Dirgantara, A. K. Ramadhan, and M. A. Ibrahim, “Optimizing Asynchronous Performance in Node.js with Express and PostgreSQL,” Procedia Computer Science, vol. 269, pp. 172–181, Jan. 2025, doi: 10.1016/j.procs.2025.08.270. 

