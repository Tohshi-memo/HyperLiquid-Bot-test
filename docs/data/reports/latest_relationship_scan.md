# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T01:37:25.676564+00:00`
- Price records: `672`
- Market context records: `4678`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `77.9225` n `136` status `ready` deltaP `11.9849` edge `6.4554` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.9617` n `136` status `ready` deltaP `10.5632` edge `0.4641` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.5065` n `136` status `ready` deltaP `9.4159` edge `0.1551` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5553` n `136` status `ready` deltaP `1.2636` edge `0.0249` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8467` n `136` status `ready` deltaP `2.735` edge `-0.0145` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.858` n `136` status `ready` deltaP `-2.655` edge `0.0064` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.8888` n `136` status `ready` deltaP `-0.7802` edge `-0.0005` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0238` n `136` status `ready` deltaP `-3.7733` edge `-0.0047` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2535` n `136` status `ready` deltaP `4.9139` edge `0.0173` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.4004` n `136` status `ready` deltaP `0.0718` edge `-0.0031` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7386` n `136` status `ready` deltaP `-4.7508` edge `-0.0128` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8258` n `136` status `ready` deltaP `-4.0463` edge `-0.0785` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.5801` n `136` status `ready` deltaP `-10.4677` edge `-0.011` maxDD `-5.4047`
- `market_context_high->commodity_24h` score `-5.1416` n `136` status `ready` deltaP `12.2957` edge `0.04` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6187` n `136` status `ready` deltaP `-2.8047` edge `-0.1208` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7608` n `136` status `ready` deltaP `-5.583` edge `-0.1509` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.2588` n `136` status `ready` deltaP `-10.2227` edge `-0.0826` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6738` n `136` status `ready` deltaP `-3.6765` edge `-0.2218` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.298` n `136` status `ready` deltaP `-1.9368` edge `-0.2938` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7117` n `136` status `ready` deltaP `-4.3849` edge `-0.3817` maxDD `-81.9122`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
