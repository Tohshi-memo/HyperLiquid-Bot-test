# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T20:37:38.535019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `5.7771` n `88` status `ready` deltaP `1.967` edge `0.7743` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6186` n `88` status `ready` deltaP `14.8119` edge `0.2604` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3895` n `109` status `ready` deltaP `14.8327` edge `0.0842` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.3036` n `88` status `ready` deltaP `10.9717` edge `0.1868` maxDD `-5.7715`
- `market_context_high->fx_24h` score `1.2493` n `88` status `ready` deltaP `28.08` edge `0.0607` maxDD `-2.3515`
- `market_context_high->commodity_1h` score `0.8779` n `110` status `ready` deltaP `11.6576` edge `0.0311` maxDD `-0.8524`
- `market_context_high->equity_1h` score `-0.1818` n `110` status `ready` deltaP `6.1514` edge `0.0267` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.2202` n `110` status `ready` deltaP `5.1443` edge `-0.0031` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4326` n `109` status `ready` deltaP `5.4864` edge `0.0027` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.5921` n `109` status `ready` deltaP `2.1551` edge `-0.0032` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.6182` n `110` status `ready` deltaP `-1.9134` edge `-0.004` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.9954` n `110` status `ready` deltaP `-4.031` edge `-0.0065` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.0199` n `109` status `ready` deltaP `7.8205` edge `-0.0034` maxDD `-7.6983`
- `market_context_high->metal_4h` score `-1.1794` n `109` status `ready` deltaP `1.4097` edge `-0.0068` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.4071` n `110` status `ready` deltaP `-5.871` edge `-0.0152` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.258` n `110` status `ready` deltaP `-6.663` edge `-0.0441` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.2839` n `88` status `ready` deltaP `6.1834` edge `-0.0846` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.3093` n `109` status `ready` deltaP `-4.7326` edge `-0.0794` maxDD `-6.5193`
- `market_context_high->crypto_alt_24h` score `-5.0337` n `88` status `ready` deltaP `-18.7304` edge `-0.1503` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.1786` n `109` status `ready` deltaP `-9.1785` edge `-0.1876` maxDD `-18.954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
