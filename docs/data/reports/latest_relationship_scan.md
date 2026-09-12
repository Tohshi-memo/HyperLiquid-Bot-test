# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T10:52:30.996368+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11807`

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

- `market_context_high->unknown_24h` score `3191.2046` n `112` status `ready` deltaP `13.6657` edge `265.8478` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2249` n `82` status `ready` deltaP `-3.6038` edge `32.0016` maxDD `-1.7068`
- `risk_on_high->unknown_24h` score `101.0737` n `63` status `ready` deltaP `15.4514` edge `8.3198` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `101.0737` n `63` status `ready` deltaP `15.4514` edge `8.3198` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `24.4106` n `59` status `ready` deltaP `54.505` edge `1.7609` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `20.749` n `63` status `ready` deltaP `40.6746` edge `1.4809` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.749` n `63` status `ready` deltaP `40.6746` edge `1.4809` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.6062` n `59` status `ready` deltaP `29.967` edge `1.3162` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `17.5464` n `112` status `ready` deltaP `34.3254` edge `1.3161` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2375` n `59` status `ready` deltaP `33.9366` edge `0.8034` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0125` n `63` status `ready` deltaP `37.3264` edge `0.5022` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0125` n `63` status `ready` deltaP `37.3264` edge `0.5022` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6957` n `112` status `ready` deltaP `37.3264` edge `0.4758` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3885` n `59` status `ready` deltaP `53.6458` edge `0.3414` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.2295` n `63` status `ready` deltaP `42.2788` edge `0.4411` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2295` n `63` status `ready` deltaP `42.2788` edge `0.4411` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9093` n `59` status `ready` deltaP `51.4713` edge `0.3253` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.9544` n `63` status `ready` deltaP `50.0992` edge `0.0831` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9544` n `63` status `ready` deltaP `50.0992` edge `0.0831` maxDD `-0.0051`
- `risk_on_high->crypto_major_4h` score `4.7578` n `63` status `ready` deltaP `24.1725` edge `0.3212` maxDD `-3.8693`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
