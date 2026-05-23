# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T08:07:15.316862+00:00`
- Price records: `672`
- Market context records: `1611`
- Flow alert records: `6547`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `12.813` n `186` status `ready` deltaP `28.6738` edge `1.0059` maxDD `-6.678`
- `market_context_high->crypto_alt_24h` score `7.4343` n `186` status `ready` deltaP `24.9888` edge `0.9499` maxDD `-37.0904`
- `market_context_high->crypto_major_24h` score `6.3581` n `186` status `ready` deltaP `24.8376` edge `0.7363` maxDD `-26.4299`
- `market_context_high->equity_24h` score `4.1029` n `186` status `ready` deltaP `19.3548` edge `0.4709` maxDD `-16.3087`
- `market_context_high->index_24h` score `3.8977` n `186` status `ready` deltaP `20.8109` edge `0.2947` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2951` n `195` status `ready` deltaP `10.9162` edge `0.1446` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2558` n `195` status `ready` deltaP `13.1324` edge `0.2772` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1295` n `195` status `ready` deltaP `9.2378` edge `0.2259` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1959` n `186` status `ready` deltaP `7.9469` edge `0.0356` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3008` n `195` status `ready` deltaP `0.661` edge `0.0594` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.503` n `195` status `ready` deltaP `1.19` edge `0.031` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6801` n `195` status `ready` deltaP `0.4192` edge `0.0037` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8751` n `195` status `ready` deltaP `-0.8552` edge `0.0292` maxDD `-6.1883`
- `market_context_high->fx_1h` score `-0.8766` n `195` status `ready` deltaP `-0.9634` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.9059` n `195` status `ready` deltaP `0.0915` edge `0.0328` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.121` n `195` status `ready` deltaP `-0.3424` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1562` n `195` status `ready` deltaP `4.805` edge `0.0052` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.4091` n `195` status `ready` deltaP `8.9188` edge `0.0923` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4109` n `195` status `ready` deltaP `-11.0248` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1972` n `195` status `ready` deltaP `-14.1307` edge `-0.1094` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
