# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T03:07:25.299630+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10425`

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

- `risk_on_high->unknown_24h` score `511.8917` n `95` status `ready` deltaP `26.7361` edge `42.4794` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `511.8917` n `95` status `ready` deltaP `26.7361` edge `42.4794` maxDD `0.0`
- `market_context_high->unknown_1h` score `22.9388` n `243` status `ready` deltaP `-2.8326` edge `2.0029` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.551` n `95` status `ready` deltaP `33.5819` edge `1.5404` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.551` n `95` status `ready` deltaP `33.5819` edge `1.5404` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.1396` n `95` status `ready` deltaP `30.5556` edge `0.9746` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.1396` n `95` status `ready` deltaP `30.5556` edge `0.9746` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.9499` n `184` status `ready` deltaP `24.0339` edge `0.6431` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5728` n `184` status `ready` deltaP `23.0903` edge `0.3938` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.36` n `119` status `ready` deltaP `29.03` edge `0.2903` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.36` n `119` status `ready` deltaP `29.03` edge `0.2903` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.3464` n `95` status `ready` deltaP `23.0903` edge `0.2916` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.3464` n `95` status `ready` deltaP `23.0903` edge `0.2916` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.8446` n `119` status `ready` deltaP `22.0575` edge `0.2592` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8446` n `119` status `ready` deltaP `22.0575` edge `0.2592` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7276` n `95` status `ready` deltaP `23.4046` edge `0.0755` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7276` n `95` status `ready` deltaP `23.4046` edge `0.0755` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6185` n `184` status `ready` deltaP `21.6712` edge `0.0952` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `0.954` n `95` status `ready` deltaP `16.663` edge `0.1268` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.954` n `95` status `ready` deltaP `16.663` edge `0.1268` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
