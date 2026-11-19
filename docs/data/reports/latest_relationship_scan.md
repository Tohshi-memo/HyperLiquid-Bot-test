# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T19:52:34.488085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2668`

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

- `market_context_high->unknown_1h` score `11996.7309` n `108` status `ready` deltaP `0.8373` edge `999.7418` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7535.416` n `107` status `ready` deltaP `-0.0071` edge `627.9798` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.2599` n `88` status `ready` deltaP `43.1976` edge `1.793` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.867` n `88` status `ready` deltaP `24.7475` edge `1.4957` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.6268` n `107` status `ready` deltaP `3.3237` edge `0.3953` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.9671` n `107` status `ready` deltaP `4.3908` edge `0.2589` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.4988` n `88` status `ready` deltaP `19.0656` edge `0.2233` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.31` n `107` status `ready` deltaP `16.9905` edge `0.0418` maxDD `-6.0054`
- `market_context_high->index_1h` score `-0.3223` n `108` status `ready` deltaP `2.3675` edge `0.0041` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3295` n `108` status `ready` deltaP `3.9477` edge `0.0711` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.3531` n `108` status `ready` deltaP `3.5928` edge `0.0131` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.8181` n `108` status `ready` deltaP `-2.8332` edge `0.0362` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.4313` n `108` status `ready` deltaP `5.4447` edge `0.0223` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6816` n `108` status `ready` deltaP `-12.2976` edge `-0.0022` maxDD `-0.4757`
- `market_context_high->index_4h` score `-2.0977` n `107` status `ready` deltaP `-4.5703` edge `-0.01` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4144` n `107` status `ready` deltaP `-15.4875` edge `-0.0047` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4223` n `108` status `ready` deltaP `-9.8193` edge `-0.0282` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2584` n `88` status `ready` deltaP `-24.9842` edge `-0.011` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1641` n `107` status `ready` deltaP `-29.6188` edge `-0.1136` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.1689` n `107` status `ready` deltaP `-9.0182` edge `-0.1196` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
