# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T16:22:31.499350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2622`

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

- `market_context_high->unknown_1h` score `12131.4447` n `107` status `ready` deltaP `0.5751` edge `1010.9697` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8048.551` n `102` status `ready` deltaP `-0.3736` edge `670.7435` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.035` n `88` status `ready` deltaP `45.2809` edge `1.8437` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7204` n `88` status `ready` deltaP `23.5322` edge `1.485` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.0361` n `102` status `ready` deltaP `4.0292` edge `0.4247` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.423` n `102` status `ready` deltaP `4.9438` edge `0.2932` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5459` n `102` status `ready` deltaP `18.6873` edge `0.0499` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.4093` n `88` status `ready` deltaP `18.892` edge `0.217` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2231` n `107` status `ready` deltaP `3.7607` edge `0.0128` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2723` n `107` status `ready` deltaP `4.2825` edge `0.0762` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3288` n `107` status `ready` deltaP `2.377` edge `0.0032` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.1894` n `102` status `ready` deltaP `-2.7679` edge `0.0003` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.2967` n `107` status `ready` deltaP `-2.7086` edge `0.0322` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.5748` n `107` status `ready` deltaP `5.1807` edge `0.0121` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6651` n `107` status `ready` deltaP `-12.1272` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.3851` n `102` status `ready` deltaP `-15.0586` edge `-0.0038` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.5134` n `107` status `ready` deltaP `-10.521` edge `-0.0315` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1365` n `88` status `ready` deltaP `-23.5954` edge `-0.0101` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3542` n `102` status `ready` deltaP `-31.0049` edge `-0.1276` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.129` n `102` status `ready` deltaP `-7.7804` edge `-0.0412` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
