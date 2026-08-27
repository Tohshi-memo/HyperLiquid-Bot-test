# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T02:07:24.923066+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.3073` n `50` status `ready` deltaP `11.5717` edge `4.0318` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.1683` n `50` status `ready` deltaP `36.5872` edge `0.9809` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2909` n `50` status `ready` deltaP `25.5549` edge `0.8638` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.3374` n `50` status `ready` deltaP `29.5959` edge `0.4241` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.7995` n `50` status `ready` deltaP `44.439` edge `0.0294` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.5665` n `50` status `ready` deltaP `36.3592` edge `0.07` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1335` n `137` status `ready` deltaP `24.2556` edge `0.1401` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.8038` n `50` status `ready` deltaP `37.0328` edge `-0.009` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.6496` n `50` status `ready` deltaP `15.3293` edge `0.1542` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4569` n `50` status `ready` deltaP `19.6048` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3307` n `50` status `ready` deltaP `17.4132` edge `0.0227` maxDD `-0.2319`
- `market_context_high->unknown_1h` score `1.2817` n `137` status `ready` deltaP `12.7016` edge `0.0671` maxDD `-1.5974`
- `news_risk_high->equity_4h` score `1.2605` n `50` status `ready` deltaP `19.75` edge `0.0499` maxDD `-2.1218`
- `market_context_high->unknown_24h` score `0.6326` n `134` status `ready` deltaP `5.6016` edge `0.0885` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5339` n `50` status `ready` deltaP `14.5988` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1443` n `50` status `ready` deltaP `7.509` edge `0.0024` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.132` n `50` status `ready` deltaP `7.0854` edge `0.0035` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.001` n `50` status `ready` deltaP `3.9042` edge `-0.0033` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.2648` n `50` status `ready` deltaP `6.3963` edge `-0.0116` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3321` n `137` status `ready` deltaP `4.5391` edge `0.0004` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
