Task1
Large social network needs a dashboard for real-time analytics, showing user engagement, trending topics, and advertising performance.
Currently, analytics data is processed t - 1 (nightly), causing delays in decision-making
Prepare system architecture providing near real-time processing, aggregation, and visualization of analytics data. 
Don't forget to describe data pipelines, stream processing frameworks, databases, and frontend visualization components

Task2
City's public transportation system experiences persistent inefficiencies, with overcrowded buses during peak hours and empty buses at off-peak times, causing dissatisfaction among passengers and poor utilization of resources.
Local administration is considering integrating **self-driving (autonomous) vehicles** into the existing public transit fleet to optimize resource allocation, reduce costs, and improve passenger experience
Design fleet management and optimization system that integrates self-driving buses into the city's existing transit infrastructure. Your solution should adjust vehicle allocation, routes, and scheduling (near real-time) based on demand, traffic conditions, and vehicle availability
P.S: remember about safety, clearly identify potential trade-offs and how your architecture resolve these challenges

Task3
Students worldwide struggle to discover international internship opportunities, while companies find it difficult to recruit globally due to complex hiring procedures, visas, and documentation requirements
Design global internship marketplace that matches international students with internship opportunities worldwide, handling application processes, document verification and compliance with international labor regulations

Task4
Your microservice API currently faces performance degradation during traffic spikes due to uncontrolled request bursts from clients
Implement a **rate-limiting mechanism** within your microservice to ensure API stability and consistent performance. Clearly describe your approach, chosen algorithms, and configurations in README. 
P.S: Send link to public repository with implementation, and description in README

Task5
Country aims to transition from paper to an online e-voting system for national elections
System must handle millions of simultaneous users, ensure anonymity, election transparency, security, and resilience against cyber-attacks
Design e-voting system architecture that meets these requirements
Outline your design choices and discuss (potential) trade-offs

Task6
During humanitarian crises, distributing aid (food, money, medical supplies) is chaotic and often leads to duplication, fraud, or missed recipients, especially where IDs are unavailable or unreliable
Coalition of non-governmental organizations and United Nation want to build digital system to manage and track aid distribution fairly and transparently, even in remote or offline regions
Design system that enables volunteers to register people using **biometrics or digital IDs**, track aid deliveries, and audit distribution fairness
Recipients should **own their data** and be able to **use their ID across aid programs**
P.S: offline design; think about synchronization; Explain how your architecture maintains trust without centralized control