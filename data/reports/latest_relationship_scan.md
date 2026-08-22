# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T23:07:25.734132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `2.4744` n `30` status `ready` deltaP `28.4731` edge `0.0282` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.6193` n `139` status `ready` deltaP `5.3796` edge `0.1218` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.4701` n `30` status `ready` deltaP `20.0399` edge `0.0059` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `1.1927` n `30` status `ready` deltaP `26.7066` edge `-0.0068` maxDD `-0.4666`
- `market_context_high->unknown_4h` score `1.0079` n `139` status `ready` deltaP `19.4771` edge `-0.007` maxDD `-0.4415`
- `news_risk_high->equity_1h` score `0.7083` n `30` status `ready` deltaP `17.006` edge `0.0056` maxDD `-0.9204`
- `market_context_high->fx_4h` score `0.1307` n `139` status `ready` deltaP `8.6693` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0697` n `139` status `ready` deltaP `5.9945` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0981` n `139` status `ready` deltaP `2.8217` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->crypto_major_1h` score `-0.2342` n `30` status `ready` deltaP `12.3653` edge `-0.0247` maxDD `-5.0209`
- `news_risk_high->metal_1h` score `-0.2524` n `30` status `ready` deltaP `-1.3473` edge `-0.0094` maxDD `-0.1184`
- `market_context_high->equity_1h` score `-0.34` n `139` status `ready` deltaP `4.56` edge `0.033` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3984` n `139` status `ready` deltaP `6.7786` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.5238` n `139` status `ready` deltaP `0.4513` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.617` n `139` status `ready` deltaP `2.0793` edge `0.0106` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.9835` n `123` status `ready` deltaP `0.6097` edge `0.009` maxDD `-2.1321`
- `market_context_high->commodity_4h` score `-0.9903` n `139` status `ready` deltaP `-6.08` edge `-0.0014` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1343` n `139` status `ready` deltaP `-8.6891` edge `-0.0025` maxDD `-1.1328`
- `market_context_high->crypto_alt_4h` score `-1.5655` n `139` status `ready` deltaP `6.5034` edge `-0.027` maxDD `-7.0785`
- `news_risk_high->index_1h` score `-1.7284` n `30` status `ready` deltaP `-16.0679` edge `-0.0016` maxDD `-0.1583`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
