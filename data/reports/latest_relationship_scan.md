# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T13:52:33.261760+00:00`
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

- `risk_on_high->unknown_24h` score `381.7621` n `93` status `ready` deltaP `24.8264` edge `31.648` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `381.7621` n `93` status `ready` deltaP `24.8264` edge `31.648` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.3976` n `93` status `ready` deltaP `38.9337` edge `1.6586` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.3976` n `93` status `ready` deltaP `38.9337` edge `1.6586` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1958` n `93` status `ready` deltaP `32.1181` edge `1.0522` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1958` n `93` status `ready` deltaP `32.1181` edge `1.0522` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.4405` n `199` status `ready` deltaP `24.5804` edge `0.597` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.2915` n `199` status `ready` deltaP `18.9236` edge `0.3148` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.2893` n `117` status `ready` deltaP `28.8058` edge `0.2859` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.2893` n `117` status `ready` deltaP `28.8058` edge `0.2859` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.5619` n `93` status `ready` deltaP `18.9236` edge `0.254` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.5619` n `93` status `ready` deltaP `18.9236` edge `0.254` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3939` n `117` status `ready` deltaP `24.3043` edge `0.29` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3939` n `117` status `ready` deltaP `24.3043` edge `0.29` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.3438` n `93` status `ready` deltaP `20.2117` edge `0.0648` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.3438` n `93` status `ready` deltaP `20.2117` edge `0.0648` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.5611` n `199` status `ready` deltaP `14.3923` edge `0.0735` maxDD `-0.1483`
- `risk_on_high->metal_24h` score `0.8346` n `93` status `ready` deltaP `17.1875` edge `0.108` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8346` n `93` status `ready` deltaP `17.1875` edge `0.108` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.787` n `117` status `ready` deltaP `3.6479` edge `0.0765` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
