# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T02:07:29.613187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1458.706` n `134` status `ready` deltaP `1.9097` edge `121.5461` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.7253` n `134` status `ready` deltaP `30.1746` edge `1.4675` maxDD `-7.9908`
- `news_risk_high->equity_24h` score `8.9624` n `134` status `ready` deltaP `30.0088` edge `0.7817` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.923` n `134` status `ready` deltaP `25.495` edge `0.889` maxDD `-15.8971`
- `news_risk_high->index_24h` score `4.0902` n `134` status `ready` deltaP `36.2563` edge `0.1483` maxDD `-0.5992`
- `news_risk_high->metal_24h` score `3.6724` n `134` status `ready` deltaP `28.2442` edge `0.2556` maxDD `-3.0287`
- `news_risk_high->equity_4h` score `2.9085` n `137` status `ready` deltaP `29.354` edge `0.2068` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.2156` n `137` status `ready` deltaP `12.4043` edge `0.3679` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1714` n `137` status `ready` deltaP `9.3863` edge `0.1261` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8139` n `137` status `ready` deltaP `8.5253` edge `0.0733` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.519` n `137` status `ready` deltaP `9.1241` edge `0.0112` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0611` n `137` status `ready` deltaP `7.7611` edge `0.0285` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2622` n `137` status `ready` deltaP `3.0967` edge `0.074` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4787` n `137` status `ready` deltaP `1.2063` edge `0.015` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2806` n `137` status `ready` deltaP `-7.7344` edge `0.0297` maxDD `-3.0517`
- `news_risk_high->crypto_major_4h` score `-1.3609` n `137` status `ready` deltaP `-2.6983` edge `0.115` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4554` n `137` status `ready` deltaP `6.5037` edge `-0.0086` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8456` n `137` status `ready` deltaP `-8.9744` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8887` n `137` status `ready` deltaP `-9.7426` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2573` n `137` status `ready` deltaP `-9.004` edge `0.0125` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
