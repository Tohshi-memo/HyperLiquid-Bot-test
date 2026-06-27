# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T20:07:34.448981+00:00`
- Price records: `672`
- Market context records: `4967`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.6681` n `100` status `ready` deltaP `9.3054` edge `1.4604` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.3208` n `93` status `ready` deltaP `29.1372` edge `0.8839` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4961` n `93` status `ready` deltaP `22.0184` edge `0.6003` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.2159` n `93` status `ready` deltaP `22.4921` edge `0.5866` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8822` n `90` status `ready` deltaP `27.3958` edge `0.3418` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7737` n `93` status `ready` deltaP `14.3637` edge `0.1902` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5521` n `93` status `ready` deltaP `12.3164` edge `0.1218` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9586` n `93` status `ready` deltaP `12.1886` edge `0.0448` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.9235` n `100` status `ready` deltaP `9.0` edge `0.0743` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9028` n `100` status `ready` deltaP `6.491` edge `0.1358` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.7186` n `100` status `ready` deltaP `8.4491` edge `0.1058` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0262` n `100` status `ready` deltaP `3.7904` edge `0.0349` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.4278` n `100` status `ready` deltaP `1.2515` edge `0.0123` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.6198` n `100` status `ready` deltaP `0.994` edge `0.0077` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0205` n `93` status `ready` deltaP `6.763` edge `-0.0056` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.0807` n `93` status `ready` deltaP `-5.7616` edge `-0.0031` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4505` n `90` status `ready` deltaP `-1.9445` edge `-0.0125` maxDD `-2.6327`
- `market_context_high->fx_1h` score `-1.5655` n `100` status `ready` deltaP `-9.9581` edge `-0.0041` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-4.1052` n `90` status `ready` deltaP `19.0625` edge `0.0417` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0175` n `90` status `ready` deltaP `-9.9306` edge `0.0269` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
