# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T14:37:26.592225+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3271.0957` n `31` status `ready` deltaP `1.4825` edge `272.599` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3168.9857` n `31` status `ready` deltaP `3.3291` edge `264.0656` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.2949` n `31` status `ready` deltaP `26.0417` edge `1.1843` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.1017` n `31` status `ready` deltaP `25.5208` edge `1.005` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.8467` n `31` status `ready` deltaP `25.1736` edge `0.8194` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7037` n `31` status `ready` deltaP `20.2055` edge `0.5943` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.8725` n `31` status `ready` deltaP `30.3649` edge `0.335` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8262` n `31` status `ready` deltaP `13.1196` edge `0.673` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.138` n `31` status `ready` deltaP `13.4577` edge `0.2826` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.5771` n `31` status `ready` deltaP `27.0833` edge `0.0342` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5681` n `31` status `ready` deltaP `16.0952` edge `0.1254` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5174` n `31` status `ready` deltaP `30.06` edge `0.0354` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3859` n `31` status `ready` deltaP `28.8488` edge `0.015` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9131` n `31` status `ready` deltaP `6.1184` edge `0.2506` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6984` n `31` status `ready` deltaP `8.9627` edge `0.1937` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1971` n `31` status `ready` deltaP `25.5408` edge `0.0111` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3256` n `31` status `ready` deltaP `11.2903` edge `0.0222` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1166` n `31` status `ready` deltaP `7.6072` edge `0.004` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5221` n `31` status `ready` deltaP `-3.559` edge `0.0064` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
