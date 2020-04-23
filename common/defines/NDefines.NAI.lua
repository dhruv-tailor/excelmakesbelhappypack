-- Only Changes to NDefines.NAI should be here.
-- #arumba - changes to condottieri to block non-participation contracts
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_PARTICIPATION_BREAK = -1.1 -- (was -1.8) --At this level of (lack of) participation from the player, the AI will break the condottieri agreement and tell all their friends.  
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_PARTICIPATION_WARN = -0.5 -- At this level of (lack of) participation from the player, a warning alert will be displayed about impendent AI discontent.  -- (was -1.2)
-- #arumba - AI should want to use its army, like a player
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_ONLY_MILITARY_RULERS = 0.5 --If set to 1, AI will only send Condottieri while having a miliaristic ruler.
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_ONLY_NEIGHBORS = 0.5 --If set to 1, AI will only send Condottieri to neighbors, regardless of access.

-- #arumba -- tweaks to AI peace deals *WIP*
NDefines.NAI.PEACE_BASE_RELUCTANCE = 0 -- AI base stubbornness to refuse peace (always applied)
NDefines.NAI.PEACE_BATTLE_RELUCTANCE = 60 -- Reluctance multiplied by fraction of support limit currently in an ongoing battle in this war (to encourage battle resolution before peacing).
NDefines.NAI.PEACE_EXCESSIVE_DEMANDS_FACTOR = 0.005 -- AI unwillingness to peace based on demanding more stuff than you have warscore
NDefines.NAI.PEACE_EXCESSIVE_DEMANDS_THRESHOLD = 20 -- If you have less warscore than this, excessive demands will be factored in more highly

NDefines.NAI.PEACE_TIME_MONTHS = 36 -- Months of additional AI stubbornness in a war
-- PEACE_TIME_MONTHS = 60, -- Months of additional AI stubbornness in a war

NDefines.NAI.PEACE_TIME_MAX_MONTHS = 600 -- Max months applied to time factor in a war

NDefines.NAI.PEACE_TIME_EARLY_FACTOR = 1.0 -- During months of stubbornness the effect of time passed is multiplied by this
-- PEACE_TIME_EARLY_FACTOR = 0.75, -- During months of stubbornness the effect of time passed is multiplied by this

NDefines.NAI.PEACE_TIME_LATE_FACTOR = 3.0 -- After months of stubbornness the effect of time passed is multiplied by this (only applied to positive war enthusiasm)
-- PEACE_TIME_LATE_FACTOR = 1.0, -- After months of stubbornness the effect of time passed is multiplied by this (only applied to positive war enthusiasm)

