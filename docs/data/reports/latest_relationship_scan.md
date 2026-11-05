# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T18:07:33.178652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4188`

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

- `news_risk_high->crypto_alt_4h` score `0.6482` n `146` status `ready` deltaP `8.7519` edge `0.2884` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.137` n `146` status `ready` deltaP `4.4274` edge `0.0757` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.671` n `146` status `ready` deltaP `3.1437` edge `0.0031` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.73` n `146` status `ready` deltaP `-3.1211` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4712` n `146` status `ready` deltaP `-7.8387` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5758` n `146` status `ready` deltaP `-8.9902` edge `-0.0199` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6508` n `146` status `ready` deltaP `1.6743` edge `0.0073` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1495` n `146` status `ready` deltaP `-4.3905` edge `0.0213` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.3687` n `146` status `ready` deltaP `-17.5661` edge `-0.0157` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3863` n `146` status `ready` deltaP `-9.6752` edge `0.0023` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.5713` n `146` status `ready` deltaP `-4.5628` edge `-0.0113` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.8506` n `146` status `ready` deltaP `-12.2504` edge `0.0004` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.72` n `146` status `ready` deltaP `-13.1659` edge `0.0132` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.6467` n `146` status `ready` deltaP `-9.4369` edge `-0.0057` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7376` n `146` status `ready` deltaP `-12.8615` edge `-0.0719` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-8.1597` n `146` status `ready` deltaP `-12.7632` edge `-0.2367` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9171` n `146` status `ready` deltaP `-14.4928` edge `0.1796` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.1336` n `146` status `ready` deltaP `2.7397` edge `0.0567` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.7061` n `146` status `ready` deltaP `9.8989` edge `0.2422` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9324` n `146` status `ready` deltaP `1.9266` edge `-0.356` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
