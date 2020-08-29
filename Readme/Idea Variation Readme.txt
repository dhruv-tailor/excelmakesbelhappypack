###################################################################
###################################################################
####### Idea Variation Mod by flogi
###################################################################
###################################################################


###################################################################
####### Version 3.3.2 (2bf4)
###################################################################

###################################################################
####### General
###################################################################

- Fixed: Removed some old test code in the government reforms that wasn't supposed to be there anymore
- Fixed: Localisation Issue where Conscription and Mercenary Army Policy localisation were interchanged
- Fixed: Noble Elite Reform will now give the correct idea group (Republic)
- Fixed: The Dynastic Decision is now only available when you're not in a consort regency (fixing consort regency bug)
- Enacting the Dynasty Decision now gives Agressive Expansion, but costs less money and lost the cooldown
- The Dynastic Unification CB gives a bit less AE
- The AI should not do Summer Feasts anymore when in debt
- AI won't lose any stability anymore upon changing government type and has reduced corruption cost for doing so
- Endgame interface reworked to avoid crashes


###################################################################
####### Version 3.3.1 (1420)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted building syntax so that compatibility issues with events and missions
- The edict decreasing autonomy is now cheaper on the state maintenance
- Fixed some localisation issues
- Improved Idea description (English) (Big thanks to Picasso Sparks)
- Estates can now control a province that has a seat of parliament
- The Council will no get influence from advisors instead of estates (avoids an issue where the influence could end up on one faction only)

###################################################################
####### Buildings
###################################################################

- Buffed the trade building chain a bit
- The land forcelimit building chain is now not deleted when in province that has a building is not in a state

###################################################################
####### Government Reforms & Estates
###################################################################

- Financing a project and giving out a favor will no longer decrease loyalty of other estates
- Financing project now gives 15 loyalty instead of 10
- Estate bonuses from government reforms were buffed considerably
- Government Reforms will reduce less legitimacy, devotion and rep. tradition
- Changing government will no longer cost reforms but 3 stability and reduced reformprogress for 10 years

###################################################################
####### Version 3.3.0 (2379)
###################################################################


###################################################################
####### General
###################################################################

- Units will no longer loose drill over time, but still when taking losses obviously
- The russian streltsy button now only gives infantry equal to 15% of forcelimit
- Hardmode (AI Boni) now gives free policies for AI
- Moved the late game fortress buildings a bit back in tech
- Reduced the additional attrition given by fortress buildings, was a bit too high
- Fixed: Development Malus for provinces over 152 not working as it should have
- Changing a government reform in a tier now costs 5 corruption and 1 stability instead of 10 corruption
- Regiments that drill will now get 10 more discipline instead of the fire and shock boni
- Made Legitimacy more impactful
- Innovativeness, instead of 10% for all power cost now gives at 100%: 10% tech cost, 10% idea cost, 25 max absolutism, +1 yearly absolutism, 3 splendor
- Removed free base policies
- Added more late game fire for cav by tech
- Removed the Development Cost Reduction from trade centers affecting the whole state
- Naval Combat System fine tuned (Galley vs Heavy Ship Balancing) 
- Scaling in Ages: More Global Engagement Width (Better Fleet Management)

###################################################################
####### Government Reforms
###################################################################

- Added over 80 new government reforms (not counting double ones in some government types)
- Completely reworked reforms for monarchies, republics and theocracies
- Monarchies, republics and theocracies can now change their government type in the first reform tier

###################################################################
####### Estates 
###################################################################

- Completely reworked estates
- Estates are now available for most government types
- Estates will now only provide substantial bonuses when they are loyal
- Provinces that are controlled by estates will no longer have a set autonomy of 25, but increase the local autonomy of the province if they are neutral or disloyal, but reduce it when they are loyal
- Provinces that are controlled by estates will only give good bonuses when the estate is loyal
- Added many new estate interactions for nearly every estate
- Reworked some vanilla estate interactions

###################################################################
####### Ideas & Policies
###################################################################

