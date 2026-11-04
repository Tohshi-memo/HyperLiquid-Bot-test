# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T04:22:27.243168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->crypto_alt_4h` score `0.7297` n `146` status `ready` deltaP `9.1338` edge `0.2963` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2672` n `146` status `ready` deltaP `3.3795` edge `0.066` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6412` n `146` status `ready` deltaP `-1.4744` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7405` n `146` status `ready` deltaP `2.5449` edge `0.0013` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2027` n `146` status `ready` deltaP `-3.9004` edge `-0.006` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3212` n `146` status `ready` deltaP `12.2979` edge `0.1661` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4646` n `146` status `ready` deltaP `-7.622` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6808` n `146` status `ready` deltaP `2.0715` edge `0.0549` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7553` n `146` status `ready` deltaP `0.3842` edge `0.0025` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3168` n `146` status `ready` deltaP `-17.6798` edge `-0.0083` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4146` n `146` status `ready` deltaP `-5.139` edge `-0.0077` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4558` n `146` status `ready` deltaP `-10.1243` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.9165` n `146` status `ready` deltaP `-6.5089` edge `-0.0271` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8036` n `146` status `ready` deltaP `-12.1701` edge `-0.0004` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3336` n `146` status `ready` deltaP `-3.3369` edge `-0.0184` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0567` n `146` status `ready` deltaP `-10.5726` edge `-0.0323` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.3636` n `146` status `ready` deltaP `21.4517` edge `0.7406` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.3659` n `146` status `ready` deltaP `19.0212` edge `0.6264` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.3947` n `146` status `ready` deltaP `0.5367` edge `-0.0337` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2947` n `146` status `ready` deltaP `-20.2626` edge `-0.0634` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
