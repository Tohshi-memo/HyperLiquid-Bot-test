# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T17:37:43.295079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2642`

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

- `market_context_high->unknown_1h` score `12132.1347` n `107` status `ready` deltaP `0.5751` edge `1011.0272` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7942.8107` n `103` status `ready` deltaP `-0.2975` edge `661.9313` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.7689` n `88` status `ready` deltaP `44.7601` edge `1.825` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7728` n `88` status `ready` deltaP `23.8795` edge `1.4894` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.0642` n `103` status `ready` deltaP `3.9915` edge `0.4273` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.4487` n `103` status `ready` deltaP `4.9061` edge `0.2956` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5707` n `103` status `ready` deltaP `18.9069` edge `0.0505` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.4556` n `88` status `ready` deltaP `19.0656` edge `0.2197` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2091` n `107` status `ready` deltaP `3.9104` edge `0.0136` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2497` n `107` status `ready` deltaP `4.4322` edge `0.0781` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3062` n `107` status `ready` deltaP `2.6764` edge `0.0041` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.1995` n `103` status `ready` deltaP `-2.9008` edge `-0.0001` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.2212` n `107` status `ready` deltaP `-2.4092` edge `0.0365` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.444` n `107` status `ready` deltaP `5.4801` edge `0.021` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6519` n `107` status `ready` deltaP `-11.9775` edge `-0.0021` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.4075` n `103` status `ready` deltaP `-15.4585` edge `-0.004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4931` n `107` status `ready` deltaP `-10.3713` edge `-0.0308` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1691` n `88` status `ready` deltaP `-23.9426` edge `-0.0105` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.266` n `103` status `ready` deltaP `-30.5188` edge `-0.122` maxDD `-15.0703`
- `market_context_high->equity_4h` score `-9.147` n `103` status `ready` deltaP `-7.6753` edge `-0.0434` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
