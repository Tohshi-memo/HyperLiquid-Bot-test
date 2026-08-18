# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T08:06:55.525831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.0565` n `78` status `ready` deltaP `4.8993` edge `0.2595` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.2731` n `78` status `ready` deltaP `14.6758` edge `0.2487` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.938` n `97` status `ready` deltaP `8.5762` edge `0.0514` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7334` n `97` status `ready` deltaP `9.7216` edge `0.0984` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.6489` n `97` status `ready` deltaP `13.6126` edge `0.0209` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5847` n `97` status `ready` deltaP `12.0532` edge `0.0071` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5148` n `97` status `ready` deltaP `9.3108` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4682` n `97` status `ready` deltaP `11.8557` edge `0.1127` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `-0.016` n `78` status `ready` deltaP `13.6626` edge `-0.0736` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.0845` n `97` status `ready` deltaP `3.6082` edge `0.0076` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2455` n `97` status `ready` deltaP `2.8099` edge `0.0003` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2972` n `97` status `ready` deltaP `3.0094` edge `0.022` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3734` n `97` status `ready` deltaP `3.8047` edge `0.0118` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4611` n `97` status `ready` deltaP `-3.5913` edge `0.001` maxDD `-0.2273`
- `market_context_high->equity_4h` score `-0.4724` n `97` status `ready` deltaP `0.3583` edge `0.0487` maxDD `-2.5696`
- `market_context_high->crypto_major_1h` score `-0.4741` n `97` status `ready` deltaP `1.3797` edge `0.0145` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.7413` n `97` status `ready` deltaP `-0.4919` edge `0.007` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9097` n `97` status `ready` deltaP `-7.2829` edge `-0.0068` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.2527` n `78` status `ready` deltaP `-3.384` edge `0.035` maxDD `-5.1772`
- `market_context_high->index_24h` score `-3.4223` n `78` status `ready` deltaP `-11.0452` edge `-0.1521` maxDD `-8.3755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
