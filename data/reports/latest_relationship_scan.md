# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T20:07:32.404347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->crypto_alt_24h` score `25.853` n `40` status `ready` deltaP `50.8681` edge `1.8153` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `25.853` n `40` status `ready` deltaP `50.8681` edge `1.8153` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.0645` n `40` status `ready` deltaP `44.7917` edge `1.0401` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.0645` n `40` status `ready` deltaP `44.7917` edge `1.0401` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.2742` n `70` status `ready` deltaP `28.2448` edge `0.6274` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.2742` n `70` status `ready` deltaP `28.2448` edge `0.6274` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.3407` n `40` status `ready` deltaP `71.3542` edge `0.0527` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3407` n `40` status `ready` deltaP `71.3542` edge `0.0527` maxDD `0.0`
- `risk_on_high->equity_24h` score `6.3124` n `40` status `ready` deltaP `39.4097` edge `0.2633` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.3124` n `40` status `ready` deltaP `39.4097` edge `0.2633` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2247` n `40` status `ready` deltaP `53.2986` edge `0.1634` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2247` n `40` status `ready` deltaP `53.2986` edge `0.1634` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.3949` n `70` status `ready` deltaP `28.0183` edge `0.2911` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.3949` n `70` status `ready` deltaP `28.0183` edge `0.2911` maxDD `-0.5985`
- `market_context_high->unknown_4h` score `5.3165` n `149` status `ready` deltaP `21.054` edge `0.3497` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5833` n `117` status `ready` deltaP `37.0593` edge `0.2368` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.5803` n `70` status `ready` deltaP `18.2665` edge `0.3082` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.5803` n `70` status `ready` deltaP `18.2665` edge `0.3082` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.7141` n `70` status `ready` deltaP `34.1507` edge `0.1005` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.7141` n `70` status `ready` deltaP `34.1507` edge `0.1005` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
