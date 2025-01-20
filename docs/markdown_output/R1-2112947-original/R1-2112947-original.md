#### **3GPP TSG-RAN WG1 Meeting #107-e** *R1-2112947* **Electronic Meeting, November 11 th – 19 th , 2021**

|  |  |  |  |  | CR-Form-v12.1 |
| --- | --- | --- | --- | --- | --- |
|  |  | CHANGE REQUEST |  |  |  |
| 38.214 CR 0026 | rev | - | Current version: |  | 16.7.0 |
| For HELP on using this form: comprehensive instructions can be found at |  |  |  |  |  |
| http://www.3gpp.org/Change-Requests. |  |  |  |  |  |
| Proposed change affects: | UICC apps | ME X | Radio Access Network | X | Core Network |
| Title: | Introduction of DL 1024QAM for NR FR1 |  |  |  |  |
| Source to WG: Nokia |  |  |  |  |  |
| Source to TSG: |  |  |  |  |  |
| Work item code: NR_DL1024QAM_FR1-Core |  |  | Date: | 2021-12-08 |  |
| Category: B |  |  | Release: | Rel-17 |  |
| Use one of the following categories: |  |  |  | Use one of the following releases: |  |
| F (correction) |  |  | Rel-8 | (Release 8) |  |
| A (mirror corresponding to a change in an earlier |  |  | Rel-9 | (Release 9) |  |
|  |  |  | release) Rel-10 | (Release 10) |  |
| B (addition of feature), |  |  | Rel-11 | (Release 11) |  |
| C (functional modification of feature) |  |  | … |  |  |
| D (editorial modification) |  |  | Rel-15 | (Release 15) |  |
| Detailed explanations of the above categories can |  |  | Rel-16 | (Release 16) |  |
| be found in 3GPP TR 21.900. |  |  | Rel-17 | (Release 17) |  |
|  |  |  | Rel-18 | (Release 18) |  |
| Reason for change: | Introduction of DL 1024QAM for NR FR1 |  |  |  |  |
| Summary of change: |  |  | Introduction of 1024QAM related procedures in modulation order and target |  |  |
|  |  | code rate determination, TBS determination, PT-RS operation, CQI |  |  |  |
| Consequences if not | Incomplete support of DL 1024QAM for NR FR1 |  |  |  |  |
| approved: |  |  |  |  |  |
| Clauses affected: | 5.1.3, 5.1.3.1, 5.1.3.2, 5.1.6.3, 5.2.2.1 |  |  |  |  |
| Y N |  |  |  |  |  |
| Other specs X | Other core specifications |  | TS 38.211, TS 38.212 |  |  |
| affected: X | Test specifications |  | TS/TR ... CR ... |  |  |
| (show related CRs) X | O&M Specifications |  | TS/TR ... CR ... |  |  |
| Other comments: |  |  |  |  |  |
| This CR's revision history: |  |  |  |  |  |

#### <omitted text>

## 5.1.3 Modulation order, target code rate, redundancy version and transport block size determination

To determine the modulation order, target code rate, and transport block size(s) in the physical downlink shared channel, the UE shall first

- read the 5-bit modulation and coding scheme field (*IMCS*) in the DCI to determine the modulation order (*Qm*) and target code rate (*R*) based on the procedure defined in Clause 5.1.3.1, and
- read '*redundancy version'* field (*rv*) in the DCI to determine the redundancy version.

and second

- the UE shall use the number of layers (ʋ), the total number of allocated PRBs before rate matching (*nPRB*) to determine to the transport block size based on the procedure defined in Clause 5.1.3.2.
The UE may skip decoding a transport block in an initial transmission if the effective channel code rate is higher than 0.95, where the effective channel code rate is defined as the number of downlink information bits (including CRC bits) divided by the number of physical channel bits on PDSCH.

The UE is not expected to handle any transport blocks (TBs) in a 14 consecutive-symbol duration for normal CP (or 12 for extended CP) ending at the last symbol of the latest PDSCH transmission within an active BWP on a serving cell whenever

$$2^{\operatorname*{max}{(0,\mu-\mu^{r})}}.\sum_{i\in S}\left|{\frac{C_{i}^{r}}{L_{i}}}\right|x_{i}.F_{i}>\left|{\frac{X}{4}}\right|.{\frac{1}{R_{L B R M}}}.T B S_{L B R M}$$

where, for the serving cell,

- S is the set of TBs belonging to PDSCH(s) that are partially or fully contained in the consecutive-symbol duration
- for the *i*th TB
	- *- Ci'* is the number of scheduled code blocks for as defined in [5, 38.212].
	- *- Li* is the number of OFDM symbols assigned to the PDSCH
	- *- xi* is the number of OFDM symbols of the PDSCH contained in the consecutive-symbol duration
	- = max =0,...,−1 (min(0, + ,,)) based on the values defined in Clause 5.4.2.1 [5, TS 38.212]
		- 0, is the starting location of RV for the th transmission
		- = min() of the scheduled code blocks for the th transmission
		- , is the circular buffer length
		- − 1 is the current (re)transmission for the *i*th TB
	- ′ corresponds to the subcarrier spacing of the BWP (across all configured BWPs of a carrier) that has the largest configured number of PRBs
		- in case there is more than one BWP corresponding to the largest configured number of PRBs, *µ'* follows the BWP with the largest subcarrier spacing.
	- corresponds to the subcarrier spacing of the active BWP
	- RLBRM = 2/3 as defined in Clause 5.4.2.1 [5, TS 38.212]
	- TBSLBRM as defined in Clause 5.4.2.1 [5, TS 38.212]
	- X as defined for downlink in Clause 5.4.2.1 [5, TS 38.212].

