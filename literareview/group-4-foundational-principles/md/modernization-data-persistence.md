Enabling data persistence in microservices 

## AWS Prescriptive Guidance

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/85a951081f2c26631ff2708ae15f83840f78245cfbc5193f09b2604a0c6a5b8e.jpg)


## AWS Prescriptive Guidance: Enabling data persistence in microservices

Copyright © 2026 Amazon Web Services, Inc. and/or its afiliates. All rights reserved. 

Amazon's trademarks and trade dress may not be used in connection with any product or service that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are the property of their respective owners, who may or may not be afiliated with, connected to, or sponsored by Amazon. 

## Table of Contents

Introduction .... 1
Targeted business outcomes .... 3
Patterns for enabling data persistence .... 4
Database-per-service pattern .... 4
API composition pattern .... 6
CQRS pattern .... 8
Event sourcing pattern .... 11
Amazon Kinesis Data Streams implementation .... 12
Amazon EventBridge implementation .... 13
Saga pattern .... 14
Shared-database-per-service pattern .... 16
FAQ .... 18
When can I modernize my monolithic database as part of my modernization journey? .... 18
Can I keep a legacy monolithic database for multiple microservices? .... 18
What should I consider when designing databases for a microservices architecture? .... 18
What is a common pattern for maintaining data consistency across different microservices? .... 18
How do I maintain transaction automation? .... 19
Do I have to use a separate database for each microservice? .... 19
How can I keep a microservice's persistent data private if they all share a single database? .... 19
Resources .... 20
Related guides .... 20
Other resources .... 20
Document history .... 21 

## Enabling data persistence in microservices

Tabby Ward and Balaji Mohan, Amazon Web Services 

Organizations constantly seek new processes to create growth opportunities and reduce time to market. You can increase your organization's agility and eficiency by modernizing your applications, software, and IT systems. Modernization also helps you deliver faster and better services to your customers. 

Application modernization is a gateway to continuous improvement for your organization, and it begins by refactoring a monolithic application into a set of independently developed, deployed, and managed microservices. This process has the following steps: 

• Decompose monoliths into microservices – Use patterns to break down monolithic applications into microservices. 

• Integrate microservices – Integrate the newly created microservices into a microservices architecture by using Amazon Web Services (AWS) serverless services. 

• Enable data persistence for microservices architecture – Promote polyglot persistence among your microservices by decentralizing their data stores. 

Although you can use a monolithic application architecture for some use cases, modern application features often don't work in a monolithic architecture. For example, the entire application can't remain available while you upgrade individual components, and you can't scale individual components to resolve bottlenecks or hotspots (relatively dense regions in your application's data). Monoliths can become large, unmanageable applications, and significant efort and coordination is required among multiple teams to introduce small changes. 

Legacy applications typically use a centralized monolithic database, which makes schema changes dificult, creates a technology lock-in with vertical scaling as the only way to respond to growth, and imposes a single point of failure. A monolithic database also prevents you from building the decentralized and independent components required for implementing a microservices architecture. 

Previously, a typical architectural approach was to model all user requirements in one relational database that was used by the monolithic application. This approach was supported by popular relational database architecture, and application architects usually designed the relational schema at the earliest stages of the development process, built a highly normalized schema, and then sent it to the developer team. However, this meant that the database drove the data model for the application use case, instead of the other way round. 

By choosing to decentralize your data stores, you promote polyglot persistence among your microservices, and identify your data storage technology based on the data access patterns and other requirements of your microservices. Each microservice has its own data store and can be independently scaled with low-impact schema changes, and data is gated through the microservice's API. Breaking down a monolithic database is not easy, and one of the biggest challenges is structuring your data to achieve the best possible performance. Decentralized polyglot persistence also typically results in eventual data consistency, and other potential challenges that require a thorough evaluation include data synchronization during transactions, transactional integrity, data duplication, and joins and latency. 

This guide is for application owners, business owners, architects, technical leads, and project managers. The guide provides the following six patterns to enable data persistence among your microservices: 

• Database-per-service pattern 

• API composition pattern 

• CQRS pattern 

• Event sourcing pattern 

• Saga pattern 

