# Migrating Monolithic to Microservices: Comparative Performance Testing Evaluation Between Architectures

Asep Wahyudin<sup>1*</sup>, Herbert Siregar<sup>2</sup>, Ani Anisyah<sup>3</sup>, Sekar Madu Kusumawardani<sup>4</sup>, Erlangga<sup>5</sup> <sup>1,</sup> <sup>2,</sup> <sup>3,</sup> <sup>4,</sup> <sup>5,</sup>Department of Computer Science, Universitas Pendidikan Indonesia, Indonesia 

## Abstract.

Purpose: Various organizations and industries have migrated their systems from previously adopting monolithic architecture to microservices architecture. One of the advantages of microservices architecture that is desired to be achieved from the migration process is the performance side. Therefore, this research aims to conducted performance testing on the system that was migrated from monolithic to microservices in the previous study. 

Methods: This research was conducted in several stages, such as designing and implementing software and applications, creating performance testing scenarios, executing scenario testing with load testing, stability testing (soak testing), and stress testing such as load testing, soak testing, and stress testing, and finally analyzing and reporting testing results using performance indicator in terms of response time, throughput, and error rate. 

Result: The test results showed a significant increase in performance before and after the migration of the monolithic system to microservices. Application response time became faster, more requests could be handled, and the failure rate experienced by the system was smaller. This shows that system performance is better with the implementation o microservices architecture. 

Novelty: This research presents a novelty in the form of a comparative evaluation of real deployment-based system performance between Laravel monolithic architecture and Golang gRPC-based microservices on the same application, with a seven-stage performance testing approach and the use of in-depth quantitative metrics using Apache JMeter. 

Keywords: Performance testing, Monolithic architecture, Microservices architecture, Software migration testing Received June 2025 / Revised November 2025 / Accepted December 2025 

This work is licensed under a Creative Commons Attribution 4.0 International License. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/3eab8e1ba1859d207aa2a3908641ceb004307240edfcbec21b138a6b6814d276.jpg)


## INTRODUCTION

There are a number of software architectures that are changing to better fit the needs and features of system applications [1]. The goal is to get the most out of applications in terms of performance, scalability, flexibility, complexity, maintainability, and resilience. More and more, monolithic design is becoming less popular in favor of different architectures [2]–[4]. This architecture is simple and easy to use in small-scale settings [5]. However, as application development has become more popular, monolithic architecture has become less scalable, less performant, less fault-tolerant, and harder to maintain [3], [6]–[9]. Because of this, a lot of companies, like Uber, SoundCloud, Netflix, Amazon, eBay, and Spotify, moved their monolithic apps to microservices [2], [10]–[15]. 

Several studies have shown that moving from a monolithic system to microservices can make the system better in many ways, such as by making it run faster [14]–[20]. As an increasing number of individuals move from monolithic architectures to microservices, we can compare how well both designs work in the system migration we did for the same application. We do performance testing and look at the results based on a set of non-functional requirements, like figuring out how fast the system responds, how much data it can handle, and how reliable it is under a certain workload [21]. When the reaction time is low and the throughput is high, the application works better [22]. 

Monolithic and microservice architectures offer contrasting blueprints for organizing web applications, each bringing distinct advantages and disadvantages in terms of performance, scalability, maintenance, and day-to-day operational complexity. Monolithic designs combine the user interface, business logic, and data layers into a single, self-contained unit, which facilitates rapid in-process communication, easier deployment, and minimal overhead during early development [23], [24]. When studied in controlled laboratory settings as well as typical cloud configurations, monolithic applications typically deliver higher throughput and lower latency compared to their microservice counterparts [23], [25]. For example, Wang and colleagues note that monolithic systems outperform microservices by about 6 percent in experiments with many connections, a gap that is partially closed by service discovery frameworks such as Consul [26]. Similarly, findings published in ACM SIGAPP show that monolithic architectures outperform microservices in CPU-constrained workloads on both on-premises and in Azure, especially when the majority of processing time is spent executing business rules [23]. However, these benefits do not eliminate the inherent scalability limitations of monoliths; adding capacity requires cloning the entire application, a wasteful approach when only certain components face spikes in demand [4], [27]. Additionally, interconnected codebases can hamper the pace of feature releases and amplify the propagation of errors— a modification in one module may inadvertently break behavior in another module, triggering failures far beyond the intended scope [28]. As an application’s footprint grows, monoliths often accumulate technical debt that resists clean refactoring and makes it difficult to experiment with different programming languages or frameworks [29]. 

A microservice architecture breaks a large application into smaller, independently deployable services, each of which handles a specific business function [30], [31]. This separation increases modularity, making it possible to scale a single service, release updates, or choose a different technology stack without affecting the entire system [4], [27]. One major financial platform migration reported tighter internal cohesion, lower CPU and memory overhead, and clearer boundaries between services after the monolith was split [28]. A long-term study by Lenarduzzi and colleagues shows that, while moving to microservices briefly accelerates technical debt, the rate of new debt accumulation is subsequently slower than with a maintained monolith [29]. However, these benefits do not come without costs. Combining multiple microservices turns an application into a distributed system that requires service discovery, API gateways, container orchestration such as Kubernetes, and a shared dashboard for logging and tracing [32], [33]. All of these moving parts add overhead, especially additional network hops, which can hinder performance when workloads are already CPU-bound [23], [25]. Keeping different services in step, versioning their contracts, and running thorough end-to-end testing can push teams toward richer CI/CD pipelines and tighter operational habits [23], [27]. 

The choice between monolithic and microservice architectures ultimately depends on the planned scale of the system, the skills of the development team, the performance characteristics required, and the long-term roadmap for maintaining and evolving the software. For new products or medium-sized applications, monoliths still make sense because their single code base is easier to maintain and tends to perform better from the start [23], [24]. In contrast, very large systems that grow rapidly benefit from microservices, because independent teams can scale, deploy, and maintain modules with minimal disruption, even if that independence adds complexity to monitoring and operations [4], [27]. Future empirical work should quantify this trade-off across industries, particularly by identifying the system sizes and levels of infrastructure maturity that truly warrant a migration to a microservice model. 

Performance testing is usually broken down into three types: load testing, soak/stability testing, and stress testing. Load testing involves continuously testing the system by introducing traffic or load within specific limits that are gradually increased. This helps to find the system's capacity and load limits. Soak/stability testing checks how the system performs over a long period to ensure it can handle requests consistently and identify any errors that may arise over time. Stress testing applies maximum load and pressure to a system until it fails. The aim is to find out which conditions and levels of load lead to failure. Furthermore, there are several metrics that are most commonly used to evaluate system performance, namely response time (the time required for the system to respond to a client request, which is determined by the start of the request to the end of the response from the system received), throughput (the number of requests that the system can handle in a certain unit of time), and error rate (the number of transactions that are successfully and failed to be handled) [6], [30], [31]. 

Performance testing was carried out on the UPI Tracer Study application in both monolithic (pre-migration) and microservices (post-migration) configurations. The UPI Tracer Study monolithic application was built with Laravel technology, while the microservices application was created with Golang gRPC technology. Application development using the Go language is ideal for building API Gateways in microservices architectures due to its high performance, low latency, and efficient concurrency support through goroutines. Compared to other languages such as Node.js, Python, or Java, Go offers smaller memory usage and very fast startup times. This makes API Gateways more responsive, scalable, and resource-efficient in cloud-native environments. Furthermore, the mature Go ecosystem supports the creation of stable, lightweight, and easily deployable gateways. 

Testing was carried out with the Apache JMeter tool, which is an open-source desktop-based testing software developed in Java that supports a variety of API connection protocols, including REST, SOAP, and gRPC. 

## RELATED RESEARCH

The following is Table 1 as a list of research related to the research conducted. Several previous studies have been conducted with different objectives and performance tests. Based on previous research, it can be concluded that the differences between this study and previous studies in the type of testing, measurement parameters, and application development approach. This study not only focus on one type of testing, but also includes three main types of testing such as load testing, soak testing, and stress testing to conduct more comprehensive performance evaluation result. In addition, system performance measurements in this study include various important metrics such as response time, throughput, resource utilization, goals, limitations, and error rates, thus providing a more detailed picture of system performance under various load conditions. Another difference is in the application development approach, where this study uses a microservice architecture with REST API and gRPC API implementations as a comparison to analyze communication efficiency between services, which has not been widely done in previous studies. 


Table 1. List of related research


<table><tr><td>Contributions</td><td>Architecture/Method</td><td>Output</td><td>Matric</td><td>Author</td></tr><tr><td>Testing the feasibility and benefits of the MMSD (Microservices Migration using the Strangler pattern and DDD) approach on a monolithic Green Button application. [16]</td><td>- Migration: Strangler Fig Pattern and Domain-Driven Design (DDD)- Testing: Performance Testing with first AUT (Application Under Test)</td><td>The Green Button system that has been migrated to MMSD has higher reliability and a lower error rate compared to the monolithic Green Button system.</td><td>- Average (ms)- Error (%) - Throughput (sec)- Average Response Size (byte)</td><td>Li, C., Ma, S., Lu, T. (2020)</td></tr><tr><td>Improve scalability and performance of Open Library applications by migrating applications from monolithic to microservices. [34]</td><td>Method: Domain-Driven Design (DDD) dan Strangler Fig Pattern Performance Testing: load test, stress test, spike test, endurance test, scalability test and volume test</td><td>Improved application performance and increased freedom for organizational developers in choosing development technologies</td><td>- Average Response Time- Failure Request- Peak User</td><td>Ferdinand, J., Syahrina, A., &amp; Musnansyah A. (2021)</td></tr><tr><td>Refactoring the SmartCampus application from monolithic to microservices to improve application performance. [7]</td><td>- Refactoring: Domain decomposition and Strangler Pattern.- Testing: Performance Testing : load testing, spike testing, stress testing, and soak testing</td><td>The SmartCampus system implements a microservices architecture and performs better than previous monolithic systems.</td><td>- Average Response Time (ms)- Latency (ms)- Throughput</td><td>Riyanto, Hermadi, I., Nurhadryani, Y. (2023)</td></tr><tr><td>Analyzing the practical aspects of using REST APIs and gRPC for communication processes within applications in a microservices-based ecosystem. [14]</td><td>Performance Testing: load testing, stress testing, endurance testing, spike testing, and volume testing</td><td>The research results show that both technologies (REST and gRPC API) are excellent for intra-service communication within a microservices ecosystem.</td><td>Response Time</td><td>Paszkiewicz, A., Ganzha, M., Paprzycki, M., Sowinski, P., Lacalle, I., Palau, C. (2022)</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/b930e458dfb22f84d60301228a4711c9e60670bef3eb33013a7cdc19a21e111e.jpg)



