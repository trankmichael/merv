# Management for Emergency Response Volunteers

##Django Apps: 
Tasks, Recommender, API, merv

**Tasks:** handles task creation, storage, updating, and deleting

  * ***Models*** 
   * Task
     * id : Task ID
     * collaborative : team collaboration skills necessary
     * language : foreign language experience needed
     * outdoor : task environment - indoor vs outdoor
     * transportation : transportation resources required
     * strength : corresponds to physical intensity of the given task
     * task_name : name of the task
     * task_description : description of task
     * timestamp : datetime of task creation
     * updated : datetime of last task update
  * ***Views***:
    * TaskCreate: view for creating a task
    * TaskUpdate: view for updating a task
    * TaskList: generate task recommendations for a User
    * TaskDetail: API endpoint for task CRUD
    * Generate: generate and populate the Task Model with randomized test values 
  * ***URLS***: /tasks/
    * create, tasklist, taskdetail/\<pk\>, /\<pk\>, rate/\<pk\>
    * <pk> : the primary key of each task
   
**Recommender:** handles user-task ratings, and recommendations
 * ***Models***
  * Rating
    * id: Rating ID
    * task: foreignkey corresponding to a task
    * user: foreignkey corresponding to a user
    * score: rating for the given task from the user
  * Recommendation
    * id: Recommendation ID
    * task: foreignkey corresponding to a task
    * user: foreignkey corresponding to a user
    * predicted_score: predicted rating for the given task for a user
  * CosineTaskSimilarity - used in content based filtering
    * id: Cosine similarity ID
    * user: foreignkey corresponding to a user
    * task: foreignkey corresponding to a task
    * similarity: cosine similarity between a task and a user

**Accounts**
 * ***Models***
  * User - extends AbstractBaseUser and PermissionsMixin
   * id: User ID
   * date_joined: DateTimeField of when the user registered
   * email: EmailField storing user email
   * first_name: CharField storing user's first name
   * last_name: CharField storing the user's last name
   * password: PBKDF2 encrypted password
  * ***Views***
   * userlist : generate a list of all users
   * UserDetail : get details of the current user

## API Endpoints
 * tasklist - returns the list of recommend tasks for the current user
 * taskdetail - returns the details of a specific task
 * userlist - returns a list of users
 * userdetail - returns the details of a user given their primary key
