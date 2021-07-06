"""A place for public enums"""

from enum import Enum


class ArgumentType(Enum):
    PRO = 'pro'
    CONTRA = 'contra'


class EkklesiaUserType(str, Enum):
    PLAIN_MEMBER = 'plain member'
    ELIGIBLE_MEMBER = 'eligible member'
    SYSTEM_USER = 'system user'
    DELETED = 'deleted user'
    GUEST = 'guest'


class Majority(str, Enum):
    SIMPLE = '1/2'
    TWO_THIRDS = '2/3'


class PropositionStatus(str, Enum):
    DRAFT = 'draft'
    SUBMITTED = 'submitted'
    CHANGING = 'changing'
    ABANDONED = 'abandoned'
    QUALIFIED = 'qualified'
    SCHEDULED = 'scheduled'
    VOTING = 'voting'
    FINISHED = 'finished'


class PropositionRelationType(str, Enum):
    REPLACES = 'replaces'
    MODIFIES = 'modifies'


class PropositionVisibility(str, Enum):
    PUBLIC = 'public'
    UNLISTED = 'unlisted'
    HIDDEN = 'hidden'


class SecretVoterStatus(str, Enum):
    ACTIVE = 'active'
    EXPIRED = 'expired'
    RETRACTED = 'retracted'


class SupporterStatus(str, Enum):
    ACTIVE = 'active'
    EXPIRED = 'expired'
    RETRACTED = 'retracted'


class VotingType(str, Enum):
    ONLINE = 'online'
    ASSEMBLY = 'assembly'
    BOARD = 'board'
    URN = 'urn'


class VotingStatus(str, Enum):
    PREPARING = 'preparing'  # voting has not been started yet
    VOTING = 'voting'  # ballots have been transferred to a voting module and voting is open
    FINISHED = 'finished'  # voting is closed, results have been fetched
    ABORTED = 'aborted'  # voting stopped by administration


class OpenSlidesVotingResult(str, Enum):
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    NOT_DECIDED = 'not decided'


class VotingSystem(str, Enum):
    RANGE_APPROVAL = 'range_approval'


class VoteByUser(str, Enum):
    UNSURE = 'unsure'
    ACCEPT = 'accept'
    DECLINE = 'decline'
    ABSTENTION = 'abstention'
