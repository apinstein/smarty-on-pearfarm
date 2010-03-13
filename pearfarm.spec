<?php

$version = getenv('SMARTY_VERSION');
$stability = 'stable';
if (preg_match('/b[0-9]+$/', $version))
{
    $stability = 'beta';
}
else if (preg_match('/a[0-9]+$/', $version))
{
    $stability = 'alpha';
}
$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('smarty')
             ->setChannel('apinstein.pearfarm.org')
             ->setSummary('Smarty Template Engine')
             ->setDescription('See http://www.smarty.net')
             ->setReleaseVersion(getenv('SMARTY_VERSION'))
             ->setReleaseStability('alpha')
             ->setApiVersion('0.0.1')
             ->setApiStability($stability)
             ->setLicense(Pearfarm_PackageSpec::LICENSE_LGPL)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Alan Pinstein', 'apinstein', 'apinstein@mac.com')
             ->addFilesRegex('/smarty-to-package\/Smarty-2.6.26\/libs\/.*/', Pearfarm_PackageSpec::ROLE_PHP, array(Pearfarm_PackageSpec::OPT_BASEDIR => 'Smarty'))
             ;
