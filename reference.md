# Reference
## AppCategories
<details><summary><code>client.app_categories.<a href="src/pipedream/app_categories/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.apps.list()
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.accounts.list(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The app slug or ID to filter accounts by.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.create(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**app_id:** `typing.Optional[str]` — The app slug or ID to filter accounts by.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.retrieve(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.delete(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.accounts.delete_by_app(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.delete_external_user(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

## Components
<details><summary><code>client.components.<a href="src/pipedream/components/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.components.list(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.retrieve(
    project_id="project_id",
    component_id="component_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.configure_prop(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**configure_prop_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Previous context for pagination
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.components.reload_props(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**reload_props_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.actions.list(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.retrieve(
    project_id="project_id",
    component_id="component_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.configure_prop(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**configure_prop_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Previous context for pagination
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.reload_props(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**reload_props_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.run(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the action
    
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

## Triggers
<details><summary><code>client.triggers.<a href="src/pipedream/triggers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.triggers.list(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.retrieve(
    project_id="project_id",
    component_id="component_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

<dl>
<dd>

**component_id:** `str` — The key that uniquely identifies the component (e.g., 'slack-send-message')
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.configure_prop(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**configure_prop_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**prev_context:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Previous context for pagination
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.reload_props(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**async_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocking:** `typing.Optional[bool]` — Whether this operation should block until completion
    
</dd>
</dl>

<dl>
<dd>

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the component
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**reload_props_opts_async_handle:** `typing.Optional[str]` — Handle for async operations
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.triggers.deploy(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the trigger
    
</dd>
</dl>

<dl>
<dd>

**dynamic_props_id:** `typing.Optional[str]` — The ID for dynamic props
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Optional webhook URL to receive trigger events
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.deployed_triggers.list(
    project_id="project_id",
    external_user_id="external_user_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.retrieve(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**configured_props:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The configured properties for the trigger
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the trigger
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.delete(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_events(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_workflows(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update_workflows(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.list_webhooks(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.deployed_triggers.update_webhooks(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

## Projects
<details><summary><code>client.projects.<a href="src/pipedream/projects/client.py">retrieve_info</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.projects.retrieve_info(
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
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

## Proxy
<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.get(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.post(
    project_id="project_id",
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"key": "value"},
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
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

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.put(
    project_id="project_id",
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"key": "value"},
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
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

<details><summary><code>client.proxy.<a href="src/pipedream/proxy/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.delete(
    project_id="project_id",
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.proxy.patch(
    project_id="project_id",
    url_64="url_64",
    external_user_id="external_user_id",
    account_id="account_id",
    request={"key": "value"},
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

**project_id:** `str` — The project ID, which starts with 'proj_'.
    
</dd>
</dl>

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

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
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

## Tokens
<details><summary><code>client.tokens.<a href="src/pipedream/tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tokens.create(
    external_user_id="external_user_id",
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

**external_user_id:** `str` — Your end user ID, for whom you're creating the token
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — The ID of the project
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tokens.validate(
    ctok="ctok",
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

**ctok:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[ValidateTokenParams]` 
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pipedream import Pipedream

client = Pipedream(
    pd_environment="YOUR_PD_ENVIRONMENT",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

