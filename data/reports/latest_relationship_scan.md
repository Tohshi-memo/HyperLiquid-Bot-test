# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T20:07:27.422268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `10573.5281` n `75` status `ready` deltaP `12.7847` edge `881.0473` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `9332.0593` n `35` status `ready` deltaP `15.4514` edge `777.5686` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `9332.0593` n `35` status `ready` deltaP `15.4514` edge `777.5686` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1664` n `82` status `ready` deltaP `-5.4002` edge `32.0087` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.2747` n `70` status `ready` deltaP `44.623` edge `1.5153` maxDD `-7.1917`
- `news_risk_high->crypto_alt_24h` score `17.1836` n `70` status `ready` deltaP `30.1736` edge `1.2796` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `15.056` n `35` status `ready` deltaP `35.8879` edge `1.0384` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.056` n `35` status `ready` deltaP `35.8879` edge `1.0384` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.5448` n `75` status `ready` deltaP `28.8403` edge `1.0192` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.0652` n `35` status `ready` deltaP `42.5347` edge `0.5552` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.0652` n `35` status `ready` deltaP `42.5347` edge `0.5552` maxDD `0.0`
- `market_context_high->equity_24h` score `9.632` n `75` status `ready` deltaP `42.5347` edge `0.5191` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.0234` n `70` status `ready` deltaP `23.9633` edge `0.6801` maxDD `-3.3657`
- `news_risk_high->index_24h` score `6.6575` n `70` status `ready` deltaP `43.9137` edge `0.2797` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.2389` n `70` status `ready` deltaP `39.0129` edge `0.3039` maxDD `-0.526`
- `risk_on_high->crypto_alt_4h` score `5.8202` n `47` status `ready` deltaP `28.1136` edge `0.3589` maxDD `-2.5715`
- `risk_on_and_context->crypto_alt_4h` score `5.8202` n `47` status `ready` deltaP `28.1136` edge `0.3589` maxDD `-2.5715`
- `risk_on_high->index_24h` score `5.3591` n `35` status `ready` deltaP `53.9137` edge `0.0914` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3591` n `35` status `ready` deltaP `53.9137` edge `0.0914` maxDD `-0.005`
- `market_context_high->index_24h` score `3.3838` n `75` status `ready` deltaP `36.7708` edge `0.0762` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