Figure 1. WorkFlow diagram of the process research conducted, methods, and evaluation


This section explains the research process used to compare the performance of monolithic and microservices systems. It begins by outlining the application architectural design used for the evaluation. This section covers scenario development, performance testing, data collection, experiments, and preliminary results. Finally, it discusses the performance results of testing tools and their employability based on performance indicators. Figure 1 depicts a workflow diagram for the research process, techniques, and evaluation. 

## Design and implementation of a software application

## Application design for monolithic architecture over client-server side

The system architecture diagram of the Tracer Study UPI provides a high-level representation of the software components, emphasizing their functions, implementations, and interrelationships. As illustrated in Figure 2, the diagram depicts the integration of servers, web servers, databases, and the application of specific design patterns within the Tracer Study UPI system. The architecture is structured as a monolithic system, in which all core functionalities are consolidated within a single deployment unit. Analyzing this architectural model reveals the role of each component in supporting the system’s functionality, as well as the flow of data and the operational processes within the system. 

The application architecture integrates both client-side and server-side components within a single, unified codebase. All services within the application access a common database, reflecting a shared data layer. Core functionalities such as configuration management, logging, and task scheduling are centralized within the application. Since the services are developed as part of the same project, they utilize a consistent technology stack. Furthermore, the services exhibit a high degree of interdependence; thus, failures, updates, or modifications in one service—or changes to the database—can propagate and affect other components. The system is deployed as a monolithic application, running within a single process. Consequently, when one service experiences increased traffic, the system must be scaled by replicating the entire application instance, rather than scaling individual services independently. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/f67c573475d81a8d07da9ad9fe7c2ce66c16896da3b2ce29de061728b0033135.jpg)



Figure 1. Monolithic architecture



Application design for microservices architecture over docker containers


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/756c2f08ec96c80a4e1c4e4c239457b579a580060c83874c827d20b61f26a633.jpg)



Figure 3. Microservices architecture


The design of the microservices architecture is represented through a comprehensive architectural diagram (Figure 3), which outlines the individual services, their associated databases, inter-service relationships, and the interactions between microservices, clients, and third-party services. This diagram illustrates the communication among several predefined services, including the Post Service, Tracer Service, SIAK Service, and Auth Service. Additionally, two new services—Data Pipeline Service and API Gateway— have been introduced to facilitate the system’s migration from a monolithic to a microservices architecture. The Data Pipeline Service is responsible for synchronizing data between the monolithic database and the new Tracer database. This synchronization process encompasses a sequence of operations such as data copying, transformation, cleaning, validation, and normalization. 

The development result of architecture are packaged using containers that carried out using Docker. Each service represents a single container, and each database is also created as a separate container. This method aims to simulate the implementation of microservices deployed on different servers. Containerization isolates services so that the resources and environments of each service are not mixed, and it also isolates operating system failures that occur in one service from those of another. 

Containers on the server are run using the base Docker image of each service that has been pushed to Docker Hub. Each service runs as a separate container, as shown in Figure 4.24. Each service communicates internally through the Docker Network. External clients can only communicate with the API Gateway service through the NGINX Web Server. Once running, the containers can be managed using Docker commands. 

The API Gateway serves as an intermediary layer between clients and backend services. Its core functions include protocol translation, centralized routing, and request mapping from clients to the appropriate microservices. Each service in the architecture is equipped with its own authentication middleware, which enforces security by performing token-based authorization for every incoming request. This process ensures that access to resources is granted only to authorized users, in accordance with Zero Trust Architecture (ZTA) principles, thereby strengthening the security of inter-service communications. 

Furthermore, inter-service communication within the microservices environment is implemented using the gRPC (Google Remote Procedure Call) framework. gRPC leverages the HTTP/2 protocol and Protocol Buffers (a compact binary serialization format), offering performance and efficiency benefits ideal for internal service-to-service interactions. In contrast, external communication with clients is established using RESTful APIs (Representational State Transfer), providing greater flexibility and compatibility with various client types. 

## Performance testing scenario

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/dfc07552b4bf99485148484a0a5158f9dfcb371e524ca69d2587941c5cbc30e2.jpg)



Figure 4. Performance testing stage


The performance testing stages on the monolithic and microservice systems that have been developed as depicted in Figure 4 are carried out by following several stages based on the testing stages according to Meier et al. [2] as follows: identifying the test environment, identifying performance acceptance criteria, planning and designing tests, configuring the test environment, implementing the test design, running tests, and analyzing, reporting results and retesting. 

The test environment identification stage is carried out by selecting testing tools and preparing the server. The next stage is to identify performance acceptance criteria, at this stage the performance acceptance criteria indicators are determined. The indicators used as a reference for performance acceptance criteria are in accordance with Table 2. 


Table 2. Performance testing indicator assessment


<table><tr><td>No</td><td>Indicator</td><td>Description</td></tr><tr><td rowspan="4">1.</td><td>Response Time</td><td>The time from the first byte of page interest sent to the last byte received from the server response.</td></tr><tr><td>Min</td><td>Minimum response time</td></tr><tr><td>Average</td><td>Average response time</td></tr><tr><td>Max</td><td>Maximum response time</td></tr><tr><td rowspan="3">2.</td><td>Throughput</td><td>The measure of the number of transactions or requests that can be processed by a system or application in a given time period, usually measured in units of transactions per second (TPS) to transactions per day (TPD).</td></tr><tr><td>Request per Second</td><td>Number of requests handled per second</td></tr><tr><td>Request per Day</td><td>Number of requests handled per day</td></tr><tr><td>3</td><td>Error Rate</td><td>Percentage of requests that encountered problems against all requests. This percentage counts all HTTP status codes that returned an error to the server. In addition, it can also count requests that timed out.</td></tr></table>

The system performance assessment indicators by looking at response time can be categorized into key response times as explained in Table 3. 


Table 3. Response time values description


<table><tr><td>Response Time</td><td>Description</td></tr><tr><td>0,1 second</td><td>This response time is the best time. If the response time is 0.1 indicates that the user feels that the system responds instantly, and the user feels that there is no interference with the system.</td></tr><tr><td>1,0 second</td><td>This response time is the maximum acceptable response time. Users do not feel any disruption although they may experience some delays. Response times longer than 1 second can disrupt the user experience.</td></tr><tr><td>10 second</td><td>This response time is the maximum limit after the response time exceeds the acceptable limit. However, currently, if the response time exceeds 6 seconds, the user will leave the site or exit the application.</td></tr></table>

In general, response times should be as fast as possible, in the range of 0.1 – 1 second. However, users can adapt to slower response times, but users will never be happy with a response time of more than 2 seconds. In addition, performance indicators are measured from the throughput value which can be calculated using the throughput calculation formula as follows: 

Throughput = Number of Samples / Time (seconds) 

Number of Samples: Total number of requests successfully completed. 

Time: Total time required to complete all requests (from start to finish). 

For example, if there are 1000 requests and the average time for each request to be completed is 10 seconds, then the throughput value is 1000 requests / 10 seconds = 100 requests/second. 

These two performance assessments, namely the response time value and the throughput value of a request indicate that the smaller the response time value and the greater the throughput value, the better the performance of the web application [7]. This good performance will certainly optimize the use of the application in terms of access speed. Good access speed can make users more comfortable when using the application [14]. Throughput represents the server's ability to handle heavy loads. The higher the Throughput, the better the server performance [5]. 

The next stage is planning and designing testing carried out by creating various test scenarios. Designing test scenarios includes determining the name of the scenario/feature/transaction, sampler/function call/method, number of threads/users/requests, ramp-up period, and loop count. Classification and Performance Testing Indicators, the types of performance testing applied at this testing stage are load testing, soak testing, and stress testing. Load testing is carried out to test the resilience and capacity of the system with a test load according to the scenario that is carried out continuously at a certain time. Soak testing is carried out to determine the stability of the system and evaluate failures that occur over a fairly long period of access. Stress testing is carried out by giving a large load and stopping when the load given results in 100% failure, which means that the system is completely unable to handle the load. 

At the configuration and preparation stage of the testing environment, the application is installed/deployed on the server and the testing tools used are set up. The source code deployment process for the UPI monolithic Tracer Study application is carried out using containers. The application is built into a Docker Image and run on the server in the container. The monolithic database is also run in a different MySQL container. In order for the application to run, the environment configuration is also carried out. 

## Experiment, analyze, and report

The implementation stage of the test design is carried out by implementing scenarios and test specifications with testing tools. The total number of scenarios implemented is a scenario or thread group. To create a sampler, recording and tracking of application usage activities on the browser is also carried out using JMeter. The results of the activity recording will be saved as a step in each test scenario. In addition, to record test results, it is necessary to install a listener on each scenario or thread group, such as the View Results Tree, View Results in Table, and Summary Report listeners. After that, the test execution is carried out in stages starting with the load testing, soak testing, and stress testing stages. The test results that are run are then analyzed and written in a report in the form of a table and if needed, retesting can be carried out. 

