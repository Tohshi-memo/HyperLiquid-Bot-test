# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T03:52:33.729229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7652`

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

- `news_risk_high->unknown_24h` score `590.8812` n `139` status `ready` deltaP `1.2153` edge `49.232` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.4469` n `139` status `ready` deltaP `14.8794` edge `0.4999` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.7317` n `139` status `ready` deltaP `19.4145` edge `0.0844` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9534` n `139` status `ready` deltaP `20.3013` edge `0.1296` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.5564` n `139` status `ready` deltaP `18.1797` edge `0.0861` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.2825` n `139` status `ready` deltaP `13.7827` edge `0.1873` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.1985` n `139` status `ready` deltaP `5.3709` edge `0.0718` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0934` n `139` status `ready` deltaP `4.7097` edge `0.0054` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.0045` n `139` status `ready` deltaP `4.2606` edge `0.0381` maxDD `-1.957`
- `news_risk_high->crypto_major_24h` score `-0.6049` n `139` status `ready` deltaP `10.3105` edge `0.3243` maxDD `-26.1424`
- `news_risk_high->metal_1h` score `-0.6143` n `139` status `ready` deltaP `0.5923` edge `0.0078` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.8851` n `139` status `ready` deltaP `-0.0493` edge `0.0119` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9862` n `139` status `ready` deltaP `-2.5471` edge `0.0188` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1158` n `139` status `ready` deltaP `-7.9202` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->crypto_alt_4h` score `-1.1283` n `139` status `ready` deltaP `3.6202` edge `0.1478` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `-1.1701` n `139` status `ready` deltaP `10.8966` edge `-0.0013` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7503` n `139` status `ready` deltaP `-13.1196` edge `0.0125` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9501` n `139` status `ready` deltaP `-10.6686` edge `-0.0114` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.2059` n `139` status `ready` deltaP `-10.5786` edge `-0.069` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.496` n `139` status `ready` deltaP `-8.4258` edge `0.0067` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
