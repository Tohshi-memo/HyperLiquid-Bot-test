# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T02:22:30.010180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7628`

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

- `news_risk_high->unknown_24h` score `591.2496` n `139` status `ready` deltaP `1.2153` edge `49.2627` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.8164` n `139` status `ready` deltaP `13.8377` edge `0.4543` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.5703` n `139` status `ready` deltaP `18.3728` edge `0.0779` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.8706` n `139` status `ready` deltaP `20.3013` edge `0.1227` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.32` n `139` status `ready` deltaP `17.2651` edge `0.0725` maxDD `-9.2079`
- `news_risk_high->index_1h` score `0.0179` n `139` status `ready` deltaP `3.8115` edge `0.0051` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0137` n `139` status `ready` deltaP `4.4727` edge `0.0601` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.0495` n `139` status `ready` deltaP `3.9612` edge `0.0356` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.2808` n `139` status `ready` deltaP `12.741` edge `0.1473` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6346` n `139` status `ready` deltaP `0.4426` edge `0.0071` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.9751` n `139` status `ready` deltaP `-0.9639` edge `0.0105` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-1.0306` n `139` status `ready` deltaP `-2.9962` edge `0.0161` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1234` n `139` status `ready` deltaP `11.6588` edge `-0.0004` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.15` n `139` status `ready` deltaP `-8.519` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.3759` n `139` status `ready` deltaP `9.2688` edge `0.267` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.4595` n `139` status `ready` deltaP `2.7055` edge `0.1263` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7918` n `139` status `ready` deltaP `-13.272` edge `0.0082` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9617` n `139` status `ready` deltaP `-10.8183` edge `-0.0119` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.3541` n `139` status `ready` deltaP `-11.4933` edge `-0.0819` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5642` n `139` status `ready` deltaP `-9.188` edge `0.0061` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
