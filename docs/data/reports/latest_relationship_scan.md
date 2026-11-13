# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T09:07:28.841417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11174`

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

- `market_context_high->unknown_24h` score `298.0916` n `77` status `ready` deltaP `6.0832` edge `24.8145` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `81.9112` n `87` status `ready` deltaP `6.0485` edge `6.8304` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.4381` n `53` status `ready` deltaP `31.4106` edge `2.5644` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.8933` n `77` status `ready` deltaP `27.735` edge `2.0435` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.8035` n `53` status `ready` deltaP `41.8698` edge `1.6871` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5312` n `53` status `ready` deltaP `35.478` edge `0.7541` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.3949` n `77` status `ready` deltaP `48.4285` edge `1.4194` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.3667` n `77` status `ready` deltaP `44.0544` edge `0.3615` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.1169` n `53` status `ready` deltaP `38.5417` edge `0.2528` maxDD `0.0`
- `market_context_high->index_24h` score `4.6116` n `77` status `ready` deltaP `25.2007` edge `0.2258` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.601` n `53` status `ready` deltaP `43.9571` edge `0.128` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1478` n `53` status `ready` deltaP `24.2695` edge `0.2142` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4224` n `53` status `ready` deltaP `20.4384` edge `0.2977` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3369` n `53` status `ready` deltaP `18.1646` edge `0.22` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0695` n `53` status `ready` deltaP `28.2358` edge `0.0929` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0451` n `53` status `ready` deltaP `19.808` edge `0.7089` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1511` n `53` status `ready` deltaP `25.2909` edge `0.0361` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9746` n `53` status `ready` deltaP `20.4412` edge `0.0719` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.911` n `53` status `ready` deltaP `26.4985` edge `0.2322` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.219` n `53` status `ready` deltaP `16.7269` edge `0.0202` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
