import datetime
from uuid import uuid4

import ekklesia_portal.lib.vvvote.schema as vvvote_schema


def ballot_to_vvvote_question(ballot, question_id=1):
    options = []
    voting_scheme_yes_no = vvvote_schema.YesNoScheme(
        name='yesNo', abstention=True, abstentionAsNo=False, quorum=2, mode=vvvote_schema.SchemeMode.QUORUM
    )

    voting_scheme_score = vvvote_schema.ScoreScheme(name='score', minScore=0, maxScore=3)

    voting_scheme = [voting_scheme_yes_no, voting_scheme_score]

    for option_id, proposition in enumerate(ballot.propositions, start=1):
        proponents = [s.name for s in proposition.supporters]
        option = vvvote_schema.Option(
            optionID=option_id,
            proponents=proponents,
            optionTitle=proposition.title,
            optionDesc=proposition.content,
            reasons=proposition.motivation,
        )
        options.append(option)

    if len(ballot.propositions) == 1:
        question_wording = ballot.propositions[0].title
    else:
        question_wording = ballot.name

    question = vvvote_schema.Question(
        questionWording=question_wording,
        questionID=question_id,
        scheme=voting_scheme,
        options=options,
        findWinner=['yesNo', 'score', 'random']
    )

    return question


def voting_phase_to_vvvote_election_config(module_config, phase) -> vvvote_schema.ElectionConfig:
    questions = [ballot_to_vvvote_question(b, ii) for ii, b in enumerate(phase.ballots, start=1)]

    voting_start = phase.voting_start
    if voting_start is None:
        raise ValueError("Cannot create voting for phase {phase}, voting_start is None")

    end = phase.voting_end
    if end is None:
        raise ValueError("Cannot create voting for phase {phase}, voting_end is None")

    registration_days_before_voting = module_config.get("registration_days_before_voting", 0)
    registration_start = voting_start - datetime.timedelta(days=registration_days_before_voting)

    auth_data = vvvote_schema.OAuthConfig(
        eligible=module_config["must_be_eligible"],
        external_voting=True,
        verified=module_config["must_be_verified"],
        nested_groups=[module_config["required_role"]],
        serverId=module_config["auth_server_id"],
        RegistrationStartDate=registration_start,
        RegistrationEndDate=end,
        VotingStart=voting_start,
        VotingEnd=end,
    )
    config = vvvote_schema.ElectionConfig(
        electionId=str(uuid4()),
        electionTitle=phase.title or phase.name or phase.phase_type.name,
        tally=vvvote_schema.Tally.CONFIGURABLE,
        auth=vvvote_schema.Auth.OAUTH,
        authData=auth_data,
        questions=questions
    )
    return config
