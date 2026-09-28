# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T04:22:28.150829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7786`

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

- `news_risk_high->unknown_24h` score `590.6472` n `139` status `ready` deltaP `1.2153` edge `49.2125` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.6595` n `139` status `ready` deltaP `15.2266` edge `0.5153` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.7834` n `139` status `ready` deltaP `19.7617` edge `0.0864` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9798` n `139` status `ready` deltaP `20.3013` edge `0.1318` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.6516` n `139` status `ready` deltaP `18.4846` edge `0.092` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.4579` n `139` status `ready` deltaP `14.1299` edge `0.1996` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.2273` n `139` status `ready` deltaP `5.5206` edge `0.0732` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0814` n `139` status `ready` deltaP `4.56` edge `0.0054` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0099` n `139` status `ready` deltaP `4.1109` edge `0.0379` maxDD `-1.957`
- `news_risk_high->crypto_major_24h` score `-0.3023` n `139` status `ready` deltaP `10.6577` edge `0.3472` maxDD `-26.1424`
- `news_risk_high->metal_1h` score `-0.6143` n `139` status `ready` deltaP `0.5923` edge `0.0078` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.8499` n `139` status `ready` deltaP `0.2556` edge `0.0128` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9699` n `139` status `ready` deltaP `-2.3974` edge `0.0199` maxDD `-7.2607`
- `news_risk_high->crypto_alt_4h` score `-0.9899` n `139` status `ready` deltaP `3.925` edge `0.1573` maxDD `-15.9436`
- `news_risk_high->fx_1h` score `-1.0994` n `139` status `ready` deltaP `-7.6208` edge `-0.0021` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1803` n `139` status `ready` deltaP `10.7442` edge `-0.0016` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7394` n `139` status `ready` deltaP `-13.1196` edge `0.0139` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9516` n `139` status `ready` deltaP `-10.6686` edge `-0.0116` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.1261` n `139` status `ready` deltaP `-10.2737` edge `-0.0608` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5106` n `139` status `ready` deltaP `-8.5783` edge `0.0065` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
