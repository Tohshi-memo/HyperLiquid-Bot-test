# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T03:22:29.023442+00:00`
- Price records: `672`
- Market context records: `3648`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `37.039` n `32` status `ready` deltaP `42.1875` edge `2.8096` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.039` n `32` status `ready` deltaP `42.1875` edge `2.8096` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `33.3293` n `32` status `ready` deltaP `44.2708` edge `2.4823` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `33.3293` n `32` status `ready` deltaP `44.2708` edge `2.4823` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `29.2335` n `32` status `ready` deltaP `41.3194` edge `2.1758` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `29.2335` n `32` status `ready` deltaP `41.3194` edge `2.1758` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.9641` n `32` status `ready` deltaP `44.2708` edge `1.2852` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.9641` n `32` status `ready` deltaP `44.2708` edge `1.2852` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.574` n `32` status `ready` deltaP `20.8841` edge `0.9375` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.574` n `32` status `ready` deltaP `20.8841` edge `0.9375` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.8905` n `32` status `ready` deltaP `29.8611` edge `0.7346` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.8905` n `32` status `ready` deltaP `29.8611` edge `0.7346` maxDD `-0.7574`
- `market_context_high->equity_24h` score `9.0413` n `157` status `ready` deltaP `21.3409` edge `1.1776` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.568` n `157` status `ready` deltaP `29.6211` edge `0.6881` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.2979` n `157` status `ready` deltaP `24.1684` edge `0.6569` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `3.034` n `157` status `ready` deltaP `8.3698` edge `0.9037` maxDD `-49.5335`
- `risk_on_high->crypto_alt_4h` score `2.9832` n `32` status `ready` deltaP `1.1433` edge `0.4254` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.9832` n `32` status `ready` deltaP `1.1433` edge `0.4254` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.4825` n `32` status `ready` deltaP `9.5274` edge `0.3682` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4825` n `32` status `ready` deltaP `9.5274` edge `0.3682` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
