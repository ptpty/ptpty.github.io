This is the demo page

## Abstract
Distortion Effect Modeling 
- Digital (GuitarZK)
- Analog (EGFX)

### Audio Samples

<hr>
We provide 2 sets of sound files for digital and analog modeling. Each set contains the clean tone, real distortion and the emulated sound by the neural network.

<hr>

1. `Clean-Tone`: `Clean`
2. `Real-Distortion`: `RD`
3. `Concat-TCN`: `CT`
4. `FiLM-TCN`:  `FT`
5. `Hyper-TCN-Small`: `HTS`
6. `Hyper-TCN-Large`: `HTL`
7. `FiLM-GCN`: `FG`
8. `Hyper-GCN-Small`: `HGS`
9. `Hyper-GCN-Large`: `HGL` 

#### GuitarZK

<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>db</td>
      <td>Clean</td>
      <td>RD</td>
      <td>CT</td>
      <td>FT</td>
      <td>HTS</td>
      <td>HTL</td>
      <td>FG</td>
      <td>HGS</td>
      <td>HGL</td>
    </tr>
    <tr>
      <td rowspan="0">A</td>
      <td>24</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/a/clean.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/rd_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ct_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ft_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hts_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/htl_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/fg_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_24.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>36</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/rd_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ct_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ft_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hts_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/htl_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/fg_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_36.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>48</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/rd_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ct_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/ft_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hts_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/htl_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/fg_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/a/hgl_48.wav" type="audio/mpeg" /></audio></td>
    </tr>
  </tbody>
</table>

<hr>

<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>db</td>
      <td>Clean</td>
      <td>RD</td>
      <td>CT</td>
      <td>FT</td>
      <td>HTS</td>
      <td>HTL</td>
      <td>FG</td>
      <td>HGS</td>
      <td>HGL</td>
    </tr>
    <tr>
      <td rowspan="0">B</td>
      <td>24</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/b/cleantone.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/rd_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ct_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ft_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hts_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/htl_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/fg_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_24.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_24.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>36</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/rd_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ct_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ft_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hts_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/htl_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/fg_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_36.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_36.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>48</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/rd_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ct_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/ft_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hts_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/htl_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/fg_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_48.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/b/hgl_48.wav" type="audio/mpeg" /></audio></td>
    </tr>
  </tbody>
</table>

#### EGFX

<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>Effect Type</td>
      <td>Clean</td>
      <td>RD</td>
      <td>FT</td>
      <td>HTS</td>
      <td>HTL</td>
      <td>FG</td>
      <td>HGS</td>
      <td>HGL</td>
    </tr>
    <tr>
      <td rowspan="0">A</td>
      <td>RAT</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/c/clean.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/rd-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/ft-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hts-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/htl-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/fg-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-RAT.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>BluesDriver</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/rd-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/ft-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hts-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/htl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/fg-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>TubeScreamer</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/rd-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/ft-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hts-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/htl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/fg-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/c/hgl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
    </tr>
  </tbody>
</table>

<hr>

<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>Effect Type</td>
      <td>Clean</td>
      <td>RD</td>
      <td>FT</td>
      <td>HTS</td>
      <td>HTL</td>
      <td>FG</td>
      <td>HGS</td>
      <td>HGL</td>
    </tr>
    <tr>
      <td rowspan="0">B</td>
      <td>RAT</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/d/clean.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/rd-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/ft-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hts-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/htl-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/fg-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-RAT.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-RAT.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>BluesDriver</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/rd-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/ft-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hts-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/htl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/fg-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-BluesDriver.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>TubeScreamer</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/rd-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/ft-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hts-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/htl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/fg-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/d/hgl-TubeScreamer.wav" type="audio/mpeg" /></audio></td>
    </tr>
  </tbody>
</table>

### Contact 

<hr>