## RESULTS AND DISCUSSIONS

## Identifying the test environment

Applications tested on the UPI Tracer Study monolithic system with URL http://203.194.113.32:8000. Testing was conducted using Apache JMeter v5.6.3 software. This software is open-source and crossplatform. In this test, the server used to deploy all services is a Virtual Private Server (VPS) with Operating System: Linux Ubuntu 20.04 LTS 64-bit, CPU 2 Core, Memory 8 GB RAM, and storage 40 GB SSD. 

## Identifying performance acceptance criteria

Performance acceptance criteria indicators or metrics used in this test are response time and throughput. Response time indicators include minimum response time (min), average response time (Average), and maximum response time. Meanwhile, Throughput criteria calculated by number of handled requests per second (request per second), number of handled requests per day (Request Per Day), and percentage of errors in handling requests (error rate). 

## Planning and designing testing

In applications with monolithic architecture, testing planning and design are done by creating several test scenarios. In JMeter, one test scenario is a thread group. Scenarios are created based on features that can be used by users. Scenario design includes creating a scenario name, a list of steps or actions, test data needed, the number of users/requests/threads, ramp-up period, and loop count. The following Table 4 shows a list of several performance test scenarios that have been designed for the UPI Tracer Study monolithic system. 


Table 4. Performance testing scenario at monolithic scenario


<table><tr><td>No</td><td>Scenario</td><td>Step</td><td>URL Path</td></tr><tr><td>1.</td><td>User lists</td><td>Access control access page &gt; users</td><td>/admin/users</td></tr><tr><td>2.</td><td>Export data PKTS</td><td>Access dashboard questionnaire report &gt; click download</td><td>/admin/report_by_year/{year}</td></tr><tr><td>3.</td><td>Report By Year</td><td>Access dashboard questionnaire report</td><td>/admin/report_by_year/{year}</td></tr><tr><td>4.</td><td>Report By Study Program</td><td>Access dashboard questionnaire report by Study Program</td><td>/admin/perstudyprogram{year}/{program_study_code}</td></tr><tr><td>5.</td><td>Posts Lists</td><td>Access Home Page or Posts Page</td><td>/ or /posts</td></tr><tr><td>6.</td><td>Post Details</td><td>Access detail post page</td><td>/posts/{id_post}/{slug}</td></tr></table>

In applications with microservices architecture, testing planning and design are done by creating various test scenarios. One test scenario can include 1 or more endpoints/function calls from microservices. This is because the UPI Tracer Study microservices system breaks down functionality in a monolithic system following the Single Responsibility Principal (SRP). So that one feature or transaction in a monolithic system can be divided into several functions in the microservices system. 

Test scenario design includes determining the name of the scenario/feature/transaction, sampler/function call/method, number of threads/users/requests, ramp-up period, and loop count. The following are some performance test scenarios for microservices applications that have been designed as shown in Table 5. While the number of threads, ramp-up period, and loop count are determined based on the type of performance testing performed. 


Table 5. Performance testing scenario at microservices scenario


<table><tr><td>No</td><td>Scenario</td><td>Sampler</td></tr><tr><td>1.</td><td>User lists</td><td>GetAllUsers</td></tr><tr><td>2.</td><td>Export data PKTS</td><td>ExportPKTSReport</td></tr><tr><td>3.</td><td>Report By Year</td><td>GetPKTSRekapByYear</td></tr><tr><td>4.</td><td>Report By Study Program</td><td>GetPKTSRekapByStudyProgram</td></tr><tr><td>5.</td><td>Posts Lists</td><td>GetAllPosts</td></tr><tr><td>6.</td><td>Post Details</td><td>GetPostByIdAddVisitorGetCommentsByPostsId</td></tr></table>

As mentioned, the types of performance testing applied in this testing phase are load testing, soak testing, and stress testing. The following is the design of performance testing carried out based on its type. 

## Load testing

Load testing is performed for 30-45 minutes per scenario continuously with gradually increasing loads. This is intended to test the resilience and capacity of the system. The design of the load testing test case for each scenario is shown in Table 6. The design was also used to test the previous monolithic system. 


Table 6. Load testing scenario


<table><tr><td>Scenario</td><td>Test</td><td>Threads</td><td>Ramp-Up Period</td><td>Loop Count</td></tr><tr><td rowspan="3">User Lists</td><td>PT-a.01-001/001</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.01-002/002</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.01-003/003</td><td>100</td><td>300</td><td>3</td></tr><tr><td rowspan="3">Export Data</td><td>PT-a.02-001/004</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.02-002/005</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.02-003/006</td><td>100</td><td>300</td><td>3</td></tr><tr><td rowspan="3">Summary Data By Year</td><td>PT-a.03-001/007</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.03-002/008</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.03-003/009</td><td>100</td><td>300</td><td>3</td></tr><tr><td rowspan="3">Summary Data By Study Program</td><td>PT-a.04-001/010</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.04-002/011</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.04-003/012</td><td>100</td><td>300</td><td>3</td></tr><tr><td rowspan="3">Post List</td><td>PT-a.05-001/013</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.05-002/014</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.05-003/015</td><td>100</td><td>300</td><td>3</td></tr><tr><td rowspan="3">Detail Post</td><td>PT-a.06-001/016</td><td>10</td><td>30</td><td>5</td></tr><tr><td>PT-a.06-002/017</td><td>50</td><td>150</td><td>3</td></tr><tr><td>PT-a.06-003/018</td><td>100</td><td>300</td><td>3</td></tr></table>

## Soak testing

Soak testing is performed for 24 hours per scenario continuously with a fixed load. This is intended to determine the stability of the system and evaluate failures that occur over a long period of access. The soak testing test case design for each test scenario is shown in Table 7. The design was also used to test the previous monolithic system. 


Table 7. Soak testing scenario


<table><tr><td>Scenario</td><td>Test</td><td>Threads</td><td>Ramp-Up Period</td><td>Loop Count</td></tr><tr><td>User Lists</td><td>PT-b.01-001/001</td><td>5</td><td>30</td><td>~</td></tr><tr><td>Export Data</td><td>PT-b.02-002/002</td><td>5</td><td>30</td><td>~</td></tr><tr><td>Summary Data By Year</td><td>PT-b.03-003/003</td><td>10</td><td>30</td><td>~</td></tr><tr><td>Summary Data By Study Program</td><td>PT-b.04-004/004</td><td>10</td><td>30</td><td>~</td></tr><tr><td>Post List</td><td>PT-b.05-005/005</td><td>10</td><td>30</td><td>~</td></tr><tr><td>Detail Post</td><td>PT-b.06-006/006</td><td>10</td><td>30</td><td>~</td></tr></table>

## Stress testing

Stress testing is done by giving a large load and stopping when the load given results in 100% failure, which means the system is completely unable to handle the load. This is intended to find out what conditions or loads cause complete failure of the system. The design of stress testing test cases for each test scenario is shown in Table 8. The load is increased by 10x each time it does not meet the 100% error rate condition. This design was also used to test the previous monolithic system 


Table 8. Stress testing scenario


<table><tr><td>Scenario</td><td>Test</td><td>Threads</td><td>Ramp-Up Period</td><td>Loop Count</td></tr><tr><td>Daftar Users</td><td>PT-c.01-001/x</td><td>5-?</td><td>30</td><td>~</td></tr><tr><td>Export PKTS</td><td>PT-c.02-001/x</td><td>5-?</td><td>30</td><td>~</td></tr><tr><td>PKTS Rekap By Year</td><td>PT-c.03-001/x</td><td>10-?</td><td>30</td><td>~</td></tr><tr><td>PKTS Rekap By Prodi</td><td>PT-c.04-001/x</td><td>10-?</td><td>30</td><td>~</td></tr><tr><td>Daftar Posts</td><td>PT-c.05-001/x</td><td>10-?</td><td>30</td><td>~</td></tr><tr><td>Detail Post</td><td>PT-c.06-001/x</td><td>10-?</td><td>30</td><td>~</td></tr></table>

## Configurating testing environment

At this stage, the configuration and preparation of the testing environment is carried out, such as installing/deploying the application on the server and setting up the testing tools used. The process of deploying the source code of the UPI monolithic Tracer Study application is carried out using containers. The application is built into a Docker Image and run on the server in the container. The monolithic database is also run in a different MySQL container. In order for the application to run, the environment configuration is also carried out. The application can be accessed after the DNS configuration and web server installation are carried out. Checking the running of the application can be seen in Figure 5. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/58162b3c8ebd1d7434bcc0c14bf8fe2d4a6b1545d6acb3093e2cbdcc6716165a.jpg)



Figure 5. Deploying monolithic tracer study application to VPS


Meanwhile, for microservices applications, it is required to inspect all services that have been installed on the server by examining the running Docker Container as shown in Figure 6. The 'Up' state on the container implies that the container and the services in it are functioning well (there are no runtime issues that cause the service to terminate). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/1fe1555ff8c13aa3ecc90fbb1bc4e6d48ea96c936de03eefed43efc1471d7871.jpg)



Figure 6. Status deployed services status on microservices application in server


In addition, at this stage, preparations are made for using JMeter as a testing tool. The performance testing tool used, namely Apache JMeter, is shown in Figure 7. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/d53129dc58c7a90c7c14dbc9303a7db4d5c7be674dc2fd997e57a2bca13c033d.jpg)



Figure 7. JMeter user interface


## Implementing scenario testing

The previously designed test scenarios and specifications are implemented into the Apache JMeter testing tool as shown in Figure 8 for monolithic application testing and Figure 9 for microservices application testing. The total number of scenarios implemented is 6 scenarios or thread groups. In monolithic testing, each thread group represents the activity of using the application on the browser and records user activity (step). While in microservices testing, each thread group has a sampler which is a gRPC function involved in the scenario. In addition, in both tests, each thread group is also paired with a listener to record test results, namely View Results in Table, View Results Tree, and Summary Report. The result of this implementation is the JMeter test plan file which is stored in .jmx format in the Apache JMeter /bin folder. This design implementation represents equivalent features in both monolithic and microservices applications. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/9f67056943b857780ac1378bcd891f7124d0e0d3a63cfb16e7ada06b438df553.jpg)



