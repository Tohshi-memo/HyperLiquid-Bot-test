# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T22:07:33.095030+00:00`
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

- `market_context_high->unknown_1h` score `12009.0344` n `108` status `ready` deltaP `0.987` edge `1000.7661` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7548.8428` n `107` status `ready` deltaP `-0.0071` edge `629.0987` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.0406` n `88` status `ready` deltaP `42.6767` edge `1.7782` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `12.0316` n `88` status `ready` deltaP `25.9628` edge `1.5087` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.9586` n `107` status `ready` deltaP `4.6957` edge `0.4138` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2459` n `107` status `ready` deltaP `5.6103` edge `0.274` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5696` n `88` status `ready` deltaP `19.0656` edge `0.2292` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.4312` n `107` status `ready` deltaP `17.9051` edge `0.0458` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.176` n `108` status `ready` deltaP `5.295` edge `0.0818` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2756` n `108` status `ready` deltaP `3.116` edge `0.0051` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.3064` n `108` status `ready` deltaP `3.8922` edge `0.015` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.6849` n `108` status `ready` deltaP `-1.6356` edge `0.0453` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1902` n `108` status `ready` deltaP `6.1932` edge `0.0374` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6313` n `108` status `ready` deltaP `-11.6988` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9351` n `107` status `ready` deltaP `-3.1983` edge `-0.0056` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3883` n `107` status `ready` deltaP `-15.0302` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4259` n `108` status `ready` deltaP `-9.969` edge `-0.0275` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2692` n `88` status `ready` deltaP `-24.9842` edge `-0.0119` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1083` n `107` status `ready` deltaP `-29.1615` edge `-0.112` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.4819` n `107` status `ready` deltaP `-7.6462` edge `-0.0715` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
