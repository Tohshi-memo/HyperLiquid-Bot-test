# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T08:07:27.777889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10439`

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

- `risk_on_high->unknown_24h` score `465.9605` n `93` status `ready` deltaP `26.7361` edge `38.6518` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `465.9605` n `93` status `ready` deltaP `26.7361` edge `38.6518` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1944` n `241` status `ready` deltaP `-2.3778` edge `2.1045` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `21.8637` n `93` status `ready` deltaP `36.8504` edge `1.628` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `21.8637` n `93` status `ready` deltaP `36.8504` edge `1.628` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.997` n `93` status `ready` deltaP `31.5972` edge `1.0391` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.997` n `93` status `ready` deltaP `31.5972` edge `1.0391` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.218` n `187` status `ready` deltaP `25.1801` edge `0.6578` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5517` n `187` status `ready` deltaP `22.9167` edge `0.3932` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.6622` n `117` status `ready` deltaP `30.4826` edge `0.3058` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6622` n `117` status `ready` deltaP `30.4826` edge `0.3058` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.3817` n `93` status `ready` deltaP `22.9167` edge `0.2957` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.3817` n `93` status `ready` deltaP `22.9167` edge `0.2957` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3469` n `117` status `ready` deltaP `24.1518` edge `0.2871` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3469` n `117` status `ready` deltaP `24.1518` edge `0.2871` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.6877` n `93` status `ready` deltaP `22.8159` edge `0.0761` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.6877` n `93` status `ready` deltaP `22.8159` edge `0.0761` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.5116` n `187` status `ready` deltaP `20.6941` edge `0.0928` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `1.043` n `93` status `ready` deltaP `17.5348` edge `0.1324` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `1.043` n `93` status `ready` deltaP `17.5348` edge `0.1324` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
