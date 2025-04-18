# Primary-Backup Replication System: Student Assignment

## Assignment Overview

In this assignment, you will explore the concepts of primary-backup replication by using an existing distributed key-value store implementation. This assignment will help you understand fundamental concepts in distributed systems including:

- Fault tolerance through replication
- Consistency in distributed data stores
- Leader election via heartbeat mechanisms
- Failure detection and recovery

## Learning Objectives

By completing this assignment, you will be able to:

1. Explain the primary-backup replication pattern and its purpose in distributed systems
2. Set up and run a multi-component distributed system
3. Observe and analyze system behavior under normal and failure conditions
4. Evaluate trade-offs in distributed system design
5. Document and report on findings in a technical context

## Repository Access

To get started with this assignment, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/darshjoshi/primary-backup-replication.git
   cd primary-backup-replication
   ```

2. **Explore the codebase:**
   - Examine each of the Python files to understand the system architecture
   - Review the main README.md for technical documentation

## Assignment Tasks

### Part 1: Setup and Basic Operation

1. Follow the instructions in the README.md to set up and run the system
2. Perform basic GET and SET operations using the client
3. Verify that data is being replicated to the backup server
4. Document your steps and observations

### Part 2: Failure Scenario Testing

1. **Backup Server Failure:**
   - Set some key-value pairs
   - Stop the backup server
   - Perform additional operations with the client
   - Document how the primary server behaves
   - Restart the backup server and observe what happens

2. **Primary Server Failure:**
   - Set some key-value pairs
   - Stop the primary server
   - Observe how the backup server behaves (promotion)
   - Try to perform operations with the client after promotion
   - Document your observations

3. **Sequential Failures:**
   - Design and execute at least one additional failure scenario of your choice
   - Document the system behavior

### Part 3: Analysis and Recommendations

1. Analyze the system's strengths and limitations
2. Identify at least two potential improvements to the system
3. Consider how this approach compares to other replication strategies you've studied

## Submission Requirements

Your final submission should be a comprehensive report in either Markdown or PDF format containing:

### 1. Introduction (15%)
- Brief explanation of primary-backup replication
- Why it's important in distributed systems
- Your understanding of the implementation's architecture

### 2. Environment and Setup (10%)
- Your operating system and Python version
- Any modifications you made to the configuration
- Step-by-step setup process with screenshots

### 3. Basic Operation (15%)
- Description of the key-value operations you performed
- Evidence of successful operations (logs, command outputs)
- Verification of replication (with evidence)

### 4. Failure Scenarios (25%)
- Detailed description of each failure scenario you tested
- Complete logs and observations for each scenario
- Analysis of how the system behaved in each case

### 5. System Analysis (20%)
- Evaluation of system consistency guarantees
- Performance implications of the replication strategy
- Security considerations
- Limitations of the implementation

### 6. Recommendations (15%)
- At least two specific, technical improvements
- Justification for each improvement
- How these improvements would address identified limitations

### 7. Conclusion and References (10%)
- Summary of key findings
- References to relevant academic papers or documentation

## Submission Instructions

1. Submit your report (PDF or Markdown) via the course portal
2. Include any additional script files you created for testing
3. Provide links to any forks or modifications you made to the original repository

## Grading Criteria

Your assignment will be graded based on:

- **Accuracy**: Correct understanding and reporting of system behavior
- **Completeness**: Thorough testing of all required scenarios
- **Analysis**: Depth of insight into system design and limitations
- **Clarity**: Well-organized documentation with appropriate evidence
- **Creativity**: Innovation in testing and recommendations

## Academic Integrity

This is an individual assignment. While you may discuss general concepts with others, your submitted work must be your own individual effort. Proper citation is required for any external resources used.

## Resources

- [Original Repository](https://github.com/darshjoshi/primary-backup-replication)
- Distributed Systems: Principles and Paradigms by Tanenbaum
- MIT 6.824 Distributed Systems course materials

## Due Date

Please submit your completed assignment by [INSTRUCTOR TO INSERT DATE].

---

*If you have any questions about this assignment, please contact your instructor.*
