
Group
    az webapp : Manage web apps.

Subgroups:
    auth                        : Manage webapp authentication and authorization.
    config                      : Configure a web app.
    cors                        : Manage Cross-Origin Resource Sharing (CORS).
    deleted           [Preview] : Manage deleted web apps.
    deployment                  : Manage web app deployments.
    hybrid-connection [Preview] : Methods that list, add and remove hybrid-connections
                                  from webapps.
    identity                    : Manage web app's managed service identity.
    log                         : Manage web app logs.
    traffic-routing             : Manage traffic routing for web apps.
    vnet-integration  [Preview] : Methods that list, add, and remove virtual network
                                  integrations from a webapp.
    webjob                      : Allows management operations for webjobs on a web app.

Commands:
    browse                      : Open a web app in a browser.
    create                      : Create a web app.
    create-remote-connection    : Creates a remote connection using a tcp tunnel to your web app.
    delete                      : Delete a web app.
    list                        : List web apps.
    list-runtimes               : List available built-in stacks which can be used for web apps.
    restart                     : Restart a web app.
    show                        : Get the details of a web app.
    ssh               [Preview] : SSH command establishes a ssh session to the web
                                  container and developer would get a shell terminal remotely.
    start                       : Start a web app.
    stop                        : Stop a web app.
    up                          : Create a webapp and deploy code from a local workspace to the app.
                                  The command is required to run from the folder where the code is
                                  present. Current support includes Node, Python, .NET Core and
                                  ASP.NET. Node, Python apps are created as Linux apps. .Net Core,
                                  ASP.NET, and static HTML apps are created as Windows apps. Append
                                  the html flag to deploy as a static HTML app.
    update                      : Update a web app.

Please let us know how we are doing: https://aka.ms/clihats