Figure 8. Implementation of performance testing for monolithic application


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/61b17fd28a54466d5a4c868261f1fe8b3507c6f8f1314e041a8ab99d1d20c22a.jpg)



Figure 9. Implementation of performance testing for microservice application


## Executing testing

At this stage, all tests are run in stages. Starting from load testing, soak testing, to stress testing. Apache JMeter used to execute the test is run on a local machine. The following Figure 10 (monolithic) and Figure 11 (microservices) show a preview when load testing is being run using the Graphical User Interface (GUI) of the Apache JMeter application. The results of all tests are recorded by each listener installed on each thread group. The results are analyzed and reported in the next testing stage. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/b06ef938fec8a7ddf9eb664e358545735b5044f3481e685232050c73c6126c2e.jpg)



Figure 10. Running load testing for monolithic application


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/fc69b42ac346e6fe86719aafa33227538adffa457c2d1c06bf28123360041569.jpg)



Figure 11. Running load testing for microservice application


## Analyzing and report testing

Based on result of executing testing, test result data was obtained that shows the performance of the two applications with different architectures, namely monolithic and microservices. The following are the test results on load testing, soak testing, and stress testing. 

## Load testing

The results of the load testing on the monolithic application are shown in Table 9. From the data, it can be seen that the entire scenario has an average response time of 1138ms (milliseconds) and a throughput of 1rps (request per second). Meanwhile, to calculate the estimated throughput per day, the following formula can be used [rps x 60 x 60 x 24] [16]. From this calculation, the throughput value per day is 86,400 requests. From this load testing, it can also be seen that the average system error rate in handling requests is 0.23%. 


Table 9. Performance result of load testing at monolithic architecture


<table><tr><td rowspan="2">Test</td><td rowspan="2">Reqs</td><td colspan="3">Response Time (ms)</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-a.01-001/001</td><td>50</td><td>693</td><td>1557</td><td>2232</td><td>1,5</td><td>129.600</td><td>0,00%</td></tr><tr><td>PT-a.01-002/002</td><td>200</td><td>641</td><td>1382</td><td>1984</td><td>1,1</td><td>95.040</td><td>0,00%</td></tr><tr><td>PT-a.01-003/003</td><td>500</td><td>519</td><td>1041</td><td>5574</td><td>0,5</td><td>43.200</td><td>0,21%</td></tr><tr><td>PT-a.02-001/004</td><td>50</td><td>618</td><td>1497</td><td>2178</td><td>1,5</td><td>129.600</td><td>0,00%</td></tr><tr><td>PT-a.02-002/005</td><td>200</td><td>587</td><td>1428</td><td>2486</td><td>0,8</td><td>69.120</td><td>0,00%</td></tr><tr><td>PT-a.02-003/006</td><td>500</td><td>526</td><td>1040</td><td>5588</td><td>0,5</td><td>43.200</td><td>0,15%</td></tr><tr><td>PT-a.03-001/007</td><td>50</td><td>612</td><td>1468</td><td>2174</td><td>1,5</td><td>129.600</td><td>0,00%</td></tr><tr><td>PT-a.03-002/008</td><td>200</td><td>584</td><td>1395</td><td>2341</td><td>1,3</td><td>112.320</td><td>0,02%</td></tr><tr><td>PT-a.03-003/009</td><td>500</td><td>540</td><td>1031</td><td>5603</td><td>0,5</td><td>43.200</td><td>0,24%</td></tr><tr><td>PT-a.04-001/010</td><td>50</td><td>710</td><td>1547</td><td>2224</td><td>1,5</td><td>129.600</td><td>0,00%</td></tr><tr><td>PT-a.04-002/011</td><td>200</td><td>649</td><td>1193</td><td>3146</td><td>1,1</td><td>95.040</td><td>0,00%</td></tr><tr><td>PT-a.04-003/012</td><td>500</td><td>528</td><td>1068</td><td>5578</td><td>0,5</td><td>43.200</td><td>0,48%</td></tr><tr><td>PT-a.05-001/013</td><td>50</td><td>389</td><td>849</td><td>1677</td><td>1,6</td><td>138.240</td><td>0,00%</td></tr><tr><td>PT-a.05-002/014</td><td>200</td><td>345</td><td>811</td><td>1798</td><td>0,9</td><td>77.760</td><td>0,07%</td></tr><tr><td>PT-a.05-003/015</td><td>500</td><td>289</td><td>687</td><td>4784</td><td>0,5</td><td>43.200</td><td>0,59%</td></tr><tr><td>PT-a.06-001/016</td><td>50</td><td>366</td><td>909</td><td>1532</td><td>1,6</td><td>138.240</td><td>0,00%</td></tr><tr><td>PT-a.06-002/017</td><td>200</td><td>242</td><td>827</td><td>2357</td><td>1,2</td><td>103.680</td><td>0,00%</td></tr><tr><td>PT-a.06-003/018</td><td>500</td><td>326</td><td>762</td><td>4829</td><td>0,5</td><td>43.200</td><td>0,03%</td></tr><tr><td>Average</td><td>700</td><td>242</td><td>1138</td><td>5578</td><td>1</td><td>86.400</td><td>0,23%</td></tr></table>

Meanwhile, in the microservices application, the test results data are shown in Table 10 below. From the data, it can be seen that the entire scenario has an average response time of 154ms (milliseconds) and a throughput of 16.4rps (requests per second). Meanwhile, to calculate the estimated throughput per day, the following formula can be used [rps x 60 x 60 x 24]. From this calculation, the throughput value per day is 1,451,067 requests. From this load testing, it can also be seen that the average system error rate in handling requests is 0.00%. 


Table 10. Performance result of load testing at microservices architecture


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Reqs</td><td colspan="3">Response Time</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-a.01-001/001</td><td>50</td><td>14</td><td>78</td><td>324</td><td>121,4</td><td>10.488.960</td><td>0,00%</td></tr><tr><td>PT-a.01-002/002</td><td>200</td><td>12</td><td>39</td><td>324</td><td>8,5</td><td>734.400</td><td>0,00%</td></tr><tr><td>PT-a.01-003/003</td><td>500</td><td>12</td><td>34</td><td>943</td><td>12,4</td><td>1.071.840</td><td>0,00%</td></tr><tr><td>PT-a.02-001/004</td><td>50</td><td>164</td><td>331</td><td>542</td><td>14,6</td><td>1.261.440</td><td>0,00%</td></tr><tr><td>PT-a.02-002/005</td><td>200</td><td>164</td><td>523</td><td>1451</td><td>8,1</td><td>699.840</td><td>0,00%</td></tr><tr><td>PT-a.02-003/006</td><td>500</td><td>164</td><td>529</td><td>1451</td><td>12,1</td><td>1.045.440</td><td>0,00%</td></tr><tr><td>PT-a.03-001/007</td><td>50</td><td>99</td><td>322</td><td>4384</td><td>2,9</td><td>250.560</td><td>0,00%</td></tr><tr><td>PT-a.03-002/008</td><td>200</td><td>96</td><td>203</td><td>4384</td><td>8,5</td><td>734.400</td><td>0,00%</td></tr><tr><td>PT-a.03-003/009</td><td>500</td><td>96</td><td>226</td><td>4383</td><td>13,4</td><td>1.157.760</td><td>0,00%</td></tr><tr><td>PT-a.04-001/010</td><td>50</td><td>52</td><td>119</td><td>738</td><td>2,8</td><td>241.920</td><td>0,00%</td></tr><tr><td>PT-a.04-002/011</td><td>200</td><td>50</td><td>85</td><td>738</td><td>9,5</td><td>820.800</td><td>0,00%</td></tr><tr><td>PT-a.04-003/012</td><td>500</td><td>49</td><td>97</td><td>1266</td><td>14,7</td><td>1.270.080</td><td>0,00%</td></tr><tr><td>PT-a.05-001/013</td><td>50</td><td>15</td><td>39</td><td>129</td><td>22,8</td><td>1.969.920</td><td>0,00%</td></tr><tr><td>PT-a.05-002/014</td><td>200</td><td>15</td><td>31</td><td>129</td><td>9,4</td><td>812.160</td><td>0,00%</td></tr><tr><td>PT-a.05-003/015</td><td>500</td><td>14</td><td>31</td><td>129</td><td>14,2</td><td>1.226.880</td><td>0,00%</td></tr><tr><td>PT-a.06-001/016</td><td>50</td><td>12</td><td>24</td><td>64</td><td>4,8</td><td>414.720</td><td>0,00%</td></tr><tr><td>PT-a.06-002/017</td><td>200</td><td>12</td><td>31</td><td>1053</td><td>2,8</td><td>803.520</td><td>0,00%</td></tr><tr><td>PT-a.06-003/018</td><td>500</td><td>12</td><td>31</td><td>1053</td><td>12,9</td><td>1.114.560</td><td>0,00%</td></tr><tr><td>Average</td><td>700</td><td>12</td><td>154</td><td>4384</td><td>16,4</td><td>1.451.067</td><td>0,00%</td></tr></table>