If the UE skips decoding, the physical layer indicates to higher layer that the transport block is not successfully decoded.

Within a cell group, a UE is not required to handle PDSCH(s) transmissions in slot *sj* in serving cell-*j*, and for *j* = 0,1,2.. *J-1*, slot *sj* overlapping with any given point in time, if the following condition is not satisfied at that point in time:

$$\sum_{j=0}^{j-1}{\frac{\sum_{m=0}^{M-1}V_{j,m}}{T_{s l o t}^{\mu(j)}}}\leq D a t a R a t e$$

where,

- *J* is the number of configured serving cells belonging to a frequency range
- for the *j-th* serving cell,
	- *- M* is the number of TB(s) transmitted in slot *sj*. If there are two PDSCH transmission occasions of the same TB (in time domain or in frequency domain) in the slot *sj*, each transmission occasion is counted separately.
	- *- Tslot(j)* =10-3 /2*(j)*, where *(j)* is the numerology for PDSCH(s) in slot *sj* of the *j*-th serving cell.
	- for the *m*-th TB, , = ′ ∙ ⌊ ⌋
		- *- A* is the number of bits in the transport block as defined in Clause 7.2.1 [5, TS 38.212]
		- *- C* is the total number of code blocks for the transport block defined in Clause 5.2.2 [5, TS 38.212].
		- *-* ′ is the number of scheduled code blocks for the transport block as defined in Clause 5.4.2.1 [5, TS 38.212]
- [Mbps] is computed as the maximum data rate summed over all the carriers in the frequency range for any signaled band combination and feature set consistent with the configured servings cells, where the data rate value is given by the formula in Clause 4.1.2 in [13, TS 38.306], including the scaling factor *f(i).*

For a *j-*th serving cell, if higher layer parameter *processingType2Enabled* of *PDSCH-ServingCellConfig* is configured for the serving cell and set to '*enable',* or if at least one *IMCS > W* for a PDSCH, where *W* = 28 for MCS tables 5.1.3.1-1 and 5.1.3.1-3, and *W* = 27 for MCS table 5.1.3.1-2, the UE is not required to handle PDSCH transmissions, if the following condition is not satisfied:

$${\frac{\sum_{m=0}^{M-1}V_{j,m}}{L\times T_{s}^{\mu}}}\leq D a t a R a t e C$$

where

- is the number of symbols assigned to the PDSCH. For a PDSCH that consists of two PDSCH transmission occasions in time domain in one slot, is the number of symbols of one transmission occasion.
- M is the number of TB(s) in the PDSCH
- = 10−3 2∙ where is the numerology of the PDSCH
- for the *m*-th TB, , = ′ ∙ ⌊ ⌋
	- *- A* is the number of bits in the transport block as defined in Clause 7.2.1 [5, TS 38.212]
	- *- C* is the total number of code blocks for the transport block defined in Clause 5.2.2 [5, TS 38.212]
	- *-* ′ is the number of scheduled code blocks for the transport block as defined in Clause 5.4.2.1 [5, TS 38.212]
- [Mbps] is computed as the maximum data rate for a carrier in the frequency band of the serving cell for any signaled band combination and feature set consistent with the serving cell, where the data rate value is given by the formula in Clause 4.1.2 in [13, TS 38.306], including the scaling factor *f(i).*

## 5.1.3.1 Modulation order and target code rate determination

For the PDSCH scheduled by a PDCCH with DCI format 1_0, format 1_1 or format 1_2 with CRC scrambled by C-RNTI, MCS-C-RNTI, TC-RNTI, CS-RNTI, SI-RNTI, RA-RNTI, MSGB-RNTI, or P-RNTI, or for the PDSCH scheduled without corresponding PDCCH transmissions using the higher-layer-provided PDSCH configuration *SPS-Config*,

if the higher layer parameter *mcs-TableDCI-1-2* given by *PDSCH-Config* is set to 'qam256', and the PDSCH is scheduled by a PDCCH with DCI format 1_2 with CRC scrambled by C-RNTI

- the UE shall use *IMCS* and Table 5.1.3.1-2 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
elseif the UE is not configured with MCS-C-RNTI, the higher layer parameter *mcs-TableDCI-1-2* given by *PDSCH-Config* is set to 'qam64LowSE', and the PDSCH is scheduled by a PDCCH with DCI format 1_2 scrambled by C-RNTI

- the UE shall use *IMCS* and Table 5.1.3.1-3 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
elseif the higher layer parameter *mcs-Table* given by *PDSCH-Config* is set to 'qam256', and the PDSCH is scheduled by a PDCCH with DCI format 1_1 with CRC scrambled by C-RNTI

- the UE shall use *IMCS* and Table 5.1.3.1-2 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
elseif the UE is not configured with MCS-C-RNTI, the higher layer parameter *mcs-Table* given by *PDSCH-Config* is set to 'qam64LowSE', and the PDSCH is scheduled by a PDCCH with a DCI format other than DCI format 1_2 in a UE-specific search space with CRC scrambled by C-RNTI

- the UE shall use *IMCS* and Table 5.1.3.1-3 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
elseif the UE is configured with MCS-C-RNTI, and the PDSCH is scheduled by a PDCCH with CRC scrambled by MCS-C-RNTI

