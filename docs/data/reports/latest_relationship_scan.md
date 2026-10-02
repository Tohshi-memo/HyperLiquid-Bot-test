# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T17:07:32.525374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4872`

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

- `market_context_high->unknown_1h` score `359.041` n `50` status `ready` deltaP `11.024` edge `29.8515` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.796` n `50` status `ready` deltaP `10.9756` edge `24.3265` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4488` n `73` status `ready` deltaP `39.795` edge `1.043` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.1235` n `50` status `ready` deltaP `16.5347` edge `0.8204` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.0856` n `73` status `ready` deltaP `32.9266` edge `0.5861` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0032` n `50` status `ready` deltaP `32.1736` edge `0.6774` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9619` n `50` status `ready` deltaP `17.0854` edge `0.5366` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9258` n `50` status `ready` deltaP `14.9695` edge `0.4396` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.7468` n `116` status `ready` deltaP `20.8316` edge `0.3911` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `2.9555` n `50` status `ready` deltaP `13.9042` edge `0.2199` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9353` n `50` status `ready` deltaP `13.7006` edge `0.1983` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8055` n `50` status `ready` deltaP `31.3171` edge `0.0385` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4231` n `116` status `ready` deltaP `22.0984` edge `0.1242` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.7322` n `50` status `ready` deltaP `9.1458` edge `0.3473` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5169` n `73` status `ready` deltaP `6.338` edge `0.4676` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3125` n `73` status `ready` deltaP `12.8354` edge `0.2101` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.0947` n `116` status `ready` deltaP `13.7406` edge `0.2797` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8081` n `116` status `ready` deltaP `4.8008` edge `0.0914` maxDD `-2.4854`
- `market_context_high->index_24h` score `0.7386` n `50` status `ready` deltaP `14.0972` edge `0.0578` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
