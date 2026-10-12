# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T06:22:29.240603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9576`

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

- `market_context_high->unknown_4h` score `33.5631` n `119` status `ready` deltaP `-6.3781` edge `2.91` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `9.1922` n `54` status `ready` deltaP `18.8657` edge `1.3163` maxDD `-13.7531`
- `market_context_high->equity_24h` score `7.3344` n `54` status `ready` deltaP `21.7593` edge `0.5572` maxDD `-3.6186`
- `risk_on_high->crypto_major_4h` score `6.1947` n `51` status `ready` deltaP `35.2492` edge `0.3665` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.1947` n `51` status `ready` deltaP `35.2492` edge `0.3665` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.515` n `51` status `ready` deltaP `22.9436` edge `0.3514` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.515` n `51` status `ready` deltaP `22.9436` edge `0.3514` maxDD `-1.9151`
- `market_context_high->index_24h` score `4.7511` n `54` status `ready` deltaP `40.6828` edge `0.1472` maxDD `-0.1328`
- `market_context_high->crypto_alt_24h` score `4.68` n `54` status `ready` deltaP `-2.8356` edge `1.0401` maxDD `-24.0294`
- `risk_on_high->crypto_alt_1h` score `1.6626` n `60` status `ready` deltaP `9.1417` edge `0.1373` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6626` n `60` status `ready` deltaP `9.1417` edge `0.1373` maxDD `-2.4421`
- `risk_on_high->metal_4h` score `1.5606` n `51` status `ready` deltaP `17.2555` edge `0.0625` maxDD `-0.7989`
- `risk_on_and_context->metal_4h` score `1.5606` n `51` status `ready` deltaP `17.2555` edge `0.0625` maxDD `-0.7989`
- `risk_on_high->crypto_major_1h` score `1.3654` n `60` status `ready` deltaP `9.4012` edge `0.1164` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3654` n `60` status `ready` deltaP `9.4012` edge `0.1164` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.0573` n `128` status `ready` deltaP `8.3084` edge `0.1278` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.956` n `119` status `ready` deltaP `11.7198` edge `0.255` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.6234` n `128` status `ready` deltaP `4.87` edge `0.0958` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.447` n `119` status `ready` deltaP `5.8567` edge `0.2741` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.2257` n `119` status `ready` deltaP `9.9725` edge `0.0246` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
