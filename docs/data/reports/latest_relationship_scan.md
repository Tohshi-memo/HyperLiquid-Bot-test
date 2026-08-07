# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T16:37:36.280202+00:00`
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

- `market_context_high->metal_24h` score `2.3678` n `103` status `ready` deltaP `9.7071` edge `0.1902` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.5839` n `103` status `ready` deltaP `21.642` edge `0.0462` maxDD `-3.9159`
- `market_context_high->commodity_1h` score `0.4403` n `121` status `ready` deltaP `10.2526` edge `0.0297` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.4092` n `109` status `ready` deltaP `10.2428` edge `0.0688` maxDD `-2.7703`
- `market_context_high->index_24h` score `-0.0804` n `103` status `ready` deltaP `3.8867` edge `0.1187` maxDD `-5.7715`
- `market_context_high->fx_4h` score `-0.0918` n `109` status `ready` deltaP `7.7814` edge `0.0033` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.1536` n `121` status `ready` deltaP `5.821` edge `-0.005` maxDD `-1.0616`
- `market_context_high->metal_1h` score `-0.5425` n `121` status `ready` deltaP `-3.5507` edge `-0.0075` maxDD `-1.0706`
- `market_context_high->metal_4h` score `-0.7118` n `109` status `ready` deltaP `2.9397` edge `0.0081` maxDD `-1.6277`
- `market_context_high->index_1h` score `-0.8085` n `121` status `ready` deltaP `-1.8978` edge `-0.011` maxDD `-1.4977`
- `market_context_high->index_4h` score `-0.9349` n `109` status `ready` deltaP `-2.4349` edge `-0.0181` maxDD `-2.8424`
- `market_context_high->equity_1h` score `-1.2832` n `121` status `ready` deltaP `3.5941` edge `-0.032` maxDD `-10.5179`
- `market_context_high->crypto_alt_1h` score `-1.305` n `121` status `ready` deltaP `-5.2098` edge `-0.0111` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-1.714` n `121` status `ready` deltaP `-6.7254` edge `-0.0452` maxDD `-7.0428`
- `market_context_high->crypto_alt_4h` score `-1.7909` n `109` status `ready` deltaP `1.3874` edge `-0.0195` maxDD `-5.7857`
- `market_context_high->equity_24h` score `-3.7653` n `103` status `ready` deltaP `-7.7294` edge `0.2672` maxDD `-34.6888`
- `market_context_high->crypto_alt_24h` score `-4.0601` n `103` status `ready` deltaP `-12.7407` edge `-0.1091` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.6563` n `109` status `ready` deltaP `-7.6485` edge `-0.1783` maxDD `-23.0807`
- `market_context_high->crypto_major_24h` score `-4.7378` n `103` status `ready` deltaP `-2.7802` edge `-0.2371` maxDD `-20.4754`
- `market_context_high->equity_4h` score `-6.0541` n `109` status `ready` deltaP `3.9956` edge `-0.1774` maxDD `-24.2997`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
