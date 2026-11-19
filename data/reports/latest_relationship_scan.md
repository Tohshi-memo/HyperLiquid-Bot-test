# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T09:22:29.218418+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11485.4754` n `112` status `ready` deltaP `1.1175` edge `957.1353` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7192.5304` n `111` status `ready` deltaP `0.2623` edge `599.4042` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.3514` n `98` status `ready` deltaP `39.594` edge `1.6466` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.4837` n `98` status `ready` deltaP `22.0097` edge `1.4097` maxDD `-13.3222`
- `market_context_high->metal_4h` score `-0.232` n `111` status `ready` deltaP `14.1563` edge `0.0173` maxDD `-6.1475`
- `market_context_high->metal_1h` score `-0.2474` n `112` status `ready` deltaP `3.2934` edge `0.0128` maxDD `-2.6517`
- `market_context_high->metal_24h` score `-0.3037` n `98` status `ready` deltaP `15.3557` edge `0.1948` maxDD `-15.7982`
- `market_context_high->crypto_major_4h` score `-0.3197` n `111` status `ready` deltaP `1.4337` edge `0.3077` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.5593` n `111` status `ready` deltaP `1.891` edge `0.1967` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8303` n `112` status `ready` deltaP `2.5449` edge `0.0633` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8307` n `112` status `ready` deltaP `-1.62` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0767` n `112` status `ready` deltaP `-2.0744` edge `0.0261` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4057` n `112` status `ready` deltaP `-9.2013` edge `-0.0009` maxDD `-0.392`
- `market_context_high->index_4h` score `-1.9534` n `111` status `ready` deltaP `-4.0266` edge `-0.0016` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5163` n `112` status `ready` deltaP `-11.2917` edge `-0.0266` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7744` n `112` status `ready` deltaP `1.2083` edge `-0.0215` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-3.7417` n `111` status `ready` deltaP `-15.5873` edge `-0.0036` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6938` n `98` status `ready` deltaP `-18.4666` edge `-0.0038` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3282` n `111` status `ready` deltaP `-23.1817` edge `-0.0965` maxDD `-14.7713`
- `market_context_high->index_24h` score `-9.1587` n `98` status `ready` deltaP `-16.7694` edge `-0.1092` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
