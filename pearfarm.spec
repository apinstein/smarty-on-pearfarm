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
             ->setName('Smarty')
             ->setChannel('apinstein.pearfarm.org')
             ->setSummary('Smarty Template Engine')
             ->setDescription('See http://www.smarty.net')
             ->setReleaseVersion($version)
             ->setReleaseStability($stability)
             ->setApiVersion($version)
             ->setApiStability($stability)
             ->setLicense(Pearfarm_PackageSpec::LICENSE_LGPL)
             ->setNotes('This is a meta-package to provide a pear-installable smarty. See http://github.com/apinstein/smarty-on-pearfarm.')
             ->addMaintainer('lead', 'Alan Pinstein', 'apinstein', 'apinstein@mac.com')
             ->addFilesRegex('/.*/', Pearfarm_PackageSpec::ROLE_PHP, array(Pearfarm_PackageSpecFile::BASEINSTALLDIR => 'Smarty'))
             ->addExcludeFiles('pearfarm.spec')
             ;
