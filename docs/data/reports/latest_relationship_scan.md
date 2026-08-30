# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T18:52:27.961657+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11710`

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

- `risk_on_high->crypto_alt_24h` score `26.2309` n `35` status `ready` deltaP `51.7361` edge `1.841` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.2309` n `35` status `ready` deltaP `51.7361` edge `1.841` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.728` n `35` status `ready` deltaP `45.6597` edge `1.0896` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.728` n `35` status `ready` deltaP `45.6597` edge `1.0896` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.6087` n `65` status `ready` deltaP `27.1459` edge `0.6626` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.6087` n `65` status `ready` deltaP `27.1459` edge `0.6626` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.749` n `35` status `ready` deltaP `40.2778` edge `0.2939` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.749` n `35` status `ready` deltaP `40.2778` edge `0.2939` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.4054` n `35` status `ready` deltaP `72.2222` edge `0.0523` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4054` n `35` status `ready` deltaP `72.2222` edge `0.0523` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2554` n `35` status `ready` deltaP `53.4722` edge `0.1648` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2554` n `35` status `ready` deltaP `53.4722` edge `0.1648` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.5613` n `149` status `ready` deltaP `21.054` edge `0.3701` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.273` n `65` status `ready` deltaP `26.4798` edge `0.2912` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.273` n `65` status `ready` deltaP `26.4798` edge `0.2912` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5036` n `117` status `ready` deltaP `36.3782` edge `0.2347` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.1696` n `65` status `ready` deltaP `15.8489` edge `0.2901` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.1696` n `65` status `ready` deltaP `15.8489` edge `0.2901` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.6438` n `65` status `ready` deltaP `33.2716` edge `0.1005` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.6438` n `65` status `ready` deltaP `33.2716` edge `0.1005` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
