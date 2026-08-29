# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T18:07:28.243155+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `32.4169` n `62` status `ready` deltaP `4.4523` edge `2.7691` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `17.016` n `62` status `ready` deltaP `30.3708` edge `1.5531` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `10.7191` n `104` status `ready` deltaP `20.9535` edge `0.8268` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `5.8489` n `72` status `ready` deltaP `8.8076` edge `0.4877` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.7018` n `104` status `ready` deltaP `34.415` edge `0.2643` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.8218` n `72` status `ready` deltaP `2.5117` edge `0.2541` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5478` n `129` status `ready` deltaP `19.5311` edge `0.1253` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.395` n `72` status `ready` deltaP `34.9085` edge `0.0218` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3336` n `41` status `ready` deltaP `18.4862` edge `0.0093` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3336` n `41` status `ready` deltaP `18.4862` edge `0.0093` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.875` n `129` status `ready` deltaP `21.3438` edge `0.2757` maxDD `-20.9394`
- `market_context_high->unknown_1h` score `0.6777` n `141` status `ready` deltaP `8.1263` edge `0.0504` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.5046` n `72` status `ready` deltaP `14.6623` edge `0.0058` maxDD `-0.108`
- `news_risk_high->equity_24h` score `0.3773` n `62` status `ready` deltaP `16.2522` edge `0.2309` maxDD `-18.9364`
- `risk_on_high->crypto_alt_1h` score `0.2834` n `41` status `ready` deltaP `9.3289` edge `0.0217` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.2834` n `41` status `ready` deltaP `9.3289` edge `0.0217` maxDD `-2.1381`
- `market_context_high->crypto_alt_4h` score `0.2688` n `129` status `ready` deltaP `23.478` edge `0.3505` maxDD `-31.4361`
- `news_risk_high->commodity_1h` score `0.2148` n `72` status `ready` deltaP `8.3333` edge `0.004` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0892` n `129` status `ready` deltaP `10.1378` edge `0.0127` maxDD `-3.3377`
- `news_risk_high->index_24h` score `-0.092` n `62` status `ready` deltaP `10.7471` edge `0.0028` maxDD `-2.2325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
