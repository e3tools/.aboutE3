## Software Development Methodology

The following chapter describes our philosophy and approach to software development.
We outline the core principles that guide our work, emphasizing the importance of
usability.

Our methodology is designed to put our end users first, allowing a co-creation approach
with communities and policymakers. We also discuss how this approach fosters
innovation, collaboration, and continuous improvement within our development teams.

### Human-Centered Approach

Our development process begins with understanding the needs, motivations, and contexts of our users. We prioritize direct engagement with stakeholders through interviews, workshops, and iterative feedback cycles to ensure that the software we develop is meaningful and impactful. Prototypes and mockups are used early in the design phase to gather insights and adapt quickly to feedback.

This approach ensures that users are not passive recipients but active contributors, shaping tools that are intuitive, inclusive, and adaptable to real-world challenges.

### Lean Development

We follow lean development principles to maximize value and reduce waste. This means:

- Building the smallest, most valuable product possible (MVP) first.
- Iterating rapidly based on feedback.
- Avoiding over-engineering and focusing on what delivers measurable impact.

By working in short, focused development sprints and validating progress through user testing, we stay agile and responsive to change. Continuous integration, automated testing, and code reviews ensure a high standard of quality while enabling rapid delivery.

Our lean mindset helps us remain adaptable, efficient, and aligned with the evolving needs of our users.

---

## Contribution Guidelines

Teams are not only welcome but encouraged to propose new modules for the different
tools. The process for collaborating, which is a testament to our shared commitment to
innovation, is as follows:

1. The team must fork the main repository into their own GitHub account.
2. Create a feature branch for the new module using the following convention:
   `feature/new-module`
3. Develop the new module on the feature branch, ensuring to commit regularly. This
   practice is crucial for maintaining a clear and traceable development history.
4. Regularly synchronize the feature branch with the main repository to avoid conflicts.
5. Once the new module is developed and pushed into your feature branch, create a
   pull request from your fork into the main repository.
6. The e3 Tools maintainers team will review the pull request and, once approved,
   merge it into the `develop` branch.
7. Once the new module is tested on the `develop` branch, it will be merged into the
   `main` branch and released.

Please ensure that your contributions follow our [coding standards](./CODING_STANDARDS.md) and include:

- Adequate documentation
- Unit and integration tests
- A brief description of the module's purpose in the pull request

Together, we can build a flexible, powerful platform that evolves with the needs of our users and communities.