NDefines.NAI.PEACE_STALLED_WAR_TIME_FACTOR = 0.34 -- Applied to number of years war has been stalled to determine how much positive war enthusiasm is reduced
NDefines.NAI.PEACE_STALLED_WAR_THRESHOLD = 3 -- If the warscore has changed by this amount or less in the last year, the war is stalled
NDefines.NAI.PEACE_WAR_EXHAUSTION_FACTOR = 1.0 -- AI willingness to peace based on war exhaustion
NDefines.NAI.PEACE_HIGH_WAR_EXHAUSTION_THRESHOLD = 10 -- Threshold for when PEACE_HIGH_WAR_EXHAUSTION_FACTOR is applied
NDefines.NAI.PEACE_HIGH_WAR_EXHAUSTION_FACTOR = 2.0 -- Additional AI willingness to peace based on war exhaustion above the high threshold
NDefines.NAI.PEACE_WAR_DIRECTION_FACTOR = 0.5 -- AI willingness to peace based on who's making gains in the war
NDefines.NAI.PEACE_WAR_DIRECTION_WINNING_MULT = 5.0 -- Multiplies AI emphasis on war direction if it's the one making gains
NDefines.NAI.PEACE_FORCE_BALANCE_FACTOR = 0.2 -- AI willingness to peace based on strength estimation of both sides
NDefines.NAI.PEACE_INDEPENDENCE_FACTOR = 50 -- Revolting AI's unwillingness to peace while between -5 and cost of independence wargoal in an independence war.
NDefines.NAI.PEACE_WARGOAL_FACTOR = 0 -- AI unwillingness to peace based on holding the wargoal
NDefines.NAI.PEACE_CAPITAL_FACTOR = 5 -- AI unwillingness to peace based on holding their own capital
NDefines.NAI.PEACE_MILITARY_STRENGTH_FACTOR = 10 -- AI unwillingness to peace based on manpower & forcelimits
NDefines.NAI.PEACE_ALLY_BASE_RELUCTANCE_MULT = 2.0 -- Multiplies PEACE_BASE_RELUCTANCE for allies in a war
NDefines.NAI.PEACE_ALLY_WARSCORE_MULT = 1.0 -- How much extra war enthusiasm from overall warscore allies in a war get
-- NDefines.NAI.PEACE_ALLY_WARSCORE_MULT = 0.5 -- How much extra war enthusiasm from overall warscore allies in a war get
NDefines.NAI.PEACE_ALLY_TIME_MULT = 1.0 -- Multiplies PEACE_TIME_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_EXCESSIVE_DEMANDS_MULT = 2.0 -- Multiplies PEACE_EXCESSIVE_DEMANDS_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_WAR_EXHAUSTION_MULT = 1.0 -- Multiplies PEACE_WAR_EXHAUSTION_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_WAR_DIRECTION_MULT = 0 -- Multiplies PEACE_WAR_DIRECTION_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_FORCE_BALANCE_MULT = 0 -- Multiplies PEACE_FORCE_BALANCE_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_WARGOAL_MULT = 0 -- Multiplies PEACE_WARGOAL_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_CAPITAL_MULT = 1.0 -- Multiplies PEACE_CAPITAL_FACTOR for allies in a war
NDefines.NAI.PEACE_ALLY_MILITARY_STRENGTH_MULT = 2.0 -- Multiplies PEACE_MILITARY_STRENGTH_FACTOR for allies in a war
NDefines.NAI.PEACE_OTHER_WAR_FORCE_BALANCE_MULT = 0.5 -- Multiplies the force balance of other countries who are involved in a different war with either side
NDefines.NAI.PEACE_INCONCLUSIVE_THRESHOLD = 1 -- no demands will be accepted by AI if under this warscore
NDefines.NAI.PEACE_DESPERATION_FACTOR = 30 -- AI willingness to peace based on desperation from occupied homelands
NDefines.NAI.PEACE_ALLY_DESPERATION_MULT = 1.0 -- Multiplies PEACE_DESPERATION_FACTOR for allies in a war
NDefines.NAI.PEACE_REBELS_FACTOR = 20 -- AI willingness to peace based on number of revolts in their provinces
NDefines.NAI.PEACE_COALITION_FACTOR = 30 -- AI unwillingness to peace based on being in a coalition war
NDefines.NAI.PEACE_ALLY_REBELS_MULT = 1.0 -- Multiplies PEACE_REBELS_FACTOR for allies in a war
NDefines.NAI.PEACE_CALL_FOR_PEACE_FACTOR = 10 -- How much AI wants peace based on having call for peace

NDefines.NAI.PEACE_TERMS_BASE_SCORE = 10 -- Base AI scoring for any peace demand
NDefines.NAI.PEACE_RANDOM_FACTOR = 0.75 -- How much randomness is applied to AI weighting (as a fraction of the goal score)
NDefines.NAI.PEACE_TERMS_CB_MULT = 2.0 -- AI desire for a wargoal is multiplied by this for having the right CB
NDefines.NAI.PEACE_TERMS_STRATEGY_MULT = 0.5 -- AI desire for a wargoal is multiplied by this if it doesn't fit into their general strategy
NDefines.NAI.PEACE_TERMS_MIN_SCORE = 1 -- AI "does not want" peace treaties that get a lower score than this (modified by ai personality)

