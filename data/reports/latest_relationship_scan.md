# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T15:07:40.302940+00:00`
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

- `news_risk_high->unknown_1h` score `3268.1161` n `31` status `ready` deltaP `1.4825` edge `272.3507` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3171.8561` n `31` status `ready` deltaP `3.3291` edge `264.3048` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.2102` n `31` status `ready` deltaP `25.8681` edge `1.1784` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.8651` n `31` status `ready` deltaP `25.1736` edge `0.9876` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7632` n `31` status `ready` deltaP `25.0` edge `0.8136` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.6917` n `31` status `ready` deltaP `20.2055` edge `0.5933` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.8341` n `31` status `ready` deltaP `30.3649` edge `0.3318` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8168` n `31` status `ready` deltaP `13.1196` edge `0.6718` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.0718` n `31` status `ready` deltaP `13.1105` edge `0.2794` maxDD `-0.1986`
- `news_risk_high->equity_1h` score `2.5501` n `31` status `ready` deltaP `16.0952` edge `0.1239` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.5265` n `31` status `ready` deltaP `26.7361` edge `0.0323` maxDD `0.0`
- `news_risk_high->index_4h` score `2.509` n `31` status `ready` deltaP `30.06` edge `0.0347` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.3823` n `31` status `ready` deltaP `28.8488` edge `0.0147` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9217` n `31` status `ready` deltaP `6.1184` edge `0.2517` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6906` n `31` status `ready` deltaP `8.9627` edge `0.1927` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.194` n `31` status `ready` deltaP `25.5408` edge `0.0107` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3279` n `31` status `ready` deltaP `11.2903` edge `0.0225` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.148` n `31` status `ready` deltaP `7.9121` edge `0.006` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5089` n `31` status `ready` deltaP `-3.4093` edge `0.0065` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
