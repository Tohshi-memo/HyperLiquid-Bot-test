# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T11:37:28.099016+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `11144.3629` n `116` status `ready` deltaP `1.8171` edge `928.7046` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.1993` n `108` status `ready` deltaP `0.5194` edge `621.3749` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4517` n `102` status `ready` deltaP `30.77` edge `1.3418` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.688` n `102` status `ready` deltaP `16.8812` edge `1.1321` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.9911` n `108` status `ready` deltaP `6.2274` edge `0.4063` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.731` n `108` status `ready` deltaP `7.2944` edge `0.3032` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5158` n `108` status `ready` deltaP `17.7168` edge `0.0593` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.087` n `116` status `ready` deltaP `5.3892` edge `0.0194` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.4143` n `116` status `ready` deltaP `3.7425` edge `0.0616` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.422` n `116` status `ready` deltaP `3.3657` edge `0.0036` maxDD `-1.2295`
- `market_context_high->equity_1h` score `-1.2228` n `116` status `ready` deltaP `6.401` edge `0.0333` maxDD `-10.8962`
- `market_context_high->crypto_alt_1h` score `-1.2346` n `116` status `ready` deltaP `-2.292` edge `0.0346` maxDD `-5.4428`
- `market_context_high->fx_1h` score `-1.3622` n `116` status `ready` deltaP `-8.44` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.6641` n `108` status `ready` deltaP `-0.3952` edge `-0.0017` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.145` n `116` status `ready` deltaP `-7.0153` edge `-0.0188` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3613` n `108` status `ready` deltaP `-14.6454` edge `-0.0035` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.6331` n `102` status `ready` deltaP `14.5425` edge `0.1133` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5503` n `102` status `ready` deltaP `-16.7177` edge `-0.0071` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.7965` n `108` status `ready` deltaP `-26.8236` edge `-0.1016` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.7838` n `108` status `ready` deltaP `-4.3078` edge `-0.0211` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
