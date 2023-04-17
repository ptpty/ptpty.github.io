This is the demo page for the paper **"Designing Bias-free Models for Neural Audio Effect Modeling"**.

## Abstract
Micro-temporal convolutional network (micro-TCN) has gained popularity as a promising architecture for modeling neural audio effects. The network utilizes dilated 1D convolutions to process music in the waveform domain and incorporates conditioning modules that adjust the gain and bias of each layer based on control parameters that emulate a specific audio effect. Despite the effectiveness of micro-TCN, our research has uncovered an issue related to the biases arose from its convolution layers and conditioning modules. Such biases lead to audible artefacts at the output when the input signal is silent,  and may unfavorably decrease the headroom of dynamic range in general. To account for this issue, we propose a ``bias-free'' alternative of micro-TCN that avoids adapting the bias in each intermediate layer. This involves using gated convolutions as the model backbone, hyper networks as the conditioning module, and removing batch normalization entirely. Our experiments on emulating time-invariant guitar effects created by either software or real devices demonstrate that the proposed design eliminates unwanted DC bias without losing the capacity of micro-TCN in audio effect modeling.


## Motivation 

Observation in three secanrios. 
<img src="./assets/imgs/bias_variation.png" width="400" height="300">

(a) Given a silent input, the output of the FiLM-TCN has unexpectedly a DC shift, while the proposed bias-free model Hyper-GCN does not.
<br>
(b) The incurred DC shift varies as a function of the imposed condition parameter for FiLM-TCN, while there is no DC bias at all for Hyper-GCN.
<br>
(c) Given a non-silent input, we calculate the mean amplitude of the output of the FiLM-TCN. We can see that the DC bias variation is similar to (b). 
<br>

The above situation shows the following problems:
1. When silent input to the model is not silent out, the unexpected pop sound or the unexpected noise will occur. 
2. The bias value varying with condition may hurt the headroom of the dynamic range or lead to the sound clipping.  

## Audio Samples

<hr>
We have provided two sets of audio files for each simulated effect in our experiments. Each sets contains DI, real, and results simulated by different models. The detailed information is shown below. 
<hr>

1. `DI`: clean audio which is considered to be the input to our model. 
2. `RD`: effected audio which is considered to be the target we aim to simulate.
3. `FT`: effected audio created from the model `FiLM-TCN` 
4. `FG`: effected audio created from the model `FiLM-GCN` 
5. `HG`: effected audio created from the model `Hyper-GCN`
6. `HG-WS`: effected audio created from the model `Hyper-GCN-WS` (Hyper-GCN with weight sharing strategy)

#### EGDB + Distortion
<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>db</td>
      <td>DI</td>
      <td>RD</td>
      <td>FT</td>
      <td>FG</td>
      <td>HG</td>
      <td>HG-WS</td>
    </tr>
    <tr>
      <td rowspan="0">A</td>
      <td>20</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/di.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/20/rd.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/20/ft.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/20/fg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/20/hg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/20/hg_ws.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>25</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/25/rd.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/25/ft.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/25/fg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/25/hg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/A/25/hg_ws.wav" type="audio/mpeg" /></audio></td>
    </tr>
  </tbody>
</table>

<hr>

<table style='text-align: center;'>
  <tbody>
    <tr>
      <td></td>
      <td>db</td>
      <td>DI</td>
      <td>RD</td>
      <td>FT</td>
      <td>FG</td>
      <td>HG</td>
      <td>HG-WS</td>
    </tr>
    <tr>
      <td rowspan="0">B</td>
      <td>20</td>
      <td rowspan="0"><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/di.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/20/rd.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/20/ft.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/20/fg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/20/hg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/20/hg_ws.wav" type="audio/mpeg" /></audio></td>
    </tr>
    <tr>
      <td>25</td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/25/rd.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/25/ft.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/25/fg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/25/hg.wav" type="audio/mpeg" /></audio></td>
      <td><audio controls="" style="width: 100px;"><source src="./assets/audios/Distortion/B/25/hg_ws.wav" type="audio/mpeg" /></audio></td>
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


