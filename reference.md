# Reference
## AppCategories
<details><summary><code>client.app_categories.<a href="src/pipedream/app_categories/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all available categories for integrated apps
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_categories.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_categories.<a href="src/pipedream/app_categories/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific app category by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_categories.retrieve(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the app category to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Apps
<details><summary><code>client.apps.<a href="src/pipedream/apps/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all available apps with optional filtering and sorting
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.apps.list(
    after="after",
    before="before",
    limit=1,
    q="q",
    sort_key="name",
    sort_direction="asc",
    has_components=True,
    has_actions=True,
    has_triggers=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A search query to filter the apps
    
</dd>
</dl>

<dl>
<dd>

**sort_key:** `typing.Optional[AppsListRequestSortKey]` — The key to sort the apps by
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[AppsListRequestSortDirection]` — The direction to sort the apps
    
</dd>
</dl>

<dl>
<dd>

**category_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Only return apps in these categories
    
</dd>
</dl>

<dl>
<dd>

**has_components:** `typing.Optional[bool]` — Only return apps that have components (actions or triggers)
    
</dd>
</dl>

<dl>
<dd>

**has_actions:** `typing.Optional[bool]` — Only return apps that have actions
    
</dd>
</dl>

<dl>
<dd>

**has_triggers:** `typing.Optional[bool]` — Only return apps that have triggers
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/pipedream/apps/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific app by ID or name slug
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.apps.retrieve(
    app_id="app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — The name slug or ID of the app (e.g., 'slack', 'github')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounts
<details><summary><code>client.accounts.<a href="src/pipedream/accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all connected accounts for the project with optional filtering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.accounts.list(
    external_user_id="external_user_id",
    oauth_app_id="oauth_app_id",
    after="after",
    before="before",
    limit=1,
    app="app",
    include_credentials=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_app_id:** `typing.Optional[str]` — The OAuth app ID to filter by, if applicable
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**app:** `typing.Optional[str]` — The app slug or ID to filter accounts by.
    
</dd>
</dl>

<dl>
<dd>

**include_credentials:** `typing.Optional[bool]` — Whether to retrieve the account's credentials or not
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/pipedream/accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect a new account for an external user in the project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.create(
    external_user_id="external_user_id",
    oauth_app_id="oauth_app_id",
    app_slug="app_slug",
    cfmap_json="cfmap_json",
    connect_token="connect_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_slug:** `str` — The app slug for the account
    
</dd>
</dl>

<dl>
<dd>

**cfmap_json:** `str` — JSON string containing the custom fields mapping
    
</dd>
</dl>

<dl>
<dd>

**connect_token:** `str` — The connect token for authentication
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_app_id:** `typing.Optional[str]` — The OAuth app ID to filter by, if applicable
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional name for the account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/pipedream/accounts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details for a specific connected account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.retrieve(
    account_id="account_id",
    include_credentials=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_credentials:** `typing.Optional[bool]` — Whether to retrieve the account's credentials or not
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/pipedream/accounts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a connected account and its associated credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.delete(
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/pipedream/accounts/client.py">delete_by_app</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove all connected accounts for a specific app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.delete_by_app(
    app_id="app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/pipedream/users/client.py">delete_external_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an external user and all their associated accounts and resources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.delete_external_user(
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/pipedream/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all external users for the project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.users.list(
    after="after",
    before="before",
    limit=1,
    q="q",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Filter users by external_id (partial match)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Components
<details><summary><code>client.components.<a href="src/pipedream/components/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve available components with optional search and app filtering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.components.list(
    after="after",
    before="before",
    limit=1,
    q="q",
    app="app",
    registry="public",
    component_type="trigger",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A search query to filter the components
    
</dd>
</dl>

<dl>
<dd>

**app:** `typing.Optional[str]` — The ID or name slug of the app to filter the components
    
</dd>
</dl>

<dl>
<dd>

**registry:** `typing.Optional[ComponentsListRequestRegistry]` — The registry to retrieve components from. Defaults to 'all' ('public', 'private', or 'all')
    
</dd>
</dl>

<dl>
<dd>

**component_type:** `typing.Optional[ComponentType]` — The type of the component to filter the components
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/pipedream/components/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed configuration for a specific component by its key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.retrieve(
    component_id="component_id",
    version="1.2.3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional semantic version of the component to retrieve (for example '1.0.0')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/pipedream/components/client.py">configure_prop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve remote options for a given prop for a component
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.configure_prop(
    id="id",
    external_user_id="external_user_id",
    prop_name="prop_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**prop_name:** `str` — The name of the prop to configure
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Previous context for pagination
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query for filtering options
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.components.<a href="src/pipedream/components/client.py">reload_props</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reload the prop definition based on the currently configured props
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.reload_props(
    id="id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions
<details><summary><code>client.actions.<a href="src/pipedream/actions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve available actions with optional search and app filtering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.actions.list(
    after="after",
    before="before",
    limit=1,
    q="q",
    app="app",
    registry="public",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A search query to filter the actions
    
</dd>
</dl>

<dl>
<dd>

**app:** `typing.Optional[str]` — The ID or name slug of the app to filter the actions
    
</dd>
</dl>

<dl>
<dd>

**registry:** `typing.Optional[ActionsListRequestRegistry]` — The registry to retrieve actions from. Defaults to 'all' ('public', 'private', or 'all')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/pipedream/actions/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed configuration for a specific action by its key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.retrieve(
    component_id="component_id",
    version="1.2.3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional semantic version of the component to retrieve (for example '1.0.0')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/pipedream/actions/client.py">configure_prop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve remote options for a given prop for a action
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.configure_prop(
    id="id",
    external_user_id="external_user_id",
    prop_name="prop_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**prop_name:** `str` — The name of the prop to configure
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Previous context for pagination
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query for filtering options
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/pipedream/actions/client.py">reload_props</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reload the prop definition based on the currently configured props
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.reload_props(
    id="id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/pipedream/actions/client.py">run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute an action with the provided configuration and return results
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.run(
    id="id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The action component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional action component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**stash_id:** `typing.Optional[RunActionOptsStashId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Triggers
<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve available triggers with optional search and app filtering
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.triggers.list(
    after="after",
    before="before",
    limit=1,
    q="q",
    app="app",
    registry="public",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A search query to filter the triggers
    
</dd>
</dl>

<dl>
<dd>

**app:** `typing.Optional[str]` — The ID or name slug of the app to filter the triggers
    
</dd>
</dl>

<dl>
<dd>

**registry:** `typing.Optional[TriggersListRequestRegistry]` — The registry to retrieve triggers from. Defaults to 'all' ('public', 'private', or 'all')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed configuration for a specific trigger by its key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.retrieve(
    component_id="component_id",
    version="1.2.3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional semantic version of the component to retrieve (for example '1.0.0')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">configure_prop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve remote options for a given prop for a trigger
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.configure_prop(
    id="id",
    external_user_id="external_user_id",
    prop_name="prop_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**prop_name:** `str` — The name of the prop to configure
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Previous context for pagination
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query for filtering options
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">reload_props</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reload the prop definition based on the currently configured props
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.reload_props(
    id="id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">deploy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy a trigger to listen for and emit events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.deploy(
    id="id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The trigger component ID
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional trigger component version (in SemVer format, for example '1.0.0'), defaults to latest
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` — Optional ID of a workflow to receive trigger events
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Optional webhook URL to receive trigger events
    
</dd>
</dl>

<dl>
<dd>

**emit_on_deploy:** `typing.Optional[bool]` — Whether the trigger should emit events during the deploy hook execution. Defaults to true if not specified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DeployedTriggers
<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all deployed triggers for a specific external user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.deployed_triggers.list(
    after="after",
    before="before",
    limit=1,
    external_user_id="external_user_id",
    emitter_type="email",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_user_id:** `str` — Your end user ID, for whom you deployed the trigger
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**emitter_type:** `typing.Optional[EmitterType]` — Filter deployed triggers by emitter type (defaults to 'source' if not provided)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific deployed trigger by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.retrieve(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — Your end user ID, for whom you deployed the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the configuration of a deployed trigger, including active status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the trigger should be active
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[ConfiguredProps]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the trigger
    
</dd>
</dl>

<dl>
<dd>

**emit_on_deploy:** `typing.Optional[bool]` — Whether the trigger should emit events during deployment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a deployed trigger and stop receiving events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.delete(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
    ignore_hook_errors=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**ignore_hook_errors:** `typing.Optional[bool]` — Whether to ignore errors during deactivation hook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">list_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve recent events emitted by a deployed trigger
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_events(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
    n=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — Your end user ID, for whom you deployed the trigger
    
</dd>
</dl>

<dl>
<dd>

**n:** `typing.Optional[int]` — The number of events to retrieve (defaults to 20 if not provided)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">list_workflows</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get workflows connected to receive events from this trigger
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_workflows(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">update_workflows</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect or disconnect workflows to receive trigger events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update_workflows(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
    workflow_ids=["workflow_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**workflow_ids:** `typing.Sequence[str]` — Array of workflow IDs to set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">list_webhooks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get webhook URLs configured to receive trigger events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_webhooks(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">update_webhooks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure webhook URLs to receive trigger events. `signing_key` is only returned for OAuth-authenticated requests.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update_webhooks(
    trigger_id="trigger_id",
    external_user_id="external_user_id",
    webhook_urls=["webhook_urls"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**webhook_urls:** `typing.Sequence[str]` — Array of webhook URLs to set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">retrieve_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific webhook for a deployed trigger, including its signing key
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.retrieve_webhook(
    trigger_id="trigger_id",
    webhook_id="webhook_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deployed_triggers.<a href="src/pipedream/deployed_triggers/client.py">regenerate_webhook_signing_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate the signing key for a specific webhook on a deployed trigger
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.regenerate_webhook_signing_key(
    trigger_id="trigger_id",
    webhook_id="webhook_id",
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID who owns the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProjectEnvironment
<details><summary><code>client.project_environment.<a href="src/pipedream/project_environment/client.py">retrieve_webhook</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the webhook configured for a project environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project_environment.retrieve_webhook()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_environment.<a href="src/pipedream/project_environment/client.py">update_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the webhook URL for a project environment. Creating a webhook returns `signing_key`; updating an existing webhook does not.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project_environment.update_webhook(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — The webhook URL to set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_environment.<a href="src/pipedream/project_environment/client.py">delete_webhook</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the webhook configured for a project environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project_environment.delete_webhook()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_environment.<a href="src/pipedream/project_environment/client.py">regenerate_webhook_signing_key</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate the signing key for the project environment webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project_environment.regenerate_webhook_signing_key()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the projects that are available to the authenticated Connect client
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.projects.list(
    after="after",
    before="before",
    limit=1,
    q="q",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — The cursor to start from for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — The cursor to end before for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A search query to filter the projects
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project for the authenticated workspace
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the project
    
</dd>
</dl>

<dl>
<dd>

**app_name:** `typing.Optional[str]` — Display name for the Connect application
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — Support email displayed to end users
    
</dd>
</dl>

<dl>
<dd>

**connect_require_key_auth_test:** `typing.Optional[bool]` — Send a test request to the upstream API when adding Connect accounts for key-based apps
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the project details for a specific project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.retrieve(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project ID, which starts with `proj_`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project owned by the authenticated workspace
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.delete(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project ID, which starts with `proj_`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update project details or application information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.update(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project ID, which starts with `proj_`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the project
    
</dd>
</dl>

<dl>
<dd>

**app_name:** `typing.Optional[str]` — Display name for the Connect application
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — Support email displayed to end users
    
</dd>
</dl>

<dl>
<dd>

**connect_require_key_auth_test:** `typing.Optional[bool]` — Send a test request to the upstream API when adding Connect accounts for key-based apps
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">update_logo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload or replace the project logo
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.update_logo(
    project_id="project_id",
    logo="data:image/png;base64,AAAAAA...",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The project ID, which starts with `proj_`.
    
</dd>
</dl>

<dl>
<dd>

**logo:** `str` — Data URI containing the new Base64 encoded image
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">retrieve_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve project configuration and environment details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.retrieve_info()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FileStash
<details><summary><code>client.file_stash.<a href="src/pipedream/file_stash/client.py">download_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a file from File Stash
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.file_stash.download_file(
    s_3_key="s3_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**s_3_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxy
<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward an authenticated GET request to an external API using an external user's account credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.get(
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url_64:** `str` — Base64-encoded target URL
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID for the proxy request
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The account ID to use for authentication
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward an authenticated POST request to an external API using an external user's account credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.post(
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"string": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url_64:** `str` — Base64-encoded target URL
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID for the proxy request
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The account ID to use for authentication
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward an authenticated PUT request to an external API using an external user's account credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.put(
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"string": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url_64:** `str` — Base64-encoded target URL
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID for the proxy request
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The account ID to use for authentication
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward an authenticated DELETE request to an external API using an external user's account credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.delete(
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url_64:** `str` — Base64-encoded target URL
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID for the proxy request
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The account ID to use for authentication
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward an authenticated PATCH request to an external API using an external user's account credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.patch(
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"string": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url_64:** `str` — Base64-encoded target URL
    
</dd>
</dl>

<dl>
<dd>

**external_user_id:** `str` — The external user ID for the proxy request
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — The account ID to use for authentication
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/pipedream/tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a Connect token to use for client-side authentication
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tokens.create(
    external_user_id="external_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_user_id:** `str` — Your end user ID, for whom you're creating the token
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[typing.Sequence[str]]` — List of allowed origins for CORS
    
</dd>
</dl>

<dl>
<dd>

**error_redirect_uri:** `typing.Optional[str]` — URI to redirect to on error
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[int]` — Token TTL in seconds (max 14400 = 4 hours). Defaults to 4 hours if not specified.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Space-separated scopes to restrict token permissions. Defaults to 'connect:*' if not specified. See https://pipedream.com/docs/connect/api-reference/authentication#connect-token-scopes for more information.
    
</dd>
</dl>

<dl>
<dd>

**success_redirect_uri:** `typing.Optional[str]` — URI to redirect to on success
    
</dd>
</dl>

<dl>
<dd>

**webhook_uri:** `typing.Optional[str]` — Webhook URI for notifications
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/pipedream/tokens/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirm the validity of a Connect token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tokens.validate(
    ctok="ctok",
    app_id="app_id",
    oauth_app_id="oauth_app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ctok:** `ConnectToken` 
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` — The app ID to validate against
    
</dd>
</dl>

<dl>
<dd>

**oauth_app_id:** `typing.Optional[str]` — The OAuth app ID to validate against (if the token is for an OAuth app)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/pipedream/usage/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve Connect usage records for a time window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.usage.list(
    start_ts=1,
    end_ts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_ts:** `int` — Usage window start timestamp (seconds)
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `int` — Usage window end timestamp (seconds)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OauthTokens
<details><summary><code>client.oauth_tokens.<a href="src/pipedream/oauth_tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange OAuth credentials for an access token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.oauth_tokens.create(
    client_id="client_id",
    client_secret="client_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Optional space-separated scopes for the access token. Defaults to `*`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