- Reworked Shock Ideas
- Standing Army now has reduced drill decay of 50% (essentially reducing the drill you loose when you reinforce)
- The policy activated by the influence idea group now gives +25 liberty desire
- Centralism Ideas built time reduced to 33% (from 50)
- It is no longer possible to get 100% built time reduction from policies and ideas alone
- Removed Adm. Tech Cost from Jurisprudence Ideas, added legitimacy equivalent bonuses
- Prestige from Dynstic Ideas was improved from 0.5 to 1
- Added missionary maintenance for religious idea groups
- Nerfed Influence Ideas (AE and Forcelimit)
- Republican Ideas now only give 0.5 republican tradition, but instead give 15% government reform progress
- Propaganda Ideas gained 15% government reform progress
- The policy of Imperialism Ideas changed from 100% core decay to 50%
- Innovative Ideas now give 33% government reform progress and 15% innovativeness gain instead of the free policies
- Added expel minorities for exploration idea group
- Nerfed naval and land forcelimit in Imperialism Ideas
- Added 15% government reform progress to Assimilation Ideas
- Tactic Ideas got 33% global supply limit modifier

###################################################################
####### Version 3.2.2 (XXXX)
###################################################################

###################################################################
####### Allgemein
###################################################################

- Small fixes here and there
- Added 6 more buildings slots to the interface
- Changed the Settings event where you can deactivate additional state maintenance cost by buildings so that it now also deactivates additional development cost by buildings


###################################################################
####### Version 3.2.1 (XXXX)
###################################################################

###################################################################
####### General 
###################################################################

- Adjusted files to work with the new patch
- Reworked advisor interface to allow better looking scrolling
- The government building (Court) can only be built once in a state but will grant its bonus for the whole state by using province modifiers. 
  You can not built more buildings at the same time when the government buildings are startet and the building has to be leveled up from 1 to 4 for engine reasons 
- Adjusted edicts accordingly (you will get better edicts for the state when the second level of government buildings is reached)
- The last 4 Development Decision levels will now cost 250 Gold instead of 15% of your yearly income
- Removed Reduced Moral Damage for reserves from professionalism, Added 10 % siege abilty instead
- Removed scaled siege ability from professionalism 
- Some Minor Advisor Changes
- Removed Country Idea Groups so that countries can also freely pick their first idea
- Added Idea Cost Bonus for later dates
- One can Pick up to 12 policies (4 per category)

###################################################################
####### Ideas & Policies
###################################################################

- Reworked policy system to function with the new patch
- Added 58 new special policies that only require one Ideagroup (you only need one idea despite the game showing more for interface reasons)
- Added 100 Forcelimit Increase for Galley Ideas/Age
- The Flat Forcelimit Boni from War Production will now be scaled over the Ages as well
- Removed siege ability from Fire Ideas
- Removed siege ability from War Production Ideas, added 2.5% more Fire Damage
- Reworked some Religious Idea Groups a bit
- Spy Ideas and Imperialism Ideas now only give 2.5% Discipline
- Removed 10% Heavy Ship Combat Ability from Trade Ship Ideas, Added -25% more Sailor Maintenance
- Expansion Ideas now only give 7 more states (10 before)
- Moved siege bonuses from the special Ship Idea Groups to the new idea group specific policies
- Maritime Ideas now only give one naval maneuver (2 before)
- Upon having 50% professionalism and the Mercenary Army Idea Group completed your lose professionalism yearly the higher your professionalism is
- Instead of the Decision to search for an heir Elective Monarchies  gained +1 Prestige and +1 Adm Power for their rulers (Monarchy Ideas)
- Reworked Maritime Ideas, added the bonus abilities to the special maritime policy
- Innovative Ideas lost tech cost but gained 1 free policy

###################################################################
####### Version 3.2.0 (304a)
###################################################################

###################################################################
####### General 
###################################################################

- New CB: Vassalisation against countries below 150 development (Imperialist Ambition Ideas)
- Automatic Idea Group Change moved to on_action for religions
- Automatic Idea Group Change for all religious idea groups currently in the game and for every combination currently possible
- Automatic Idea Group change for government events groups now invisible (and added missing ones)
- Impearlist Ambition Ideas will automatically change to Imperialism Ideas when Empire Rank is reached
- Deactivated Maritime War CB for the AI, as it had problems dealing with it
- Improved english localisatin for General Staff Ideas and Standing Army Ideas (Thanks to Big Boss Man)
- Increased State Maintenance Cost from Buildings can now be deactivated at game start
- 10 more Base Influence for Janissaries when 1700 is reached
- Some more small adjustments