• For steps to implement the saga pattern by using AWS Step Functions, see the pattern Implement the serverless saga pattern by using AWS Step Functions on the AWS Prescriptive Guidance website. 

• Shared-database-per-service pattern 

The guide is part of a content series that covers the application modernization approach recommended by AWS. The series also includes: 

• Phased approach to modernizing applications in the AWS Cloud 

• Evaluating modernization readiness for applications in the AWS Cloud 

Decomposing monoliths into microservices 

Integrating microservices by using AWS serverless services 

## Targeted business outcomes

Many organizations find that innovating and improving the user experience is negatively impacted by monolithic applications, databases, and technologies. Legacy applications and databases reduce your options for adopting modern technology frameworks, and constrain your competitiveness and innovation. However, when you modernize applications and their data stores, they become easier to scale and faster to develop. A decoupled data strategy improves fault tolerance and resiliency, which helps accelerate the time to market for your new application features. 

You should expect the following six outcomes from promoting data persistence among your microservices: 

• Remove legacy monolithic databases from your application portfolio. 

• Improve fault tolerance, resiliency, and availability for your applications. 

• Shorten your time to market for new application features. 

• Reduce your overall licensing expenses and operational costs. 

• Take advantage of open-source solutions (for example, MySQL or PostgreSQL). 

• Build highly scalable and distributed applications by choosing from more than 15 purposebuilt database engines on the AWS Cloud. 

## Patterns for enabling data persistence

The following patterns are used to enable data persistence in your microservices. 

## Topics

Database-per-service pattern 

• API composition pattern 

• CQRS pattern 

• Event sourcing pattern 

• Saga pattern 

• Shared-database-per-service pattern 

## Database-per-service pattern

Loose coupling is the core characteristic of a microservices architecture, because each individual microservice can independently store and retrieve information from its own data store. By deploying the database-per-service pattern, you choose the most appropriate data stores (for example, relational or non-relational databases) for your application and business requirements. This means that microservices don't share a data layer, changes to a microservice's individual database do not impact other microservices, individual data stores cannot be directly accessed by other microservices, and persistent data is accessed only by APIs. Decoupling data stores also improves the resiliency of your overall application, and ensures that a single database can't be a single point of failure. 

In the following illustration, diferent AWS databases are used by the "Sales," "Customer," and "Compliance" microservices. These microservices are deployed as AWS Lambda functions and accessed through an Amazon API Gateway API. AWS Identity and Access Management (IAM) policies ensure that data is kept private and not shared among the microservices. Each microservice uses a database type that meets its individual requirements; for example, "Sales" uses Amazon Aurora, "Customer" uses Amazon DynamoDB, and "Compliance" uses Amazon Relational Database Service (Amazon RDS) for SQL Server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/66401015c40647b818bd89b06901b4b563bf80d2149719fe70ad60c9358a2c81.jpg)


You should consider using this pattern if: 

• Loose coupling is required between your microservices. 

• Microservices have diferent compliance or security requirements for their databases. 

• More granular control of scaling is required. 

There are the following disadvantages to using the database-per-service pattern: 

• It might be challenging to implement complex transactions and queries that span multiple microservices or data stores. 

• You have to manage multiple relational and non-relational databases. 

• Your data stores must meet two of the CAP theorem requirements: consistency, availability, or partition tolerance. 

## Note

If you use the database-per-service pattern, you must deploy another pattern to implement queries that span multiple microservices. You can use the API composition pattern (which you can speed up with the CQRS pattern) or the event sourcing pattern to create aggregated results. 

## API composition pattern

This pattern uses an API composer, or aggregator, to implement a query by invoking individual microservices that own the data. It then combines the results by performing an in-memory join. 

The following diagram illustrates how this pattern is implemented. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/99ac3573c51771fdd97b66aa44ad1edcbab54ec031fcaab5ffa2ba5e10d379af.jpg)


The diagram shows the following workflow: 

1. An API gateway serves the "/customer" API, which has an "Orders" microservice that tracks customer orders in an Amazon Aurora database. 

2. The "Support" microservice tracks customer support issues and stores them in an Amazon OpenSearch Service database. 

3. The "CustomerDetails" microservice maintains customer attributes (for example, address, phone number, or payment details) in an Amazon DynamoDB table. 

