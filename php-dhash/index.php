<?php

require __DIR__ . '/vendor/autoload.php';
//require __DIR__ . '/src/Implementation.php';
//require __DIR__ . '/src/Implementations/DifferenceHash.php';
//require __DIR__ . '/src/ImageHash.php';

use Jenssegers\ImageHash\Implementations\DifferenceHash;
use Jenssegers\ImageHash\ImageHash;

function dHash($file) {
    $implementation = new DifferenceHash;
    $hasher = new ImageHash($implementation);
    $hash = $hasher->multipleHash($file);
    return $hash;
}

function distance($file1, $file2) {
    $implementation = new DifferenceHash;
    $hasher = new ImageHash($implementation);
    return $hasher->multipleCompare($file1, $file2);
}