###################################################################
####### Ideas & Policies
###################################################################

- Added 300 new Idea Group specific events like the flavour vanilla events for the new idea groups
- New Idea: Imperialist Ambition for Kingdoms, will be replaced by Imperialism Ideas when Empire Rank is reached
- Added Idea Groups for nahuatl, mesoamerican, inti and totemism (now every vanilla religion has its own idea group)
- Reworked Fortress Ideas a bit
- Tengri Ideas: Removed Looting speed
- Horde Ideas: Lost Looting speed, gained 1 Diplomatic Reputation
- Flat Manpower Ideas and Policies scaled with ages (improve when ages pass)
- Imperial Authority and Mandate (Imperialism Idea) are scaled in ages as well
- Added coloured dots to show which ideas are mutually exclusive

###################################################################
####### Buildings
###################################################################

- Reduced cost for the first three Fortress Idea buildings
- The first two buildings of the court building line don't cost a building slot


###################################################################
####### Advisors
###################################################################

- Reduced the state maintenance advisor bonus from 30% to 25%
- Added 9 new advisortypes
- Added 'brilliant advisor" events for the new Idea Variation advisors (32)
- Advisor Interface has been reworked to support more than one modifier
- Scripted Advisor Bonus reduced to 33% (before: 50%)

###################################################################
####### Version 3.1.0 (2164)
###################################################################

###################################################################
####### General
###################################################################

- Fixed some Localisation Issues
- Added naval boni to hard mode
- Added a corruption buff for ottomans and changed some things in the Janissary estate, cause the AI is dumb 
- Janissary Estate now require you to be in the islamic religion group
- Fixed some small bugs
- Removed Estate Loyalty/Influence buffs from estates
- Added some idea dependent interactions
- Minor adjustments
- New Decision in Monarchy Ideas: Promote Heir

###################################################################
####### Buildings
###################################################################

- Only tax, production, trade and manufactory buildings will increase development cost from now on
- Reduced state maintenance cost for early buildings quite a bit
- Rebalanced wharfs
- Minor adjustments

###################################################################
####### Ideas & Policies
###################################################################

- Reevaluated all policies, added some modifiers to policies that were still missing (mercenary diszipline for example)
- Huge spring cleaning of adm/dip ideas, removed some useless modifiers and rebalanced stuff (Completely reworked: Basically redid the whole group; Reworked: Changed some more important things; Small Adjustment: Minor Rebalancing)

Completely Reworked:
- Monarchy Ideas:
- Aristocratic Ideas now Theocratic Ideas
- Republican Ideas
- Colonial Empire Ideas
- Expansion Ideas

Reworked:
- Spy Ideas
- Dynastic Ideas
- Fleetbase Ideas
- State Administration Ideas

Small Adjustments:
- Influence Ideas
- Administrative Ideas
- Humanist Ideas
- Protestantism Ideas
- Reformed Ideas
- Islam Ideas
- Orthodox Ideas
- Nordic Ideas
- Shinto Ideas
- Cathar Ideas
- Hellenism Ideas
- Trade Ship Focus
- Assimilation Ideas
- Propaganda Ideas
- Imperialism Ideas
- General Staff Ideas
- Standing Army Ideas
- Conscription Ideas
- War Production Ideas
- Centralism Ideas
- Militarism Ideas


###################################################################
####### Version 3.0.7 (4200)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch
- Added Anglican Ideas

###################################################################
####### Version 3.0.6 (17a4)
###################################################################

###################################################################
####### General
###################################################################

- The first edict level is now available at game start like it used to be, however courthouses in every state province will improve edicts 
- The siege ability advisor now grants 20% siege ability (up from 15)
- Idea Variation Hard Mode gained some more adjustments (you can now choose playing with player maluses)

###################################################################
####### Buildings
###################################################################

- The Fortress Buildings now increase state maintenance 
- Fortress Idea Buildings now cost way more than before
- Slightly buffed tax collector buildings, slightly reduced production efficiency from the workshop buildings

###################################################################
####### Ideas & Policies
###################################################################

