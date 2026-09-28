# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T05:22:26.665366+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7862`

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

- `news_risk_high->unknown_24h` score `590.8848` n `139` status `ready` deltaP `1.2153` edge `49.2323` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.0271` n `139` status `ready` deltaP `15.921` edge `0.5413` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.8846` n `139` status `ready` deltaP `20.4561` edge `0.0902` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.035` n `139` status `ready` deltaP `20.3013` edge `0.1364` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.8324` n `139` status `ready` deltaP `19.0944` edge `0.103` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.7835` n `139` status `ready` deltaP `14.8243` edge `0.2221` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.2177` n `139` status `ready` deltaP `5.3709` edge `0.0734` maxDD `-4.2849`
- `news_risk_high->crypto_major_24h` score `0.1984` n `139` status `ready` deltaP `11.3521` edge `0.3843` maxDD `-26.1424`
- `news_risk_high->index_1h` score `0.0694` n `139` status `ready` deltaP `4.4103` edge `0.0054` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0231` n `139` status `ready` deltaP `3.9612` edge `0.0378` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.6274` n `139` status `ready` deltaP `0.4426` edge `0.0077` maxDD `-0.7016`
- `news_risk_high->crypto_alt_4h` score `-0.6664` n `139` status `ready` deltaP `4.5348` edge `0.1802` maxDD `-15.9436`
- `news_risk_high->index_4h` score `-0.7843` n `139` status `ready` deltaP `0.8653` edge `0.0142` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9488` n `139` status `ready` deltaP `-2.2477` edge `0.0216` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1243` n `139` status `ready` deltaP `-8.0699` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2088` n `139` status `ready` deltaP `10.2869` edge `-0.0022` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7087` n `139` status `ready` deltaP `-12.8147` edge `0.0158` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9617` n `139` status `ready` deltaP `-10.8183` edge `-0.0119` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.9251` n `139` status `ready` deltaP `-9.664` edge `-0.0391` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5494` n `139` status `ready` deltaP `-8.8832` edge `0.0053` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