4. The "GetCustomer" AWS Lambda function runs the APIs for these microservices, and performs an inmemory join on the data before returning it to the requester. This helps easily retrieve customer information in one network call to the user-facing API, and keeps the interface very simple. 

The API composition pattern ofers the simplest way to gather data from multiple microservices. However, there are the following disadvantages to using the API composition pattern: 

• It might not be suitable for complex queries and large datasets that require in-memory joins. 

• Your overall system becomes less available if you increase the number of microservices connected to the API composer. 

• Increased database requests create more network trafic, which increases your operational costs. 

## CQRS pattern

The command query responsibility segregation (CQRS) pattern separates the data mutation, or the command part of a system, from the query part. You can use the CQRS pattern to separate updates and queries if they have diferent requirements for throughput, latency, or consistency. The CQRS pattern splits the application into two parts: the command side and the query side. The command side handles create, update, and delete requests. The query side runs the query part by using the read replicas. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/fa1716c21ecd9dbdb4fdda2fbaf7518781e64237d21f16e18d43f9b9858af8b7.jpg)


The diagram shows the following process: 

1. The business interacts with the application by sending commands through an API. Commands are actions such as creating, updating or deleting data. 

2. The application processes the incoming command on the command side. This involves validating, authorizing, and running the operation. 

3. The application persists the command's data in the write (command) database. 

4. After the command is stored in the write database, events are triggered to update the data in the read (query) database. 

5. The read (query) database processes and persists the data. Read databases are designed to be optimized for specific query requirements. 

6. The business interacts with read APIs to send queries to the query side of the application. 

7. The application processes the incoming query on the query side and retrieves the data from the read database. 

You can implement the CQRS pattern by using various combinations of databases, including: 

• Using relational database management system (RDBMS) databases for both the command and the query side. Write operations go to the primary database and read operations can be routed to read replicas. Example: Amazon RDS read replicas 

• Using an RDBMS database for the command side and a NoSQL database for the query side. Example: Modernize legacy databases using event sourcing and CQRS with AWS DMS 

• Using NoSQL databases for both the command and the query side. Example: Build a CQRS event store with Amazon DynamoDB 

• Using a NoSQL database for the command side and an RDBMS database for the query side, as discussed in the following example. 

In the following illustration, a NoSQL data store, such as DynamoDB, is used to optimize the write throughput and provide flexible query capabilities. This achieves high write scalability on workloads that have well-defined access patterns when you add data. A relational database, such as Amazon Aurora, provides complex query functionality. A DynamoDB stream sends data to a Lambda function that updates the Aurora table. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/0f085a1b35cf0a5b5d7ede835781c39de70d9d3e3410721b30d0f8edf1d8b4a5.jpg)


Implementing the CQRS pattern with DynamoDB and Aurora provides these key benefits: 

• DynamoDB is a fully managed NoSQL database that can handle high-volume write operations, and Aurora ofers high read scalability for complex queries on the query side. 

• DynamoDB provides low-latency, high-throughput access to data, which makes it ideal for handling command and update operations, and Aurora performance can be fine-tuned and optimized for complex queries. 

• Both DynamoDB and Aurora ofer serverless options, which enables your business to pay for resources based on usage only. 

• DynamoDB and Aurora are fully managed services, which reduces the operational burden of managing databases, backups and scalability. 

You should consider using the CQRS pattern if: 

• You implemented the database-per-service pattern and want to join data from multiple microservices. 

• Your read and write workloads have separate requirements for scaling, latency, and consistency. 

• Eventual consistency is acceptable for the read queries. 

## Important

The CQRS pattern typically results in eventual consistency between the data stores. 

## Event sourcing pattern

The event sourcing pattern is typically used with the CQRS pattern to decouple read from write workloads, and optimize for performance, scalability, and security. Data is stored as a series of events, instead of direct updates to data stores. Microservices replay events from an event store to compute the appropriate state of their own data stores. The pattern provides visibility for the current state of the application and additional context for how the application arrived at that state. The event sourcing pattern works efectively with the CQRS pattern because data can be reproduced for a specific event, even if the command and query data stores have diferent schemas. 