- Generally nerfed some defesiveness boni
- Expansion Ideas gained some siege ability
- Humanism Ideas no longer reduce corruption
- Added some siege ability in Catholic, Protestant, Reformed and Islam Ideas
- Reworked Defensive and Offensive Ideas somewhat, Defensive gained fire damage received, Offensive gained the land attrition bonus formerly found in defensive
- Militarism gained -10% Land Attrition
- Warproduction Ideas gained 5% Fire Damage, losing the Production Efficiency
- Fire gained 1 max Artillery Siege Bonus
- Propaganda gained 10% siege ability
- Galley Ideas gained 15% siege ability
- Trade Ship Ideas now give +1 on Siege Roles when the province is blockaded
- Heavy Ship Idea gained +1 max Artillery Siege Bonus
- Adjusted the liberty desire granted by Colonial Empire Ideas (looks like Paradox changed something here in the last patch, the former effect was not worth mentioning)
- Adjusted some policies (focus on defensiveness vs siege ability)

###################################################################
####### Version 3.0.5 (1842)
###################################################################

###################################################################
####### General
###################################################################

- Bhudism Idea group is now available for mahayana and vajrayana as well
- Changed edicts to be dependent on the government buildings - edicts will get better with better buildings, but you'll need a government building in every state province
- Raised Infantry fire damage at tech 5 and 11 by 0.25 cause cav was way better in relation
- Big Colonial nations now give 5% forcelimit modifier and 10% ship forcelimit modifier instead of the flat 5 and 10
- Marches now give 5% land forcelimit modifier and 10% more mercenaries
- Vasalls now give 10% naval forcelimit modifier
- Subject Nations now don't loose their 6 offmap base tax just because they are subjects

###################################################################
####### Buildings
###################################################################

- Adjusted development cost for the irrigation (desert building) to the new vanilla value
- Every building built will now raise development cost of the province by 5%
- Nearly every building will raise state maintenance considerably
- Landforcelimit Buildings can now only be built in state provinces
- The fortress buildings now raise max_attrition in provinces they are build in (max 10)


###################################################################
####### Ideas
###################################################################

- When completing the Mercenary Army Idea, one will no longer loose professionalism when recruiting mercenaries
- Slightly nerfed the shinto idea group 

###################################################################
####### Version 3.0.4 (3192)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch

###################################################################
####### Version 3.0.3 (c73e)
###################################################################

###################################################################
####### General
###################################################################

- The mod events will fire on game start
- Fixed: a crash for the GB trade company decision
- Adjusted the janissary disaster
- Janissaries now want provinces that are not sunni (like the dhimmi)
- Adjusted events and missions to work with the new buildings
- Ajusted the spawns for ministers
- Raised cost increase for new mil tech to 4 (former 3%)
- Raised state maintenance per development considerably, but reduced the malus for land on another continent
- Raised base interest from 4 to 5

###################################################################
####### Ideas
###################################################################

- Added Professionalism boni to Standing Army and Mercenary Army Ideas
- Added drill bonus for Conscription
- Added drill and professionalism bonus for General Staff Ideas
- Added mandate and Imperial Authority Bonus for Imperialism Ideas
- Added a small mandate bonus in Conucianism Ideas
- Added -50% cost for enforcing religion in the catholic ideas (removed legitimacy)
 
###################################################################
####### Buildings
###################################################################

- Pushed production building 3 and 4 a bit back in time
- Considerably increased building costs
- Nerfed Infrastructure Building chain
- Some terrain buildings are now available one tech earlier for aesthetic reasons



###################################################################
####### Version 3.0.2 (52e3)
###################################################################

###################################################################
####### General
###################################################################

- Fixed an issue with the Development Modifier System
- Fixed an issue with the new cbs as Paradox changed the syntax there 


###################################################################
####### Version 3.0.1 (e0da)
###################################################################

###################################################################
####### General
###################################################################

- Fixed a small problem with the production buildings
- Fixed an issue where the fortress buildings were not giving some manpower as desired
- Conscription Ideas now give 15 morale instead of 10
- Buffed weapon quality ideas somewhat
- The first nationalism idea now enables the new nationalist estate, which is pretty nice
- Added 5 new advisor types (4 dip, 1 adm)
- Adjusted humanism decision accordingly


###################################################################
####### Version 3.0.0 (d173)
###################################################################

