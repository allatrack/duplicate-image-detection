<?php

function loadImage($file)
{
    list($w, $h, $t) = getimagesize($file);
    switch($t) {
        case 1:
            $oi = imagecreatefromgif($file);
            break;
        case 2:
            $oi = imagecreatefromjpeg($file);
            break;
        case 3:
            $oi = imagecreatefrompng($file);
            break;
        default:
            $oi = imagecreatefromjpeg($file);
            break;
    }

    return [
        'width' => $w,
        'height' => $h,
        'source' => $oi,
    ];
}

function dHash($source, int $src_x, int $src_y, int $src_w, int $src_h)
{
    $hash = '';
    $size = 8;
    $im = imagecreatetruecolor($size + 1, $size);
    imagefilter($im, IMG_FILTER_GRAYSCALE);

    imagecopyresampled($im, $source, 0, 0, $src_x, $src_y, $size + 1, $size, $src_w, $src_h);
    for ($y = 0; $y < $size; $y++) {
        $val = '';
        for ($x = 0; $x < $size; $x++) {
            $curr = imagecolorat($im, $x, $y);
            $next = imagecolorat($im, $x + 1, $y);
            $val .= ($curr > $next) ? 1 : 0;
        }
        $hash .= str_pad(dechex(bindec($val)), 2, 0, STR_PAD_LEFT);
    }
    imagedestroy($im);
    return $hash;
}


function multipleDHash($file)
{
    $image = loadImage($file);
    $hashes = [
        'full_hash' => dHash($image["source"], 0, 0, $image["width"], $image["height"]),
        'left_hash' => dHash($image["source"], 0, 0, $image["width"] / 2, $image["height"]),
        'right_hash' => dHash($image["source"], $image["width"] / 2, 0, $image["width"] / 2, $image["height"]),
    ];
    imagedestroy($image["source"]);
    return $hashes;
}