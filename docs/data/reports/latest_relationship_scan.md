# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T00:37:21.925167+00:00`
- Price records: `672`
- Market context records: `1373`
- Flow alert records: `5864`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.1329` n `145` status `ready` deltaP `31.1099` edge `1.0002` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.1959` n `145` status `ready` deltaP `13.5213` edge `1.0929` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.6588` n `145` status `ready` deltaP `28.6602` edge `0.8988` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1184` n `145` status `ready` deltaP `22.1156` edge `0.3044` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6162` n `145` status `ready` deltaP `15.1808` edge `0.3495` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5631` n `170` status `ready` deltaP `8.7231` edge `0.1551` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2833` n `145` status `ready` deltaP `9.7306` edge `0.0456` maxDD `-1.2826`
- `market_context_high->index_1h` score `-0.0803` n `182` status `ready` deltaP `3.5567` edge `0.0125` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1541` n `170` status `ready` deltaP `10.5236` edge `0.0601` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.2106` n `182` status `ready` deltaP `2.16` edge `0.0239` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3584` n `170` status `ready` deltaP `0.4429` edge `0.06` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4188` n `182` status `ready` deltaP `2.1995` edge `-0.003` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4468` n `182` status `ready` deltaP `5.8482` edge `0.0026` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.6845` n `182` status `ready` deltaP `-0.2484` edge `0.0061` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.7763` n `182` status `ready` deltaP `0.204` edge `0.021` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.9791` n `182` status `ready` deltaP `-1.9954` edge `-0.0057` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3207` n `170` status `ready` deltaP `-8.6047` edge `-0.0149` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.6293` n `170` status `ready` deltaP `6.8221` edge `0.1507` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.8527` n `170` status `ready` deltaP `3.2245` edge `0.095` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-3.1106` n `170` status `ready` deltaP `1.6535` edge `-0.1827` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
