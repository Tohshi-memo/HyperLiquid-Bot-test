# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T07:07:26.674488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `264.5509` n `84` status `ready` deltaP `6.2996` edge `22.018` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `60.9972` n `94` status `ready` deltaP `6.7333` edge `5.083` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.9238` n `53` status `ready` deltaP `30.0217` edge `2.5308` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.9064` n `84` status `ready` deltaP `27.753` edge `1.8778` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.3233` n `53` status `ready` deltaP `40.4809` edge `1.6348` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.2869` n `84` status `ready` deltaP `48.5119` edge `1.405` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.1252` n `53` status `ready` deltaP `34.2585` edge `0.7284` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.1917` n `84` status `ready` deltaP `44.0724` edge `0.3468` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.3624` n `53` status `ready` deltaP `39.9306` edge `0.264` maxDD `0.0`
- `market_context_high->index_24h` score `4.511` n `84` status `ready` deltaP `25.8929` edge `0.2128` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.447` n `53` status `ready` deltaP `42.7376` edge `0.1233` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1027` n `53` status `ready` deltaP `24.0959` edge `0.2116` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4176` n `53` status `ready` deltaP `20.4384` edge `0.2973` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.205` n `53` status `ready` deltaP `17.5658` edge `0.213` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1509` n `53` status `ready` deltaP `28.998` edge `0.0946` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.8493` n `53` status `ready` deltaP `18.5927` edge `0.6919` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0648` n `53` status `ready` deltaP `24.5424` edge `0.0339` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9898` n `53` status `ready` deltaP `26.4985` edge `0.2423` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.8374` n `53` status `ready` deltaP `19.2217` edge `0.0686` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `16.1281` edge `0.0193` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
