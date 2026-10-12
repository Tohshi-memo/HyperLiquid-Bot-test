# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T07:07:25.014288+00:00`
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

- `market_context_high->unknown_4h` score `33.8882` n `119` status `ready` deltaP `-5.0023` edge `2.922` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `9.9269` n `54` status `ready` deltaP `20.544` edge `1.3993` maxDD `-13.7531`
- `market_context_high->crypto_alt_24h` score `6.3264` n `54` status `ready` deltaP `2.1991` edge `1.187` maxDD `-22.5805`
- `risk_on_high->crypto_major_4h` score `5.8107` n `51` status `ready` deltaP `35.2492` edge `0.3345` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.8107` n `51` status `ready` deltaP `35.2492` edge `0.3345` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.9114` n `51` status `ready` deltaP `22.9436` edge `0.3011` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9114` n `51` status `ready` deltaP `22.9436` edge `0.3011` maxDD `-1.9151`
- `market_context_high->index_24h` score `4.0558` n `54` status `ready` deltaP `35.6482` edge `0.1377` maxDD `-0.3232`
- `market_context_high->equity_24h` score `4.0315` n `54` status `ready` deltaP `16.7245` edge `0.5188` maxDD `-5.4083`
- `risk_on_high->crypto_alt_1h` score `1.8465` n `57` status `ready` deltaP `10.8704` edge `0.1411` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.8465` n `57` status `ready` deltaP `10.8704` edge `0.1411` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.5557` n `57` status `ready` deltaP `10.655` edge `0.1239` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.5557` n `57` status `ready` deltaP `10.655` edge `0.1239` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.1504` n `125` status `ready` deltaP `9.1581` edge `0.1299` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8617` n `119` status `ready` deltaP `11.7198` edge `0.2429` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.684` n `125` status `ready` deltaP `5.2515` edge `0.0983` maxDD `-3.4384`
- `risk_on_high->metal_4h` score `0.677` n `51` status `ready` deltaP `11.8305` edge `0.0415` maxDD `-1.1164`
- `risk_on_and_context->metal_4h` score `0.677` n `51` status `ready` deltaP `11.8305` edge `0.0415` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `0.2972` n `119` status `ready` deltaP `5.8567` edge `0.2549` maxDD `-13.8008`
- `market_context_high->unknown_1h` score `0.1856` n `125` status `ready` deltaP `-4.8898` edge `0.0817` maxDD `-1.024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
