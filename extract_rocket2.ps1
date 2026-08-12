Add-Type -AssemblyName System.Drawing
$imagePath = 'C:\Users\rafas\.gemini\antigravity-ide\brain\40601238-bda2-4ce6-8415-8cb1c59fc40e\media__1786501419609.png'
$outPath = Join-Path (Get-Location) 'images\logo_foguete.png'

$img = [System.Drawing.Image]::FromFile($imagePath)
$bmp = New-Object System.Drawing.Bitmap $img

$width = $bmp.Width
$height = $bmp.Height

$minX = $width
$minY = $height
$maxX = 0
$maxY = 0

$bg = $bmp.GetPixel(0, 0)

for ($y = 0; $y -lt $height; $y++) {
    for ($x = 0; $x -lt $width; $x++) {
        $pixel = $bmp.GetPixel($x, $y)
        $diff = [Math]::Abs($pixel.R - $bg.R) + [Math]::Abs($pixel.G - $bg.G) + [Math]::Abs($pixel.B - $bg.B)
        
        if ($diff -gt 15) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

$newWidth = $maxX - $minX + 1
$newHeight = $maxY - $minY + 1

if ($newWidth -le 0 -or $newHeight -le 0) {
    Write-Host "Failed to find rocket"
    exit
}

$newBmp = New-Object System.Drawing.Bitmap $newWidth, $newHeight

for ($y = 0; $y -lt $newHeight; $y++) {
    for ($x = 0; $x -lt $newWidth; $x++) {
        $origX = $x + $minX
        $origY = $y + $minY
        $pixel = $bmp.GetPixel($origX, $origY)
        
        $diff = [Math]::Abs($pixel.R - $bg.R) + [Math]::Abs($pixel.G - $bg.G) + [Math]::Abs($pixel.B - $bg.B)
        
        if ($diff -gt 15) {
            $alpha = [math]::Min([math]::Max(($diff * 8), 0), 255)
            $newColor = [System.Drawing.Color]::FromArgb($alpha, 238, 105, 0)
            $newBmp.SetPixel($x, $y, $newColor)
        } else {
            $newColor = [System.Drawing.Color]::FromArgb(0, 0, 0, 0)
            $newBmp.SetPixel($x, $y, $newColor)
        }
    }
}

$newBmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
$newBmp.Dispose()
$img.Dispose()
Write-Host "Rocket extracted to $outPath"
