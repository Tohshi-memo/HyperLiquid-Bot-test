# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T07:52:27.989567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9600`

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

- `market_context_high->unknown_4h` score `34.5599` n `119` status `ready` deltaP `-3.6265` edge `2.9688` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `10.6273` n `54` status `ready` deltaP `20.544` edge `1.4891` maxDD `-13.7531`
- `market_context_high->crypto_alt_24h` score `7.9006` n `54` status `ready` deltaP `7.2338` edge `1.331` maxDD `-21.6397`
- `risk_on_high->crypto_alt_4h` score `4.4842` n `51` status `ready` deltaP `22.9436` edge `0.2655` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.4842` n `51` status `ready` deltaP `22.9436` edge `0.2655` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6779` n `51` status `ready` deltaP `35.2492` edge `0.3218` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6779` n `51` status `ready` deltaP `35.2492` edge `0.3218` maxDD `-4.1548`
- `market_context_high->equity_24h` score `3.348` n `54` status `ready` deltaP `11.6899` edge `0.484` maxDD `-6.9493`
- `market_context_high->index_24h` score `2.1977` n `54` status `ready` deltaP `30.6134` edge `0.129` maxDD `-0.4399`
- `risk_on_high->crypto_alt_1h` score `1.5249` n `54` status `ready` deltaP `9.0708` edge `0.1263` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.5249` n `54` status `ready` deltaP `9.0708` edge `0.1263` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.2306` n `54` status `ready` deltaP `8.5108` edge `0.1111` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.2306` n `54` status `ready` deltaP `8.5108` edge `0.1111` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.0192` n `122` status `ready` deltaP `8.4029` edge `0.124` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8234` n `119` status `ready` deltaP `11.7198` edge `0.238` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.5254` n `122` status `ready` deltaP `4.1695` edge `0.0923` maxDD `-3.4384`
- `market_context_high->unknown_1h` score `0.2904` n `122` status `ready` deltaP `-5.3499` edge `0.0935` maxDD `-1.024`
- `market_context_high->crypto_alt_4h` score `0.1919` n `119` status `ready` deltaP `5.8567` edge `0.2414` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.1426` n `122` status `ready` deltaP `5.5806` edge `0.007` maxDD `-0.4868`
- `risk_on_high->metal_4h` score `-0.1601` n `51` status `ready` deltaP `6.4054` edge `0.0226` maxDD `-1.2916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