By choosing this pattern, you can identify and reconstruct the application's state for any point in time. This produces a persistent audit trail and makes debugging easier. However, data becomes eventually consistent and this might not be appropriate for some use cases. 

This pattern can be implemented by using either Amazon Kinesis Data Streams or Amazon EventBridge. 

## Amazon Kinesis Data Streams implementation

In the following illustration, Kinesis Data Streams is the main component of a centralized event store. The event store captures application changes as events and persists them on Amazon Simple Storage Service (Amazon S3). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/cda4510d5f3ca58bae07e37701738c082c9e82a1112e7f1a476afaa87ea34cf8.jpg)


The workflow consists of the following steps: 

1. When the "/withdraw" or "/credit" microservices experience an event state change, they publish an event by writing a message into Kinesis Data Streams. 

2. Other microservices, such as "/balance" or "/creditLimit," read a copy of the message, filter it for relevance, and forward it for further processing. 

## Amazon EventBridge implementation

The architecture in the following illustration uses EventBridge. EventBridge is a serverless service that uses events to connect application components, which makes it easier for you to build scalable, event-driven applications. Event-driven architecture is a style of building loosely coupled software systems that work together by emitting and responding to events. EventBridge provides a default event bus for events that are published by AWS services, and you can also create a custom event bus for domain-specific buses. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/86458c08af1e6624a5964cd08b19f025cfd691f354a2f40160b4c0d604fd7ede.jpg)


The workflow consists of the following steps: 

1. "OrderPlaced" events are published by the "Orders" microservice to the custom event bus. 

2. Microservices that need to take action after an order is placed, such as the "/route" microservice, are initiated by rules and targets. 

3. These microservices generate a route to ship the order to the customer and emit a "RouteCreated" event. 

4. Microservices that need to take further action are also initiated by the "RouteCreated" event. 

5. Events are sent to an event archive (for example, EventBridge archive) so that they can be replayed for reprocessing, if required. 

6. Historical order events are sent to a new Amazon Simple Queue Service (Amazon SQS) queue (replay queue) for reprocessing, if required. 

7. If targets are not initiated, the afected events are placed in a dead letter queue (DLQ) for further analysis and reprocessing. 

You should consider using this pattern if: 

• Events are used to completely rebuild the application's state. 

• You require events to be replayed in the system and that an application's state can be determined at any point in time. 

• You want to be able to reverse specific events without having to start with a blank application state. 

• Your system requires a stream of events that can easily be serialized to create an automated log. 

• Your system requires heavy read operations but is light on write operations; heavy read operations can be directed to an in-memory database, which is kept updated with the events stream. 

Important: If you use the event sourcing pattern, you must deploy the Saga pattern to maintain data consistency across microservices. 

## Saga pattern

The saga pattern is a failure management pattern that helps establish consistency in distributed applications, and coordinates transactions between multiple microservices to maintain data consistency. A microservice publishes an event for every transaction, and the next transaction is initiated based on the event's outcome. It can take two diferent paths, depending on the success or failure of the transactions. 

The following illustration shows how the saga pattern implements an order processing system by using AWS Step Functions. Each step (for example, "ProcessPayment") also has separate steps to handle the success (for example, "UpdateCustomerAccount") or failure (for example, "Cancel Order") of the process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/1cb7b5aa62b28356c08f829ade5f01cbc434f81852401d066d6668d2e8ffcdb1.jpg)


You should consider using this pattern if: 

• The application needs to maintain data consistency across multiple microservices without tight coupling. 

• There are long-lived transactions and you don't want other microservices to be blocked if one microservice runs for a long time. 

• You need to be able to roll back if an operation fails in the sequence. 

## Important

The saga pattern is dificult to debug and its complexity increases with the number of microservices. The pattern requires a complex programming model that develops and designs compensating transactions for rolling back and undoing changes. 

## Shared-database-per-service pattern

In the shared-database-per-service pattern, the same database is shared by several microservices. You need to carefully assess the application architecture before adopting this pattern, and make sure that you avoid hot tables (single tables that multiple microservices write to). All your database changes must also be backward-compatible; for example, developers can drop columns or tables only if objects are not referenced by the current and previous versions of all microservices. 

