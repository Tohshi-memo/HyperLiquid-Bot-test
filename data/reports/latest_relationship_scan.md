# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T16:07:30.919746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11757`

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

- `market_context_high->metal_24h` score `2.1549` n `105` status `ready` deltaP `8.41` edge `0.1811` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.6894` n `121` status `ready` deltaP `10.2526` edge `0.0307` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.5058` n `105` status `ready` deltaP `20.6248` edge `0.0449` maxDD `-4.071`
- `market_context_high->commodity_4h` score `0.3756` n `109` status `ready` deltaP `10.2428` edge `0.0645` maxDD `-2.7703`
- `market_context_high->fx_1h` score `-0.0381` n `121` status `ready` deltaP `7.1745` edge `-0.0044` maxDD `-1.0616`
- `market_context_high->index_24h` score `-0.2662` n `105` status `ready` deltaP `2.8987` edge `0.1098` maxDD `-5.7715`
- `market_context_high->fx_4h` score `-0.2734` n `109` status `ready` deltaP `7.0163` edge `0.0016` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.512` n `121` status `ready` deltaP `-2.874` edge `-0.0072` maxDD `-1.1422`
- `market_context_high->metal_4h` score `-0.7625` n `109` status `ready` deltaP `2.1748` edge `0.0064` maxDD `-1.422`
- `market_context_high->crypto_alt_1h` score `-0.9006` n `121` status `ready` deltaP `-5.8866` edge `-0.0133` maxDD `-2.3669`
- `market_context_high->index_1h` score `-0.9848` n `121` status `ready` deltaP `-2.5746` edge `-0.0115` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2824` n `121` status `ready` deltaP `3.5941` edge `-0.0319` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7733` n `109` status `ready` deltaP `-3.1998` edge `-0.0231` maxDD `-3.6005`
- `market_context_high->crypto_alt_4h` score `-1.7933` n `109` status `ready` deltaP `1.3874` edge `-0.0197` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6225` n `121` status `ready` deltaP `-6.7254` edge `-0.044` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-4.0104` n `105` status `ready` deltaP `-12.0885` edge `-0.1093` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.7544` n `109` status `ready` deltaP `-7.6485` edge `-0.1788` maxDD `-24.0463`
- `market_context_high->crypto_major_24h` score `-5.2297` n `105` status `ready` deltaP `-3.6545` edge `-0.2545` maxDD `-22.9955`
- `market_context_high->equity_24h` score `-5.4867` n `105` status `ready` deltaP `-8.6785` edge `0.2051` maxDD `-40.0243`
- `market_context_high->equity_4h` score `-7.2897` n `109` status `ready` deltaP `3.2306` edge `-0.2113` maxDD `-28.7503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
