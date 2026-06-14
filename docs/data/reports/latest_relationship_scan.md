# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T02:07:24.836384+00:00`
- Price records: `672`
- Market context records: `3848`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13787`

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

- `risk_on_high->crypto_major_24h` score `33.7534` n `32` status `ready` deltaP `34.0278` edge `2.5902` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.7534` n `32` status `ready` deltaP `34.0278` edge `2.5902` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.6879` n `32` status `ready` deltaP `42.0139` edge `1.9439` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.6879` n `32` status `ready` deltaP `42.0139` edge `1.9439` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.7075` n `32` status `ready` deltaP `31.9444` edge `1.7778` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.7075` n `32` status `ready` deltaP `31.9444` edge `1.7778` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.278` n `32` status `ready` deltaP `31.25` edge `0.7315` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.278` n `32` status `ready` deltaP `31.25` edge `0.7315` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.4703` n `128` status `ready` deltaP `-19.2708` edge `4.1908` maxDD `-200.1879`
- `market_context_high->equity_24h` score `6.5595` n `128` status `ready` deltaP `14.6701` edge `0.7518` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0519` n `128` status `ready` deltaP `25.7812` edge `0.4464` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.5707` n `63` status `ready` deltaP `16.7925` edge `0.4645` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5707` n `63` status `ready` deltaP `16.7925` edge `0.4645` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.9261` n `128` status `ready` deltaP `22.6563` edge `0.3193` maxDD `-9.1203`
- `risk_on_high->unknown_4h` score `2.657` n `63` status `ready` deltaP `11.4475` edge `0.4785` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `2.657` n `63` status `ready` deltaP `11.4475` edge `0.4785` maxDD `-13.467`
- `risk_on_high->equity_4h` score `2.648` n `63` status `ready` deltaP `24.9177` edge `0.168` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.648` n `63` status `ready` deltaP `24.9177` edge `0.168` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4198` n `32` status `ready` deltaP `14.0625` edge `0.0507` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4198` n `32` status `ready` deltaP `14.0625` edge `0.0507` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
