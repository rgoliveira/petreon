# Petreon
![Petreon Logo](/assets/petreon.png)

This is a project that aids the creation of a platform for Non-Profit
Organizations that targets dog adoption/donation campaigns via a web interface.

## Development Guide on Windows

1. Install PHP into some folder and add that to your PATH (using the [x64 Thread Safe version](http://windows.php.net/download/))
2. Rename php.ini-development to php.ini in the PHP folder
3. Uncomment line 738 where it says `extension_dir = "ext"`
4. Uncomment line 907 where it says `extension=php_openssl.dll`
5. Install Composer (which has an [installer](https://getcomposer.org/download/))
6. Browse to /api
7. Run `composer install`
8. Run `composer start`
9. The server is running at http://localhost:8080

## Provided to you by the team number one
![Team One Flag](/assets/team_flag.png)
