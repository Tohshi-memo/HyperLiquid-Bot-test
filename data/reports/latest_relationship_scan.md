# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T14:22:36.848493+00:00`
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

- `news_risk_high->unknown_1h` score `3271.1257` n `31` status `ready` deltaP `1.4825` edge `272.6015` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3169.4083` n `31` status `ready` deltaP `3.4815` edge `264.0998` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.3844` n `31` status `ready` deltaP `26.2153` edge `1.1906` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.2248` n `31` status `ready` deltaP `25.6944` edge `1.0141` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9206` n `31` status `ready` deltaP `25.3472` edge `0.8244` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7373` n `31` status `ready` deltaP `20.2055` edge `0.5971` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.8965` n `31` status `ready` deltaP `30.3649` edge `0.337` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8511` n `31` status `ready` deltaP `13.1196` edge `0.6762` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.1711` n `31` status `ready` deltaP `13.6313` edge `0.2842` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.603` n `31` status `ready` deltaP `27.2569` edge `0.0352` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5801` n `31` status `ready` deltaP `16.0952` edge `0.1264` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.5222` n `31` status `ready` deltaP `30.06` edge `0.0358` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3871` n `31` status `ready` deltaP `28.8488` edge `0.0151` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9349` n `31` status `ready` deltaP `6.1184` edge `0.2534` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.721` n `31` status `ready` deltaP `8.9627` edge `0.1966` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1979` n `31` status `ready` deltaP `25.5408` edge `0.0112` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3248` n `31` status `ready` deltaP `11.2903` edge `0.0221` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1024` n `31` status `ready` deltaP `7.4547` edge `0.0032` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5065` n `31` status `ready` deltaP `-3.4093` edge `0.0067` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
