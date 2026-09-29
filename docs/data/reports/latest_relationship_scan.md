# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T01:37:28.557944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2637.5832` n `139` status `ready` deltaP `1.2153` edge `219.7905` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.9129` n `139` status `ready` deltaP `29.2891` edge `1.276` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.2373` n `139` status `ready` deltaP `28.8868` edge `0.7495` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.4568` n `139` status `ready` deltaP `24.5466` edge `0.9012` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7548` n `139` status `ready` deltaP `34.5186` edge `0.1523` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.2104` n `139` status `ready` deltaP `26.8985` edge `0.2737` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5503` n `139` status `ready` deltaP `27.1736` edge `0.1923` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9321` n `139` status `ready` deltaP `8.3458` edge `0.288` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.749` n `139` status `ready` deltaP `7.4667` edge `0.1037` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6267` n `139` status `ready` deltaP `8.1528` edge `0.064` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4994` n `139` status `ready` deltaP `9.2007` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1197` n `139` status `ready` deltaP `7.2678` edge `0.0269` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4824` n `139` status `ready` deltaP `1.7899` edge `0.0108` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5607` n `139` status `ready` deltaP `0.5966` edge `0.0524` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2497` n `139` status `ready` deltaP `-10.3154` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3573` n `139` status `ready` deltaP `8.0003` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4327` n `139` status `ready` deltaP `-9.1562` edge `0.0268` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9189` n `139` status `ready` deltaP `-5.853` edge `0.0645` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0124` n `139` status `ready` deltaP `-11.5668` edge `-0.0134` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7448` n `139` status `ready` deltaP `-10.56` edge `0.0002` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
