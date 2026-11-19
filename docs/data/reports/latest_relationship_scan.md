# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T21:37:31.674916+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2630`

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

- `market_context_high->unknown_1h` score `12002.3421` n `108` status `ready` deltaP `0.8373` edge `1000.2094` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7541.9104` n `107` status `ready` deltaP `-0.0071` edge `628.521` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.0754` n `88` status `ready` deltaP `42.6767` edge `1.7811` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `12.0168` n `88` status `ready` deltaP `25.9628` edge `1.5068` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8718` n `107` status `ready` deltaP `4.3908` edge `0.4086` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1843` n `107` status `ready` deltaP `5.3054` edge `0.2709` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5456` n `88` status `ready` deltaP `19.0656` edge `0.2272` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3876` n `107` status `ready` deltaP `17.6003` edge `0.0442` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.2165` n `108` status `ready` deltaP `4.9956` edge `0.0786` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2935` n `108` status `ready` deltaP `2.8166` edge `0.0048` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.316` n `108` status `ready` deltaP `3.8922` edge `0.0142` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.7215` n `108` status `ready` deltaP `-1.935` edge `0.0426` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.2873` n `108` status `ready` deltaP `5.8938` edge `0.0313` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6313` n `108` status `ready` deltaP `-11.6988` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9715` n `107` status `ready` deltaP `-3.5032` edge `-0.0066` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3962` n `107` status `ready` deltaP `-15.1826` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4259` n `108` status `ready` deltaP `-9.969` edge `-0.0275` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2668` n `88` status `ready` deltaP `-24.9842` edge `-0.0117` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1095` n `107` status `ready` deltaP `-29.1615` edge `-0.1121` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.6431` n `107` status `ready` deltaP `-7.9511` edge `-0.0829` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