NDefines.NAI.PEACE_TERMS_REVOKE_ELECTOR_BASE_MULT = 1000.0 -- only applied if CB is valid for it
NDefines.NAI.PEACE_TERMS_INDEPENDENCE_BASE_MULT = 1000.0 -- only applied if CB is valid for it
NDefines.NAI.PEACE_TERMS_UNION_BASE_MULT = 1000.0 -- only applied if CB is valid for it
NDefines.NAI.PEACE_TERMS_VASSAL_BASE_MULT = 500.0 -- only applied if the AI has vassalize priority
NDefines.NAI.PEACE_TERMS_TAKE_MANDATE_BASE_MULT = 1000.0
NDefines.NAI.PEACE_TERMS_CHANGE_GOVERNMENT_BASE_MULT = 0.75 -- only applied if CB is valid for it
NDefines.NAI.PEACE_TERMS_CHANGE_RELIGION_BASE_MULT = 100.0 -- only applied if CB is valid for it
NDefines.NAI.PEACE_TERMS_ANNEX_BASE_MULT = 100.0
NDefines.NAI.PEACE_TERMS_PROVINCE_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_TRADE_POWER_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_HUMILIATE_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_REVOKE_CORES_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_REVOKE_REFORM_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_RETURN_CORES_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_RELEASE_VASSALS_BASE_MULT = 0.75
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSALS_BASE_MULT = 0.75
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_BASE_MULT = 0.75
NDefines.NAI.PEACE_TERMS_ANNUL_TREATIES_BASE_MULT = 0.75
NDefines.NAI.PEACE_TERMS_GOLD_BASE_MULT = 0.1
NDefines.NAI.PEACE_TERMS_GIVE_UP_CLAIM = 0.0
NDefines.NAI.PEACE_TERMS_GIVE_UP_CLAIM_PERMANENT = 0.75
NDefines.NAI.PEACE_TERMS_CONCEDE_DEFEAT_BASE_MULT = 0.1
NDefines.NAI.PEACE_TERMS_DISMANTLE_REVOLUTION_BASE_MULT = 1000.0
NDefines.NAI.PEACE_TERMS_CHANGE_HRE_RELIGION_BASE_MULT = 1000.0
NDefines.NAI.PEACE_TERMS_HUMILIATE_RIVAL_BASE_MULT = 1.0
NDefines.NAI.PEACE_TERMS_ENFORCE_REBEL_DEMANDS_BASE_MULT = 1000.0
NDefines.NAI.PEACE_TERMS_TRIBUTARY_BASE_MULT = 5.0 -- Multiplies with strategic interest of making them our Tributary

