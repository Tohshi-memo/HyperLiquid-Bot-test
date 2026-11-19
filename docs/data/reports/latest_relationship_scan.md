# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T19:37:27.783635+00:00`
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

- `market_context_high->unknown_1h` score `12133.4607` n `107` status `ready` deltaP `0.7248` edge `1011.1367` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7535.6368` n `107` status `ready` deltaP `-0.0071` edge `627.9982` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.3146` n `88` status `ready` deltaP `43.3712` edge `1.7964` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.8662` n `88` status `ready` deltaP `24.7475` edge `1.4956` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.6292` n `107` status `ready` deltaP `3.3237` edge `0.3955` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.9441` n `107` status `ready` deltaP `4.2383` edge `0.258` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.4952` n `88` status `ready` deltaP `19.0656` edge `0.223` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.31` n `107` status `ready` deltaP `16.9905` edge `0.0418` maxDD `-6.0054`
- `market_context_high->metal_1h` score `-0.199` n `107` status `ready` deltaP `4.0601` edge `0.0139` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2552` n `107` status `ready` deltaP `4.4322` edge `0.0774` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2969` n `107` status `ready` deltaP `2.8261` edge `0.0043` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2152` n `107` status `ready` deltaP `-2.4092` edge `0.037` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3589` n `107` status `ready` deltaP `5.9292` edge `0.0251` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6651` n `107` status `ready` deltaP `-12.1272` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->index_4h` score `-2.1001` n `107` status `ready` deltaP `-4.5703` edge `-0.0102` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4044` n `107` status `ready` deltaP `-9.6228` edge `-0.0284` maxDD `-3.9584`
- `market_context_high->fx_4h` score `-2.4231` n `107` status `ready` deltaP `-15.6399` edge `-0.0048` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.2433` n `88` status `ready` deltaP `-24.8106` edge `-0.0109` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1823` n `107` status `ready` deltaP `-29.7712` edge `-0.1141` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.1965` n `107` status `ready` deltaP `-9.0182` edge `-0.1219` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
