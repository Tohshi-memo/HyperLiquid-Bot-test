# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T12:07:32.355385+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12066`

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

- `market_context_high->unknown_24h` score `3727.3627` n `107` status `ready` deltaP `13.5822` edge `310.5282` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `780.4897` n `58` status `ready` deltaP `15.4514` edge `64.9378` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `780.4897` n `58` status `ready` deltaP `15.4514` edge `64.9378` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.117` n `82` status `ready` deltaP `-4.3523` edge `31.9976` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.401` n `59` status `ready` deltaP `54.505` edge `1.7601` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `19.2518` n `58` status `ready` deltaP `39.9904` edge `1.3607` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.2518` n `58` status `ready` deltaP `39.9904` edge `1.3607` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5402` n `59` status `ready` deltaP `29.967` edge `1.3107` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `16.5882` n `107` status `ready` deltaP `33.6578` edge `1.2407` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2615` n `59` status `ready` deltaP `33.9366` edge `0.8054` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.8997` n `58` status `ready` deltaP `37.3264` edge `0.4928` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8997` n `58` status `ready` deltaP `37.3264` edge `0.4928` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6309` n `107` status `ready` deltaP `37.3264` edge `0.4704` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4509` n `58` status `ready` deltaP `41.7314` edge `0.4632` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4509` n `58` status `ready` deltaP `41.7314` edge `0.4632` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.3837` n `59` status `ready` deltaP `53.6458` edge `0.341` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9045` n `59` status `ready` deltaP `51.4713` edge `0.3249` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8891` n `58` status `ready` deltaP `49.6887` edge `0.0804` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8891` n `58` status `ready` deltaP `49.6887` edge `0.0804` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2214` n `58` status `ready` deltaP `37.9205` edge `0.1083` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