NDefines.NAI.PEACE_TERMS_PROVINCE_IMPERIAL_LIBERATION_MULT = 0.25 -- AI Emperor's desire for a province is multiplied by this if this is an Imperial Liberation CB war.
NDefines.NAI.PEACE_TERMS_PROVINCE_NO_CB_MULT = 0.5 -- AI desire for a province is multiplied by this if it doesn't have a valid cb for it (only used when annexing, not applied to cores)
NDefines.NAI.PEACE_TERMS_PROVINCE_CORE_MULT = 3.0 -- AI desire for a province is multiplied by this if it has a core on it
NDefines.NAI.PEACE_TERMS_PROVINCE_WARGOAL_MULT = 2.0 -- AI desire for a province is multiplied by this if it is the wargoal
NDefines.NAI.PEACE_TERMS_PROVINCE_CLAIM_MULT = 2.0 -- AI desire for a province is multiplied by this if it has a claim on it
NDefines.NAI.PEACE_TERMS_PROVINCE_NOT_CULTURE_MULT = 0.75 -- AI desire for a province is multiplied by this if it is not the same culture
NDefines.NAI.PEACE_TERMS_PROVINCE_VASSAL_MULT = 1.00 -- AI desire for a province is multiplied by this if it would go to their vassal instead of themselves
NDefines.NAI.PEACE_TERMS_PROVINCE_REAL_ADJACENT_MULT = 0.5 -- AI desire for a province is increased by this multiplier for each owned adjacent province
NDefines.NAI.PEACE_TERMS_PROVINCE_NOT_ADJACENT_MULT = 0.5 -- AI desire for a province is multiplied by this if it is not adjacent at all (including vassals and other provinces being taken in peace)
NDefines.NAI.PEACE_TERMS_PROVINCE_NO_INTEREST_MULT = 0 -- AI desire for a province is multiplied by this if it is not on their conquest list
NDefines.NAI.PEACE_TERMS_PROVINCE_OVEREXTENSION_MIN_MULT = 0.75 -- AI desire for a province is multiplied by this if it has 99% overextension (not applied to cores)
NDefines.NAI.PEACE_TERMS_PROVINCE_OVEREXTENSION_MAX_MULT = 1.5 -- AI desire for a province is multiplied by this if it has 0% overextension (not applied to cores)
NDefines.NAI.PEACE_TERMS_PROVINCE_ISOLATED_CAPITAL_MULT = 0.9 -- AI desire for a province if it is capital (costs a bit more to take)
NDefines.NAI.PEACE_TERMS_PROVINCE_ALLY_MULT = 0.5 -- AI desire for giving (non-core) provinces to its allies
NDefines.NAI.PEACE_TERMS_PROVINCE_IMPORTANT_ALLY_MULT = 2 -- AI desire for giving provinces to allies that it has promised land
NDefines.NAI.PEACE_TERMS_TRADE_POWER_VALUE_MULT = 0.1 -- AI desire for transfering trade power is multiplied by this for each 0.1 trade value in shared nodes
NDefines.NAI.PEACE_TERMS_TRADE_POWER_VALUE_MAX = 2.0 -- Max AI desire for transfering trade power from shared node value
NDefines.NAI.PEACE_TERMS_TRADE_POWER_NO_TRADE_INTEREST_MULT = 0 -- AI desire for transfering trade power is multiplied by this if they are not a merchant republic
NDefines.NAI.PEACE_TERMS_HUMILIATE_VALUE_MULT = 1 -- AI desire for humiliating is multiplied by this for each 1 prestige the enemy has
NDefines.NAI.PEACE_TERMS_HUMILIATE_VALUE_MAX = 2.0 -- Max AI desire for humiliating its' enemy
NDefines.NAI.PEACE_TERMS_REVOKE_CORE_VASSAL_MULT = 0.75 -- AI desire for revoking cores is multiplied by this if the cores are on their vassal instead of themselves
NDefines.NAI.PEACE_TERMS_REVOKE_CORE_FEAR_MULT = 2.0 -- AI desire for revoking cores is multiplied by this if they are afraid of the other country
NDefines.NAI.PEACE_TERMS_RETURN_CORES_VASSAL_MULT = 2.0 -- AI desire for returning core provinces is multiplied by this for their vassals
NDefines.NAI.PEACE_TERMS_RETURN_CORES_NOT_FRIEND_MULT = 0.75 -- AI desire for returning core provinces is multiplied by this if they are not friends of the country core is being returned to
NDefines.NAI.PEACE_TERMS_RETURN_CORES_IMPERIAL_LIBERATION_MULT = 2.0 --AI desire for returning core province is multiplied by this if it's a target of Imperial Liberation CB war.
NDefines.NAI.PEACE_TERMS_ANNUL_TREATIES_NO_INTEREST_MULT = 0 -- AI desire for annuling a treaty is multiplied by this if they have no strategic interests in doing so
NDefines.NAI.PEACE_TERMS_PROVINCE_HRE_UNJUSTIFIED_MULT = 0 -- AI desire for a province is multiplied by this for HRE provinces if they are a member of the empire and don't have a CB, claim or core to it
NDefines.NAI.PEACE_TERMS_MIN_MONTHS_OF_GOLD = 5 -- If they don't have at least this much warscore worth of gold, prefer concede defeat
NDefines.NAI.PEACE_TERMS_PROVINCE_STRATEGY_THRESHOLD = 1 -- If province has at least this strategic priority, AI values it higher in peace deals
NDefines.NAI.PEACE_TERMS_RETURN_PROVINCE_STRATEGY_MULT = 0.5 -- If we have strategic priority on a province, AI desire to release it to another nation is multiplied by this amount
NDefines.NAI.PEACE_TERMS_EMPEROR_RELEASE_PRINCE = 50.0 -- This is added, not multiplied
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_SIZE_MULT = 0.1 -- AI desire mult for releasing vassal increased by this for each province they hold
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_MAX_MULT = 1.3 -- Max AI desire mult for releasing vassals
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_HRE_MULT = 2.0 -- AI desire for releasing a vassal is multiplied by this if both are HRE members
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_ELECTOR_MULT = 10.0 -- AI desire for releasing an elector is multiplied by this for Emperor
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_SAME_CULTURE_MULT = 0.65 -- AI desire for releasing a country is multiplied by this if they are the same culture group as releaser
NDefines.NAI.PEACE_TERMS_RELEASE_VASSAL_SAME_CULTURE_GROUP_MULT = 0.75 -- AI desire for releasing a country is multiplied by this if they are the same culture group (but not same culture) as releaser
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_SIZE_MULT = 0.1 -- AI desire mult for releasing vassal increased by this for each province they hold
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_MAX_MULT = 1.3 -- Max AI desire mult for releasing vassals
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_HRE_MULT = 2.0 -- AI desire for releasing a vassal is multiplied by this if both are HRE members
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_ELECTOR_MULT = 10.0 -- AI desire for releasing an elector is multiplied by this for Emperor
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_SAME_CULTURE_MULT = 0.65 -- AI desire for releasing a country is multiplied by this if they are the same culture group as releaser
NDefines.NAI.PEACE_TERMS_TRANSFER_VASSAL_SAME_CULTURE_GROUP_MULT = 0.75 -- AI desire for releasing a country is multiplied by this if they are the same culture group (but not same culture) as releaser
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_SIZE_MULT = 0.01 -- AI desire mult for releasing countries is increased by this for each development they hold
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_MAX_MULT = 1.3 -- Max AI desire mult for releasing countries
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_KARMA_LOW_MULT = 1.5 --AI desire mult when below karma bonus
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_KARMA_VERY_LOW_MULT = 2.0 --AI desire mult when karma low enough for penalty
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_HRE_MULT = 2.0 -- AI desire for releasing a country is multiplied by this if both are HRE members
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_SAME_CULTURE_MULT = 0.65 -- AI desire for releasing a country is multiplied by this if they are the same culture group as releaser
NDefines.NAI.PEACE_TERMS_RELEASE_ANNEXED_SAME_CULTURE_GROUP_MULT = 0.75 -- AI desire for releasing a country is multiplied by this if they are the same culture group (but not same culture) as releaser
NDefines.NAI.PEACE_TERMS_MIL_ACCESS_BASE_MULT = 0 -- AI desire for mil access through peace
NDefines.NAI.PEACE_TERMS_FLEET_BASING_BASE_MULT = 0 -- AI desire for fleet basing rights through peace
NDefines.NAI.PEACE_TERMS_WAR_REPARATIONS_BASE_MULT = 0.1 -- AI desire for war reparations through peace
NDefines.NAI.PEACE_TERMS_WAR_REPARATIONS_MIN_INCOME_RATIO = 0.5 -- AI only wants war reparations if other country has at least this % of their income

