import re
import pandas as pd

# On importe le string avec les data qui nous intéressent
raw_string = """<option id="catalyst_affiliateid_"  value="684">.CO</option>
<option id="catalyst_affiliateid__1"  value="8503">01Booster (GAN)</option>
<option id="catalyst_affiliateid__2"  value="9663">185 Spadina</option>
<option id="catalyst_affiliateid__3"  value="15784">1909</option>
<option id="catalyst_affiliateid__4"  value="1302">21212</option>
<option id="catalyst_affiliateid__5"  value="9943">2iLabs</option>
<option id="catalyst_affiliateid__6"  value="8543">406 Labs (GAN)</option>
<option id="catalyst_affiliateid__7"  value="10543">42entrepreneurs</option>
<option id="catalyst_affiliateid__8"  value="2102">500 Durians</option>
<option id="catalyst_affiliateid__9"  value="524">500 Mexico City</option>
<option id="catalyst_affiliateid__10"  value="266">500 Startups</option>
<option id="catalyst_affiliateid__11"  value="19242">?rbita Aceleradora Startups</option>
<option id="catalyst_affiliateid__12"  value="17802">A3 Collider</option>
<option id="catalyst_affiliateid__13"  value="8545">ABQid (GAN)</option>
<option id="catalyst_affiliateid__14"  value="19400">AIC-ADT Baramati Foundation</option>
<option id="catalyst_affiliateid__15"  value="14502">AIC-RNTU Foundation</option>
<option id="catalyst_affiliateid__16"  value="15944">ALTS Capital Online Accelerator</option>
<option id="catalyst_affiliateid__17"  value="16838">APEX Bridge</option>
<option id="catalyst_affiliateid__18"  value="274">ATDC Select Startup</option>
<option id="catalyst_affiliateid__19"  value="1862">Acceleprise</option>
<option id="catalyst_affiliateid__20"  value="11543">Accelerace.io</option>
<option id="catalyst_affiliateid__21"  value="267">Accelerate Okanagan</option>
<option id="catalyst_affiliateid__22"  value="8505">Acceleration Business City (GAN)</option>
<option id="catalyst_affiliateid__23"  value="2382">Accelerator Academy</option>
<option id="catalyst_affiliateid__24"  value="268">AcceleratorHK</option>
<option id="catalyst_affiliateid__25"  value="17238">Act Venture Capital</option>
<option id="catalyst_affiliateid__26"  value="18000">Adventures Lab</option>
<option id="catalyst_affiliateid__27"  value="8583">AeroInnovate (GAN)</option>
<option id="catalyst_affiliateid__28"  value="19600">Alchemist Accelerator</option>
<option id="catalyst_affiliateid__29"  value="269">AlphaLab (GAN)</option>
<option id="catalyst_affiliateid__30"  value="8507">AltCity Bootcamp (GAN)</option>
<option id="catalyst_affiliateid__31"  value="15984">Amity Innovation Incubator</option>
<option id="catalyst_affiliateid__32"  value="8585">Ampersand-et (GAN)</option>
<option id="catalyst_affiliateid__33"  value="270">Amplify</option>
<option id="catalyst_affiliateid__34"  value="14862">Andhra Pradesh Innovation Society</option>
<option id="catalyst_affiliateid__35"  value="15584">AngelHack Winners</option>
<option id="catalyst_affiliateid__36"  value="19080">Anges Quebec</option>
<option id="catalyst_affiliateid__37"  value="19960">Antikythera Capital</option>
<option id="catalyst_affiliateid__38"  value="14422">Anubix Ventures</option>
<option id="catalyst_affiliateid__39"  value="487">AppCampus</option>
<option id="catalyst_affiliateid__40"  value="2983">AppWorks</option>
<option id="catalyst_affiliateid__41"  value="5943">Aquahack</option>
<option id="catalyst_affiliateid__42"  value="11823">Area 31</option>
<option id="catalyst_affiliateid__43"  value="16638">Arka Venture Labs</option>
<option id="catalyst_affiliateid__44"  value="6503">Arrow Electronics</option>
<option id="catalyst_affiliateid__45"  value="15864">Asociaci?n Fintech de Chile</option>
<option id="catalyst_affiliateid__46"  value="11463">Astana Hub</option>
<option id="catalyst_affiliateid__47"  value="3983">Augusta Cloud</option>
<option id="catalyst_affiliateid__48"  value="17638">Aurelia Ventures</option>
<option id="catalyst_affiliateid__49"  value="17358">Axeleo</option>
<option id="catalyst_affiliateid__50"  value="11663">B8 Accelerator</option>
<option id="catalyst_affiliateid__51"  value="14542">BIC Montpellier Mediterranee Metropole</option>
<option id="catalyst_affiliateid__52"  value="19440">Backed VC</option>
<option id="catalyst_affiliateid__53"  value="14020">Barcelona Tech City</option>
<option id="catalyst_affiliateid__54"  value="2825">Barclays Accelerator</option>
<option id="catalyst_affiliateid__55"  value="8303">Barclays Eagle Labs</option>
<option id="catalyst_affiliateid__56"  value="5743">Batchey</option>
<option id="catalyst_affiliateid__57"  value="10823">Baylor Business New Venture Competition</option>
<option id="catalyst_affiliateid__58"  value="275">Beta Ltd</option>
<option id="catalyst_affiliateid__59"  value="20080">Beta-i</option>
<option id="catalyst_affiliateid__60"  value="8509">Better Ventures (GAN)</option>
<option id="catalyst_affiliateid__61"  value="18720">Bilgiyi Ticarile?tirme Merkezi</option>
<option id="catalyst_affiliateid__62"  value="15866">BioCity Group</option>
<option id="catalyst_affiliateid__63"  value="15664">Biotechtown</option>
<option id="catalyst_affiliateid__64"  value="17880">Birmingham Enterprise Community</option>
<option id="catalyst_affiliateid__65"  value="8587">Bishop Ranch Innovation Intelligence Accelerator (BRIIA) (GAN)</option>
<option id="catalyst_affiliateid__66"  value="11547">Bizmaker</option>
<option id="catalyst_affiliateid__67"  value="14060">BlockSpaces</option>
<option id="catalyst_affiliateid__68"  value="9223">Blockchain Centre, Melbourne</option>
<option id="catalyst_affiliateid__69"  value="11867">Blockchain Hub Spain</option>
<option id="catalyst_affiliateid__70"  value="3543">Blue Ridge Labs @ Robin Hood (GAN)</option>
<option id="catalyst_affiliateid__71"  value="278">Blue Startups (GAN)</option>
<option id="catalyst_affiliateid__72"  value="11913">BlueOcean</option>
<option id="catalyst_affiliateid__73"  value="18520">BoB India</option>
<option id="catalyst_affiliateid__74"  value="8463">Boldstart Ventures</option>
<option id="catalyst_affiliateid__75"  value="281">BoomStartup (GAN)</option>
<option id="catalyst_affiliateid__76"  value="2022">Boomtown (GAN)</option>
<option id="catalyst_affiliateid__77"  value="282">Boot HK</option>
<option id="catalyst_affiliateid__78"  value="16144">BrainPlow</option>
<option id="catalyst_affiliateid__79"  value="10783">Buildily</option>
<option id="catalyst_affiliateid__80"  value="20200">Building Global Innovators</option>
<option id="catalyst_affiliateid__81"  value="767">Business Booster</option>
<option id="catalyst_affiliateid__82"  value="14302">CIIE, IIM Ahmedabad</option>
<option id="catalyst_affiliateid__83"  value="17038">CLOwork</option>
<option id="catalyst_affiliateid__84"  value="15504">CQIB</option>
<option id="catalyst_affiliateid__85"  value="8589">CREWW (GAN)</option>
<option id="catalyst_affiliateid__86"  value="19760">Cajamar Innova</option>
<option id="catalyst_affiliateid__87"  value="10743">Call For Code 42 Fremont - Winners</option>
<option id="catalyst_affiliateid__88"  value="14182">Call For Code Columbia</option>
<option id="catalyst_affiliateid__89"  value="10703">Call For Code Event - Kerala</option>
<option id="catalyst_affiliateid__90"  value="10903">Call For Code Event - Pitney Bowes</option>
<option id="catalyst_affiliateid__91"  value="10863">Call For Code Event - RBS</option>
<option id="catalyst_affiliateid__92"  value="14144">Call For Code RPI</option>
<option id="catalyst_affiliateid__93"  value="10585">Call For Code Sponsor - Delta</option>
<option id="catalyst_affiliateid__94"  value="10583">Call For Code Sponsor - Ingram Micro</option>
<option id="catalyst_affiliateid__95"  value="10343">Call For Code Sponsor - Persistent</option>
<option id="catalyst_affiliateid__96"  value="14142">Call For Code Syracuse</option>
<option id="catalyst_affiliateid__97"  value="14742">Call for Code - California Wildfires</option>
<option id="catalyst_affiliateid__98"  value="10623">Call for Code Authors</option>
<option id="catalyst_affiliateid__99"  value="12503">Call for Code Winners</option>
<option id="catalyst_affiliateid__100"  value="3823">Campus Emprear</option>
<option id="catalyst_affiliateid__101"  value="7903">Canopy Boulder (GAN)</option>
<option id="catalyst_affiliateid__102"  value="5063">Capital Factory</option>
<option id="catalyst_affiliateid__103"  value="8547">Carao Ventures (GAN)</option>
<option id="catalyst_affiliateid__104"  value="286">Catalyst Website</option>
<option id="catalyst_affiliateid__105"  value="288">Chinaccelerator (GAN)</option>
<option id="catalyst_affiliateid__106"  value="8743">CitiT4I</option>
<option id="catalyst_affiliateid__107"  value="289">CoCoon</option>
<option id="catalyst_affiliateid__108"  value="20520">CoCoon Capital</option>
<option id="catalyst_affiliateid__109"  value="8823">Cognitive Class</option>
<option id="catalyst_affiliateid__110"  value="4985">Collide Village</option>
<option id="catalyst_affiliateid__111"  value="291">Communitech HYPERDRIVE (GAN)</option>
<option id="catalyst_affiliateid__112"  value="12543">Conector</option>
<option id="catalyst_affiliateid__113"  value="20120">Conector Startup Accelerator</option>
<option id="catalyst_affiliateid__114"  value="292">Connective Hub</option>
<option id="catalyst_affiliateid__115"  value="11583">Copenhagenfintech</option>
<option id="catalyst_affiliateid__116"  value="17280">Corredores Digitais</option>
<option id="catalyst_affiliateid__117"  value="18840">Council.Club</option>
<option id="catalyst_affiliateid__118"  value="11949">Cuatrecasas Acelera</option>
<option id="catalyst_affiliateid__119"  value="293">Cyberport Entrepreneur Centre</option>
<option id="catalyst_affiliateid__120"  value="19000">D?zce Teknopark A.?.</option>
<option id="catalyst_affiliateid__121"  value="8511">DAI (GAN)</option>
<option id="catalyst_affiliateid__122"  value="8513">DFS Lab (GAN)</option>
<option id="catalyst_affiliateid__123"  value="19640">DIGITALHUB.DE</option>
<option id="catalyst_affiliateid__124"  value="14342">DILA Capital</option>
<option id="catalyst_affiliateid__125"  value="11343">DV / IBM Innovation Space</option>
<option id="catalyst_affiliateid__126"  value="19360">Darwin Innovation Hub</option>
<option id="catalyst_affiliateid__127"  value="18842">Darwin/HARDS</option>
<option id="catalyst_affiliateid__128"  value="15904">Data Lab VC</option>
<option id="catalyst_affiliateid__129"  value="10223">Day of Workshop</option>
<option id="catalyst_affiliateid__130"  value="16598">Deakin university</option>
<option id="catalyst_affiliateid__131"  value="17438">Decacorn Capital</option>
<option id="catalyst_affiliateid__132"  value="17118">Decelera</option>
<option id="catalyst_affiliateid__133"  value="11863">Demium</option>
<option id="catalyst_affiliateid__134"  value="8623">Desai Accelerator (GAN)</option>
<option id="catalyst_affiliateid__135"  value="1742">Developer</option>
<option id="catalyst_affiliateid__136"  value="8863">Digital Currency Group</option>
<option id="catalyst_affiliateid__137"  value="19720">Digital Health Germany</option>
<option id="catalyst_affiliateid__138"  value="11383">District Ventures</option>
<option id="catalyst_affiliateid__139"  value="15224">ELEVATE by TheVentury</option>
<option id="catalyst_affiliateid__140"  value="297">ERA (GAN)</option>
<option id="catalyst_affiliateid__141"  value="18242">ESIC</option>
<option id="catalyst_affiliateid__142"  value="17558">ETC Labs</option>
<option id="catalyst_affiliateid__143"  value="2142">East Ventures</option>
<option id="catalyst_affiliateid__144"  value="11423">Ejad Labs</option>
<option id="catalyst_affiliateid__145"  value="7383">Elevator (GAN)</option>
<option id="catalyst_affiliateid__146"  value="442">Eleven (GAN)</option>
<option id="catalyst_affiliateid__147"  value="8625">Elmspring (GAN)</option>
<option id="catalyst_affiliateid__148"  value="12143">Embarc Collective</option>
<option id="catalyst_affiliateid__149"  value="18760">Emera ideaHUB</option>
<option id="catalyst_affiliateid__150"  value="9543">Emirate Hack</option>
<option id="catalyst_affiliateid__151"  value="19880">EnergyLab</option>
<option id="catalyst_affiliateid__152"  value="8515">Engage Ventures (GAN)</option>
<option id="catalyst_affiliateid__153"  value="17078">Enpact Egypt</option>
<option id="catalyst_affiliateid__154"  value="15184">Enterprize Tasmania</option>
<option id="catalyst_affiliateid__155"  value="19200">Entrepreneur Club Winterthur</option>
<option id="catalyst_affiliateid__156"  value="2425">Entrepreneurs First</option>
<option id="catalyst_affiliateid__157"  value="16438">Entrepreneurs' Organization</option>
<option id="catalyst_affiliateid__158"  value="16358">Entrepreneurship and Product Innovation Center</option>
<option id="catalyst_affiliateid__159"  value="8627">Envestnet-Yodlee (GAN)</option>
<option id="catalyst_affiliateid__160"  value="17158">Esselerator</option>
<option id="catalyst_affiliateid__161"  value="10503">Expert Dojo</option>
<option id="catalyst_affiliateid__162"  value="18240">Exponential Impact</option>
<option id="catalyst_affiliateid__163"  value="299">Extreme Startups</option>
<option id="catalyst_affiliateid__164"  value="2222">F6S</option>
<option id="catalyst_affiliateid__165"  value="7063">F6S Alpha</option>
<option id="catalyst_affiliateid__166"  value="16024">FACIAP INOVALAB</option>
<option id="catalyst_affiliateid__167"  value="6263">FFL Accelerator</option>
<option id="catalyst_affiliateid__168"  value="14222">FOSSASIA</option>
<option id="catalyst_affiliateid__169"  value="11223">FalconX</option>
<option id="catalyst_affiliateid__170"  value="9143">Fat Cat Fab Lab</option>
<option id="catalyst_affiliateid__171"  value="15544">Female Founders Alliance</option>
<option id="catalyst_affiliateid__172"  value="16224">Finance Montreal</option>
<option id="catalyst_affiliateid__173"  value="20360">Fintech Community Frankfurt GmbH (TechQuartier)</option>
<option id="catalyst_affiliateid__174"  value="300">Flat6Labs (GAN)</option>
<option id="catalyst_affiliateid__175"  value="20440">Flexper</option>
<option id="catalyst_affiliateid__176"  value="302">Founder Fuel</option>
<option id="catalyst_affiliateid__177"  value="16264">Founder Institute</option>
<option id="catalyst_affiliateid__178"  value="1942">Founder Institute Toronto</option>
<option id="catalyst_affiliateid__179"  value="16104">Founderlist</option>
<option id="catalyst_affiliateid__180"  value="14702">Founderly</option>
<option id="catalyst_affiliateid__181"  value="304">Founders Network</option>
<option id="catalyst_affiliateid__182"  value="20160">Fundaci?n Empresa y Sociedad</option>
<option id="catalyst_affiliateid__183"  value="2383">Fundica</option>
<option id="catalyst_affiliateid__184"  value="12263">GSVlabs</option>
<option id="catalyst_affiliateid__185"  value="306">Galvanize</option>
<option id="catalyst_affiliateid__186"  value="307">GameFounders</option>
<option id="catalyst_affiliateid__187"  value="310">Gener8tor (GAN)</option>
<option id="catalyst_affiliateid__188"  value="16184">Gilda VC</option>
<option id="catalyst_affiliateid__189"  value="10143">Global Accelerator Network</option>
<option id="catalyst_affiliateid__190"  value="8663">Global Insurance Accelerator (GAN)</option>
<option id="catalyst_affiliateid__191"  value="15384">Global Startup Ecosystem Inc.</option>
<option id="catalyst_affiliateid__192"  value="10303">Global Technology Unit / GTU</option>
<option id="catalyst_affiliateid__193"  value="17760">GoFloaters</option>
<option id="catalyst_affiliateid__194"  value="4023">Grand Central Tech</option>
<option id="catalyst_affiliateid__195"  value="9503">Groupe Mutuel / Innopeaks</option>
<option id="catalyst_affiliateid__196"  value="15464">Growth Circuit</option>
<option id="catalyst_affiliateid__197"  value="16304">Grupa</option>
<option id="catalyst_affiliateid__198"  value="8665">H-Camp (GAN)</option>
<option id="catalyst_affiliateid__199"  value="315">H-Farm (GAN)</option>
<option id="catalyst_affiliateid__200"  value="9583">H2O Hackathon Stockton</option>
<option id="catalyst_affiliateid__201"  value="18120">HAG Ventures</option>
<option id="catalyst_affiliateid__202"  value="18880">HARDS</option>
<option id="catalyst_affiliateid__203"  value="9823">HHS Innovation Exchange</option>
<option id="catalyst_affiliateid__204"  value="16478">HI Capital</option>
<option id="catalyst_affiliateid__205"  value="11183">HK Cyberport</option>
<option id="catalyst_affiliateid__206"  value="11143">HKSTP</option>
<option id="catalyst_affiliateid__207"  value="19240">Hack+</option>
<option id="catalyst_affiliateid__208"  value="8629">Hackmind (GAN)</option>
<option id="catalyst_affiliateid__209"  value="1784">Harvard Innovation Lab</option>
<option id="catalyst_affiliateid__210"  value="18560">Hatch CoLab</option>
<option id="catalyst_affiliateid__211"  value="1664">Hong Kong Science Park</option>
<option id="catalyst_affiliateid__212"  value="20040">Hub Cerrado</option>
<option id="catalyst_affiliateid__213"  value="14062">HubHub</option>
<option id="catalyst_affiliateid__214"  value="5223">IBM Alpha Zone</option>
<option id="catalyst_affiliateid__215"  value="11303">IBM Blockchain Accelerator</option>
<option id="catalyst_affiliateid__216"  value="9783">IBM Code Day - Montevideo</option>
<option id="catalyst_affiliateid__217"  value="7943">IBM Developer Advocate</option>
<option id="catalyst_affiliateid__218"  value="17398">IBM Hyper Protect Accelerator</option>
<option id="catalyst_affiliateid__219"  value="11503">IBM Innovation Space - Hamilton</option>
<option id="catalyst_affiliateid__220"  value="12063">IBM Q Startup Program</option>
<option id="catalyst_affiliateid__221"  value="1222">IBM Referral</option>
<option id="catalyst_affiliateid__222"  value="9743">IBM Scale Zone</option>
<option id="catalyst_affiliateid__223"  value="14902">IBM Services</option>
<option id="catalyst_affiliateid__224"  value="8631">ICELab (GAN)</option>
<option id="catalyst_affiliateid__225"  value="16398">ICTAM</option>
<option id="catalyst_affiliateid__226"  value="8703">IDEABOOST (GAN)</option>
<option id="catalyst_affiliateid__227"  value="11703">IITM Incubation Cell</option>
<option id="catalyst_affiliateid__228"  value="18960">INCUBATE</option>
<option id="catalyst_affiliateid__229"  value="18680">Ilab Accelerator</option>
<option id="catalyst_affiliateid__230"  value="11903">Impact Accelerator</option>
<option id="catalyst_affiliateid__231"  value="18640">Impact Ventures</option>
<option id="catalyst_affiliateid__232"  value="8517">IndiaAccelerator (GAN)</option>
<option id="catalyst_affiliateid__233"  value="16758">Ingressive LLC</option>
<option id="catalyst_affiliateid__234"  value="14582">Initialized Capital</option>
<option id="catalyst_affiliateid__235"  value="19160">InnoStart Capital</option>
<option id="catalyst_affiliateid__236"  value="10463">Innogy Innovation Hub</option>
<option id="catalyst_affiliateid__237"  value="11915">Innolab</option>
<option id="catalyst_affiliateid__238"  value="13980">Innovate Canmore</option>
<option id="catalyst_affiliateid__239"  value="11023">Innovate Celebrate</option>
<option id="catalyst_affiliateid__240"  value="14822">Innovate! Longmont</option>
<option id="catalyst_affiliateid__241"  value="15744">InnovatetheNext</option>
<option id="catalyst_affiliateid__242"  value="9103">Innovation Boulevard</option>
<option id="catalyst_affiliateid__243"  value="10183">Innovation Place</option>
<option id="catalyst_affiliateid__244"  value="16678">InnovationHQ Workspace</option>
<option id="catalyst_affiliateid__245"  value="14942">Innovatum Startup</option>
<option id="catalyst_affiliateid__246"  value="11943">Insomnia</option>
<option id="catalyst_affiliateid__247"  value="9183">Inspire 9, Melbourne</option>
<option id="catalyst_affiliateid__248"  value="18400">Instituto Polit?cnico de Set?bal</option>
<option id="catalyst_affiliateid__249"  value="13940">InsurLab Germany</option>
<option id="catalyst_affiliateid__250"  value="9063">IntelaEdu</option>
<option id="catalyst_affiliateid__251"  value="9023">Intelainc</option>
<option id="catalyst_affiliateid__252"  value="16718">Inventure</option>
<option id="catalyst_affiliateid__253"  value="17680">Investopad</option>
<option id="catalyst_affiliateid__254"  value="8519">Iowa AgriTech Accelerator (GAN)</option>
<option id="catalyst_affiliateid__255"  value="3903">Iowa Startup Accelerator (GAN)</option>
<option id="catalyst_affiliateid__256"  value="11263">IvyCamp</option>
<option id="catalyst_affiliateid__257"  value="325">JFDI.Asia (GAN)</option>
<option id="catalyst_affiliateid__258"  value="3103">Jaarvis Accelerator</option>
<option id="catalyst_affiliateid__259"  value="16918">Jazz xlr8</option>
<option id="catalyst_affiliateid__260"  value="11745">Kasvu Open</option>
<option id="catalyst_affiliateid__261"  value="14982">Kiuas</option>
<option id="catalyst_affiliateid__262"  value="19680">Kivuhub</option>
<option id="catalyst_affiliateid__263"  value="14382">Konvoy Ventures</option>
<option id="catalyst_affiliateid__264"  value="10103">Kubernetes 101</option>
<option id="catalyst_affiliateid__265"  value="8707">LUISS ENLABS (GAN)</option>
<option id="catalyst_affiliateid__266"  value="12583">La Salle Technova</option>
<option id="catalyst_affiliateid__267"  value="9983">Lair East Labs Accelerator</option>
<option id="catalyst_affiliateid__268"  value="11905">Lanzadera</option>
<option id="catalyst_affiliateid__269"  value="1022">Launch</option>
<option id="catalyst_affiliateid__270"  value="1786">Launch Academy</option>
<option id="catalyst_affiliateid__271"  value="8705">Launch Alaska (GAN)</option>
<option id="catalyst_affiliateid__272"  value="422">LaunchHub</option>
<option id="catalyst_affiliateid__273"  value="8633">Lighthouse Labs (GAN)</option>
<option id="catalyst_affiliateid__274"  value="13900">Lot Fourteen</option>
<option id="catalyst_affiliateid__275"  value="12103">MDR Labs</option>
<option id="catalyst_affiliateid__276"  value="338">MIT</option>
<option id="catalyst_affiliateid__277"  value="14102">MTS Startup Hub</option>
<option id="catalyst_affiliateid__278"  value="335">MaRS Commons</option>
<option id="catalyst_affiliateid__279"  value="8423">Madrona Ventures Labs</option>
<option id="catalyst_affiliateid__280"  value="17640">Mainstage Incubator</option>
<option id="catalyst_affiliateid__281"  value="336">MassChallenge</option>
<option id="catalyst_affiliateid__282"  value="10983">Mercia Tech</option>
<option id="catalyst_affiliateid__283"  value="18200">Monterrey Digital Hub</option>
<option id="catalyst_affiliateid__284"  value="339">MuckerLab (GAN)</option>
<option id="catalyst_affiliateid__285"  value="15024">MutliPass Ventures</option>
<option id="catalyst_affiliateid__286"  value="9423">NASSCOM 10K</option>
<option id="catalyst_affiliateid__287"  value="8667">NIIC (GAN)</option>
<option id="catalyst_affiliateid__288"  value="5703">NUMA (GAN)</option>
<option id="catalyst_affiliateid__289"  value="346">NXTP Labs (GAN)</option>
<option id="catalyst_affiliateid__290"  value="16064">NYDesigns</option>
<option id="catalyst_affiliateid__291"  value="18600">Newchip Accelerator</option>
<option id="catalyst_affiliateid__292"  value="8635">Nex Cubed (Nex3) (GAN)</option>
<option id="catalyst_affiliateid__293"  value="10663">Nexea</option>
<option id="catalyst_affiliateid__294"  value="821">Next Canada</option>
<option id="catalyst_affiliateid__295"  value="12423">NextAI</option>
<option id="catalyst_affiliateid__296"  value="344">NextSpace</option>
<option id="catalyst_affiliateid__297"  value="14662">Nordic Innovation House</option>
<option id="catalyst_affiliateid__298"  value="11907">Oarsis</option>
<option id="catalyst_affiliateid__299"  value="11103">OneDay</option>
<option id="catalyst_affiliateid__300"  value="20320">Open Water Accelerator</option>
<option id="catalyst_affiliateid__301"  value="15424">Orion Parque Tecnol?gico</option>
<option id="catalyst_affiliateid__302"  value="8709">OrionStartups (GAN)</option>
<option id="catalyst_affiliateid__303"  value="349">Other</option>
<option id="catalyst_affiliateid__304"  value="15704">Oui Capital</option>
<option id="catalyst_affiliateid__305"  value="16558">Oxford Garage</option>
<option id="catalyst_affiliateid__306"  value="18800">Ozyegin University</option>
<option id="catalyst_affiliateid__307"  value="16798">Padup Ventures</option>
<option id="catalyst_affiliateid__308"  value="10063">PanaceaStars</option>
<option id="catalyst_affiliateid__309"  value="18160">Pantera Capital</option>
<option id="catalyst_affiliateid__310"  value="10383">PlanetM</option>
<option id="catalyst_affiliateid__311"  value="19480">Play Ventures</option>
<option id="catalyst_affiliateid__312"  value="8669">PlayLabs@MIT (GAN)</option>
<option id="catalyst_affiliateid__313"  value="5783">Plug and Play</option>
<option id="catalyst_affiliateid__314"  value="352">Plug-in @ Blk 71</option>
<option id="catalyst_affiliateid__315"  value="14984">Powers & Roots</option>
<option id="catalyst_affiliateid__316"  value="15104">Praxis Center for Venture Development</option>
<option id="catalyst_affiliateid__317"  value="17960">Professional Mantra</option>
<option id="catalyst_affiliateid__318"  value="20000">Propellant Labs</option>
<option id="catalyst_affiliateid__319"  value="7863">QC FinTech</option>
<option id="catalyst_affiliateid__320"  value="6703">R/GA (GAN)</option>
<option id="catalyst_affiliateid__321"  value="9343">RWDevCon18</option>
<option id="catalyst_affiliateid__322"  value="10943">Raed Ventures</option>
<option id="catalyst_affiliateid__323"  value="15624">RealCo</option>
<option id="catalyst_affiliateid__324"  value="14782">RealTechX Pty Limited</option>
<option id="catalyst_affiliateid__325"  value="9065">Reassigned Intela</option>
<option id="catalyst_affiliateid__326"  value="17840">Red Electrica</option>
<option id="catalyst_affiliateid__327"  value="358">Referral</option>
<option id="catalyst_affiliateid__328"  value="17518">Ripple Ventures</option>
<option id="catalyst_affiliateid__329"  value="10023">Rise HK</option>
<option id="catalyst_affiliateid__330"  value="9187">River City Labs, Brisbane</option>
<option id="catalyst_affiliateid__331"  value="17720">Runway Innovation Hub</option>
<option id="catalyst_affiliateid__332"  value="360">Ryerson DMZ</option>
<option id="catalyst_affiliateid__333"  value="18440">SANDIP INCUBATOR ASSOCIATION</option>
<option id="catalyst_affiliateid__334"  value="19840">SEK Lab EdTech Accelerator</option>
<option id="catalyst_affiliateid__335"  value="9623">SF Hack</option>
<option id="catalyst_affiliateid__336"  value="3943">SOSV</option>
<option id="catalyst_affiliateid__337"  value="8637">STING (GAN)</option>
<option id="catalyst_affiliateid__338"  value="17278">STYLABS</option>
<option id="catalyst_affiliateid__339"  value="375">SXSW</option>
<option id="catalyst_affiliateid__340"  value="15344">Sand Box</option>
<option id="catalyst_affiliateid__341"  value="19800">Santa Clara University - Bronco Venture Accelerator</option>
<option id="catalyst_affiliateid__342"  value="8695">Scratchpad Accelerator (GAN)</option>
<option id="catalyst_affiliateid__343"  value="982">Seattle Tech Meetup</option>
<option id="catalyst_affiliateid__344"  value="8671">SecureSet (GAN)</option>
<option id="catalyst_affiliateid__345"  value="17920">Seed + speed Ventures</option>
<option id="catalyst_affiliateid__346"  value="8673">Seed Fuel - Rowad (GAN)</option>
<option id="catalyst_affiliateid__347"  value="421">SeedCamp</option>
<option id="catalyst_affiliateid__348"  value="11909">Seedrocket</option>
<option id="catalyst_affiliateid__349"  value="3623">Seedstars World</option>
<option id="catalyst_affiliateid__350"  value="11911">Ship2B</option>
<option id="catalyst_affiliateid__351"  value="16878">Silicon Valley in Your Pocket</option>
<option id="catalyst_affiliateid__352"  value="20280">Sistema Asia</option>
<option id="catalyst_affiliateid__353"  value="17198">SixBerries</option>
<option id="catalyst_affiliateid__354"  value="8675">Skystar Ventures (GAN)</option>
<option id="catalyst_affiliateid__355"  value="18080">Sling Capital</option>
<option id="catalyst_affiliateid__356"  value="9189">Slingshot, Australia</option>
<option id="catalyst_affiliateid__357"  value="16998">Smart Araucan?a</option>
<option id="catalyst_affiliateid__358"  value="19520">Smart Infrastructure Ventures</option>
<option id="catalyst_affiliateid__359"  value="9903">SmartGateVC</option>
<option id="catalyst_affiliateid__360"  value="17962">Social Alpha</option>
<option id="catalyst_affiliateid__361"  value="9185">Spacecubed, Perth</option>
<option id="catalyst_affiliateid__362"  value="1864">SparkLabs (GAN)</option>
<option id="catalyst_affiliateid__363"  value="902">Spartups</option>
<option id="catalyst_affiliateid__364"  value="8711">Speen@BDD (GAN)</option>
<option id="catalyst_affiliateid__365"  value="12343">Spherik Accelerator</option>
<option id="catalyst_affiliateid__366"  value="1142">Sprint Accelerator (GAN)</option>
<option id="catalyst_affiliateid__367"  value="11585">Starfab_Taira</option>
<option id="catalyst_affiliateid__368"  value="12623">Starfish Network</option>
<option id="catalyst_affiliateid__369"  value="6383">Start it @kbc (GAN)</option>
<option id="catalyst_affiliateid__370"  value="1262">StartCo. (GAN)</option>
<option id="catalyst_affiliateid__371"  value="363">StartFast Venture Accelerator (GAN)</option>
<option id="catalyst_affiliateid__372"  value="8677">StartZone (GAN)</option>
<option id="catalyst_affiliateid__373"  value="1306">Startup Brazil</option>
<option id="catalyst_affiliateid__374"  value="365">Startup Chile</option>
<option id="catalyst_affiliateid__375"  value="1304">Startup Farm</option>
<option id="catalyst_affiliateid__376"  value="4025">Startup Grind</option>
<option id="catalyst_affiliateid__377"  value="1182">Startup Haven</option>
<option id="catalyst_affiliateid__378"  value="542">Startup Monthly</option>
<option id="catalyst_affiliateid__379"  value="368">Startup Reykjavik (GAN)</option>
<option id="catalyst_affiliateid__380"  value="369">Startup Sauna</option>
<option id="catalyst_affiliateid__381"  value="1502">Startup Socials</option>
<option id="catalyst_affiliateid__382"  value="4787">Startup Studio</option>
<option id="catalyst_affiliateid__383"  value="11623">Startup TW</option>
<option id="catalyst_affiliateid__384"  value="9263">Startup Victoria, Victoria</option>
<option id="catalyst_affiliateid__385"  value="371">Startup Weekend</option>
<option id="catalyst_affiliateid__386"  value="862">Startup World</option>
<option id="catalyst_affiliateid__387"  value="482">Startup Yard (GAN)</option>
<option id="catalyst_affiliateid__388"  value="18762">StartupX</option>
<option id="catalyst_affiliateid__389"  value="372">Startupbootcamp (GAN)</option>
<option id="catalyst_affiliateid__390"  value="2863">StartupsHK</option>
<option id="catalyst_affiliateid__391"  value="11545">Suinkubator</option>
<option id="catalyst_affiliateid__392"  value="12463">Sultan Ventures</option>
<option id="catalyst_affiliateid__393"  value="8521">Summer Institute (GAN)</option>
<option id="catalyst_affiliateid__394"  value="19040">Suncorp</option>
<option id="catalyst_affiliateid__395"  value="15824">Sustainable Ocean Alliance</option>
<option id="catalyst_affiliateid__396"  value="4543">T-HUB</option>
<option id="catalyst_affiliateid__397"  value="9225">Tank Stream Labs, Sydney</option>
<option id="catalyst_affiliateid__398"  value="378">Tech Crunch</option>
<option id="catalyst_affiliateid__399"  value="12023">Tech Garden</option>
<option id="catalyst_affiliateid__400"  value="379">Tech Wildcatters (GAN)</option>
<option id="catalyst_affiliateid__401"  value="18920">TechGrind Incubator & Venture Capital</option>
<option id="catalyst_affiliateid__402"  value="484">TechPeaks</option>
<option id="catalyst_affiliateid__403"  value="13860">TechPlace</option>
<option id="catalyst_affiliateid__404"  value="19320">Techcelerate</option>
<option id="catalyst_affiliateid__405"  value="19560">Technologiegr?nderfonds Sachsen</option>
<option id="catalyst_affiliateid__406"  value="9703">Techstars</option>
<option id="catalyst_affiliateid__407"  value="8639">Techstars Adelaide (GAN)</option>
<option id="catalyst_affiliateid__408"  value="8679">Techstars Alexa (GAN)</option>
<option id="catalyst_affiliateid__409"  value="8681">Techstars Anywhere (GAN)</option>
<option id="catalyst_affiliateid__410"  value="7789">Techstars Atlanta (Cox Enterprises) (GAN)</option>
<option id="catalyst_affiliateid__411"  value="7743">Techstars Austin (GAN)</option>
<option id="catalyst_affiliateid__412"  value="8523">Techstars Autonomous (GAN)</option>
<option id="catalyst_affiliateid__413"  value="8641">Techstars Barclays Cape Town (GAN)</option>
<option id="catalyst_affiliateid__414"  value="8643">Techstars Barclays London (GAN)</option>
<option id="catalyst_affiliateid__415"  value="8683">Techstars Barclays NYC (GAN)</option>
<option id="catalyst_affiliateid__416"  value="8685">Techstars Barclays Tel Aviv (GAN)</option>
<option id="catalyst_affiliateid__417"  value="3463">Techstars Berlin (GAN)</option>
<option id="catalyst_affiliateid__418"  value="381">Techstars Boston (GAN)</option>
<option id="catalyst_affiliateid__419"  value="382">Techstars Boulder (GAN)</option>
<option id="catalyst_affiliateid__420"  value="383">Techstars Chicago (GAN)</option>
<option id="catalyst_affiliateid__421"  value="384">Techstars Cloud</option>
<option id="catalyst_affiliateid__422"  value="8645">Techstars Comcast (GAN)</option>
<option id="catalyst_affiliateid__423"  value="8525">Techstars Dubai (GAN)</option>
<option id="catalyst_affiliateid__424"  value="8713">Techstars Energy Australia (GAN)</option>
<option id="catalyst_affiliateid__425"  value="7747">Techstars Healthcare (Cedars-Sinai) (GAN)</option>
<option id="catalyst_affiliateid__426"  value="7749">Techstars IoT (GAN)</option>
<option id="catalyst_affiliateid__427"  value="7795">Techstars Kansas City (GAN)</option>
<option id="catalyst_affiliateid__428"  value="2823">Techstars London (GAN)</option>
<option id="catalyst_affiliateid__429"  value="7751">Techstars Los Angeles (GAN)</option>
<option id="catalyst_affiliateid__430"  value="3507">Techstars Metro Retail  (GAN)</option>
<option id="catalyst_affiliateid__431"  value="8687">Techstars Mobility (GAN)</option>
<option id="catalyst_affiliateid__432"  value="7785">Techstars Music (GAN)</option>
<option id="catalyst_affiliateid__433"  value="385">Techstars New York (GAN)</option>
<option id="catalyst_affiliateid__434"  value="8647">Techstars Paris (GAN)</option>
<option id="catalyst_affiliateid__435"  value="386">Techstars Patriot Boot Camp</option>
<option id="catalyst_affiliateid__436"  value="7787">Techstars Retail (Target) (GAN)</option>
<option id="catalyst_affiliateid__437"  value="8649">Techstars SAP.io (GAN)</option>
<option id="catalyst_affiliateid__438"  value="387">Techstars Seattle (GAN)</option>
<option id="catalyst_affiliateid__439"  value="8689">Techstars Toronto (GAN)</option>
<option id="catalyst_affiliateid__440"  value="10263">Tel Aviv Blockchain</option>
<option id="catalyst_affiliateid__441"  value="2783">Telefonica Open Future</option>
<option id="catalyst_affiliateid__442"  value="19120">Ten Eleven Ventures</option>
<option id="catalyst_affiliateid__443"  value="11783">Terkko Health Hub</option>
<option id="catalyst_affiliateid__444"  value="389">Tetuan Valley</option>
<option id="catalyst_affiliateid__445"  value="12303">Texas Healthcare Challenge</option>
<option id="catalyst_affiliateid__446"  value="14262">The BHub</option>
<option id="catalyst_affiliateid__447"  value="284">The Brandery (GAN)</option>
<option id="catalyst_affiliateid__448"  value="11865">The Cube</option>
<option id="catalyst_affiliateid__449"  value="621">The DEC</option>
<option id="catalyst_affiliateid__450"  value="8535">The Edge (GAN)</option>
<option id="catalyst_affiliateid__451"  value="17318">The Fabric</option>
<option id="catalyst_affiliateid__452"  value="394">The Hive</option>
<option id="catalyst_affiliateid__453"  value="9265">The Moonshine Laboratory, South Australia</option>
<option id="catalyst_affiliateid__454"  value="12383">The Studio, Australia</option>
<option id="catalyst_affiliateid__455"  value="8715">TheFactory (GAN)</option>
<option id="catalyst_affiliateid__456"  value="9863">ThinkTank Innovation </option>
<option id="catalyst_affiliateid__457"  value="20400">TiE ScaleUp</option>
<option id="catalyst_affiliateid__458"  value="11145">TiE50</option>
<option id="catalyst_affiliateid__459"  value="5663">TiE50 2016 Winner</option>
<option id="catalyst_affiliateid__460"  value="8023">TiE50 2017</option>
<option id="catalyst_affiliateid__461"  value="8529">TopSeedsLab (GAN)</option>
<option id="catalyst_affiliateid__462"  value="8531">Travelport Labs (GAN)</option>
<option id="catalyst_affiliateid__463"  value="8983">TreeHacks</option>
<option id="catalyst_affiliateid__464"  value="15304">Tribe Accelerator</option>
<option id="catalyst_affiliateid__465"  value="9972">Tulane Albert Lepage Center for Entrepreneurship and Innovation</option>
<option id="catalyst_affiliateid__466"  value="15144">Turkish Technology Team Foundation Startup Center</option>
<option id="catalyst_affiliateid__467"  value="1982">UC Berkeley</option>
<option id="catalyst_affiliateid__468"  value="18280">UNSW Founders 10x Accelerator</option>
<option id="catalyst_affiliateid__469"  value="18480">UPTEC</option>
<option id="catalyst_affiliateid__470"  value="8717">UTEC Ventures (GAN)</option>
<option id="catalyst_affiliateid__471"  value="9463">UW Co-Motion</option>
<option id="catalyst_affiliateid__472"  value="1782">Unified Cloud Program</option>
<option id="catalyst_affiliateid__473"  value="7543">UpRamp (GAN)</option>
<option id="catalyst_affiliateid__474"  value="14622">Upward Labs</option>
<option id="catalyst_affiliateid__475"  value="16958">UrbanUs</option>
<option id="catalyst_affiliateid__476"  value="19280">Urbantech</option>
<option id="catalyst_affiliateid__477"  value="19920">Uretken Akademi</option>
<option id="catalyst_affiliateid__478"  value="19122">VGU GCEC Incubation Center</option>
<option id="catalyst_affiliateid__479"  value="8533">Valley Venture Mentors (VVM) (GAN)</option>
<option id="catalyst_affiliateid__480"  value="5103">Velocity (GAN)</option>
<option id="catalyst_affiliateid__481"  value="18040">Venture Lane</option>
<option id="catalyst_affiliateid__482"  value="17598">Venture Villa Accelerator</option>
<option id="catalyst_affiliateid__483"  value="14462">Venture X</option>
<option id="catalyst_affiliateid__484"  value="12223">VentureLab</option>
<option id="catalyst_affiliateid__485"  value="11743">Vertical</option>
<option id="catalyst_affiliateid__486"  value="11945">ViaGalicia</option>
<option id="catalyst_affiliateid__487"  value="11983">Village by CA Paris</option>
<option id="catalyst_affiliateid__488"  value="8691">Vocus UpStart (GAN)</option>
<option id="catalyst_affiliateid__489"  value="17478">Vodafone</option>
<option id="catalyst_affiliateid__490"  value="502">Volta</option>
<option id="catalyst_affiliateid__491"  value="20480">Warwick Manufacturing Group, WMG Accelerator</option>
<option id="catalyst_affiliateid__492"  value="402">Wayra</option>
<option id="catalyst_affiliateid__493"  value="663">Wayra Brazil</option>
<option id="catalyst_affiliateid__494"  value="3223">WeWork NYC</option>
<option id="catalyst_affiliateid__495"  value="403">WeWork SF</option>
<option id="catalyst_affiliateid__496"  value="10423">WeXelerate</option>
<option id="catalyst_affiliateid__497"  value="4383">Web Summit</option>
<option id="catalyst_affiliateid__498"  value="11063">Westartup</option>
<option id="catalyst_affiliateid__499"  value="7023">X-Prize</option>
<option id="catalyst_affiliateid__500"  value="8693">XEdu (GAN)</option>
<option id="catalyst_affiliateid__501"  value="17800">XLerateHealth</option>
<option id="catalyst_affiliateid__502"  value="407">Y Combinator</option>
<option id="catalyst_affiliateid__503"  value="9303">York Butter Factory, Victoria (YBF Ventures)</option>
<option id="catalyst_affiliateid__504"  value="15264">Youngstown Business Inucubator</option>
<option id="catalyst_affiliateid__505"  value="15064">ZOLLHOF</option>
<option id="catalyst_affiliateid__506"  value="11947">Zarpamos</option>
<option id="catalyst_affiliateid__507"  value="2104">Zone Startups</option>"""

# On créé une liste vide qui contiendra les données retraitées
liste_finale = []

# On sépare la string pour en faire une liste
elements = re.split("""<option id="catalyst_affiliateid__[0-9]*"  value="[0-9]*">""", raw_string)

# On itère pour traîter les données et les stocker dans la "liste_finale"
for element in elements:
    liste_finale.append(element.replace("</option>\n", ""))

# dataframe Name and Age columns
df = pd.DataFrame({'Affiliates': liste_finale})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Affiliates Startup with IBM.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