In the following illustration, an insurance database is shared by all the microservices and an IAM policy provides access to the database. This creates development time coupling; for example, a change in the "Sales" microservice needs to coordinate schema changes with the "Customer" microservice. This pattern does not reduce dependencies between development teams, and introduces runtime coupling because all microservices share the same database. For example, long-running "Sales" transactions can lock the "Customer" table and this blocks the "Customer" transactions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-25/e8b57041-32e0-4914-b0f5-53dcff131628/b4c27b12dec9566d510c0a533f837cb8fbdc69387ac52f727a1062209155067c.jpg)


You should consider using this pattern if: 

• You don't want too much refactoring of your existing code base. 

• You enforce data consistency by using transactions that provide atomicity, consistency, isolation, and durability (ACID). 

• You want to maintain and operate only one database. 

• Implementing the database-per-service pattern is dificult because of interdependencies among your existing microservices. 

• You don't want to completely redesign your existing data layer. 

## FAQ

# When can I modernize my monolithic database as part of my modernization journey?

You should focus on modernizing your monolithic database when you begin to decompose monolithic applications into microservices. Make sure that you create a strategy to split your database into multiple small databases that are aligned with your applications. 

## Can I keep a legacy monolithic database for multiple microservices?

Keeping a shared monolithic database for multiple microservices creates tight coupling, which means you can't independently deploy changes to your microservices, and that all schema changes must be coordinated among your microservices. Although you can use a relational data store as your monolithic database, NoSQL databases might be a better choice for some of your microservices. 

## What should I consider when designing databases for a microservices architecture?

You should design your application based on domains that align with your application's functionality. Make sure that you evaluate the application's functionality and decide if it requires a relational database schema. You should also consider using a NoSQL database, if it fits your requirements. 

## What is a common pattern for maintaining data consistency across diferent microservices?

The most common pattern is using an event-driven architecture. 

## How do I maintain transaction automation?

In a microservices architecture, a transaction consists of multiple local transactions handled by diferent microservices. If a local transaction fails, you need to roll back the successful transactions that were previously completed. You can use the saga pattern to avoid this. 

## Do I have to use a separate database for each microservice?

The main advantage of a microservices architecture is loose coupling. Each microservice's persistent data must be kept private and accessible only through a microservice's API. Changes to the data schema must be carefully evaluated if your microservices share the same database. 

## How can I keep a microservice's persistent data private if they all share a single database?

If your microservices share a relational database, make sure that you have private tables for each microservice. You can also create individual schemas that are private to the individual microservices. 

## Resources

## Related guides

• Phased approach to modernizing applications in the AWS Cloud 

• Evaluating modernization readiness for applications in the AWS Cloud 

Decomposing monoliths into microservices 

• Integrating microservices by using AWS serverless services 

## Other resources

Application modernization with AWS 

• Build highly available microservices to power applications of any size and scale 

• Cloud-native application modernization with AWS 

• Cost optimization and innovation: An introduction to application modernization 

• Developer guide: Scale with microservices 

Distributed data management - Saga Pattern 

Implementing microservice architectures using AWS services: Command query responsibility segregation pattern 

• Implementing microservice architectures using AWS services: Event sourcing pattern 

• Modern applications: Creating value through application design 

• Modernize your applications, drive growth and reduce TCO 

## Document history

The following table describes significant changes to this guide. 

<table><tr><td>Change</td><td>Description</td><td>Date</td></tr><tr><td>Clarifications</td><td>We clarified some of the information for thedatabase-per-serviceandshared-database-per-servicepatterns.</td><td>April 7, 2025</td></tr><tr><td>Updated pattern</td><td>We updated theAmazon EventBridge implementationsection of the event sourcing pattern.</td><td>December 4, 2023</td></tr><tr><td>Expanded section</td><td>We updated theCQRSpatternwith more information.</td><td>November 17, 2023</td></tr><tr><td>Added a link for implementing the saga pattern with Step Functions</td><td>We updated the introduction andSaga patternsections with the link to the patternImplement the serverless saga pattern by using AWSStep Functionsfrom the AWSPrescriptive Guidance website.</td><td>February 23, 2021</td></tr></table>