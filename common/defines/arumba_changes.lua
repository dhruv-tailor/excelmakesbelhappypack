NDefines.NEconomy.EDICTS_COST_INCREASE = 1		-- % increase on state maintenance.  *reduced from 200% to 100% to allow more tactical usage of edicts.
NDefines.NEconomy.EDICTS_DURATION_MONTHS = 6	-- months lasting at least. removed because its annoying to remember managing and being blocked from doing it when you remember.

-- #arumba - changes to condottieri to block non-participation contracts
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_PARTICIPATION_BREAK = -1.0 -- (was -1.8) --At this level of (lack of) participation from the player, the AI will break the condottieri agreement and tell all their friends.  
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_PARTICIPATION_WARN = -0.4 -- At this level of (lack of) participation from the player, a warning alert will be displayed about impendent AI discontent.  -- (was -1.2)

-- #arumba - trying to encourage shorter term/immediate impact contracts
NDefines.NDiplomacy.CONDOTTIERI_MIN_DURATION = 12 -- Minimum duration for Condottieri agreements that must be paid for in advance and that cannot be cancelled.

NDefines.NMilitary.LOOT_DEVASTATION_IMPACT = 20 -- doubled from 10. 
NDefines.NMilitary.LOOTED_MAX = 10 -- doubled from 5 ducats/mo max to 10 because of +looting speed multipliers in the mod

-- #arumba - AI should want to use its army, like a player
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_ONLY_MILITARY_RULERS = 0 --If set to 1, AI will only send Condottieri while having a miliaristic ruler.
NDefines.NAI.DIPLOMATIC_ACTION_OFFER_CONDOTTIERI_ONLY_NEIGHBORS = 0 --If set to 1, AI will only send Condottieri to neighbors, regardless of access.
