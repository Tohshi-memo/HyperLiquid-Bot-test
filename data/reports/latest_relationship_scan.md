# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T15:07:40.493715+00:00`
- Price records: `672`
- Market context records: `3903`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11358`

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

- `risk_on_high->unknown_4h` score `47.0605` n `72` status `ready` deltaP `4.6748` edge `6.2164` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.0605` n `72` status `ready` deltaP `4.6748` edge `6.2164` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `28.8411` n `36` status `ready` deltaP `25.0` edge `2.302` maxDD `-3.5528`
- `risk_on_and_context->crypto_major_24h` score `28.8411` n `36` status `ready` deltaP `25.0` edge `2.302` maxDD `-3.5528`
- `risk_on_high->equity_24h` score `24.7715` n `36` status `ready` deltaP `42.0139` edge `1.7842` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.7715` n `36` status `ready` deltaP `42.0139` edge `1.7842` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `17.5539` n `36` status `ready` deltaP `22.9167` edge `1.4098` maxDD `-6.3133`
- `risk_on_and_context->crypto_alt_24h` score `17.5539` n `36` status `ready` deltaP `22.9167` edge `1.4098` maxDD `-6.3133`
- `risk_on_high->index_24h` score `10.2208` n `36` status `ready` deltaP `30.0347` edge `0.6515` maxDD `0.0`
- `risk_on_and_context->index_24h` score `10.2208` n `36` status `ready` deltaP `30.0347` edge `0.6515` maxDD `0.0`
- `market_context_high->equity_24h` score `6.4808` n `163` status `ready` deltaP `20.5415` edge `0.7061` maxDD `-14.5715`
- `market_context_high->unknown_4h` score `6.4067` n `209` status `ready` deltaP `-1.9839` edge `1.3755` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `5.7604` n `72` status `ready` deltaP `20.5284` edge `0.4554` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.7604` n `72` status `ready` deltaP `20.5284` edge `0.4554` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.803` n `163` status `ready` deltaP `25.7402` edge `0.3426` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.0853` n `163` status `ready` deltaP `20.8312` edge `0.2614` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6575` n `209` status `ready` deltaP `16.6807` edge `0.2867` maxDD `-9.4488`
- `risk_on_high->equity_4h` score `2.6001` n `72` status `ready` deltaP `24.9492` edge `0.1638` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6001` n `72` status `ready` deltaP `24.9492` edge `0.1638` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.8668` n `163` status `ready` deltaP `3.9196` edge `0.5758` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
