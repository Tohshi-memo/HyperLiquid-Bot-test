# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T18:37:30.609168+00:00`
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

- `market_context_high->unknown_1h` score `12133.5315` n `107` status `ready` deltaP `0.5751` edge `1011.1436` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7536.376` n `107` status `ready` deltaP `-0.0071` edge `628.0598` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.5285` n `88` status `ready` deltaP `44.0656` edge `1.8096` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.8134` n `88` status `ready` deltaP `24.2267` edge `1.4923` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.5` n `107` status `ready` deltaP `2.714` edge `0.3888` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.7585` n `107` status `ready` deltaP `3.6286` edge `0.2466` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.476` n `88` status `ready` deltaP `19.0656` edge `0.2214` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.2932` n `107` status `ready` deltaP `16.9905` edge `0.0404` maxDD `-6.0054`
- `market_context_high->metal_1h` score `-0.2013` n `107` status `ready` deltaP `4.0601` edge `0.0136` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2661` n `107` status `ready` deltaP `4.4322` edge `0.076` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2891` n `107` status `ready` deltaP `2.9758` edge `0.0043` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2403` n `107` status `ready` deltaP `-2.5589` edge `0.0359` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3637` n `107` status `ready` deltaP `5.9292` edge `0.0247` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.677` n `107` status `ready` deltaP `-12.2769` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->index_4h` score `-2.1217` n `107` status `ready` deltaP `-4.5703` edge `-0.012` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4398` n `107` status `ready` deltaP `-15.9448` edge `-0.0049` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4703` n `107` status `ready` deltaP `-10.2216` edge `-0.0299` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.2132` n `88` status `ready` deltaP `-24.4634` edge `-0.0107` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2659` n `107` status `ready` deltaP `-30.381` edge `-0.117` maxDD `-15.5426`
- `market_context_high->index_24h` score `-10.3672` n `88` status `ready` deltaP `-25.1262` edge `-0.1542` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