The figure 12,13,14 and 15 explaining table 9, shows how response time graphs can help you see how well a system is working. The throughput, error rate, and heatmap all show a consistent pattern when it comes to stability and processing power at different load levels. The average response time for 50 and 200 users is usually between 580 and 710 ms. This is longer than some 500 user load scenarios, which actually show shorter response times. This suggests that the system is optimized internally in some cases, but not always. When there are few users, the system can handle the most transactions, with 138,240 transactions per day. But when there are 500 users, it can only handle 43,200 transactions per day, which shows that it can't handle more load. The error rate graph shows that most of the 50 and 200 user load scenarios don't have any errors. However, there are big spikes in a few 500 user load scenarios, especially in the 04-003 and 05- 003 series, where errors range from 0.48% to 0.59%. The heatmap highlights this pattern by showing that there are a lot of light colors in the 500 loads column. This shows that errors are mostly happening in highflow situations. In general, these results show that the system works very well and stably when the load is low to medium. However, when the load is high, the performance drops, the number of errors goes up, and the throughput goes down. This means that architectural improvements or load handling mechanisms are needed for larger applications. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/d77e5f4d718c28e930e458a64c8c5c516db2fa454149f91d2cf195194fe0ef5e.jpg)



Figure 12. Bar chart response time (average), displays a comparison of avg response time values for al test cases


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/dda8a54a219e7008f3c4729c41baf82cd8bf25bbc51beea4ee835d3adcc5f3e4.jpg)



Figure 13. Bar chart throughput (per day), shows the processing capacity of each scenario per day


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/7b5736c5311673d5a7567502b16b2af9d246ce2adb06f0da3d33aad6fcf2aa2e.jpg)



Figure 14. Line chart error rates, eror trend graph for each test


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/209d74f7-7d78-4b97-9ca8-284f1ed3834a/79315f532c87cdbc1c4e4f93dd725ec4e7eb0841e93df8fe30899f911b14f76a.jpg)



Figure 15. Error distribution heatmap created from 18 error rate datapoints mapped onto a 6×3 grid


## Soak testing

Soak testing that has been done for 24 hours found that each request has a different percentage of request handling failure or error rate. In monolithic applications, the average error rate of all scenarios is 2.53%. Meanwhile, detailed error rate data per scenario can be seen in Table 11. Based on data recorded by the listener of each thread group, the errors that occur include having the status codes Internal Server Error, Time Out, and Bad Gateway. 


Table 11. Performance result of soak testing at monolithic architecture


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Reqs</td><td colspan="3">Response Time (ms)</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-b.01-001/001</td><td>5</td><td>325</td><td>697</td><td>1226</td><td>1,2</td><td>103.680</td><td>0,96%</td></tr><tr><td>PT-b.02-002/002</td><td>5</td><td>618</td><td>1256</td><td>1978</td><td>1,8</td><td>155.520</td><td>2,21%</td></tr><tr><td>PT-b.03-003/003</td><td>10</td><td>635</td><td>1394</td><td>2575</td><td>1,1</td><td>95.040</td><td>1,57%</td></tr><tr><td>PT-b.04-004/004</td><td>10</td><td>713</td><td>1344</td><td>2087</td><td>1,2</td><td>103.680</td><td>2,13%</td></tr><tr><td>PT-b.05-005/005</td><td>10</td><td>392</td><td>874</td><td>2349</td><td>1,3</td><td>112.320</td><td>2,95%</td></tr><tr><td>PT-b.06-006/006</td><td>10</td><td>386</td><td>1034</td><td>1825</td><td>1,9</td><td>164.160</td><td>3,46%</td></tr><tr><td>Average</td><td>8</td><td>325</td><td>1099</td><td>2575</td><td>1,4</td><td>120.960</td><td>2,53%</td></tr></table>

Meanwhile, in microservices applications, the average error rate of all scenarios is 0.03%. Meanwhile, detailed error rate data per scenario can be seen in Table 12. Based on data recorded by the listener of each thread group, the errors that occur include having the status codes Unavailable, Deadline Exceeded, and Resource Exhausted. 


Table 12. Performance result of soak testing at microservices architecture


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Reqs</td><td colspan="3">Response Time</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-b.01-001/001</td><td>5</td><td>12</td><td>24</td><td>65</td><td>4,5</td><td>388.800</td><td>0,00%</td></tr><tr><td>PT-b.02-002/002</td><td>5</td><td>168</td><td>245</td><td>412</td><td>5,5</td><td>475.200</td><td>0,04%</td></tr><tr><td>PT-b.03-003/003</td><td>10</td><td>49</td><td>87</td><td>231</td><td>5</td><td>432.000</td><td>0,01%</td></tr><tr><td>PT-b.04-004/004</td><td>10</td><td>93</td><td>149</td><td>375</td><td>4,6</td><td>397.440</td><td>0,01%</td></tr><tr><td>PT-b.05-005/005</td><td>10</td><td>14</td><td>25</td><td>86</td><td>1,3</td><td>112.320</td><td>0,02%</td></tr><tr><td>PT-b.06-006/006</td><td>10</td><td>14</td><td>22</td><td>76</td><td>4,5</td><td>388.800</td><td>0,03%</td></tr><tr><td>Average</td><td>8</td><td>12</td><td>92</td><td>412</td><td>4,2</td><td>430.560</td><td>0,03%</td></tr></table>

## Stress testing

Stress testing that is carried out continuously until the system experiences 100% failure, finds that in monolithic applications the system will go down when given an average load of 23,000 requests per second. This shows that the system has a limit in handling the maximum load received at that amount every second. In addition to the system, this limit is also influenced by the specifications of the machine/server used for the implementation of the system. The maximum load limit that can cause failure in each scenario is shown in Table 13. 


Table 13. Performance result of stress testing at monolithic architecture


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Reqs</td><td colspan="3">Response Time</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-c.01-001/011</td><td>5</td><td>53</td><td>69</td><td>84</td><td>9,2</td><td>794.880</td><td>0,00%</td></tr><tr><td>PT-c.01-002/012</td><td>50</td><td>47</td><td>62</td><td>78</td><td>10,8</td><td>933.120</td><td>0,17%</td></tr><tr><td>PT-c.01-003/013</td><td>500</td><td>91</td><td>154</td><td>188</td><td>7,6</td><td>656.640</td><td>37,19%</td></tr><tr><td>PT-c.01-004/014</td><td>5.000</td><td>90</td><td>189</td><td>265</td><td>3,3</td><td>285.120</td><td>71,82%</td></tr><tr><td>PT-c.01-005/015</td><td>50.000</td><td>86</td><td>203</td><td>478</td><td>0,2</td><td>17.280</td><td>100,00%</td></tr><tr><td>PT-c.02-001/020</td><td>5</td><td>128</td><td>152</td><td>212</td><td>5,3</td><td>457.920</td><td>0,00%</td></tr><tr><td>PT-c.02-002/021</td><td>50</td><td>111</td><td>161</td><td>249</td><td>3,2</td><td>276.480</td><td>44,62%</td></tr><tr><td>PT-c.02-003/022</td><td>500</td><td>117</td><td>178</td><td>285</td><td>2,7</td><td>233.280</td><td>100,00%</td></tr><tr><td>PT-c.03-001/023</td><td>10</td><td>166</td><td>192</td><td>239</td><td>7,4</td><td>639.360</td><td>0,00%</td></tr><tr><td>PT-c.03-002/024</td><td>100</td><td>159</td><td>210</td><td>240</td><td>5,8</td><td>501.120</td><td>19,78%</td></tr><tr><td>PT-c.03-003/025</td><td>1.000</td><td>151</td><td>485</td><td>793</td><td>3,1</td><td>267.840</td><td>75,33%</td></tr><tr><td>PT-c.03-004/026</td><td>10.000</td><td>164</td><td>397</td><td>726</td><td>2,2</td><td>190.080</td><td>100,00%</td></tr><tr><td>PT-c.04-001/027</td><td>10</td><td>160</td><td>182</td><td>214</td><td>4,7</td><td>406.080</td><td>0,00%</td></tr><tr><td>PT-c.04-002/028</td><td>100</td><td>154</td><td>189</td><td>223</td><td>3,4</td><td>293.760</td><td>0,25%</td></tr><tr><td>PT-c.04-003/029</td><td>1.000</td><td>162</td><td>294</td><td>328</td><td>2,5</td><td>216.000</td><td>80,31%</td></tr><tr><td>PT-c.04-004/030</td><td>10.000</td><td>171</td><td>288</td><td>331</td><td>1,6</td><td>138.240</td><td>100,00%</td></tr><tr><td>PT-c.05-001/043</td><td>10</td><td>73</td><td>91</td><td>140</td><td>12,4</td><td>1.071.360</td><td>0,00%</td></tr><tr><td>PT-c.05-002/044</td><td>100</td><td>99</td><td>168</td><td>227</td><td>12,1</td><td>1.045.440</td><td>9,12%</td></tr><tr><td>PT-c.05-003/045</td><td>1.000</td><td>102</td><td>139</td><td>162</td><td>13,4</td><td>1.157.760</td><td>64,37%</td></tr><tr><td>PT-c.05-004/046</td><td>10.000</td><td>159</td><td>237</td><td>285</td><td>10,5</td><td>907.200</td><td>100,00%</td></tr><tr><td>PT-c.06-001/047</td><td>10</td><td>70</td><td>120</td><td>161</td><td>11,1</td><td>959.040</td><td>0,00%</td></tr><tr><td>PT-c.06-002/048</td><td>100</td><td>92</td><td>139</td><td>192</td><td>10,6</td><td>915.840</td><td>19,04%</td></tr><tr><td>PT-c.06-003/049</td><td>1.000</td><td>105</td><td>146</td><td>189</td><td>11,1</td><td>959.040</td><td>46,71%</td></tr><tr><td>PT-c.06-004/050</td><td>10.000</td><td>144</td><td>229</td><td>341</td><td>8,3</td><td>717.120</td><td>100,00%</td></tr><tr><td>Average</td><td>306.100</td><td>47</td><td>178</td><td>793</td><td>21,9</td><td>672.224</td><td>68,31%</td></tr></table>