- the UE shall use *IMCS* and Table 5.1.3.1-3 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel. elseif the UE is not configured with the higher layer parameter *mcs-Table* given by *SPS-config*, and the higher layer parameter *mcs-TableDCI-1-2* given by *PDSCH-Config* is set to 'qam256',

- if the PDSCH is scheduled by a PDCCH with DCI format 1_2 with CRC scrambled by CS-RNTI or
- if the PDSCH with SPS activated by DCI format 1_2 is scheduled without corresponding PDCCH transmission using *SPS-Config*,
- the UE shall use *IMCS* and Table 5.1.3.1-2 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.

elseif the UE is not configured with the higher layer parameter *mcs-Table* given by *SPS-Config*, and the higher layer parameter *mcs-Table* given by *PDSCH-Config* is set to 'qam256',

- if the PDSCH is scheduled by a PDCCH with DCI format 1_1 with CRC scrambled by CS-RNTI or
- if the PDSCH with SPS activated by DCI format 1_1 is scheduled without corresponding PDCCH transmission using *SPS-Config*,
	- the UE shall use *IMCS* and Table 5.1.3.1-2 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.

elseif the UE is configured with the higher layer parameter *mcs-Table* given by *SPS-Config* set to 'qam64LowSE'

- if the PDSCH is scheduled by a PDCCH with CRC scrambled by CS-RNTI or
- if the PDSCH is scheduled without corresponding PDCCH transmission using *SPS-Config*,

- the UE shall use *IMCS* and Table 5.1.3.1-3 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
else

- the UE shall use *IMCS* and Table 5.1.3.1-1 to determine the modulation order (*Qm*) and Target code rate (*R*) used in the physical downlink shared channel.
end

The UE is not expected to decode a PDSCH scheduled with P-RNTI, RA-RNTI, SI-RNTI and *Qm* > 2

For a UE configured with the higher layer parameter *repetitionScheme* set to 'fdmSchemeB', and when the UE is indicated with two TCI states in a codepoint of the DCI field *'Transmission Configuration Indication'* and DM-RS port(s) within one CDM group in the DCI field '*Antenna Port(s)*', the determined modulation order of PDSCH transmission occasion associated with the first TCI state is applied to the PDSCH transmission occasion associated with the second TCI state.

| MCS Index | Modulation Order | Target code Rate R x [1024] | Spectral |
| --- | --- | --- | --- |
| IMCS | Qm |  | efficiency |
| 0 | 2 | 120 | 0.2344 |
| 1 | 2 | 157 | 0.3066 |
| 2 | 2 | 193 | 0.3770 |
| 3 | 2 | 251 | 0.4902 |
| 4 | 2 | 308 | 0.6016 |
| 5 | 2 | 379 | 0.7402 |
| 6 | 2 | 449 | 0.8770 |
| 7 | 2 | 526 | 1.0273 |
| 8 | 2 | 602 | 1.1758 |
| 9 | 2 | 679 | 1.3262 |
| 10 | 4 | 340 | 1.3281 |
| 11 | 4 | 378 | 1.4766 |
| 12 | 4 | 434 | 1.6953 |
| 13 | 4 | 490 | 1.9141 |
| 14 | 4 | 553 | 2.1602 |
| 15 | 4 | 616 | 2.4063 |
| 16 | 4 | 658 | 2.5703 |
| 17 | 6 | 438 | 2.5664 |
| 18 | 6 | 466 | 2.7305 |
| 19 | 6 | 517 | 3.0293 |
| 20 | 6 | 567 | 3.3223 |
| 21 | 6 | 616 | 3.6094 |
| 22 | 6 | 666 | 3.9023 |
| 23 | 6 | 719 | 4.2129 |
| 24 | 6 | 772 | 4.5234 |
| 25 | 6 | 822 | 4.8164 |
| 26 | 6 | 873 | 5.1152 |
| 27 | 6 | 910 | 5.3320 |
| 28 | 6 | 948 | 5.5547 |
| 29 | 2 | reserved |  |
| 30 | 4 | reserved |  |
| 31 | 6 | reserved |  |

**Table 5.1.3.1-1: MCS index table 1 for PDSCH**

| MCS Index | Modulation Order | Target code Rate R x [1024] | Spectral |
| --- | --- | --- | --- |
| IMCS | Qm |  | efficiency |
| 0 | 2 | 120 | 0.2344 |
| 1 | 2 | 193 | 0.3770 |
| 2 | 2 | 308 | 0.6016 |
| 3 | 2 | 449 | 0.8770 |
| 4 | 2 | 602 | 1.1758 |
| 5 | 4 | 378 | 1.4766 |
| 6 | 4 | 434 | 1.6953 |
| 7 | 4 | 490 | 1.9141 |
| 8 | 4 | 553 | 2.1602 |
| 9 | 4 | 616 | 2.4063 |
| 10 | 4 | 658 | 2.5703 |
| 11 | 6 | 466 | 2.7305 |
| 12 | 6 | 517 | 3.0293 |
| 13 | 6 | 567 | 3.3223 |
| 14 | 6 | 616 | 3.6094 |
| 15 | 6 | 666 | 3.9023 |
| 16 | 6 | 719 | 4.2129 |
| 17 | 6 | 772 | 4.5234 |
| 18 | 6 | 822 | 4.8164 |
| 19 | 6 | 873 | 5.1152 |
| 20 | 8 | 682.5 | 5.3320 |
| 21 | 8 | 711 | 5.5547 |
| 22 | 8 | 754 | 5.8906 |
| 23 | 8 | 797 | 6.2266 |
| 24 | 8 | 841 | 6.5703 |
| 25 | 8 | 885 | 6.9141 |
| 26 | 8 | 916.5 | 7.1602 |
| 27 | 8 | 948 | 7.4063 |
| 28 | 2 | reserved |  |
| 29 | 4 | reserved |  |
| 30 | 6 | reserved |  |
| 31 | 8 | reserved |  |

