# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T11:07:32.626291+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4348`

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

- `news_risk_high->crypto_alt_4h` score `0.2999` n `146` status `ready` deltaP `6.3899` edge `0.2595` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4932` n `146` status `ready` deltaP `1.4334` edge `0.05` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6381` n `146` status `ready` deltaP `-1.3247` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9287` n `146` status `ready` deltaP `0.8982` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2338` n `146` status `ready` deltaP `-4.1998` edge `-0.008` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2752` n `146` status `ready` deltaP `-3.9634` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0269` n `146` status `ready` deltaP `-2.6646` edge `-0.012` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.0713` n `146` status `ready` deltaP `9.8673` edge `0.1198` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-2.1825` n `146` status `ready` deltaP `-3.1369` edge `0.0253` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3787` n `146` status `ready` deltaP `-17.159` edge `-0.0197` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4786` n `146` status `ready` deltaP `-9.8249` edge `-0.0044` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7217` n `146` status `ready` deltaP `-7.2348` edge `-0.0331` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3229` n `146` status `ready` deltaP `-9.0538` edge `-0.044` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2079` n `146` status `ready` deltaP `-14.914` edge `-0.0158` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4819` n `146` status `ready` deltaP `-4.8613` edge `-0.0206` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.3695` n `146` status `ready` deltaP `19.1948` edge `0.7549` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8574` n `146` status `ready` deltaP `-13.6214` edge `-0.0787` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.4786` n `146` status `ready` deltaP `14.3337` edge `0.4864` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2878` n `146` status `ready` deltaP `-0.6828` edge `-0.1` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9542` n `146` status `ready` deltaP `-24.082` edge `-0.0929` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
