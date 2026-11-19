# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T22:22:27.084259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2618`

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

- `market_context_high->unknown_1h` score `12009.2576` n `108` status `ready` deltaP `1.1367` edge `1000.7837` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7548.9712` n `107` status `ready` deltaP `-0.0071` edge `629.1094` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.0118` n `88` status `ready` deltaP `42.6767` edge `1.7758` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `12.0324` n `88` status `ready` deltaP `25.9628` edge `1.5088` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.0068` n `107` status `ready` deltaP `4.8481` edge `0.4168` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2821` n `107` status `ready` deltaP `5.7627` edge `0.276` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5816` n `88` status `ready` deltaP `19.0656` edge `0.2302` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.453` n `107` status `ready` deltaP `18.0576` edge `0.0466` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.1752` n `108` status `ready` deltaP `5.295` edge `0.0819` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2833` n `108` status `ready` deltaP `2.9663` edge `0.0051` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.2908` n `108` status `ready` deltaP `4.0419` edge `0.0153` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.6818` n `108` status `ready` deltaP `-1.6356` edge `0.0457` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1902` n `108` status `ready` deltaP `6.1932` edge `0.0374` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6313` n `108` status `ready` deltaP `-11.6988` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9193` n `107` status `ready` deltaP `-3.0459` edge `-0.0053` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3883` n `107` status `ready` deltaP `-15.0302` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4259` n `108` status `ready` deltaP `-9.969` edge `-0.0275` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2704` n `88` status `ready` deltaP `-24.9842` edge `-0.012` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1083` n `107` status `ready` deltaP `-29.1615` edge `-0.112` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.4169` n `107` status `ready` deltaP `-7.4938` edge `-0.0671` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
