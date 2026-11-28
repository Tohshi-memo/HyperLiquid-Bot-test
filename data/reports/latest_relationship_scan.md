# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T18:52:29.962611+00:00`
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

- `news_risk_high->unknown_4h` score `3270.4527` n `31` status `ready` deltaP `3.1766` edge `272.5222` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `2757.0264` n `31` status `ready` deltaP `2.231` edge `229.7549` maxDD `-0.7395`
- `news_risk_high->crypto_major_24h` score `25.4008` n `31` status `ready` deltaP `39.4097` edge `1.854` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6536` n `31` status `ready` deltaP `37.5` edge `1.3878` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2602` n `31` status `ready` deltaP `29.6875` edge `0.9071` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5347` n `31` status `ready` deltaP `24.7787` edge `0.7164` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.033` n `31` status `ready` deltaP `33.871` edge `0.325` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0003` n `31` status `ready` deltaP `19.0647` edge `0.7839` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2155` n `31` status `ready` deltaP `43.4476` edge `0.1578` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9053` n `31` status `ready` deltaP `17.1035` edge `0.2389` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7545` n `31` status `ready` deltaP `33.4137` edge `0.0328` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.5598` n `31` status `ready` deltaP `27.2569` edge `0.0316` maxDD `0.0`
- `news_risk_high->index_1h` score `2.4062` n `31` status `ready` deltaP `29.4476` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.333` n `31` status `ready` deltaP `15.6461` edge `0.1088` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1391` n `31` status `ready` deltaP `7.6154` edge `0.2696` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9961` n `31` status `ready` deltaP `11.0585` edge `0.2179` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1878` n `31` status `ready` deltaP `25.5408` edge `0.0099` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.5864` n `65` status `ready` deltaP `11.8293` edge `0.0096` maxDD `-0.1673`
- `news_risk_high->commodity_4h` score `0.5857` n `31` status `ready` deltaP `12.7901` edge `0.0296` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4836` n `31` status `ready` deltaP `13.7293` edge `0.0262` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
