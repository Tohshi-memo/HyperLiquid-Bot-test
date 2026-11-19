# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T18:07:27.740063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2638`

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

- `market_context_high->unknown_1h` score `12133.6407` n `107` status `ready` deltaP `0.5751` edge `1011.1527` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7736.4454` n `105` status `ready` deltaP `-0.1495` edge `644.7332` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.6559` n `88` status `ready` deltaP `44.4128` edge `1.8179` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.8087` n `88` status `ready` deltaP `24.2267` edge `1.4917` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.7177` n `105` status `ready` deltaP `3.3348` edge `0.4028` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.0422` n `105` status `ready` deltaP `4.2494` edge `0.2661` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.4652` n `88` status `ready` deltaP `19.0656` edge `0.2205` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.4265` n `105` status `ready` deltaP `18.0052` edge `0.0445` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.2099` n `107` status `ready` deltaP `3.9104` edge `0.0135` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2591` n `107` status `ready` deltaP `4.4322` edge `0.0769` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2984` n `107` status `ready` deltaP `2.8261` edge `0.0041` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2391` n `107` status `ready` deltaP `-2.5589` edge `0.036` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.4164` n `107` status `ready` deltaP `5.6298` edge `0.0223` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6651` n `107` status `ready` deltaP `-12.1272` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->index_4h` score `-1.9842` n `105` status `ready` deltaP `-3.7515` edge `-0.006` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4284` n `105` status `ready` deltaP `-15.7869` edge `-0.0045` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4907` n `107` status `ready` deltaP `-10.3713` edge `-0.0306` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1842` n `88` status `ready` deltaP `-24.1162` edge `-0.0106` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2467` n `105` status `ready` deltaP `-30.4544` edge `-0.1189` maxDD `-15.2235`
- `market_context_high->equity_4h` score `-9.7406` n `105` status `ready` deltaP `-8.3595` edge `-0.0883` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
