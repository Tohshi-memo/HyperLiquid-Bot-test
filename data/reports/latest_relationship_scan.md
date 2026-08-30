# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T19:22:24.256053+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `risk_on_high->crypto_alt_24h` score `26.1899` n `37` status `ready` deltaP `51.3889` edge `1.8399` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.1899` n `37` status `ready` deltaP `51.3889` edge `1.8399` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.579` n `37` status `ready` deltaP `45.3125` edge `1.0795` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.579` n `37` status `ready` deltaP `45.3125` edge `1.0795` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.5434` n `67` status `ready` deltaP `27.6051` edge `0.6541` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.5434` n `67` status `ready` deltaP `27.6051` edge `0.6541` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.624` n `37` status `ready` deltaP `39.9306` edge `0.2858` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.624` n `37` status `ready` deltaP `39.9306` edge `0.2858` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.3788` n `37` status `ready` deltaP `71.875` edge `0.0524` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3788` n `37` status `ready` deltaP `71.875` edge `0.0524` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2554` n `37` status `ready` deltaP `53.4722` edge `0.1648` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2554` n `37` status `ready` deltaP `53.4722` edge `0.1648` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.4485` n `149` status `ready` deltaP `21.054` edge `0.3607` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.394` n `67` status `ready` deltaP `27.1228` edge `0.297` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.394` n `67` status `ready` deltaP `27.1228` edge `0.297` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.512` n `117` status `ready` deltaP `36.3782` edge `0.2354` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.3969` n `67` status `ready` deltaP `16.8593` edge `0.3023` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.3969` n `67` status `ready` deltaP `16.8593` edge `0.3023` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.6816` n `67` status `ready` deltaP `33.639` edge `0.1012` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.6816` n `67` status `ready` deltaP `33.639` edge `0.1012` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
