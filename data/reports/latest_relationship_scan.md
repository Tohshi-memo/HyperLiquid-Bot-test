# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T01:07:25.188682+00:00`
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

- `news_risk_high->unknown_24h` score `2644.5108` n `139` status `ready` deltaP `1.2153` edge `220.3678` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.5719` n `139` status `ready` deltaP `28.9419` edge `1.2499` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.0703` n `139` status `ready` deltaP `28.5396` edge `0.7379` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.2586` n `139` status `ready` deltaP `24.1993` edge `0.887` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7162` n `139` status `ready` deltaP `34.1714` edge `0.1514` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.1526` n `139` status `ready` deltaP `26.5513` edge `0.2712` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5647` n `139` status `ready` deltaP `27.1736` edge `0.1935` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9225` n `139` status `ready` deltaP `8.3458` edge `0.2872` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6626` n `139` status `ready` deltaP `7.1673` edge `0.0985` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5847` n `139` status `ready` deltaP `7.8534` edge `0.0625` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4863` n `139` status `ready` deltaP `9.051` edge `0.0092` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1173` n `139` status `ready` deltaP `7.2678` edge `0.0271` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4824` n `139` status `ready` deltaP `1.7899` edge `0.0108` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5996` n `139` status `ready` deltaP `0.2972` edge `0.0494` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3573` n `139` status `ready` deltaP `8.0003` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4288` n `139` status `ready` deltaP `-9.1562` edge `0.0273` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9267` n `139` status `ready` deltaP `-5.853` edge `0.0635` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0022` n `139` status `ready` deltaP `-11.4171` edge `-0.0131` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7484` n `139` status `ready` deltaP `-10.56` edge `-0.0001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
