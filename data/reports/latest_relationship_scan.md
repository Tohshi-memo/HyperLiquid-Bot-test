# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T01:22:32.412889+00:00`
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

- `news_risk_high->unknown_24h` score `2641.3416` n `139` status `ready` deltaP `1.2153` edge `220.1037` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.743` n `139` status `ready` deltaP `29.1155` edge `1.263` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.1574` n `139` status `ready` deltaP `28.7132` edge `0.744` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.3613` n `139` status `ready` deltaP `24.373` edge `0.8944` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7361` n `139` status `ready` deltaP `34.345` edge `0.1519` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.1821` n `139` status `ready` deltaP `26.7249` edge `0.2725` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5599` n `139` status `ready` deltaP `27.1736` edge `0.1931` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9237` n `139` status `ready` deltaP `8.3458` edge `0.2873` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.695` n `139` status `ready` deltaP `7.317` edge `0.1002` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6063` n `139` status `ready` deltaP `8.0031` edge `0.0633` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4994` n `139` status `ready` deltaP `9.2007` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1185` n `139` status `ready` deltaP `7.2678` edge `0.027` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4824` n `139` status `ready` deltaP `1.7899` edge `0.0108` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5848` n `139` status `ready` deltaP `0.4469` edge `0.0503` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3573` n `139` status `ready` deltaP `8.0003` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4295` n `139` status `ready` deltaP `-9.1562` edge `0.0272` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9235` n `139` status `ready` deltaP `-5.853` edge `0.0639` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0108` n `139` status `ready` deltaP `-11.5668` edge `-0.0132` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7472` n `139` status `ready` deltaP `-10.56` edge `0.0` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
