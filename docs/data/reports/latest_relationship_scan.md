# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T16:52:28.822366+00:00`
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

- `market_context_high->metal_24h` score `2.4803` n `102` status `ready` deltaP `10.3776` edge `0.1951` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.6272` n `102` status `ready` deltaP `22.1671` edge `0.047` maxDD `-3.8161`
- `market_context_high->commodity_1h` score `0.4278` n `121` status `ready` deltaP `10.2526` edge `0.0281` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.4248` n `109` status `ready` deltaP `10.2428` edge `0.0708` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.0266` n `109` status `ready` deltaP `8.5464` edge `0.0039` maxDD `-1.6928`
- `market_context_high->index_24h` score `0.0145` n `102` status `ready` deltaP `4.3977` edge `0.1232` maxDD `-5.7715`
- `market_context_high->fx_1h` score `-0.1548` n `121` status `ready` deltaP `5.821` edge `-0.0051` maxDD `-1.0616`
- `market_context_high->metal_1h` score `-0.5324` n `121` status `ready` deltaP `-3.5507` edge `-0.0072` maxDD `-0.9903`
- `market_context_high->metal_4h` score `-0.7892` n `109` status `ready` deltaP `2.9397` edge `0.0061` maxDD `-1.9841`
- `market_context_high->index_1h` score `-0.8078` n `121` status `ready` deltaP `-1.8978` edge `-0.0112` maxDD `-1.4774`
- `market_context_high->index_4h` score `-0.8711` n `109` status `ready` deltaP `-2.4349` edge `-0.0174` maxDD `-2.5774`
- `market_context_high->crypto_alt_1h` score `-1.293` n `121` status `ready` deltaP `-5.2098` edge `-0.0101` maxDD `-2.3669`
- `market_context_high->equity_1h` score `-1.3356` n `121` status `ready` deltaP `2.9173` edge `-0.0342` maxDD `-10.5179`
- `market_context_high->crypto_major_1h` score `-1.7249` n `121` status `ready` deltaP `-6.7254` edge `-0.0466` maxDD `-7.0428`
- `market_context_high->crypto_alt_4h` score `-1.8053` n `109` status `ready` deltaP `1.3874` edge `-0.0207` maxDD `-5.7857`
- `market_context_high->equity_24h` score `-2.9067` n `102` status `ready` deltaP `-7.238` edge `0.2988` maxDD `-32.0886`
- `market_context_high->crypto_alt_24h` score `-4.0835` n `102` status `ready` deltaP `-13.0774` edge `-0.1088` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.4773` n `102` status `ready` deltaP `-2.3279` edge `-0.2275` maxDD `-19.1463`
- `market_context_high->crypto_major_4h` score `-4.5948` n `109` status `ready` deltaP `-7.6485` edge `-0.1789` maxDD `-22.4012`
- `market_context_high->equity_4h` score `-5.6257` n `109` status `ready` deltaP `3.9956` edge `-0.1695` maxDD `-22.4087`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
