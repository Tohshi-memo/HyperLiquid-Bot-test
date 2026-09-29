# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T06:07:26.188172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7346`

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

- `news_risk_high->unknown_24h` score `2623.1508` n `139` status `ready` deltaP `1.2153` edge `218.5878` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6253` n `139` status `ready` deltaP `32.4141` edge `1.4812` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.5505` n `139` status `ready` deltaP `32.0118` edge `0.8381` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.9433` n `139` status `ready` deltaP `27.498` edge `1.0054` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0096` n `139` status `ready` deltaP `36.4284` edge `0.1608` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.6745` n `139` status `ready` deltaP `29.8499` edge `0.2927` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5075` n `139` status `ready` deltaP `27.4785` edge `0.1867` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.3717` n `139` status `ready` deltaP `9.5653` edge `0.3165` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7973` n `140` status `ready` deltaP `7.4551` edge `0.1078` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6317` n `140` status `ready` deltaP `8.6056` edge `0.0614` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4758` n `140` status `ready` deltaP `8.905` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0965` n `139` status `ready` deltaP `7.5726` edge `0.0268` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5188` n `140` status `ready` deltaP `0.9666` edge `0.0553` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.567` n `140` status `ready` deltaP `0.8383` edge `0.0101` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3248` n `139` status `ready` deltaP `8.61` edge `-0.0059` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4553` n `139` status `ready` deltaP `-9.1562` edge `0.0239` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7666` n `139` status `ready` deltaP `-4.7859` edge `0.0769` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8729` n `140` status `ready` deltaP `-9.6792` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0208` n `140` status `ready` deltaP `-11.7151` edge `-0.0135` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9265` n `139` status `ready` deltaP `-11.9319` edge `-0.0058` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