###################################################################
####### General
###################################################################
- Removed some old code
- The development decision will now show the correct amount of money in the tooltip
- Removed the old project cost model and replaced it with a system that starts to kick in when you control 50 or more state provinces
- Improved localisation especially concerning the visibility of special idea group mod features
- You can now stay republican dictatorship if you keep your republican tradition between 20 and 60
- Reworked naval warfare: Combat width is now 60, the morale loss when losing ship is now 0, this will lead to longer battles and less quick wipes
- Idea Variation Hard Mode: Added a new difficulty for this version for people seeking a challenge
- Mod Setting Events: Added Mod setting events to let you choose difficulty and the development system at the start of your campaign


###################################################################
####### Ideas & Policies
###################################################################

- 9 new religious Idea groups added (Jewish, Romuva, Slavic, Hellenic, Suomi, Zororastrian, Fetishist, Animist, Manichaeism)
- 2 new Admin Idea Groups (Zentralism & Dezentralism (mutually exclusive))
- 2 new Military Idea Groups (Fire & Shock Ideas (mutually exclusive))
- Balanced sailor maintenance for galley, trade ship and heavy ship ideas
- Galley, Trade Ship and Heavy Ship Ideas will give increasing naval tradition the more ships you control (e.g. the more galleys you control, you gain more navy tradition)
- Fleet Base Idea gained some reduced sailor maintenance
- Buffed quantity ideas
- Moved some policies that were connected to quality ideas giving army tradition to general staff cause this makes more sense
- Buffed Humanism
- Added a Decision for Humanism to hire an advisor of your choice. Doing this will raise advisor cost globally, it can be done every 3 years
- When having humanism and having 5 cultures accepted you will gain 7.5 land morale
- Buffed maritime Ideas
- Added Horde Ideas
- Buffed Trade Ship Focus a bit
- Nerfed Galley Focus a bit according to the new naval system
- Added a Decision for Dictatorship Ideas that will allow you to control republican tradition somewhat in order to become a monarchy, stay dictatorship or become a republic ones again
- Added ~ 150 policies for the new idea groups

###################################################################
####### Buildings
###################################################################

- Added new building system: Big Thanks to Marcin for doing the building pics and the interface
- New Building: Infrastructure
- New Building: Terrain specific buildings that will lower development cost when built
- Production, Trade, Tax, Government and Army each have gained another building level
- Idea group specific buildings: Fortress buildings for Fortress Ideas
- Idea group specific buildings: Naval Bases for Fleet Base Ideas
- Idea group specific buildings: Special Shipyards for Trade Ship/Galley and Heavy Ship Ideas



###################################################################
####### Version 2.5.4 (b94b)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch

###################################################################
####### Version 2.5.3 (4dd0)
###################################################################

###################################################################
####### General
###################################################################

- Fixed: Demanding Recruits from the nobility works again
- Fixed: The development decision won't give development to cores anymore you don't hold
- The Development Decision will now show a cash number pretty close to what you actually need to spend


###################################################################
####### Version 2.5.2 (4dd0)
###################################################################


###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch

###################################################################
####### Version 2.5.1 (ea10)
###################################################################


###################################################################
####### General
###################################################################

- Dynastic Ideas now called again dynastic ideas
- Added harmony to some ideas and policies

###################################################################
####### Version 2.5.0 (XXXX)
###################################################################


###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch
- Added triggered modifiers that will increase development cost when country reaches a certain level of development (starts at 700, scales to 1500)
- Added Janissaries as an estate (Non Common Sense Owners will keep the old modifier)
- The huge vanilla nerf to states from tech was toned down a bit
- Extended Timeline Addon: Added starting Idea Cost Bonus for later scenarios

###################################################################
####### Ideas, Advisors & Policies
###################################################################

