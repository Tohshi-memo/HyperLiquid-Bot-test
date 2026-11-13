# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T16:07:31.113779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `371.2354` n `75` status `ready` deltaP `4.4514` edge `30.9207` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.884` n `53` status `ready` deltaP `31.5842` edge `2.6004` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.6503` n `75` status `ready` deltaP `26.125` edge `2.0342` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.8278` n `75` status `ready` deltaP `50.0139` edge `1.4037` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2657` n `53` status `ready` deltaP `42.0434` edge `1.7452` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.3295` n `53` status `ready` deltaP `33.4963` edge `0.7505` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5709` n `53` status `ready` deltaP `36.1111` edge `0.2235` maxDD `0.0`
- `market_context_high->index_24h` score `4.7327` n `75` status `ready` deltaP `25.0417` edge `0.2366` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.647` n `53` status `ready` deltaP `44.262` edge `0.1298` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0518` n `53` status `ready` deltaP `23.0542` edge `0.2143` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8617` n `75` status `ready` deltaP `38.5556` edge `0.3272` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.4415` n `53` status `ready` deltaP `17.4161` edge `0.2337` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9739` n `53` status `ready` deltaP `27.626` edge `0.089` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9223` n `53` status `ready` deltaP `18.7615` edge `0.2672` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.3823` n `53` status `ready` deltaP `16.8566` edge `0.6436` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1559` n `53` status `ready` deltaP `25.2909` edge `0.0365` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.917` n `53` status `ready` deltaP `19.5266` edge `0.0732` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7051` n `53` status `ready` deltaP `25.5838` edge `0.2119` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2179` n `53` status `ready` deltaP `16.4275` edge `0.0221` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6174` n `53` status `ready` deltaP `16.8455` edge `0.0648` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
