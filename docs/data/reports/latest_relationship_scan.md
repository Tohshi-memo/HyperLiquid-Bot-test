# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T21:22:32.961573+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2636`

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

- `market_context_high->unknown_1h` score `11999.0493` n `108` status `ready` deltaP `0.8373` edge `999.935` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7538.6356` n `107` status `ready` deltaP `-0.0071` edge `628.2481` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.0814` n `88` status `ready` deltaP `42.6767` edge `1.7816` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.9875` n `88` status `ready` deltaP `25.7892` edge `1.5042` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8128` n `107` status `ready` deltaP `4.2383` edge `0.4047` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1373` n `107` status `ready` deltaP `5.153` edge `0.268` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5336` n `88` status `ready` deltaP `19.0656` edge `0.2262` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3646` n `107` status `ready` deltaP `17.4478` edge `0.0433` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.2344` n `108` status `ready` deltaP `4.8459` edge `0.0773` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3028` n `108` status `ready` deltaP `2.6669` edge `0.0046` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.322` n `108` status `ready` deltaP `3.8922` edge `0.0137` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.7402` n `108` status `ready` deltaP `-2.0847` edge `0.0412` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3377` n `108` status `ready` deltaP `5.7441` edge `0.0281` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6444` n `108` status `ready` deltaP `-11.8485` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9909` n `107` status `ready` deltaP `-3.6556` edge `-0.0072` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4049` n `107` status `ready` deltaP `-15.335` edge `-0.0045` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4271` n `108` status `ready` deltaP `-9.969` edge `-0.0276` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2656` n `88` status `ready` deltaP `-24.9842` edge `-0.0116` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1107` n `107` status `ready` deltaP `-29.1615` edge `-0.1122` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.7453` n `107` status `ready` deltaP `-8.1035` edge `-0.0904` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