Meanwhile, in the microservices application, it was found that the system would go down when given an average load of 39,000,000 requests. This shows that the system has a limit in handling the maximum load received at that amount. In addition to the system, this limit is also influenced by the machine/server specifications used for system implementation. Table 14 below shows the maximum load limits that can cause failure in each scenario. 


Table 14. Performance result of stress testing at microservice architecture


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Reqs</td><td colspan="3">Response Time</td><td colspan="2">Throughput</td><td rowspan="2">Error Rate</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Sec</td><td>Day</td></tr><tr><td>PT-c.01-001/001</td><td>10</td><td>64</td><td>81</td><td>112</td><td>6,4</td><td>552.960</td><td>0,00%</td></tr><tr><td>PT-c.01-002/002</td><td>100</td><td>83</td><td>148</td><td>218</td><td>5,9</td><td>509.760</td><td>0,07%</td></tr><tr><td>PT-c.01-003/003</td><td>1.000</td><td>127</td><td>199</td><td>294</td><td>5,1</td><td>440.640</td><td>23,00%</td></tr><tr><td>PT-c.01-004/004</td><td>10.000</td><td>119</td><td>243</td><td>326</td><td>4,4</td><td>380.140</td><td>70,23%</td></tr><tr><td>PT-c.01-005/005</td><td>100.000</td><td>121</td><td>266</td><td>314</td><td>0,2</td><td>17.280</td><td>100,00%</td></tr><tr><td>PT-c.02-001/006</td><td>5</td><td>81</td><td>128</td><td>183</td><td>4,2</td><td>362.880</td><td>0,00%</td></tr><tr><td>PT-c.02-002/007</td><td>50</td><td>79</td><td>119</td><td>162</td><td>5,3</td><td>457.920</td><td>0,02%</td></tr><tr><td>PT-c.02-003/008</td><td>500</td><td>65</td><td>129</td><td>154</td><td>4,8</td><td>414.720</td><td>13,28%</td></tr><tr><td>PT-c.02-004/009</td><td>5.000</td><td>67</td><td>182</td><td>229</td><td>3,2</td><td>622.080</td><td>49,65%</td></tr><tr><td>PT-c.02-005/010</td><td>50.000</td><td>92</td><td>201</td><td>412</td><td>1,4</td><td>120.960</td><td>100,00%</td></tr><tr><td>PT-c.03-001/011</td><td>5</td><td>53</td><td>69</td><td>84</td><td>9,2</td><td>794.880</td><td>0,00%</td></tr><tr><td>PT-c.03-002/012</td><td>50</td><td>47</td><td>62</td><td>78</td><td>10,8</td><td>933.120</td><td>0,17%</td></tr><tr><td>PT-c.03-003/013</td><td>500</td><td>91</td><td>154</td><td>188</td><td>7,6</td><td>656.640</td><td>37,19%</td></tr><tr><td>PT-c.03-004/014</td><td>5.000</td><td>90</td><td>189</td><td>265</td><td>3,3</td><td>285.120</td><td>71,82%</td></tr><tr><td>PT-c.03-005/015</td><td>50.000</td><td>86</td><td>203</td><td>478</td><td>0,2</td><td>17.280</td><td>100,00%</td></tr><tr><td>PT-c.04-001/016</td><td>10</td><td>113</td><td>148</td><td>225</td><td>2,7</td><td>233.280</td><td>0,00%</td></tr><tr><td>PT-c.04-002/017</td><td>100</td><td>102</td><td>166</td><td>231</td><td>2,3</td><td>198.720</td><td>0,01%</td></tr><tr><td>PT-c.04-003/018</td><td>1.000</td><td>133</td><td>190</td><td>274</td><td>1,4</td><td>120.960</td><td>64,80%</td></tr><tr><td>PT-c.04-004/019</td><td>10.000</td><td>112</td><td>237</td><td>389</td><td>0,6</td><td>51.840</td><td>100,00%</td></tr><tr><td>PT-c.05-001/020</td><td>5</td><td>128</td><td>152</td><td>212</td><td>5,3</td><td>457.920</td><td>0,00%</td></tr><tr><td>PT-c.05-002/021</td><td>50</td><td>111</td><td>161</td><td>249</td><td>3,2</td><td>276.480</td><td>44,62%</td></tr><tr><td>PT-c.05-003/022</td><td>500</td><td>117</td><td>178</td><td>285</td><td>2,7</td><td>233.280</td><td>100,00%</td></tr><tr><td>PT-c.06-001/023</td><td>10</td><td>166</td><td>192</td><td>239</td><td>7,4</td><td>639.360</td><td>0,00%</td></tr><tr><td>PT-c.06-002/024</td><td>100</td><td>159</td><td>210</td><td>240</td><td>5,8</td><td>501.120</td><td>19,78%</td></tr><tr><td>PT-c.06-003/025</td><td>1.000</td><td>151</td><td>485</td><td>793</td><td>3,1</td><td>267.840</td><td>75,33%</td></tr><tr><td>PT-c.06-004/026</td><td>10.000</td><td>164</td><td>397</td><td>726</td><td>2,2</td><td>190.080</td><td>100,00%</td></tr><tr><td>PT-c.07-001/027</td><td>10</td><td>160</td><td>182</td><td>214</td><td>4,7</td><td>406.080</td><td>0,00%</td></tr><tr><td>PT-c.07-002/028</td><td>100</td><td>154</td><td>189</td><td>223</td><td>3,4</td><td>293.760</td><td>0,25%</td></tr><tr><td>PT-c.07-003/029</td><td>1.000</td><td>162</td><td>294</td><td>328</td><td>2,5</td><td>216.000</td><td>80,31%</td></tr><tr><td>PT-c.07-004/030</td><td>10.000</td><td>171</td><td>288</td><td>331</td><td>1,6</td><td>138.240</td><td>100,00%</td></tr><tr><td>PT-c.08-001/031</td><td>5</td><td>128</td><td>156</td><td>219</td><td>5,2</td><td>449.280</td><td>0,00%</td></tr><tr><td>PT-c.08-002/032</td><td>50</td><td>172</td><td>237</td><td>291</td><td>5,1</td><td>440.640</td><td>0,78%</td></tr><tr><td>PT-c.08-003/033</td><td>500</td><td>224</td><td>251</td><td>299</td><td>4,3</td><td>371.520</td><td>36,10%</td></tr><tr><td>PT-c.08-004/034</td><td>5.000</td><td>241</td><td>277</td><td>319</td><td>2,8</td><td>241.920</td><td>100,00%</td></tr><tr><td>PT-c.09-001/035</td><td>10</td><td>94</td><td>112</td><td>146</td><td>11,1</td><td>959.040</td><td>0,00%</td></tr><tr><td>PT-c.09-002/036</td><td>100</td><td>91</td><td>138</td><td>172</td><td>10,4</td><td>898.560</td><td>21,94%</td></tr><tr><td>PT-c.09-003/037</td><td>1.000</td><td>115</td><td>168</td><td>202</td><td>10,1</td><td>872.640</td><td>88,12%</td></tr><tr><td>PT-c.09-004/038</td><td>10.000</td><td>149</td><td>211</td><td>276</td><td>7,3</td><td>630.720</td><td>100,00%</td></tr><tr><td>PT-c.10-001/039</td><td>10</td><td>62</td><td>97</td><td>150</td><td>8,8</td><td>760.320</td><td>0,00%</td></tr><tr><td>PT-c.10-002/040</td><td>100</td><td>79</td><td>105</td><td>162</td><td>7,7</td><td>665.280</td><td>4,92%</td></tr><tr><td>PT-c.10-003/041</td><td>1.000</td><td>97</td><td>133</td><td>151</td><td>7,2</td><td>622.080</td><td>37,28%</td></tr><tr><td>PT-c.10-004/042</td><td>10.000</td><td>155</td><td>218</td><td>270</td><td>5,2</td><td>449.280</td><td>100,00%</td></tr><tr><td>PT-c.11-001/043</td><td>10</td><td>73</td><td>91</td><td>140</td><td>12,4</td><td>1.071.360</td><td>0,00%</td></tr><tr><td>PT-c.11-002/044</td><td>100</td><td>99</td><td>168</td><td>227</td><td>12,1</td><td>1.045.440</td><td>9,12%</td></tr><tr><td>PT-c.11-003/045</td><td>1.000</td><td>102</td><td>139</td><td>162</td><td>13,4</td><td>1.157.760</td><td>64,37%</td></tr><tr><td>PT-c.11-004/046</td><td>10.000</td><td>159</td><td>237</td><td>285</td><td>10,5</td><td>907.200</td><td>100,00%</td></tr><tr><td>PT-c.12-001/047</td><td>10</td><td>70</td><td>120</td><td>161</td><td>11,1</td><td>959.040</td><td>0,00%</td></tr><tr><td>PT-c.12-002/048</td><td>100</td><td>92</td><td>139</td><td>192</td><td>10,6</td><td>915.840</td><td>19,04%</td></tr><tr><td>PT-c.12-003/049</td><td>1.000</td><td>105</td><td>146</td><td>189</td><td>11,1</td><td>959.040</td><td>46,71%</td></tr><tr><td>PT-c.12-004/050</td><td>10.000</td><td>144</td><td>229</td><td>341</td><td>8,3</td><td>717.120</td><td>100,00%</td></tr><tr><td>Average</td><td>306.100</td><td>47</td><td>178</td><td>793</td><td>21,9</td><td>672.224</td><td>68,31%</td></tr></table>

## Comparative analysis of performance test results of monolithic systems with microservices


