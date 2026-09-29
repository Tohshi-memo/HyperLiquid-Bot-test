# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T00:52:28.664618+00:00`
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

- `news_risk_high->unknown_24h` score `2647.8384` n `139` status `ready` deltaP `1.2153` edge `220.6451` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4081` n `139` status `ready` deltaP `28.7683` edge `1.2374` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.9868` n `139` status `ready` deltaP `28.366` edge `0.7321` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.1631` n `139` status `ready` deltaP `24.0257` edge `0.8802` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.6963` n `139` status `ready` deltaP `33.9978` edge `0.1509` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.1219` n `139` status `ready` deltaP `26.3777` edge `0.2698` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5719` n `139` status `ready` deltaP `27.1736` edge `0.1941` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9189` n `139` status `ready` deltaP `8.3458` edge `0.2869` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6339` n `139` status `ready` deltaP `7.0176` edge `0.0971` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5799` n `139` status `ready` deltaP `7.8534` edge `0.0621` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4851` n `139` status `ready` deltaP `9.051` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1161` n `139` status `ready` deltaP `7.2678` edge `0.0272` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4812` n `139` status `ready` deltaP `1.7899` edge `0.0109` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6067` n `139` status `ready` deltaP `0.2972` edge `0.0485` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3565` n `139` status `ready` deltaP `8.0003` edge `-0.0059` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4272` n `139` status `ready` deltaP `-9.1562` edge `0.0275` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9298` n `139` status `ready` deltaP `-5.853` edge `0.0631` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0022` n `139` status `ready` deltaP `-11.4171` edge `-0.0131` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7508` n `139` status `ready` deltaP `-10.56` edge `-0.0003` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