**Table 5.1.3.1-2: MCS index table 2 for PDSCH**

| MCS Index | Modulation Order | Target code Rate R x [1024] | Spectral |
| --- | --- | --- | --- |
| IMCS | Qm |  | efficiency |
| 0 | 2 | 30 | 0.0586 |
| 1 | 2 | 40 | 0.0781 |
| 2 | 2 | 50 | 0.0977 |
| 3 | 2 | 64 | 0.1250 |
| 4 | 2 | 78 | 0.1523 |
| 5 | 2 | 99 | 0.1934 |
| 6 | 2 | 120 | 0.2344 |
| 7 | 2 | 157 | 0.3066 |
| 8 | 2 | 193 | 0.3770 |
| 9 | 2 | 251 | 0.4902 |
| 10 | 2 | 308 | 0.6016 |
| 11 | 2 | 379 | 0.7402 |
| 12 | 2 | 449 | 0.8770 |
| 13 | 2 | 526 | 1.0273 |
| 14 | 2 | 602 | 1.1758 |
| 15 | 4 | 340 | 1.3281 |
| 16 | 4 | 378 | 1.4766 |
| 17 | 4 | 434 | 1.6953 |
| 18 | 4 | 490 | 1.9141 |
| 19 | 4 | 553 | 2.1602 |
| 20 | 4 | 616 | 2.4063 |
| 21 | 6 | 438 | 2.5664 |
| 22 | 6 | 466 | 2.7305 |
| 23 | 6 | 517 | 3.0293 |
| 24 | 6 | 567 | 3.3223 |
| 25 | 6 | 616 | 3.6094 |
| 26 | 6 | 666 | 3.9023 |
| 27 | 6 | 719 | 4.2129 |
| 28 | 6 | 772 | 4.5234 |
| 29 | 2 | reserved |  |
| 30 | 4 | reserved |  |
| 31 | 6 | reserved |  |

**Table 5.1.3.1-3: MCS index table 3 for PDSCH**

<omitted text>

## 5.1.3.2 Transport block size determination

In case the higher layer parameter *maxNrofCodeWordsScheduledByDCI* indicates that two codeword transmission is enabled, then one of the two transport blocks is disabled by DCI format 1_1 if *IMCS* = 26 and if *rvid* = 1 for the corresponding transport block. If both transport blocks are enabled, transport block 1 and 2 are mapped to codeword 0 and 1 respectively. If only one transport block is enabled, then the enabled transport block is always mapped to the first codeword.

For the PDSCH assigned by a PDCCH with DCI format 1_0, format 1_1 or format 1_2 with CRC scrambled by C-RNTI, MCS-C-RNTI, TC-RNTI, CS-RNTI, or SI-RNTI, if Table 5.1.3.1-2 is used and 0 *I MCS* 27 *,* or a table other than Table 5.1.3.1-2 is used and 0 *IMCS* 28 *,* the UE shall, except if the transport block is disabled in DCI format 1_1, first determine the TBS as specified below:

- 1) The UE shall first determine the number of REs (*NRE*) within the slot.
	- A UE first determines the number of REs allocated for PDSCH within a PRB ( ' *NRE*) by

*PRB oh PRB DMRS sh symb RB NRE* = *Nsc N* − *N* − *N* ' , where =12 *RB Nsc* is the number of subcarriers in a physical resource

block, *sh Nsymb* is the number of symbols of the PDSCH allocation within the slot, *PRB NDMRS* is the number of REs for DM-RS per PRB in the scheduled duration including the overhead of the DM-RS CDM groups without data, as indicated by DCI format 1_1 or format 1_2 or as described for format 1_0 in Clause 5.1.6.2,

- and *PRB Noh*is the overhead configured by higher layer parameter *xOverhead* in *PDSCH-ServingCellConfig*.
If the *xOverhead* in *PDSCH-ServingCellconfig* is not configured (a value from 6, 12, or 18), the *PRB Noh* is set to 0. If the PDSCH is scheduled by PDCCH with a CRC scrambled by SI-RNTI, RA-RNTI, MSGB-RNTI or P-RNTI, *PRB Noh*is assumed to be 0.

- A UE determines the total number of REs allocated for PDSCH ( *NRE* ) by ( ) ' min 156, *N N n RE PRB RE* = , where *nPRB* is the total number of allocated PRBs for the UE.
- 2) Unquantized intermediate variable (*Ninfo*) is obtained by *N*inf *o* = *NRE* ·*R*·*Qm* ·.

If *N*inf *o* 3824

Use step 3 as the next step of the TBS determination

else

Use step 4 as the next step of the TBS determination

end if

- 3) When *N*inf *o* 3824 , TBS is determined as follows
	- quantized intermediate number of information bits = *n n o o N N* 2 max 24,2 · ' inf inf , where max(3,log ( ) 6) *n* = 2 *N*inf *o* −.

