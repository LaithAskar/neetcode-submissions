class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         # Map each course to the courses it requires
        prereqs = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            # Record this prerequisite
            prereqs[course].append(prerequisite)

        visiting = set()
        safe = set()

        def dfs(course):
            # Currently in this DFS chain → cycle
            if course in visiting:
                return False

            # Previously verified → no need to repeat work
            if course in safe:
                return True

            # Begin exploring this course
            visiting.add(course)

            for prerequisite in prereqs[course]:
                # Every prerequisite chain must be safe
                if not dfs(prerequisite):
                    return False

            # Move this course from visiting to safe
            visiting.remove(course)
            safe.add(course)

            return True

        # Every course must have a safe prerequisite chain
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
