Add-Type -AssemblyName System.Drawing
$imagePath = 'C:\Users\rafas\.gemini\antigravity-ide\brain\40601238-bda2-4ce6-8415-8cb1c59fc40e\media__1786500703698.png'
$outPath = Join-Path (Get-Location) 'images\logo_foguete.png'

$img = [System.Drawing.Image]::FromFile($imagePath)
$bmp = New-Object System.Drawing.Bitmap $img

$width = $bmp.Width
$height = $bmp.Height

# Find bounding box of the rocket
$minX = $width
$minY = $height
$maxX = 0
$maxY = 0

# Rocket is white (R>200, G>200, B>200) and in top 65% of image
for ($y = 0; $y -lt [math]::Floor($height * 0.65); $y++) {
    for ($x = 0; $x -lt $width; $x++) {
        $pixel = $bmp.GetPixel($x, $y)
        if ($pixel.R -gt 200 -and $pixel.G -gt 200 -and $pixel.B -gt 200) {
            # It's part of the rocket
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}

$newWidth = $maxX - $minX + 1
$newHeight = $maxY - $minY + 1
$newBmp = New-Object System.Drawing.Bitmap $newWidth, $newHeight

for ($y = 0; $y -lt $newHeight; $y++) {
    for ($x = 0; $x -lt $newWidth; $x++) {
        $origX = $x + $minX
        $origY = $y + $minY
        $pixel = $bmp.GetPixel($origX, $origY)
        
        if ($pixel.R -gt 200 -and $pixel.G -gt 200 -and $pixel.B -gt 200) {
            # Make it orange (238, 105, 0)
            $newColor = [System.Drawing.Color]::FromArgb(255, 238, 105, 0)
            $newBmp.SetPixel($x, $y, $newColor)
        } else {
            # Make it transparent
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
