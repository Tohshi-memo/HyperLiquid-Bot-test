# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T12:22:43.014795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `12129.7804` n `107` status `ready` deltaP `0.7248` edge `1010.83` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7534.5484` n `107` status `ready` deltaP `-0.0071` edge `627.9075` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `23.0417` n `93` status `ready` deltaP `43.0779` edge `1.7618` maxDD `-8.3076`
- `market_context_high->crypto_alt_24h` score `11.386` n `93` status `ready` deltaP `23.3367` edge `1.4515` maxDD `-8.1203`
- `market_context_high->crypto_major_4h` score `1.214` n `107` status `ready` deltaP `2.4091` edge `0.367` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.3949` n `107` status `ready` deltaP `2.8664` edge `0.2391` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.0953` n `93` status `ready` deltaP `16.9467` edge `0.2038` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.0716` n `107` status `ready` deltaP `15.9234` edge `0.0288` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.2169` n `107` status `ready` deltaP `3.7607` edge `0.0136` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.5208` n `107` status `ready` deltaP `3.0122` edge `0.0746` maxDD `-8.2491`
- `market_context_high->index_1h` score `-0.6589` n `107` status `ready` deltaP `-0.8758` edge `0.0034` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.9024` n `107` status `ready` deltaP `-2.4092` edge `0.0326` maxDD `-6.2448`
- `market_context_high->index_4h` score `-1.1932` n `107` status `ready` deltaP `-2.6612` edge `-0.0009` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5301` n `107` status `ready` deltaP `-10.7435` edge `-0.0011` maxDD `-0.3827`
- `market_context_high->equity_1h` score `-2.4142` n `107` status `ready` deltaP `1.9279` edge `-0.0145` maxDD `-10.9626`
- `market_context_high->fx_4h` score `-2.4314` n `107` status `ready` deltaP `-15.4875` edge `-0.0046` maxDD `-1.9757`
- `market_context_high->commodity_1h` score `-2.5163` n `107` status `ready` deltaP `-11.0065` edge `-0.0285` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.8516` n `93` status `ready` deltaP `-20.3853` edge `-0.0066` maxDD `-5.6107`
- `market_context_high->commodity_4h` score `-7.8516` n `107` status `ready` deltaP `-26.9276` edge `-0.1129` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.5272` n `93` status `ready` deltaP `-18.9012` edge `-0.1257` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
