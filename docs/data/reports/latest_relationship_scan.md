# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T07:37:23.601534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3724`

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

- `news_risk_high->unknown_1h` score `3354.7273` n `31` status `ready` deltaP `1.4825` edge `279.5683` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3239.2005` n `31` status `ready` deltaP `3.634` edge `269.9148` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.5811` n `31` status `ready` deltaP `31.8891` edge `1.5025` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.5288` n `31` status `ready` deltaP `29.8094` edge `1.012` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8277` n `31` status `ready` deltaP `25.4766` edge `0.8158` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9299` n `31` status `ready` deltaP `20.6628` edge `0.6101` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1995` n `31` status `ready` deltaP `28.6881` edge `0.2901` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8937` n `31` status `ready` deltaP `14.644` edge `0.6715` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8256` n `31` status `ready` deltaP `39.3694` edge `0.1525` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5432` n `31` status `ready` deltaP `13.7475` edge `0.2311` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2876` n `31` status `ready` deltaP `28.1003` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2725` n `31` status `ready` deltaP `28.0783` edge `0.0282` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2667` n `31` status `ready` deltaP `25.3033` edge `0.0202` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1112` n `31` status `ready` deltaP `13.9994` edge `0.1013` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8141` n `31` status `ready` deltaP `5.5196` edge `0.2419` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.654` n `31` status `ready` deltaP `8.3639` edge `0.192` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0897` n `31` status `ready` deltaP `23.8941` edge `0.0083` maxDD `-0.2315`
- `market_context_high->equity_1h` score `0.502` n `35` status `ready` deltaP `11.9718` edge `0.0254` maxDD `-1.2685`
- `market_context_high->fx_1h` score `0.3399` n `35` status `ready` deltaP `6.9932` edge `0.0031` maxDD `-0.0451`
- `news_risk_high->commodity_4h` score `0.2993` n `31` status `ready` deltaP `7.9121` edge `0.0254` maxDD `-0.5151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
