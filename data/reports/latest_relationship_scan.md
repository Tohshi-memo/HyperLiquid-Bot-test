# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T05:07:27.046561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3218.0329` n `31` status `ready` deltaP `1.6322` edge `268.1761` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3188.359` n `31` status `ready` deltaP `3.7864` edge `265.677` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.5247` n `31` status `ready` deltaP `32.6389` edge `1.7428` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.0206` n `31` status `ready` deltaP `32.1181` edge `1.5376` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.9065` n `31` status `ready` deltaP `31.7708` edge `1.2804` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2234` n `31` status `ready` deltaP `23.4067` edge `0.6996` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.3928` n `31` status `ready` deltaP `33.1088` edge `0.4434` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9732` n `31` status `ready` deltaP `16.4732` edge `0.7977` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.7768` n `31` status `ready` deltaP `19.7077` edge `0.3775` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.757` n `31` status `ready` deltaP `39.8018` edge `0.1439` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.7216` n `31` status `ready` deltaP `33.6806` edge `0.0856` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7292` n `31` status `ready` deltaP `31.432` edge `0.0439` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.694` n `31` status `ready` deltaP `16.5443` edge `0.1329` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3847` n `31` status `ready` deltaP `28.8488` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0768` n `31` status `ready` deltaP `6.8669` edge `0.2666` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8668` n `31` status `ready` deltaP `10.0106` edge `0.2083` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1808` n `31` status `ready` deltaP `25.5408` edge `0.009` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4732` n `31` status `ready` deltaP `12.5098` edge `0.033` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0176` n `31` status `ready` deltaP `6.845` edge `-0.0036` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6252` n `31` status `ready` deltaP `-4.6069` edge `0.0048` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