- use Table 5.1.3.2-1 find the closest TBS that is not less than ' *N*inf*o*.

| Index | TBS | Index | TBS | Index | TBS | Index | TBS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 24 | 31 | 336 | 61 | 1288 | 91 | 3624 |
| 2 | 32 | 32 | 352 | 62 | 1320 | 92 | 3752 |
| 3 | 40 | 33 | 368 | 63 | 1352 | 93 | 3824 |
| 4 | 48 | 34 | 384 | 64 | 1416 |  |  |
| 5 | 56 | 35 | 408 | 65 | 1480 |  |  |
| 6 | 64 | 36 | 432 | 66 | 1544 |  |  |
| 7 | 72 | 37 | 456 | 67 | 1608 |  |  |
| 8 | 80 | 38 | 480 | 68 | 1672 |  |  |
| 9 | 88 | 39 | 504 | 69 | 1736 |  |  |
| 10 | 96 | 40 | 528 | 70 | 1800 |  |  |
| 11 | 104 | 41 | 552 | 71 | 1864 |  |  |
| 12 | 112 | 42 | 576 | 72 | 1928 |  |  |
| 13 | 120 | 43 | 608 | 73 | 2024 |  |  |
| 14 | 128 | 44 | 640 | 74 | 2088 |  |  |
| 15 | 136 | 45 | 672 | 75 | 2152 |  |  |
| 16 | 144 | 46 | 704 | 76 | 2216 |  |  |
| 17 | 152 | 47 | 736 | 77 | 2280 |  |  |
| 18 | 160 | 48 | 768 | 78 | 2408 |  |  |
| 19 | 168 | 49 | 808 | 79 | 2472 |  |  |
| 20 | 176 | 50 | 848 | 80 | 2536 |  |  |
| 21 | 184 | 51 | 888 | 81 | 2600 |  |  |
| 22 | 192 | 52 | 928 | 82 | 2664 |  |  |
| 23 | 208 | 53 | 984 | 83 | 2728 |  |  |
| 24 | 224 | 54 | 1032 | 84 | 2792 |  |  |
| 25 | 240 | 55 | 1064 | 85 | 2856 |  |  |
| 26 | 256 | 56 | 1128 | 86 | 2976 |  |  |
| 27 | 272 | 57 | 1160 | 87 | 3104 |  |  |
| 28 | 288 | 58 | 1192 | 88 | 3240 |  |  |
| 29 | 304 | 59 | 1224 | 89 | 3368 |  |  |
| 30 | 320 | 60 | 1256 | 90 | 3496 |  |  |

**Table 5.1.3.2-1: TBS for**  *N*inf*o* 3824

- 4) When *N*inf*o* 3824 , TBS is determined as follows.
	- quantized intermediate number of information bits ' inf inf 24 max 3840, 2 2 *n o o n N N round* − = , where
		- *n* = log2 (*N*inf *o* − 24)−5 and ties in the round function are broken towards the next largest integer.
	- if *R* 1/ 4

$T$B$S=8\cdot C\cdot\left[\frac{N_{\text{info}}+24}{8\cdot C}\right]-24$, where $C=\left[\frac{N_{\text{info}}+24}{3816}\right]$

else

$${\mathrm{if~}}N_{\operatorname*{inf}o}^{\cdot}>8424$$

$T$B$S=8\cdot C\cdot\left[\frac{N_{\text{info}}+24}{8\cdot C}\right]-24$, where $C=\left[\frac{N_{\text{info}}+24}{8424}\right]$

else

$$T B S=8\cdot\left[{\frac{N_{\mathrm{info}}^{\prime}+24}{8}}\right]-24$$

end if

end if

else if Table 5.1.3.1-2 is used and 28 *IMCS* 31*,* 

- the TBS is assumed to be as determined from the DCI transported in the latest PDCCH for the same transport block using 0 *I MCS* 27 . If there is no PDCCH for the same transport block using 0 *I MCS* 27 , and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH.
else

- the TBS is assumed to be as determined from the DCI transported in the latest PDCCH for the same transport block using 0 *IMCS* 28 . If there is no PDCCH for the same transport block using 0 *IMCS* 28 , and if the initial PDSCH for the same transport block is semi-persistently scheduled, the TBS shall be determined from the most recent semi-persistent scheduling assignment PDCCH.
The UE is not expected to receive a PDSCH assigned by a PDCCH with CRC scrambled by SI-RNTI with a TBS exceeding 2976 bits.

For a UE configured with the higher layer parameter *repetitionScheme* set to 'fdmSchemeB' and indicated with two TCI states in a codepoint of the DCI field *'Transmission Configuration Indication'* and DM-RS port(s) within one CDM group in the DCI field '*Antenna Port(s)*', the TBS determination follows the steps 1-4 with the following modification in

step 1: a UE determines the total number of REs allocated for PDSCH ( *NRE*) by ( ) ' min 156, *N N n REPRBRE*= , where

