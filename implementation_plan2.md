# Goal Description
The objective is to create a new module for the Admin to manage End Customers (`Clientes`) and their Direct Sales ([Vendas](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/models.py#13-24)), as defined in the `cliente` app models. The user requested two specific templates: one for visualization (listing) and one for inclusion (creation).

## Proposed Changes

### 1. Backend Logic ([cliente/views.py](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/views.py) & `cliente/urls.py`)
- **URLs**: We will create [urls.py](file:///c:/Users/Caio/Documents/BrilhaMais/app/urls.py) inside the `cliente` app and link it to the main [app/urls.py](file:///c:/Users/Caio/Documents/BrilhaMais/app/urls.py).
- **Views**:
  - `ClienteListView`: A view to fetch and display all clients and their respective sales.
  - `ClienteCreateView` & `VendaCreateView`: A combined or dedicated view to handle the creation of new clients and the registration of their purchases.

### 2. Frontend Templates (`cliente/templates/cliente/`)
We will create exactly 2 templates following the new Premium Vanilla CSS design system (extending [base.html](file:///c:/Users/Caio/Documents/BrilhaMais/app/templates/base.html) and using [premium.css](file:///c:/Users/Caio/Documents/BrilhaMais/app/static/css/premium.css)).

#### [NEW] `cliente_list.html`(file:///c:/Users/Caio/Documents/BrilhaMais/cliente/templates/cliente/cliente_list.html)
- **Purpose**: "Visualizar" - A dashboard/list view for the admin to see all registered end-customers, their contact info, and their purchase history (Vendas).
- **Features**: A premium table (`.table-responsive`) and a button to add new clients/sales.

#### [NEW] `cliente_form.html`(file:///c:/Users/Caio/Documents/BrilhaMais/cliente/templates/cliente/cliente_form.html)
- **Purpose**: "Incluir" - A form template for the admin to register a new [Cliente](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/models.py#6-12) or record a new [Venda](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/models.py#13-24) (Sale) to an existing client.
- **Features**: A `glass-card` form with `form-group` styles, fully responsive.

## Verification Plan

### Manual Verification
1. Open the Django development server.
2. Navigate to the new `/clientes/` route.
3. Verify that the list renders correctly according to the premium design.
4. Test the creation flow by adding a dummy client and a dummy sale.
5. Check if the backend correctly links the [Venda](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/models.py#13-24) to the [Cliente](file:///c:/Users/Caio/Documents/BrilhaMais/cliente/models.py#6-12) and `Produto` via Foreign Keys.