NDefines.NAI.ADVISOR_BUDGET_FRACTION = 0.10 -- nerfed to try to increase net income ratio
	-- ADVISOR_BUDGET_FRACTION = 0.3, -- AI will spend a maximum of this fraction of monthly income on advisor maintenance
NDefines.NAI.ARMY_BUDGET_FRACTION = 0.6 -- AI will spend a maximum of this fraction of monthly income on army maintenance (based off wartime costs)
	-- ARMY_BUDGET_FRACTION = 0.7, -- AI will spend a maximum of this fraction of monthly income on army maintenance (based off wartime costs)
NDefines.NAI.NAVY_BUDGET_FRACTION = 0.4 -- AI will spend a maximum of this fraction of monthly income on navy maintenance (based off wartime costs)
	-- NAVY_BUDGET_FRACTION = 0.5, -- AI will spend a maximum of this fraction of monthly income on navy maintenance (based off wartime costs)
NDefines.NAI.FORT_BUDGET_FRACTION = 0.5 -- AI will spend a maximum of this fraction of monthly income on forts
	-- FORT_BUDGET_FRACTION = 0.4, -- AI will spend a maximum of this fraction of monthly income on forts

NDefines.NAI.CANCEL_CONSTRUCTION_SIEGE_PROGRESS = 101 -- buildings don't get destroyed when sieged, not sure why AI cancels constructions at all
	-- CANCEL_CONSTRUCTION_SIEGE_PROGRESS = 0, -- If chance of fort falling is at least this, AI will cancel constructions in the province
NDefines.NAI.DESIRED_SURPLUS = 0.10 -- AI will aim for having at least this fraction of their income as surplus when they don't have large savings
	-- DESIRED_SURPLUS = 0.1, -- AI will aim for having at least this fraction of their income as surplus when they don't have large savings
NDefines.NAI.BIGSHIP_FRACTION = 0.3	-- The proportion of big ships in an AI navy of light ships and big ships (for coastal sea countries, this fraction is mostly galleys)
	-- BIGSHIP_FRACTION = 0.4,	-- The proportion of big ships in an AI navy of light ships and big ships (for coastal sea countries, this fraction is mostly galleys)

NDefines.NAI.DEVELOPMENT_CAP_BASE = 30 -- AI will not develop provinces that have more development than this or DEVELOPMENT_CAP_MULT*original development (whichever is bigger)
	-- DEVELOPMENT_CAP_BASE = 10
NDefines.NAI.DEVELOPMENT_CAP_MULT = 2

NDefines.NAI.MIN_CAV_PERCENTAGE = 0
	-- MIN_CAV_PERCENTAGE = 5, --AI will always try to have at least this many % of their army as cav, regardless of time in the game.
NDefines.NAI.MAX_CAV_PERCENTAGE = 100
	-- MAX_CAV_PERCENTAGE = 50, -- For modding, actual ratio is dynamically computed but will be no higher than this.