*nPRB* is the total number of allocated PRBs corresponding to the first TCI state, and the determined TBS of PDSCH transmission occasion associated with the first TCI state is also applied to the PDSCH transmission occasion associated with the second TCI state. For a UE configured with the higher layer parameter *repetitionScheme* set to 'tdmSchemeA' and indicated with two TCI states in a codepoint of the DCI field *'Transmission Configuration Indication'* and DM-RS port(s) within one CDM group in the DCI field '*Antenna Port(s)*', the TBS determination follows the steps 1-4 with the following modification in step 1: a UE determines the number of REs allocated for PDSCH within a PRB ( ' *NRE* ) by 

*PRB oh PRB DMRS sh symb RB NRE* = *Nsc N* − *N* − *N* ' , where *sh Nsymb* is the number of symbols of the PDSCH allocation within the slot

corresponding to the first TCI state, and the determined TBS of PDSCH transmission occasion associated with the first TCI state is also applied to the PDSCH transmission occasion associated with the second TCI state.

For the PDSCH assigned by a PDCCH with DCI format 1_0 with CRC scrambled by P-RNTI, or RA-RNTI, MsgB-RNTI, TBS determination follows the steps 1-4 with the following modification in step 2: a scaling *N S N R Q* inf *o RE m* = is applied in the calculation of *Ninfo*, where the scaling factor is determined based on the *TB scaling* field in the DCI as in Table 5.1.3.2-2.

**Table 5.1.3.2-2: Scaling factor of** *Ninfo* **for P-RNTI, RA-RNTI and MSGB-RNTI**

| TB scaling field | Scaling factor S |
| --- | --- |
| 00 | 1 |
| 01 | 0.5 |
| 10 | 0.25 |
| 11 |  |

The NDI and HARQ process ID, as signalled on PDCCH, and the TBS, as determined above, shall be reported to higher layers.

<omitted text>

## 5.1.6.3 PT-RS reception procedure

The procedures on PT-RS reception described in this clause apply to a UE receiving PDSCH scheduled by DCI format 1_2 configured with the higher layer parameter *phaseTrackingRS* in *dmrs-DownlinkForPDSCH-MappingTypeA-DCI-1- 2* or *dmrs-DownlinkForPDSCH-MappingTypeB-DCI-1-2* and to a UE receiving PDSCH scheduled by DCI format 1_0 or DCI format 1_1 configured with the higher layer parameter *phaseTrackingRS* in *dmrs-DownlinkForPDSCH-MappingTypeA* or *dmrs-DownlinkForPDSCH-MappingTypeB*.

A UE shall report the preferred MCS and bandwidth thresholds based on the UE capability at a given carrier frequency, for each subcarrier spacing applicable to data channel at this carrier frequency, assuming the MCS table with the maximum Modulation Order as it reported to support.

If a UE is configured with the higher layer parameter *phaseTrackingRS* in *DMRS-DownlinkConfig*,

- the higher layer parameters *timeDensity* and *frequencyDensity* in *PTRS-DownlinkConfig* indicate the threshold values *ptrs-MCSi*, *i*=1,2,3 and *NRB,i* , *i*=0,1, as shown in Table 5.1.6.3-1 and Table 5.1.6.3-2, respectively.
- if either or both of the additional higher layer parameters *timeDensity* and *frequencyDensity* are configured, and the RNTI equals MCS-C-RNTI, C-RNTI or CS-RNTI, the UE shall assume the PT-RS antenna port' presence and pattern is a function of the corresponding scheduled MCS of the corresponding codeword and scheduled bandwidth in corresponding bandwidth part as shown in Table 5.1.6.3-1 and Table 5.1.6.3-2,
	- if the higher layer parameter *timeDensity* given by *PTRS-DownlinkConfig* is not configured, the UE shall assume *LPT-RS* = 1.
	- if the higher layer parameter *frequencyDensity* given by *PTRS-DownlinkConfig* is not configured, the UE shall assume *KPT-RS* = 2.
- otherwise, if neither of the additional higher layer parameters *timeDensity* and *frequencyDensity* are configured and the RNTI equals MCS-C-RNTI, C-RNTI or CS-RNTI, the UE shall assume the PT-RS is present with *LPT-RS*  = 1, *KPT-RS* = 2, and the UE shall assume PT-RS is not present when
	- the scheduled MCS from Table 5.1.3.1-1 is smaller than 10, or
	- the scheduled MCS from Table 5.1.3.1-2 is smaller than 5, or
	- the scheduled MCS from Table 5.1.3.1-3 is smaller than 15, or the number of scheduled RBs is smaller than 3, or
- otherwise, if the RNTI equals RA-RNTI, [MSGB-RNTI], SI-RNTI, or P-RNTI, the UE shall assume PT-RS is not present

| Table 5.1.6.3-1: Time density of PT-RS as a function of scheduled MCS |
| --- |

| Scheduled MCS | L Time density ( ) PT − RS |
| --- | --- |
| IMCS < ptrs-MCS1 | PT-RS is not present |
| ptrs-MCS1  IMCS < ptrs-MCS2 | 4 |
|  ptrs-MCS2 IMCS < ptrs-MCS3 | 2 |
|  ptrs-MCS3 IMCS < ptrs-MCS4 | 1 |

| Table 5.1.6.3-2: Frequency density of PT-RS as a function of scheduled bandwidth |
| --- |

| Scheduled bandwidth | KPT Frequency density ( ) −RS |
| --- | --- |
| NRB < NRB0 | PT-RS is not present |
|  NRB0 NRB < NRB1 | 2 |
|  NRB1 NRB | 4 |

If a UE is not configured with the higher layer parameter *phaseTrackingRS* in *DMRS-DownlinkConfig*, the UE assumes PT-RS is not present.

The higher layer parameter *PTRS-DownlinkConfig* provides the parameters *ptrs-MCSi*, *i*=1,2,3 and with values in range 0-29 when MCS Table 5.1.3.1-1 or MCS Table 5.1.3.1-3 is used and 0-28 when MCS Table 5.1.3.1-2 is used, respectively. *ptrs-MCS4* is not explicitly configured by higher layers but assumed 29 when MCS Table 5.1.3.1-1 or MCS Table 5.1.3.1-3 is used and 28 when MCS Table 5.1.3.1-2 is used, respectively. The higher layer parameter *frequencyDensity* in *PTRS-DownlinkConfig* provides the parameters *NRBi i*=0,1 with values in range 1-276.

If the higher layer parameter *PTRS-DownlinkConfig* indicates that the time density thresholds *ptrs-MCSi* = *ptrs-MCSi+1*, then the time density *LPT-RS* of the associated row where both these thresholds appear in Table 5.1.6.3-1 is disabled. If the higher layer parameter *PTRS-DownlinkConfig* indicates that the frequency density thresholds *NRBi* = *NRBi +1*, then the frequency density *KPTRS* of the associated row where both these thresholds appear in Table 5.1.6.3-2 is disabled.

If either or both of the parameters PT-RS time density (*LPT-RS*) and PT-RS frequency density (*KPT-RS*), shown in Table 5.1.6.3-1 and Table 5.1.6.3-2, indicates that 'PT-RS not present', the UE shall assume that PT-RS is not present.

When the UE is receiving a PDSCH with allocation duration of 2 symbols as defined in Clause 7.4.1.1.2 of [4, TS 38.211] and if *LPT-RS* is set to 2 or 4, the UE shall assume PT-RS is not transmitted.

When the UE is receiving a PDSCH with allocation duration of 4 symbols and if *LPT-RS* is set to 4, the UE shall assume PT-RS is not transmitted.

When a UE is receiving PDSCH for retransmission, if the UE is scheduled with an MCS index greater than V, where V=28 for MCS Table 5.1.3.1-1 and Table 5.1.3.1-3, and V=27 for MCS Table 5.1.3.1-2 respectively, the MCS for the PT-RS time-density determination is obtained from the DCI received for the same transport block in the initial transmission, which is smaller than or equal to V.

The DL DM-RS port(s) associated with a PT-RS port are assumed to be quasi co-located with respect to 'typeA' and 'typeD'. If a UE is scheduled with one codeword, the PT-RS antenna port is associated with the lowest indexed DM-RS antenna port among the DM-RS antenna ports assigned for the PDSCH.

If a UE is scheduled with two codewords, the PT-RS antenna port is associated with the lowest indexed DM-RS antenna port among the DM-RS antenna ports assigned for the codeword with the higher MCS. If the MCS indices of the two codewords are the same, the PT-RS antenna port is associated with the lowest indexed DM-RS antenna port assigned for codeword 0.

When a UE is not indicated with a DCI that DCI field '*Time domain resource assignment*' indicating an entry which contains *repetitionNumber* in *PDSCH-TimeDomainResourceAllocation*, and if the UE is configured with the higher layer parameter *maxNrofPorts* equal to *n2*, and if the UE is indicated with two TCI states by the codepoints of the DCI field *'Transmission Configuration Indication'* and DM-RS port(s) within two CDM groups in the DCI field '*Antenna Port(s)'*, the UE shall receive two PT-RS ports which are associated to the lowest indexed DM-RS port among the DM-RS ports corresponding to the first/second indicated TCI state, respectively.

When a UE configured by the higher layer parameter *repetitionScheme* set to 'fdmSchemeA*'* or 'fdmSchemeB*',* and the UE is indicated with two TCI states in a codepoint of the DCI field *'Transmission Configuration Indication'* and DM-RS port(s) within one CDM group in the DCI field '*Antenna Port(s)*', the UE shall receive a single PT-RS port which is associated with the lowest indexed DM-RS antenna port among the DM-RS antenna ports assigned for the PDSCH, a PT-RS frequency density is determined by the number of PRBs associated to each TCI state, and a PT-RS resource element mapping is associated to the allocated PRBs for each TCI state.

<omitted text>

# 5.2.2 Channel state information

## 5.2.2.1 Channel quality indicator (CQI)

The CQI indices and their interpretations are given in Table 5.2.2.1-2 or Table 5.2.2.1-4 for reporting CQI based on QPSK, 16QAM and 64QAM. The CQI indices and their interpretations are given in Table 5.2.2.1-3 for reporting CQI based on QPSK, 16QAM, 64QAM and 256QAM.

Based on an unrestricted observation interval in time unless specified otherwise in this Clause, and an unrestricted observation interval in frequency, the UE shall derive for each CQI value reported in uplink slot *n* the highest CQI index which satisfies the following condition:

- A single PDSCH transport block with a combination of modulation scheme, target code rate and transport block size corresponding to the CQI index, and occupying a group of downlink physical resource blocks termed the CSI reference resource, could be received with a transport block error probability not exceeding:
	- 0.1, if the higher layer parameter *cqi-Table* in *CSI-ReportConfig* configures 'table1' (corresponding to Table 5.2.2.1-2), or 'table2' (corresponding to Table 5.2.2.1-3), or
	- 0.00001, if the higher layer parameter *cqi-Table* in *CSI-ReportConfig* configures 'table3' (corresponding to Table 5.2.2.1-4).

If the higher layer parameter *timeRestrictionForChannelMeasurements* is set to "*notConfigured*", the UE shall derive the channel measurements for computing CSI value reported in uplink slot *n* based on only the NZP CSI-RS, no later than the CSI reference resource, (defined in TS 38.211[4]) associated with the CSI resource setting.

If the higher layer parameter *timeRestrictionForChannelMeasurements* in *CSI-ReportConfig* is set to "*Configured*", the UE shall derive the channel measurements for computing CSI reported in uplink slot *n* based on only the most recent, no later than the CSI reference resource, occasion of NZP CSI-RS (defined in [4, TS 38.211]) associated with the CSI resource setting.

If the higher layer parameter *timeRestrictionForInterferenceMeasurements* is set to "*notConfigured*", the UE shall derive the interference measurements for computing CSI value reported in uplink slot *n* based on only the CSI-IM and/or NZP CSI-RS for interference measurement no later than the CSI reference resource associated with the CSI resource setting.

If the higher layer parameter *timeRestrictionForInterferenceMeasurements* in *CSI-ReportConfig* is set to "*Configured*", the UE shall derive the interference measurements for computing the CSI value reported in uplink slot *n* based on the most recent, no later than the CSI reference resource, occasion of CSI-IM and/or NZP CSI-RS for interference measurement (defined in [4, TS 38.211]) associated with the CSI resource setting.

For each sub-band index *s,* a 2-bit sub-band differential CQI is defined as:

- Sub-band Offset level (*s*) = sub-band CQI index (*s*) wideband CQI index.
The mapping from the 2-bit sub-band differential CQI values to the offset level is shown in Table 5.2.2.1-1

| Sub-band differential CQI value | Offset level |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | ≥ 2 |
| 3 | ≤-1 |

## **Table 5.2.2.1-1: Mapping sub-band differential CQI value to offset level**

A combination of modulation scheme and transport block size corresponds to a CQI index if:

- the combination could be signaled for transmission on the PDSCH in the CSI reference resource according to the Transport Block Size determination described in Clause 5.1.3.2, and
- the modulation scheme is indicated by the CQI index, and
- the combination of transport block size and modulation scheme when applied to the reference resource results in the effective channel code rate which is the closest possible to the code rate indicated by the CQI index. If more than one combination of transport block size and modulation scheme results in an effective channel code rate equally close to the code rate indicated by the CQI index, only the combination with the smallest of such transport block sizes is relevant.

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 |  | out of range |  |
| 1 | QPSK | 78 | 0.1523 |
| 2 | QPSK | 120 | 0.2344 |
| 3 | QPSK | 193 | 0.3770 |
| 4 | QPSK | 308 | 0.6016 |
| 5 | QPSK | 449 | 0.8770 |
| 6 | QPSK | 602 | 1.1758 |
| 7 | 16QAM | 378 | 1.4766 |
| 8 | 16QAM | 490 | 1.9141 |
| 9 | 16QAM | 616 | 2.4063 |
| 10 | 64QAM | 466 | 2.7305 |
| 11 | 64QAM | 567 | 3.3223 |
| 12 | 64QAM | 666 | 3.9023 |
| 13 | 64QAM | 772 | 4.5234 |
| 14 | 64QAM | 873 | 5.1152 |
| 15 | 64QAM | 948 | 5.5547 |

### **Table 5.2.2.1-2: 4-bit CQI Table**

### **Table 5.2.2.1-3: 4-bit CQI Table 2**

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 |  | out of range |  |
| 1 | QPSK | 78 | 0.1523 |
| 2 | QPSK | 193 | 0.3770 |
| 3 | QPSK | 449 | 0.8770 |
| 4 | 16QAM | 378 | 1.4766 |
| 5 | 16QAM | 490 | 1.9141 |
| 6 | 16QAM | 616 | 2.4063 |
| 7 | 64QAM | 466 | 2.7305 |
| 8 | 64QAM | 567 | 3.3223 |
| 9 | 64QAM | 666 | 3.9023 |
| 10 | 64QAM | 772 | 4.5234 |
| 11 | 64QAM | 873 | 5.1152 |
| 12 | 256QAM | 711 | 5.5547 |
| 13 | 256QAM | 797 | 6.2266 |
| 14 | 256QAM | 885 | 6.9141 |
| 15 | 256QAM | 948 | 7.4063 |

| CQI index | modulation | code rate x 1024 | efficiency |
| --- | --- | --- | --- |
| 0 |  | out of range |  |
| 1 | QPSK | 30 | 0.0586 |
| 2 | QPSK | 50 | 0.0977 |
| 3 | QPSK | 78 | 0.1523 |
| 4 | QPSK | 120 | 0.2344 |
| 5 | QPSK | 193 | 0.3770 |
| 6 | QPSK | 308 | 0.6016 |
| 7 | QPSK | 449 | 0.8770 |
| 8 | QPSK | 602 | 1.1758 |
| 9 | 16QAM | 378 | 1.4766 |
| 10 | 16QAM | 490 | 1.9141 |
| 11 | 16QAM | 616 | 2.4063 |
| 12 | 64QAM | 466 | 2.7305 |
| 13 | 64QAM | 567 | 3.3223 |
| 14 | 64QAM | 666 | 3.9023 |
| 15 | 64QAM | 772 | 4.5234 |

### **Table 5.2.2.1-4: 4-bit CQI Table 3**

<omitted text>