- Changed the policies that were giving development cost to a system where only 2 of them can be activated at the same time
- Policies will be visible in the game as soon as you have 2 idea groups activated (no need to complete one anymore)
- The orthodox idea group got the religious cb back
- Slightly buffed Islamic ideas
- Colonial Empire has lost the range bonus and gained a small malus to inflation
- The Fortress Idea has gained 10% defensiveness
- Mercenary Army Ideas now has 5% mercenary discipline instead of 5% fire damage (that was too extreme)
- Islam Ideas gained 10% cav to inf ratio
- Monarchy Ideas lost their 5 morale and 10 cav combat ability, but gained 10 cav ratio
- Monarchy Ideas now gives 20% manpower (down from 25), but +10 max absolutism and +1 yearly growth of absolutism
- Tactic ideas gained 20 cav to inf ratio
- Imperials Ideas will give + 10 absolutism but loose one relationsslot
- Nationalism Ideas will give + 10 absolutism
- Influence Ideas will give +1 yearly absolutism
- Rebalanced Aristocracy Ideas 
- Light Ship Ideas gained 10% trade power from light ships
- Buffed Expansion Ideas 
- Halfed the war exhaustion bonus in Militarism Ideas
- Tengri Ideas got 10% cav ratio
- The Dynastic Spread Decision is now available when you get the first idea of the Dynastic Idea  Group
- Some balancing for advisors
- Improved balancing of policies concerning tax, production, goods produces and trade efficiency

###################################################################
####### Decisions & Events
###################################################################

- Nerfed the boni from the military advisor events that gave 10 disci and 20 morale (now down to 3,5 and 7,5)
- The Improve Development Decision gained 3 more stages (max 30 Development total) new stages at 700,800 and 1000 dev
- The cooldown of the Development Decision is now depended on the ages (15, 12, 10, 8 years)
- Added two events changing religious idea groups when swithing between protestant, reformed and catholic and vise versa
- Reduced the negative development cost modifier after using the development decision to 10 (down from 50)
- Reduced the negative modifier from spreading your dynasty to 10 ae impact 
- The cooldown of the Dynastic Spread Decision is now depended on the ages as well (15, 12, 10, 8 years)

###################################################################
####### Version 2.4.2 (8dc5)
###################################################################

###################################################################
####### Ideen & Politiken
###################################################################

- Fixed some emergency balancing issues concerning the new modifiers 

###################################################################
####### Version 2.4.1 (ac97)
###################################################################

###################################################################
####### Ideen & Politiken
###################################################################

- Fixed some localisation issues
- Buffed Orthodox Idea Group
- Added 4 missing policies
- Deleted one policy that shouldn't be there
- State Administration got a merchant as the finisher
- Removed the improved core costs in assimilation and added a small shock defence bonus
- Removed the land maintenance bonus in the mercenary idea group and added a small fire bonus
- The improve relations modifier in the society ideas was nerfed to 15% (before: 25)
- Infiltrating administration will now require 50 spy network and will only last 8 months
- Reworked the way the AI picks ideas, it should be pretty random now with some small exceptions. You won't see the AI picking defensive and fortress that often as their 2 first military ideas for example



###################################################################
####### Version 2.4.0 (0d48)
###################################################################

###################################################################
####### Ideas & Policies
###################################################################

- Added 2 new military idea groups (tactics and militarism)
- Added new policies for the idea groups
- Rebalanced the existing policies so that pretty much every military idea gives the same number of good policies with small exceptions
- Refined balancing between galley and heavy ship ideas
- Buffed Trade Ship Ideas
- Buffed State Administration, Administrative and Innovation Idea groups
- Nerfed the vanilla military advisors a tad (morale and diszi)
- Added 8 new advisortypes
- Added State Administration to the possible Idea groups you need to reform you government

###################################################################
####### Version 2.3.0 (c0c4)
###################################################################

###################################################################
####### Ideas 
###################################################################

- Spy Ideas gained a decision to install an heir of your dynasty on another throne when certain requirements are met
- Renamed diplomatic idea group to dynastic idea group. This group will now grant a PU Unification war against countries with your own dynasty
- Buffed the influence idea group somewhat to keep up with dynastic and spy
- Adjusted some ideas & policies because of the removal of relation_decay_of_me
- Most of the special religious idea groups got a missionary
- Fixed a problem where coptic nations had access to the generic religious idea group
- The first norse religion idea will now grant the coast invasion cb as well

###################################################################
####### Version 2.2.3 (984c)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch

###################################################################
####### Version 2.2.2 (47c9)
###################################################################

###################################################################
####### Ideas & Policies
###################################################################

- Jurisprudence & Health Ideas now only give 7,5% idea cost reduction
- The society ideagroup will now give 10% institution spread and +0.05 institution spread for every institution instead of the idea cost reduction
- Rebalanced some policies that were still a bit too good to be true

