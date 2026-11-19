# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T19:22:30.816293+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2664`

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

- `market_context_high->unknown_1h` score `12133.4967` n `107` status `ready` deltaP `0.7248` edge `1011.1397` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7535.6728` n `107` status `ready` deltaP `-0.0071` edge `628.0012` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.3669` n `88` status `ready` deltaP `43.5448` edge `1.7996` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.8525` n `88` status `ready` deltaP `24.5739` edge `1.495` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.6098` n `107` status `ready` deltaP `3.1713` edge `0.3949` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.9127` n `107` status `ready` deltaP `4.0859` edge `0.2564` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.4928` n `88` status `ready` deltaP `19.0656` edge `0.2228` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3088` n `107` status `ready` deltaP `16.9905` edge `0.0417` maxDD `-6.0054`
- `market_context_high->metal_1h` score `-0.1998` n `107` status `ready` deltaP `4.0601` edge `0.0138` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2669` n `107` status `ready` deltaP `4.4322` edge `0.0759` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2969` n `107` status `ready` deltaP `2.8261` edge `0.0043` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2439` n `107` status `ready` deltaP `-2.5589` edge `0.0356` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3625` n `107` status `ready` deltaP `5.9292` edge `0.0248` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.677` n `107` status `ready` deltaP `-12.2769` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->index_4h` score `-2.1013` n `107` status `ready` deltaP `-4.5703` edge `-0.0103` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4224` n `107` status `ready` deltaP `-9.7725` edge `-0.0289` maxDD `-3.9584`
- `market_context_high->fx_4h` score `-2.4231` n `107` status `ready` deltaP `-15.6399` edge `-0.0048` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.2282` n `88` status `ready` deltaP `-24.637` edge `-0.0108` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2005` n `107` status `ready` deltaP `-29.9237` edge `-0.1146` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.2145` n `107` status `ready` deltaP `-9.0182` edge `-0.1234` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
