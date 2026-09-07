# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T13:22:26.945370+00:00`
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

- `risk_on_high->unknown_24h` score `390.4033` n `93` status `ready` deltaP `24.8264` edge `32.3681` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `390.4033` n `93` status `ready` deltaP `24.8264` edge `32.3681` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.3326` n `93` status `ready` deltaP `38.5865` edge `1.6555` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.3326` n `93` status `ready` deltaP `38.5865` edge `1.6555` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1742` n `93` status `ready` deltaP `32.1181` edge `1.0504` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1742` n `93` status `ready` deltaP `32.1181` edge `1.0504` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.5087` n `197` status `ready` deltaP `24.5039` edge `0.6032` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.4465` n `197` status `ready` deltaP `19.2708` edge `0.3254` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.2833` n `117` status `ready` deltaP `28.8058` edge `0.2854` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.2833` n `117` status `ready` deltaP `28.8058` edge `0.2854` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.6629` n `93` status `ready` deltaP `19.2708` edge `0.2601` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.6629` n `93` status `ready` deltaP `19.2708` edge `0.2601` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3567` n `117` status `ready` deltaP `24.3043` edge `0.2869` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3567` n `117` status `ready` deltaP `24.3043` edge `0.2869` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.3835` n `93` status `ready` deltaP `20.5589` edge `0.0658` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3835` n `93` status `ready` deltaP `20.5589` edge `0.0658` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6056` n `197` status `ready` deltaP `14.6476` edge `0.0755` maxDD `-0.1483`
- `risk_on_high->metal_24h` score `0.8479` n `93` status `ready` deltaP `17.1875` edge `0.1097` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8479` n `93` status `ready` deltaP `17.1875` edge `0.1097` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.7582` n `117` status `ready` deltaP `3.4982` edge `0.0751` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