Table 15. Comparison of load testing performance on monolithic and microservices systems


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Requests</td><td colspan="3">Monolithic</td><td colspan="3">Microservices</td></tr><tr><td>Response Time</td><td>RPS</td><td>Error Rate</td><td>Response Time</td><td>RPS</td><td>Error Rate</td></tr><tr><td rowspan="3">PT-a.01</td><td>50</td><td>1557 ms</td><td>1,5/s</td><td>0,00%</td><td>78 ms</td><td>121,4/s</td><td>0,00%</td></tr><tr><td>200</td><td>1382 ms</td><td>1,1/s</td><td>0,00%</td><td>39 ms</td><td>8,5/s</td><td>0,00%</td></tr><tr><td>500</td><td>1041 ms</td><td>0,5/s</td><td>0,21%</td><td>34 ms</td><td>12,4/s</td><td>0,00%</td></tr><tr><td rowspan="3">PT-a.02</td><td>50</td><td>1497 ms</td><td>1,5/s</td><td>0,00%</td><td>331 ms</td><td>14,6/s</td><td>0,00%</td></tr><tr><td>200</td><td>1428 ms</td><td>0,8/s</td><td>0,00%</td><td>523 ms</td><td>8,1/s</td><td>0,00%</td></tr><tr><td>500</td><td>1040 ms</td><td>0,5/s</td><td>0,15%</td><td>529 ms</td><td>12,1/s</td><td>0,00%</td></tr><tr><td rowspan="3">PT-a.03</td><td>50</td><td>1468 ms</td><td>1,5/s</td><td>0,00%</td><td>322 ms</td><td>2,9/s</td><td>0,00%</td></tr><tr><td>200</td><td>1395 ms</td><td>1,3/s</td><td>0,02%</td><td>203 ms</td><td>8,5/s</td><td>0,00%</td></tr><tr><td>500</td><td>1031 ms</td><td>0,5/s</td><td>0,24%</td><td>226 ms</td><td>13,4/s</td><td>0,00%</td></tr><tr><td rowspan="3">PT-a.04</td><td>50</td><td>1547 ms</td><td>1,5/s</td><td>0,00%</td><td>119 ms</td><td>2,8/s</td><td>0,00%</td></tr><tr><td>200</td><td>1193 ms</td><td>1,1/s</td><td>0,00%</td><td>85 ms</td><td>9,5/s</td><td>0,00%</td></tr><tr><td>500</td><td>1068 ms</td><td>0,5/s</td><td>0,48%</td><td>97 ms</td><td>14,7/s</td><td>0,00%</td></tr><tr><td rowspan="3">PT-a.05</td><td>50</td><td>849 ms</td><td>1,6/s</td><td>0,00%</td><td>39 ms</td><td>22,8/s</td><td>0,00%</td></tr><tr><td>200</td><td>811 ms</td><td>0,9/s</td><td>0,07%</td><td>31 ms</td><td>9,4/s</td><td>0,00%</td></tr><tr><td>500</td><td>687 ms</td><td>0,5/s</td><td>0,59%</td><td>31 ms</td><td>14,2/s</td><td>0,00%</td></tr><tr><td rowspan="3">PT-a.06</td><td>50</td><td>909 ms</td><td>1,6/s</td><td>0,00%</td><td>24 ms</td><td>4,8/s</td><td>0,00%</td></tr><tr><td>200</td><td>827 ms</td><td>1,2/s</td><td>0,00%</td><td>31 ms</td><td>2,8/s</td><td>0,00%</td></tr><tr><td>500</td><td>762 ms</td><td>0,5/s</td><td>0,03%</td><td>31 ms</td><td>12,9/s</td><td>0,00%</td></tr><tr><td>Average</td><td></td><td>1138 ms</td><td>1/s</td><td>0,23%</td><td>154 ms</td><td>16,4/s</td><td>0,00%</td></tr></table>

Table 15 presents a comparison of the results of load testing performance on monolithic and microservices systems. Based on research, the test case start with small number of concurrent users/request per second for example 1,20, 50, 100 request per second. On this test case, testing conduct from 50 request until 200 request to understand how your system behaves under light load. Gradually increase the number of users to identify the point at which your system begins to experience stress [16]. 

The data presented in Table 15 shows that there is no response time in the microservices system that exceeds the monolithic system in all scenarios. The average response time improved from 1138ms to 154ms. There was also an increase in the number of requests that can be processed in 1 second (requests per second/rps), namely from an average of 1rps to 16.4rps. System failures (marked by the error rate) that occurred also decreased from the previous average of 0.23% to 0%. These data show that there has been an improvement in the system, especially in terms of performance with the implementation of the microservices architecture. In the soak testing test carried out for 24 hours with a constant load, the results of the two system architectures also showed differences. The following Table 16 presents a comparison of the results of soak testing performance tests on monolithic and microservices systems. 


Table 16. Comparation result of soak testing monolithic and microservices system


<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Requests</td><td colspan="3">Monolithic</td><td colspan="3">Microservices</td></tr><tr><td>Response Time</td><td>RPS</td><td>Error Rate</td><td>Response Time</td><td>RPS</td><td>Error Rate</td></tr><tr><td>PT-b.01</td><td>5</td><td>697</td><td>1,2</td><td>0,96%</td><td>24</td><td>4,5</td><td>0,00%</td></tr><tr><td>PT-b.02</td><td>5</td><td>1256</td><td>1,8</td><td>2,21%</td><td>245</td><td>5,5</td><td>0,04%</td></tr><tr><td>PT-b.03</td><td>10</td><td>1394</td><td>1,1</td><td>1,57%</td><td>87</td><td>5</td><td>0,01%</td></tr><tr><td>PT-b.04</td><td>10</td><td>1344</td><td>1,2</td><td>2,13%</td><td>149</td><td>4,6</td><td>0,01%</td></tr><tr><td>PT-b.05</td><td>10</td><td>874</td><td>1,3</td><td>2,95%</td><td>25</td><td>1,3</td><td>0,02%</td></tr><tr><td>PT-b.06</td><td>10</td><td>1034</td><td>1,9</td><td>3,46%</td><td>22</td><td>4,5</td><td>0,03%</td></tr><tr><td colspan="2">Average</td><td>1099</td><td>1,4</td><td>2,53%</td><td>92</td><td>4,2</td><td>0,03%</td></tr></table>

Based on Table $^ { 1 6 , }$ the soak testing results show significant performance differences between the monolithic system and the microservices system. The microservices system consistently outperforms the monolithic system, showing a significantly lower average response time (92 ms compared to 1099 ms) and higher requests per second (RPS) (4.2 rps compared to 1.4 rps). In addition, the microservices system maintains a much lower error rate, with an average of only 0.03% compared to the monolithic system of 2.53%. These results indicate that the microservices architecture is more resilient and stable in its availability in handling loads over a sustained period of time. 

## Practical implications

Migrating from a monolithic architecture to microservices is a step organizations should consider to improve resilience and scalability. This migration process is generally undertaken when the existing architecture faces limitations in terms of scalability and flexibility, which impacts the speed of feature development and deployment. While it offers advantages, this migration process presents challenges such as distributed system complexity, data consistency management, and increased monitoring and automation requirements. These challenges must be addressed by implementing DevOps principles. To support an effective transition, organizations are advised to utilize containerization (Docker), orchestration tools (Kubernetes), API Gateway, and monitoring tools such as Prometheus and Grafana. A phased migration strategy using the strangler pattern (Fowler, 2018) is also recommended to ensure the transformation process does not disrupt existing systems. 

The findings of this study were implemented contextually on the UPI Tracer Study system using Laravel and Golang gRPC. While the microservices design principles found in this study are generally applicable, their effectiveness may vary in other programming languages or frameworks, such as Node.js or Python. Therefore, these results are best viewed as a limited empirical contribution that can be extended through studies on other technologies. 

The following adjustments can be made to implement a microservices architecture in other languages or frameworks, requiring adjustments at the communication, infrastructure, performance, and security levels. 

1. Inter-Service Communication Model Different languages and frameworks generally use varying communication mechanisms, such as REST API (HTTP/JSON), gRPC (Protocol Buffers), or GraphQL. Communication efficiency, latency, and overhead need to be re-examined because performance between protocols can vary significantly. 

2. Dependency Management and Framework Ecosystem Each language has a different ecosystem of packages and libraries to support microservices. For example, Node.js has strong support for REST APIs and event-driven architecture, while Go is more optimized for high-performance services. These differences impact modularization, testing, and dependency management strategies. 

3. Performance and Scalability Microservices architectures are highly dependent on the runtime efficiency of the language used. Go, for example, excels in concurrency and memory efficiency, while Python tends to be slower but excels in AI/analytics integration. Therefore, performance testing (load testing and stress testing) needs to be tailored to each language. 

4. Distributed Data Management Strategy Database management in microservices systems depends on the data integration pattern used, such as a database per service or a shared database. 

5. DevOps Deployment and Integration Mechanisms Different languages have different preferences for DevOps tools and pipelines. For example, Java Spring Boot is often integrated with Jenkins or ArgoCD, while Node.js often uses GitHub Actions or Docker Compose. This impacts the CI/CD process, containerization, and monitoring. 

6. Service Security and Authentication Management Security implementations, such as token-based authentication (JWT), OAuth 2.0, or mTLS, can differ across ecosystems. Each framework provides different libraries for authorization and encryption, so security configurations need to be reviewed for consistency across services. 

7. Adapting Patterns to Observability and Logging Microservices systems require comprehensive monitoring and tracing. Tools like Prometheus, Grafana, Jaeger, or ELK can be used, but integration may vary depending on the language and framework. For example, the implementation of logging middleware in Node.js differs from that in Golang or Python. 

8. Development Team Readiness and Resources Migrating or reimplementing to another language requires considering the technical capabilities of the development team. Proficiency in the language, framework, and supporting tools will directly impact implementation efficiency and system stability. 

Results from a Laravel–Golang gRPC-based system can serve as a conceptual reference, but retesting and configuration calibration on other platforms are necessary to ensure the results remain valid and optimal. 

## CONCLUSION