###################################################################
####### Version 2.2.1 (38a9)
###################################################################

###################################################################
####### Ideas & Policies
###################################################################

- Refined AI chances for policies
- Fixed liberty_desire reductions
- The architect (advisor) now gives -10% build cost
- The General Staff Idea will give + 1 navy and army tradition instead of -1% decay
- The idea giving the Coast Invasion CB was moved from first to third place in the Fleet Base Idea Group


###################################################################
####### Version 2.2.0 (ca50)
###################################################################

###################################################################
####### General
###################################################################

- Adjusted files to work with the new patch
- Added an event to automatically change the government idea groups when chaning government type
- Changed caravan power so that very small countries cannot drain as much income from inland zones
- The Raise Development Decision will now raise development only in core provinces

###################################################################
####### Ideas & Policies
###################################################################

- Big Policy Rebalancing
- Policies can be changed every 3 years
- The leader fire bonus went from offensive to defensive ideas
- The leader maneuver bonus went from offensive to defensive ideas
- Shinto Ideas now have missionary strenght (losing discipline)
- Buffed quality ideas slightly (2.5 Combat Ability for everything)
- Monarchy Ideas will give 5% land moral 
- Society ideas now give 5% land moral (7.5 before)
- Buffed War Production
- Rebalanced Fortress Ideas (losing Siege Ability, gaining artillery combat ability)
- Merchant Fleet Ideas: Rebalanced Forcelimit Boni
- Spy Ideas got some trade efficiency (compensating for costly embargos)
- Rebalanced core cost boni all around
- Assimilation Ideas: Exchanged some stuff
- Slightly buffed Conscription Ideas
- Slightly reduced Mercenaries gained from Mercenary Ideas
- The humanist (advisor) now gives 10% institution embracement cost reduction
- State Administration gained some of the new boni for institutions


###################################################################
####### Version 2.1.1 (6745)
###################################################################


###################################################################
####### General
###################################################################


- Buffed quantity ideas to the level it was before (almost)
- Improved Mercenary Army & Fortress Ideas
- All around less available mercenaries
- Updatet the tooltip accordingly to the idea changes concerning the burgher estate loyalty boni)
- Added a maritime casus belli (You and the enemy need 6 ports to declare war for naval superiority)
- Some more policy balancing


###################################################################
####### Version 2.1.0 (1f05)
###################################################################


###################################################################
####### General
###################################################################

- Fixed some localisation issues
- Refined estate loyalty boni generated by ideas and policies (due to a bug I reported, there are some issues left)
- Galleys are now buildable again by extending the combat_width of ships to 750 (basically going back to the old fleet battle system)
- Raising and decreasing tariffs now only costs 10/5 admin power
- Westernisation was tweaked a bit. Its a bit cheaper and countries can start westernizing when being 3 techs behind
- Most of the espionage actions are available much earlier
- You can now only take max 33% of idea groups from one group 

###################################################################
####### Ideas & Policies
###################################################################

- 7 new religious idea groups (Dharmic (Hindu), Norse, Tengri, Buddhism, Shinto, Confuzianism, Cathar)
- Rebalanced some policies
- Readjusted some bonuses in the Colonial Empire Ideas and added some reduced liberty desire
- When completing the maritime Idea group one can raid costs
- Galley Ideas provide even more forcelimit
- Reduced likelihood of AI taking Development and Fortress Ideas
- Galley Focus, Heavy Ship Focus and Trade Ship Focus are mutually exclusive now
- Buffed diplomacy and espionage ideas
- Buffed Assimilation Ideas

###################################################################
####### Version 2.0.2 (d927)
###################################################################


###################################################################
####### General
###################################################################

- Fixed a bug in the influence idea group


###################################################################
####### Version 2.0.1 (aade)
###################################################################


###################################################################
####### General
###################################################################

- Adjusted files to the new patch



###################################################################
####### Version 2.0.0 (732d)
###################################################################


###################################################################
####### General
###################################################################

- Fixed a problem where not all religious policy were enabled
- Fixed the decisions that needed the aristocracy ideas to work with the mod
- Added 3 new Advisor types (state maintenance, corruption, Admin), (Colonial growth, DIP)
- Added an AI Bonus that Ideas are 25% cheaper for it
- Added Extended Timeline Addon

