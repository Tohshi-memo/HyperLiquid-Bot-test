# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T07:22:32.160565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7376`

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

- `news_risk_high->unknown_24h` score `2616.036` n `139` status `ready` deltaP `1.2153` edge `217.9949` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1134` n `139` status `ready` deltaP `32.9349` edge `1.5184` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.8743` n `139` status `ready` deltaP `32.8799` edge `0.8593` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.0873` n `139` status `ready` deltaP `27.498` edge `1.0174` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1042` n `139` status `ready` deltaP `37.2964` edge `0.1629` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7908` n `139` status `ready` deltaP `30.718` edge `0.2966` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5051` n `139` status `ready` deltaP `27.4785` edge `0.1865` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0829` n `139` status `ready` deltaP `8.9555` edge `0.2965` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8988` n `142` status `ready` deltaP `7.7191` edge `0.1145` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6697` n `142` status `ready` deltaP `8.6004` edge `0.0646` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4706` n `142` status `ready` deltaP `8.7501` edge `0.0099` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0843` n `139` status `ready` deltaP `7.7251` edge `0.0268` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4546` n `142` status `ready` deltaP `1.2419` edge `0.0617` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5421` n `142` status `ready` deltaP `1.0141` edge `0.011` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3295` n `139` status `ready` deltaP `8.61` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4427` n `139` status `ready` deltaP `-9.0037` edge `0.0245` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8747` n `139` status `ready` deltaP `-5.2433` edge `0.0661` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8876` n `142` status `ready` deltaP `-9.8929` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0613` n `142` status `ready` deltaP `-12.2986` edge `-0.0148` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0085` n `139` status `ready` deltaP `-12.2368` edge `-0.0106` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
