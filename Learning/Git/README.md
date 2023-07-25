<!--ts-->

- [Handling Multiple Github Accounts on MacOS](#multiple-github-accounts-maco)
- [How to view git config file ](#view-config)

<!--te-->

<a name="multiple-github-accounts-macos"></a>

# Handling Multiple Github Accounts on MacOS

#### 1. Creating the SSH keys. For each SSH key pairs:

- run `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

- You'll be prompted: "Enter a file in which to save the key" and the suggested default filename would be `id_rsa`. This filename will be used for your SSH private and public keys so remember to make it unique, eg. `user-1`, `user-2`. This step will generate both the private and public keys, `user-1` + `user-1.pub` , `user-2` + `user-2.pub` respectively.

- [GitHub](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#generating-a-new-ssh-key) has this step in detail. We're not adding the keys to the ssh-agent.

#### 2. Register your keys to the respective GitHub accounts.

- Follow these [steps](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to do so.

#### 3. Head back over to the SSH `config` file at `~/.ssh` and amend accordingly to:

> ```bash
> #user1 account
> Host github.com-user1
>    HostName github.com
>    User git
>    IdentityFile ~/.ssh/github-user1
>    IdentitiesOnly yes
>
> #user2 account
> Host github.com-user2
>    HostName github.com
>    User git
>    IdentityFile ~/.ssh/github-user2
>    IdentitiesOnly yes
> ```
>
> Replace `user1` or `user2` with your GitHub usernames/identification-handlers

#### 4. Go ahead to git clone your respective repository

> ```
> git clone git@github.com-user1:user1/your-repo-name.git your-repo-name_user1
> ```

<a name="view-config"></a>

# How to view git config file

On Linux and MacOS

> ```
> cat ~/.gitconfig
> ```