###################################################################
####### Ideas
###################################################################

- Added 3 new diplomatic idea groups replacing the old Naval Idea Group (military): Galley Focus, Heavy Ship Focus and Trade Ship Focus
- Adjusted the old naval_ideas ideagroup Events to work with the new system
- Nerfed down discipline in ideas
- The Orthodox Idea Group now gives a bonus for state maintenance
- Reduced the build cost reduction in development ideas from 20 to 15%
- Replaced the 10% manpower bonus in Expansion Ideas with 5 additional states
- Replaced the first colonist in Colonial Empire Ideas with 5 additional states


###################################################################
####### Policies
###################################################################

- Added 262 new policies, now every policy will enable another policy with every idea group there is except those groups of their own category
- Nerved policies that were giving discipline
- Max number of policies was raised to 7
- Added a new policy interface (Big Thanks to Lord Satyr for doing that!)


###################################################################
####### Version 1.6.1 (d3e3)
###################################################################


###################################################################
####### Ideas
###################################################################

- Adjusted the vanilla ideas to the changes made in the last patch
- State Administration now reduces state maintenance
- Reduced core costs in state administration, added corruption reduction and max number of states
- Replaced reduced costs for demanding provinces with seamen in the Fleet Base Idea
- Reworked the Judiciary Idea again (added corruption, removed prestige decay)
- Added seamen in the Colonial Empire Ideas
- Fixed a localisation problem the Control Society Policy (who gives Boni to estates)



###################################################################
####### Version 1.6 (f6aa)
###################################################################


###################################################################
####### General
###################################################################

- Adjusted files to the new patch

###################################################################
####### Ideas
###################################################################

- Buffed Judiciary and Health Ideas
- Reduced the military_tech bonus in conscription ideas from 10% to 7,5%
- Exchanged the first and third idea in conscription
- Mercenary Army Ideas no longer reduce manpower, they also give a bit more bonus to mercenary maintenance
- Removed the no cost for reinforcement bonus from the Expansion Idea, now reduces land and navy maintenance
- Fixed a problem with the development decision that could occur when the country you triggered it with had less than 20 development
- Raised missionary strength in the Orthodox Ideas from 2 to 3

###################################################################
####### Version 1.5 (b692)
###################################################################

###################################################################
####### General 
###################################################################

- Fixed a bug that sometimes happened with the Increase Development Decision by letting the Decision fire an event that raises the development. Doing it directly through the decision caused issues sometimes
- Fixed a localisation problem
- More fine tuning on the balancing side

###################################################################
####### Version 1.4 (e345)
###################################################################

###################################################################
####### General 
###################################################################

- Fixed the Bourgeosie issues (finally)

###################################################################
####### Version 1.3 (49d6)
###################################################################

###################################################################
####### General 
###################################################################

- Ideas will now cost 250 monarch points
- Buffed the orthodox ideas very slightly
- Reduced missionary strength in islamic ideas, added a bit tolerance for heretics
- Fixed some interface issues
- Buffed Health Ideas slighty
- Reworked balancing for some ideas
- Fixed the Burghers estate problems
- Raised priority for military ideas for AI
- AI will now pick very important military policies more often if they have access
- Raised land maintenence per military tech from 1% to 3%


###################################################################
####### Version 1.2 (215a)
###################################################################

###################################################################
####### General 
###################################################################

- Adjusted files to work with the new patch
- Fixed some localisation issues

###################################################################
####### Version 1.1 (f897)
###################################################################

###################################################################
####### General 
###################################################################

- Did some more balancing

###################################################################
####### Version 1.0 (26d6)
###################################################################


###################################################################
####### General Features
###################################################################


- 25 new Idea groups
- 5 special Religious Idea groups (catholic, protestant, reformed, orthodox and muslim)
- Rebalanced the old Idea groups
- 110 new policies
- 1 new Casus Belli
- 7 new Advisors
- more available Idea group slots



###################################################################
####### Credits
###################################################################

- Big thanks to the Veritas et Fortitudo Mod for allowing me to use the interface adjustments needed for more Idea groups
- Thanks to Neprut from the Shattered Europa Mod for allowing me to use the basic ideas as a base so to say
- Thanks for Testing and Brainstorming: Recur, Theiln, Dieteratops