# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T20:52:29.260812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7314`

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

- `news_risk_high->unknown_24h` score `2671.2504` n `139` status `ready` deltaP `1.2153` edge `222.5961` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.1014` n `139` status `ready` deltaP `25.9905` edge `1.0637` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.5022` n `139` status `ready` deltaP `25.5882` edge `0.6269` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.2025` n `139` status `ready` deltaP `21.7688` edge `0.8152` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.3565` n `139` status `ready` deltaP `31.22` edge `0.1411` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.4977` n `139` status `ready` deltaP `23.5999` edge `0.2363` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4543` n `139` status `ready` deltaP `26.259` edge `0.1904` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.8213` n `139` status `ready` deltaP `8.0409` edge `0.2808` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6159` n `139` status `ready` deltaP `6.7182` edge `0.0976` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.538` n `139` status `ready` deltaP `7.554` edge `0.0606` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4695` n `139` status `ready` deltaP `8.9013` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1441` n `139` status `ready` deltaP `6.9629` edge `0.0269` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.51` n `139` status `ready` deltaP `1.4905` edge `0.0105` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5716` n `139` status `ready` deltaP `0.4469` edge `0.052` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1804` n `139` status `ready` deltaP `-9.1178` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2697` n `139` status `ready` deltaP `9.2198` edge `-0.0029` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4375` n `139` status `ready` deltaP `-9.3086` edge `0.0272` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8287` n `139` status `ready` deltaP `-5.2433` edge `0.072` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.056` n `139` status `ready` deltaP `-12.3153` edge `-0.014` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7946` n `139` status `ready` deltaP `-11.0173` edge `-0.0009` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
