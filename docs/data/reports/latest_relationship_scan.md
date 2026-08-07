# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T16:22:38.812909+00:00`
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

- `market_context_high->metal_24h` score `2.2602` n `104` status `ready` deltaP `9.0514` edge `0.1856` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.5474` n `104` status `ready` deltaP `21.128` edge `0.0457` maxDD `-3.9767`
- `market_context_high->commodity_1h` score `0.4426` n `121` status `ready` deltaP `10.2526` edge `0.03` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3912` n `109` status `ready` deltaP `10.2428` edge `0.0665` maxDD `-2.7703`
- `market_context_high->fx_1h` score `-0.0946` n `121` status `ready` deltaP `6.4977` edge `-0.0046` maxDD `-1.0616`
- `market_context_high->index_24h` score `-0.1731` n `104` status `ready` deltaP `3.3872` edge `0.1143` maxDD `-5.7715`
- `market_context_high->fx_4h` score `-0.2162` n `109` status `ready` deltaP `7.0163` edge `0.0022` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.5511` n `121` status `ready` deltaP `-3.5507` edge `-0.0077` maxDD `-1.1422`
- `market_context_high->metal_4h` score `-0.6773` n `109` status `ready` deltaP `2.9397` edge `0.0084` maxDD `-1.422`
- `market_context_high->crypto_alt_1h` score `-0.8584` n `121` status `ready` deltaP `-5.2098` edge `-0.0124` maxDD `-2.3669`
- `market_context_high->index_1h` score `-0.8668` n `121` status `ready` deltaP `-1.8978` edge `-0.011` maxDD `-1.5529`
- `market_context_high->index_4h` score `-1.0192` n `109` status `ready` deltaP `-2.4349` edge `-0.0201` maxDD `-3.2134`
- `market_context_high->equity_1h` score `-1.2653` n `121` status `ready` deltaP `3.5941` edge `-0.0297` maxDD `-10.5179`
- `market_context_high->crypto_major_1h` score `-1.7054` n `121` status `ready` deltaP `-6.7254` edge `-0.0441` maxDD `-7.0428`
- `market_context_high->crypto_alt_4h` score `-1.7909` n `109` status `ready` deltaP `1.3874` edge `-0.0195` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-4.0386` n `104` status `ready` deltaP `-12.4111` edge `-0.1095` maxDD `-4.5445`
- `market_context_high->equity_24h` score `-4.625` n `104` status `ready` deltaP `-8.2094` edge `0.236` maxDD `-37.335`
- `market_context_high->crypto_major_4h` score `-4.7142` n `109` status `ready` deltaP `-7.6485` edge `-0.1788` maxDD `-23.6343`
- `market_context_high->crypto_major_24h` score `-4.9908` n `104` status `ready` deltaP `-3.2224` edge `-0.2462` maxDD `-21.773`
- `market_context_high->equity_4h` score `-6.5796` n `109` status `ready` deltaP `3.9956` edge `-0.1905` maxDD `-26.4215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
