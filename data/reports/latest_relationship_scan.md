# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T18:37:30.659773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7476`

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

- `news_risk_high->unknown_4h` score `3270.4215` n `31` status `ready` deltaP `3.1766` edge `272.5196` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `2756.2992` n `31` status `ready` deltaP `2.231` edge `229.6943` maxDD `-0.7395`
- `news_risk_high->crypto_major_24h` score `25.3485` n `31` status `ready` deltaP `39.2361` edge `1.8508` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.5761` n `31` status `ready` deltaP `37.3264` edge `1.3825` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2386` n `31` status `ready` deltaP `29.6875` edge `0.9053` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5311` n `31` status `ready` deltaP `24.7787` edge `0.7161` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0318` n `31` status `ready` deltaP `33.871` edge `0.3249` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0019` n `31` status `ready` deltaP `19.0647` edge `0.7841` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2155` n `31` status `ready` deltaP `43.4476` edge `0.1578` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9089` n `31` status `ready` deltaP `17.1035` edge `0.2392` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7533` n `31` status `ready` deltaP `33.4137` edge `0.0327` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.5411` n `31` status `ready` deltaP `27.0833` edge `0.0312` maxDD `0.0`
- `news_risk_high->index_1h` score `2.405` n `31` status `ready` deltaP `29.4476` edge `0.0126` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3354` n `31` status `ready` deltaP `15.6461` edge `0.109` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1399` n `31` status `ready` deltaP `7.6154` edge `0.2697` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0117` n `31` status `ready` deltaP `11.2082` edge `0.2189` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1878` n `31` status `ready` deltaP `25.5408` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5865` n `31` status `ready` deltaP `12.7901` edge `0.0297` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.573` n `65` status `ready` deltaP `11.6768` edge `0.0095` maxDD `-0.1673`
- `market_context_high->fx_1h` score `0.5028` n `66` status `ready` deltaP `12.72` edge `0.0018` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
