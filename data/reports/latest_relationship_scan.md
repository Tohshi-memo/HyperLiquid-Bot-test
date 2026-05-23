# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T15:37:15.070925+00:00`
- Price records: `672`
- Market context records: `1643`
- Flow alert records: `6640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.513` n `173` status `ready` deltaP `27.1426` edge `0.8544` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.4859` n `173` status `ready` deltaP `19.1693` edge `0.3005` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `3.4354` n `185` status `ready` deltaP `20.4459` edge `0.4164` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `1.8726` n `185` status `ready` deltaP `16.2055` edge `0.3189` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.5791` n `185` status `ready` deltaP `11.5866` edge `0.1638` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.2274` n `173` status `ready` deltaP `18.2437` edge `0.4705` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.0713` n `194` status `ready` deltaP `3.8567` edge `0.0858` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.043` n `173` status `ready` deltaP `23.9649` edge `0.7024` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-0.4507` n `173` status `ready` deltaP `24.4878` edge `0.9801` maxDD `-88.8062`
- `market_context_high->fx_24h` score `-0.4627` n `173` status `ready` deltaP `6.5778` edge `0.0225` maxDD `-1.3925`
- `market_context_high->index_4h` score `-0.4821` n `185` status `ready` deltaP `-0.0009` edge `0.0471` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.488` n `194` status `ready` deltaP `0.9121` edge `0.0341` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.494` n `194` status `ready` deltaP `0.4645` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.6237` n `194` status `ready` deltaP `0.3488` edge `0.0451` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.6796` n `194` status `ready` deltaP `-0.2191` edge `0.008` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.8211` n `194` status `ready` deltaP `1.8952` edge `-0.0056` maxDD `-6.6507`
- `market_context_high->metal_1h` score `-1.3144` n `194` status `ready` deltaP `2.9925` edge `0.0041` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.4076` n `185` status `ready` deltaP `-11.0947` edge `-0.0136` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4813` n `185` status `ready` deltaP `7.3266` edge `0.0969` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.3777` n `185` status `ready` deltaP `9.2467` edge `-0.116` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
