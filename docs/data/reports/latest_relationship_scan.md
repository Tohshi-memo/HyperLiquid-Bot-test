# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T17:52:29.204107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2644`

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

- `market_context_high->unknown_1h` score `12132.9087` n `107` status `ready` deltaP `0.5751` edge `1011.0917` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7838.4155` n `104` status `ready` deltaP `-0.2228` edge `653.2312` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.7142` n `88` status `ready` deltaP `44.5864` edge `1.8216` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7919` n `88` status `ready` deltaP `24.0531` edge `1.4907` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8888` n `104` status `ready` deltaP `3.6585` edge `0.4149` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2529` n `104` status `ready` deltaP `4.5732` edge `0.2815` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5079` n `104` status `ready` deltaP `18.5272` edge `0.0478` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.4604` n `88` status `ready` deltaP `19.0656` edge `0.2201` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2006` n `107` status `ready` deltaP `4.0601` edge `0.0137` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2528` n `107` status `ready` deltaP `4.4322` edge `0.0777` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2977` n `107` status `ready` deltaP `2.8261` edge `0.0042` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2379` n `107` status `ready` deltaP `-2.5589` edge `0.0361` maxDD `-5.4428`
- `market_context_high->index_4h` score `-1.2421` n `104` status `ready` deltaP `-3.3302` edge `-0.0027` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-1.432` n `107` status `ready` deltaP `5.4801` edge `0.022` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6531` n `107` status `ready` deltaP `-11.9775` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.4216` n `104` status `ready` deltaP `-15.7012` edge `-0.0042` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4895` n `107` status `ready` deltaP `-10.3713` edge `-0.0305` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1842` n `88` status `ready` deltaP `-24.1162` edge `-0.0106` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2514` n `104` status `ready` deltaP `-30.4878` edge `-0.1203` maxDD `-15.1252`
- `market_context_high->equity_4h` score `-9.4027` n `104` status `ready` deltaP `-8.0207` edge `-0.0624` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
