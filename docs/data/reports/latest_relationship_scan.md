# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T13:37:27.311209+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10186`

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

- `risk_on_high->unknown_24h` score `386.0377` n `93` status `ready` deltaP `24.8264` edge `32.0043` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `386.0377` n `93` status `ready` deltaP `24.8264` edge `32.0043` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.3561` n `93` status `ready` deltaP `38.7601` edge `1.6563` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.3561` n `93` status `ready` deltaP `38.7601` edge `1.6563` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1778` n `93` status `ready` deltaP `32.1181` edge `1.0507` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1778` n `93` status `ready` deltaP `32.1181` edge `1.0507` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.471` n `198` status `ready` deltaP `24.5423` edge `0.5998` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.369` n `198` status `ready` deltaP `19.0972` edge `0.3201` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.2821` n `117` status `ready` deltaP `28.8058` edge `0.2853` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.2821` n `117` status `ready` deltaP `28.8058` edge `0.2853` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.613` n `93` status `ready` deltaP `19.0972` edge `0.2571` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.613` n `93` status `ready` deltaP `19.0972` edge `0.2571` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3699` n `117` status `ready` deltaP `24.3043` edge `0.288` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3699` n `117` status `ready` deltaP `24.3043` edge `0.288` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.3637` n `93` status `ready` deltaP `20.3853` edge `0.0653` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3637` n `93` status `ready` deltaP `20.3853` edge `0.0653` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.5834` n `198` status `ready` deltaP `14.5202` edge `0.0745` maxDD `-0.1483`
- `risk_on_high->metal_24h` score `0.8409` n `93` status `ready` deltaP `17.1875` edge `0.1088` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8409` n `93` status `ready` deltaP `17.1875` edge `0.1088` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.757` n `117` status `ready` deltaP `3.4982` edge `0.075` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