The results of performance tests on monolithic and microservices systems indicate how implementing microservices affects system performance. It was discovered that implementing the microservices system improved system performance in terms of response time, which decreased from an average of 1138ms to 154ms. Furthermore, the throughput, or number of requests that can be processed per day, jumped from an average of one per second (8400 requests per day) to 16.4 per second (1,419,960 requests per day). The microservices system also has a lower failure or error rate in normal use than the monolithic system, with an error rate of 0.00% vs an average of 0.23% in the monolithic system. These results show that the microservices design performs better than the monolithic architecture. 

## REFERENCES



[1] S. Newman, Monolith to Microservices: Evolutionary Patterns to Transform. O’Reilly Media, 2020. 





[2] J. D. Meier, C. Farre, P. Bansode, S. Barber, and D. Rea, Performance Testing Guidance for Web Applications, 1st ed. Microsoft Press, 2007. 





[3] A. Mili and F. Tchier, Software Testing: Concepts and Operations, 1st ed. John Wiley & Sons, 2015. 





[4] G. Blinowski, A. Ojdowska, and A. Przybyłek, “Monolithic vs . Microservice Architecture : A Performance and Scalability Evaluation,” IEEE Access, vol. 10, pp. 20357–20374, 2022, doi: 10.1109/ACCESS.2022.3152803. 





[5] A. Ismail, A. Y. Ananta, S. N. Arief, and E. N. Hamdana, “Performance Testing Sistem Ujian Online Menggunakan Jmeter Pada Lingkungan Virtual,” J. Inform. Polinema, no. Vol. 9 No. 2 (2023): Vol 9 No 2 (2023), pp. 159–164, 2023, [Online]. Available: https://jurnal.polinema.ac.id/index.php/jip/article/view/1728/1347 





[6] R. Mufrizal and D. Indarti, “Refactoring Arsitektur Microservice Pada Aplikasi Absensi PT. Graha Usaha Teknik,” J. Nas. Teknol. dan Sist. Inf., vol. 5, no. 1, pp. 57–68, Apr. 2019, doi: 10.25077/TEKNOSI.v5i1.2019.57-68. 





[7] Riyanto, Irman Hermadi, and Yani Nurhadryani, “Analisis Uji Performa Aplikasi Dari Hasil Implementasi Refactoring Arsitektur Monolitik Ke Mikroservis dengan Decomposition dan Strangler Pattern,” J. Sist. Cerdas, vol. 6, no. 3, pp. 189–203, Dec. 2023, doi: 10.37396/jsc.v6i3.352. 





[8] F. Tapia, M. Á. Mora, W. Fuertes, H. Aules, E. Flores, and T. Toulkeridis, “From Monolithic Systems to Microservices: A Comparative Study of Performance,” Appl. Sci., vol. 10, no. 17, p. 5797, Aug. 2020, doi: 10.3390/app10175797. 





[9] F. Auer, V. Lenarduzzi, M. Felderer, and D. Taibi, “From monolithic systems to Microservices: An assessment framework,” Inf. Softw. Technol., vol. 137, p. 106600, Sep. 2021, doi: 10.1016/j.infsof.2021.106600. 





[10] P. Di Francesco, P. Lago, and I. Malavolta, “Migrating Towards Microservice Architectures: An Industrial Survey,” in 2018 IEEE International Conference on Software Architecture (ICSA), Apr. 2018, pp. 29–2909. doi: 10.1109/ICSA.2018.00012. 





[11] J. Fritzsch, J. Bogner, S. Wagner, and A. Zimmermann, “Microservices Migration in Industry: Intentions, Strategies, and Challenges,” in 2019 IEEE International Conference on Software Maintenance and Evolution (ICSME), Sep. 2019, pp. 481–490. doi: 10.1109/ICSME.2019.00081. 





[12] D. Wolfart et al., “Modernizing Legacy Systems with Microservices: A Roadmap,” in Evaluation and Assessment in Software Engineering, Jun. 2021, pp. 149–159. doi: 10.1145/3463274.3463334. 





[13] A. de Camargo, I. Salvadori, R. dos S. Mello, and F. Siqueira, “An architecture to automate performance tests on microservices,” in Proceedings of the 18th International Conference on Information Integration and Web-based Applications and Services, Nov. 2016, pp. 422–429. doi: 10.1145/3011141.3011179. 





[14] M. Bolanowski et al., “Eficiency of REST and gRPC realizing communication tasks in microservice-based ecosystems,” Aug. 2022, doi: 10.3233/FAIA220242. 





[15] R. Chen, S. Li, and Z. Li, “From Monolith to Microservices: A Dataflow-Driven Approach,” in 2017 24th Asia-Pacific Software Engineering Conference (APSEC), Dec. 2017, pp. 466–475. doi: 10.1109/APSEC.2017.53. 





[16] C.-Y. Li, S.-P. Ma, and T.-W. Lu, “Microservice Migration Using Strangler Fig Pattern: A Case Study on the Green Button System,” in 2020 International Computer Symposium (ICS), Dec. 2020, pp. 519–524. doi: 10.1109/ICS51289.2020.00107. 





[17] L. Khoirunnisa’, “Rancang Bangun Sistem E-Learning Berbasis Microservices dan Domain Driven 





Design (Studi Kasus Probistek UIN Maulana Malik Ibrahim Malang),” UIN Maulana Malik Ibrahim Malang, 2019. [Online]. Available: http://etheses.uin-malang.ac.id/15301/1/14650045.pdf 





[18] H. Knoche and W. Hasselbring, “Using Microservices for Legacy Software Modernization,” IEEE Softw., vol. 35, no. 3, pp. 44–49, May 2018, doi: 10.1109/MS.2018.2141035. 





[19] K. S. Swarnalatha, A. Mallya, G. Mukund, and R. Ujwal Bharadwaj, “Solving Problems of Large Codebases: Uber’s Approach Using Microservice Architecture,” 2023, pp. 653–662. doi: 10.1007/978-981-19-5482-5_57. 





[20] S. Li et al., “A dataflow-driven approach to identifying microservices from monolithic applications,” J. Syst. Softw., vol. 157, p. 110380, Nov. 2019, doi: 10.1016/j.jss.2019.07.008. 





[21] K. Sharma et al., “Review of Software Architecture and Design Practices: Current Trends and Future Direction,” Tuijin Jishu/Journal Propuls. Technol., vol. 43, no. 4, pp. 1001–4055, 2022, doi: 10.52783/tjjpt.v43.i4.2341. 





[22] A. Trichur Ramachandran, Abhishek, Mamatha, Rashmi, Badrinath, and M. Parmar, “Understanding Migration from Monolithic to Microservice Architecture and its Challenges,” Int. J. Sci. Res. Eng. Dev., vol. 4, no. 3, pp. 1742–1752, 2021, [Online]. Available: https://ijsred.com/volume4/issue3/IJSRED-V4I3P243.pdf 





[23] O. Al-Debagy and P. Martinek, “A Comparative Review of Microservices and Monolithic Architectures,” in 2018 IEEE 18th International Symposium on Computational Intelligence and Informatics (CINTI), Nov. 2018, pp. 000149–000154. doi: 10.1109/CINTI.2018.8928192. 





[24] I. Molyneaux, The Art of Application Performance Testing: From Strategy to Tools, 1st ed. O’Reilly Media, 2009. 





[25] P. Tanuska, O. Vlkovic, and L. Spendla, “The Usage of Performance Testing for Information Systems,” Int. J. Comput. Theory Eng., pp. 144–147, 2012, doi: 10.7763/IJCTE.2012.V4.439. 





[26] K. Gos and W. Zabierowski, “The Comparison of Microservice and Monolithic Architecture,” in 2020 IEEE XVIth International Conference on the Perspective Technologies and Methods in MEMS Design (MEMSTECH), Apr. 2020, pp. 150–153. doi: 10.1109/MEMSTECH49584.2020.9109514. 





[27] P. Jatkiewicz and S. Okrój, “Differences in performance, scalability, and cost of using microservice and monolithic architecture,” in Proceedings of the 38th ACM/SIGAPP Symposium on Applied Computing, Mar. 2023, pp. 1038–1041. doi: 10.1145/3555776.3578725. 





[28] M. D. Marieska, Arya Yunanta, Harisatul Aulia, Alvi Syahrini Utami, and Muhammad Qurhanul Rizqie, “Performance Comparison of Monolithic and Microservices Architectures in Handling High-Volume Transactions,” J. RESTI (Rekayasa Sist. dan Teknol. Informasi), vol. 9, no. 3, pp. 594–600, Jun. 2025, doi: 10.29207/resti.v9i3.6183. 





[29] T. R. H. Barzotto and K. Farias, “Evaluation of the impacts of decomposing a monolithic application into microservices: A case study,” Aug. 2022, [Online]. Available: http://arxiv.org/abs/2203.13878 





[30] C. M. Aderaldo, N. C. Mendonca, C. Pahl, and P. Jamshidi, “Benchmark Requirements for Microservices Architecture Research,” in 2017 IEEE/ACM 1st International Workshop on Establishing the Community-Wide Infrastructure for Architecture-Based Software Engineering (ECASE), May 2017, pp. 8–13. doi: 10.1109/ECASE.2017.4. 





[31] V. Lenarduzzi, F. Lomio, N. Saarimäki, and D. Taibi, “Does Migrate a Monolithic System to Microservices Decrease the Technical Debt?,” Jul. 2020, doi: 10.1016/j.jss.2020.110710. 





[32] H. M. AlGhamdi, C. Bezemer, W. Shang, A. E. Hassan, and P. Flora, “Towards reducing the time needed for load testing,” J. Softw. Evol. Process, vol. 35, no. 3, Mar. 2023, doi: 10.1002/smr.2276. 





[34] J. F. Lombogia, A. Syahrina, and A. Munansyah, “Perancangan Arsitektur Perangkat Lunak Microservices pada Aplikasi Open Library Telkom University Menggunakan GRPC,” Telkom University, 2021. 

