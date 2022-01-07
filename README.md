[comment]: # "Auto-generated SOAR connector documentation"
# Metadefender

Publisher: Splunk  
Connector Version: 2\.0\.3  
Product Vendor: OPSWAT  
Product Name: Metadefender  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app connects to OPSWAT Metadefender for performing investigative actions pertaining to reputation checking for ip and file

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Metadefender asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_key** |  required  | password | API key

### Supported Actions  
[ip reputation](#action-ip-reputation) - Gets information about an IP  
[file reputation](#action-file-reputation) - Gets information about a hash  
[test connectivity](#action-test-connectivity) - Validates the asset configuration for connectivity  

## action: 'ip reputation'
Gets information about an IP

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | IP address to query | string |  `ip` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.ip | string |  `ip` 
action\_result\.data\.\*\.address | string | 
action\_result\.data\.\*\.geo\_info\.city\.code | string | 
action\_result\.data\.\*\.geo\_info\.city\.name | string | 
action\_result\.data\.\*\.geo\_info\.continent\.code | string | 
action\_result\.data\.\*\.geo\_info\.continent\.name | string | 
action\_result\.data\.\*\.geo\_info\.country\.code | string | 
action\_result\.data\.\*\.geo\_info\.country\.name | string | 
action\_result\.data\.\*\.geo\_info\.location\.latitude | numeric | 
action\_result\.data\.\*\.geo\_info\.location\.longitude | numeric | 
action\_result\.data\.\*\.geo\_info\.registered\_country\.code | string | 
action\_result\.data\.\*\.geo\_info\.registered\_country\.name | string | 
action\_result\.data\.\*\.geo\_info\.subdivisions\.\*\.code | string | 
action\_result\.data\.\*\.geo\_info\.subdivisions\.\*\.name | string | 
action\_result\.data\.\*\.lookup\_results\.address | string |  `ip` 
action\_result\.data\.\*\.lookup\_results\.detected\_by | numeric | 
action\_result\.data\.\*\.lookup\_results\.sources\.\*\.assessment | string | 
action\_result\.data\.\*\.lookup\_results\.sources\.\*\.detect\_time | string | 
action\_result\.data\.\*\.lookup\_results\.sources\.\*\.provider | string | 
action\_result\.data\.\*\.lookup\_results\.sources\.\*\.status | numeric | 
action\_result\.data\.\*\.lookup\_results\.sources\.\*\.update\_time | string | 
action\_result\.data\.\*\.lookup\_results\.start\_time | string | 
action\_result\.summary\.detected\_by | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'file reputation'
Gets information about a hash

Type: **investigate**  
Read only: **True**

If additional\_info is checked, additional\_details will be populated with available data\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**hash** |  required  | Hash \(md5, sha1, sha256\) | string |  `hash`  `md5`  `sha1`  `sha256` 
**additional\_info** |  optional  | Fetch additional information about the file if available | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.additional\_info | boolean | 
action\_result\.parameter\.hash | string |  `hash`  `md5`  `sha1`  `sha256` 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.autoRemoveFromRecents | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.configChanges | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.excludeFromRecents | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.exported | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.finishOnTaskLaunch | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.hardwareAccelerated | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.icon | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.intentFilters\.\*\.actions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.intentFilters\.\*\.categories\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.intentFilters\.\*\.data\.\*\.scheme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.label | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.launchMode | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.multiprocess | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.noHistory | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.resizeableActivity | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.screenOrientation | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.taskAffinity | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.activities\.\*\.theme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.allowBackup | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.hardwareAccelerated | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.icon | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.label | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.largeHeap | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.excludeFromRecents | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.icon | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.intentFilters\.\*\.actions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.intentFilters\.\*\.categories\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.label | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.noHistory | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.launcherActivities\.\*\.theme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.providers\.\*\.authorities | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.providers\.\*\.exported | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.providers\.\*\.initOrder | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.providers\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.enabled | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.exported | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.intentFilters\.\*\.actions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.intentFilters\.\*\.categories\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.intentFilters\.\*\.data\.\*\.scheme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.label | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.metaData\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.metaData\.\*\.resource | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.permission | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.receivers\.\*\.process | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.enabled | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.exported | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.intentFilters\.\*\.actions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.intentFilters\.\*\.categories\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.intentFilters\.\*\.data\.\*\.scheme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.intentFilters\.\*\.priority | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.label | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.launchMode | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.metaData\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.metaData\.\*\.resource | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.metaData\.\*\.value | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.multiprocess | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.permission | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.persistent | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.services\.\*\.process | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.supportsRtl | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.theme | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.usesLibraries\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.application\.usesLibraries\.\*\.required | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.installLocation | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.instrumentation | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.package | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.permissions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.permissions\.\*\.protectionLevel | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.platformBuildVersionCode | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.platformBuildVersionName | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.anyDensity | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.largeScreens | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.normalScreens | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.resizeable | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.smallScreens | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.supportsScreens\.xlargeScreens | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesConfiguration | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesFeatures\.\*\.glEsVersion | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesFeatures\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesFeatures\.\*\.required | boolean | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesPermissions\.\*\.maxSdkVersion | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesPermissions\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesSdk\.minSdkVersion | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.usesSdk\.targetSdkVersion | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.versionCode | numeric | 
action\_result\.data\.\*\.additional\_details\.apk\-manifest\.versionName | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.categories\.\*\.category\_name | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.categories\.\*\.wa\_category\_id | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.computer\_type\_stats\.\*\.computer\_type | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.computer\_type\_stats\.\*\.computer\_type\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.computer\_type\_stats\.\*\.computer\_type\_rank\_over\_sha1 | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.device\_identity\_stats\.\*\.device\_identity\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.device\_identity\_stats\.\*\.device\_identity\_count\_rank\_over\_sha1 | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.device\_identity\_stats\.\*\.reported\_ts\_yyww | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.file\_name | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.file\_name\_lower | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.file\_property\_version | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.file\_property\_version\_norm | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.file\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_infos\.\*\.sha1 | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_path\_stats\.\*\.file\_path | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_path\_stats\.\*\.file\_path\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.file\_path\_stats\.\*\.file\_path\_rank\_over\_sha1 | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.loaded\_component\_stats\.\*\.loaded\_component | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.loaded\_component\_stats\.\*\.loaded\_component\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.arch | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.kernel\_version | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.language | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.os\_name | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.os\_name\_norm | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.os\_type | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.service\_pack | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.os\_infos\.\*\.wa\_os\_id | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_info\_stats\.\*\.product\_name\_norm | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_info\_stats\.\*\.product\_name\_norm\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_info\_stats\.\*\.product\_name\_norm\_rank\_over\_sha1 | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_info\_stats\.\*\.product\_version\_norm | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_infos\.\*\.product\_name | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_infos\.\*\.product\_version | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_infos\.\*\.wa\_product\_id | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.product\_infos\.\*\.wa\_signature\_id | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.source\_ip\_stats\.\*\.reported\_ts\_yyww | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.source\_ip\_stats\.\*\.source\_ip\_count | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.source\_ip\_stats\.\*\.source\_ip\_count\_rank\_over\_sha1 | numeric | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.vendor\_infos\.\*\.vendor\_name | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.appinfo\.\*\.vendor\_infos\.\*\.wa\_vendor\_id | string | 
action\_result\.data\.\*\.additional\_details\.appinfo\.source | string | 
action\_result\.data\.\*\.additional\_details\.exif\.BitDepth | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.ColorType | string | 
action\_result\.data\.\*\.additional\_details\.exif\.Compression | string | 
action\_result\.data\.\*\.additional\_details\.exif\.FileSize | string | 
action\_result\.data\.\*\.additional\_details\.exif\.FileType | string | 
action\_result\.data\.\*\.additional\_details\.exif\.FileTypeExtension | string | 
action\_result\.data\.\*\.additional\_details\.exif\.Filter | string | 
action\_result\.data\.\*\.additional\_details\.exif\.Gamma | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.ImageHeight | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.ImageSize | string | 
action\_result\.data\.\*\.additional\_details\.exif\.ImageWidth | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.Interlace | string | 
action\_result\.data\.\*\.additional\_details\.exif\.MIMEType | string | 
action\_result\.data\.\*\.additional\_details\.exif\.Megapixels | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.PixelUnits | string | 
action\_result\.data\.\*\.additional\_details\.exif\.PixelsPerUnitX | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.PixelsPerUnitY | numeric | 
action\_result\.data\.\*\.additional\_details\.exif\.SRGBRendering | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.compilation\_time | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.machine\_type | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.number\_of\_sections | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.number\_of\_symbols | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.optional\_header\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.headers\.pointer\_to\_symbol\_table | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.imphash | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.imported\_dlls\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.checksum | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.code\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.entry\_point | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.image\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.image\_version | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.initialized\_data\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.linker\_version | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.os\_version | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.pe\_type | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.subsystem | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.subsystem\_version | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.optional\_headers\.uninitialized\_data\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.pehash | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.entropy | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.md5 | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.name | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.number\_of\_linenumbers | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.number\_of\_relocations | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.pointer\_to\_linenumbers | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.pointer\_to\_raw\_data | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.pointer\_to\_relocations | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.raw\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.virtual\_address | string | 
action\_result\.data\.\*\.additional\_details\.peinfo\.section\_headers\.\*\.virtual\_size | numeric | 
action\_result\.data\.\*\.additional\_details\.peinfo\.signature\.parsing\_error | string | 
action\_result\.data\.\*\.appinfo | boolean | 
action\_result\.data\.\*\.data\_id | string | 
action\_result\.data\.\*\.extracted\_files\.data\_id | string | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.data\_id | string | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.detected\_by | numeric | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.display\_name | string | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.file\_size | numeric | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.file\_type | string | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.progress\_percentage | numeric | 
action\_result\.data\.\*\.extracted\_files\.files\_in\_archive\.\*\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.file\_id | string | 
action\_result\.data\.\*\.file\_info\.display\_name | string | 
action\_result\.data\.\*\.file\_info\.file\_size | numeric | 
action\_result\.data\.\*\.file\_info\.file\_type\_category | string | 
action\_result\.data\.\*\.file\_info\.file\_type\_description | string | 
action\_result\.data\.\*\.file\_info\.file\_type\_extension | string | 
action\_result\.data\.\*\.file\_info\.md5 | string |  `hash`  `md5` 
action\_result\.data\.\*\.file\_info\.sha1 | string |  `hash`  `sha1` 
action\_result\.data\.\*\.file\_info\.sha256 | string |  `hash`  `sha256` 
action\_result\.data\.\*\.file\_info\.upload\_timestamp | string | 
action\_result\.data\.\*\.malware\_family | string | 
action\_result\.data\.\*\.parent\_data\_id | string | 
action\_result\.data\.\*\.process\_info\.blocked\_reason | string | 
action\_result\.data\.\*\.process\_info\.file\_type\_skipped\_scan | boolean | 
action\_result\.data\.\*\.process\_info\.post\_processing\.actions\_failed | string | 
action\_result\.data\.\*\.process\_info\.post\_processing\.actions\_ran | string | 
action\_result\.data\.\*\.process\_info\.post\_processing\.converted\_destination | string | 
action\_result\.data\.\*\.process\_info\.post\_processing\.converted\_to | string | 
action\_result\.data\.\*\.process\_info\.post\_processing\.copy\_move\_destination | string | 
action\_result\.data\.\*\.process\_info\.profile | string | 
action\_result\.data\.\*\.process\_info\.progress\_percentage | numeric | 
action\_result\.data\.\*\.process\_info\.result | string | 
action\_result\.data\.\*\.process\_info\.user\_agent | string | 
action\_result\.data\.\*\.rest\_version | string | 
action\_result\.data\.\*\.sandbox | boolean | 
action\_result\.data\.\*\.sanitized\.data\_id | string | 
action\_result\.data\.\*\.sanitized\.reason | string | 
action\_result\.data\.\*\.sanitized\.result | string | 
action\_result\.data\.\*\.scan\_result\_history\_length | numeric | 
action\_result\.data\.\*\.scan\_results\.data\_id | string | 
action\_result\.data\.\*\.scan\_results\.progress\_percentage | numeric | 
action\_result\.data\.\*\.scan\_results\.rescan\_available | boolean | 
action\_result\.data\.\*\.scan\_results\.scan\_all\_result\_a | string | 
action\_result\.data\.\*\.scan\_results\.scan\_all\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.\*\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.\*\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.\*\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.\*\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AVG\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AVG\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AVG\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AVG\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AegisLab\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AegisLab\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AegisLab\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.AegisLab\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Agnitum\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Agnitum\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Agnitum\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Agnitum\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ahnlab\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ahnlab\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ahnlab\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ahnlab\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Antiy\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Antiy\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Antiy\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Antiy\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Avira\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Avira\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Avira\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Avira\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Baidu\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Baidu\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Baidu\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Baidu\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.BitDefender\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.BitDefender\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.BitDefender\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.BitDefender\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ByteHero\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ByteHero\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ByteHero\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ByteHero\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamAV\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamAV\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamAV\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamAV\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamWin\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamWin\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamWin\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ClamWin\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Comodo\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Comodo\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Comodo\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Comodo\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.CrowdStrike Falcon ML\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.CrowdStrike Falcon ML\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.CrowdStrike Falcon ML\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.CrowdStrike Falcon ML\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Cyren\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Cyren\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Cyren\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Cyren\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Dr\.Web Gateway\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Dr\.Web Gateway\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Dr\.Web Gateway\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Dr\.Web Gateway\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ESET\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ESET\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ESET\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ESET\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Emsisoft\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Emsisoft\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Emsisoft\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Emsisoft\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-prot\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-prot\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-prot\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-prot\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-secure\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-secure\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-secure\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.F\-secure\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Filseclab\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Filseclab\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Filseclab\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Filseclab\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Fortinet\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Fortinet\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Fortinet\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Fortinet\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.GFI\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.GFI\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.GFI\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.GFI\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Hauri\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Hauri\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Hauri\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Hauri\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Huorong\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Huorong\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Huorong\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Huorong\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ikarus\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ikarus\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ikarus\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Ikarus\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Jiangmin\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Jiangmin\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Jiangmin\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Jiangmin\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.K7\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.K7\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.K7\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.K7\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Kaspersky\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Kaspersky\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Kaspersky\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Kaspersky\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Lavasoft\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Lavasoft\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Lavasoft\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Lavasoft\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\-Gateway\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\-Gateway\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\-Gateway\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\-Gateway\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.McAfee\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Microsoft Security Essentials\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Microsoft Security Essentials\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Microsoft Security Essentials\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Microsoft Security Essentials\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.NANOAV\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.NANOAV\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.NANOAV\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.NANOAV\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Preventon\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Preventon\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Preventon\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Preventon\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Quick Heal\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Quick Heal\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Quick Heal\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Quick Heal\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.RocketCyber\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.RocketCyber\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.RocketCyber\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.RocketCyber\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.STOPzilla\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.STOPzilla\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.STOPzilla\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.STOPzilla\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.SUPERAntiSpyware\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.SUPERAntiSpyware\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.SUPERAntiSpyware\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.SUPERAntiSpyware\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Sophos\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Sophos\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Sophos\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Sophos\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TACHYON\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TACHYON\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TACHYON\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TACHYON\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Tencent\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Tencent\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Tencent\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Tencent\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ThreatTrack\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ThreatTrack\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ThreatTrack\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.ThreatTrack\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Total Defense\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Total Defense\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Total Defense\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Total Defense\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro House Call\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro House Call\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro House Call\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro House Call\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.TrendMicro\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT ML\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT ML\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT ML\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT ML\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT eXplorer\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT eXplorer\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT eXplorer\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Vir\.IT eXplorer\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirIT\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirIT\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirIT\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirIT\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirusBlokAda\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirusBlokAda\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirusBlokAda\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.VirusBlokAda\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Webroot SMD\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Webroot SMD\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Webroot SMD\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Webroot SMD\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Windows Defender\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Windows Defender\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Windows Defender\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Windows Defender\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Xvirus Personal Guard\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Xvirus Personal Guard\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Xvirus Personal Guard\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Xvirus Personal Guard\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zillya\!\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zillya\!\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zillya\!\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zillya\!\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zoner\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zoner\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zoner\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.Zoner\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.nProtect\.def\_time | string | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.nProtect\.scan\_result\_i | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.nProtect\.scan\_time | numeric | 
action\_result\.data\.\*\.scan\_results\.scan\_details\.nProtect\.threat\_found | string | 
action\_result\.data\.\*\.scan\_results\.start\_time | string | 
action\_result\.data\.\*\.scan\_results\.total\_avs | numeric | 
action\_result\.data\.\*\.scan\_results\.total\_detected\_avs | numeric | 
action\_result\.data\.\*\.scan\_results\.total\_time | numeric | 
action\_result\.data\.\*\.share\_file | numeric | 
action\_result\.data\.\*\.stored | boolean | 
action\_result\.data\.\*\.threat\_name | string | 
action\_result\.data\.\*\.votes\.down | numeric | 
action\_result\.data\.\*\.votes\.up | numeric | 
action\_result\.summary | string | 
action\_result\.summary\.file\_result | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'test connectivity'
Validates the asset configuration for connectivity

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output