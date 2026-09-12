# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T19:37:26.542886+00:00`
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

- `market_context_high->unknown_24h` score `9989.4792` n `77` status `ready` deltaP `12.854` edge `832.3761` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `8188.2409` n `37` status `ready` deltaP `15.4514` edge `682.2504` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `8188.2409` n `37` status `ready` deltaP `15.4514` edge `682.2504` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.4327` n `82` status `ready` deltaP `-5.2505` edge `32.0299` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.6524` n `69` status `ready` deltaP `45.8031` edge `1.5353` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.1712` n `69` status `ready` deltaP `29.8837` edge `1.2805` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `15.4742` n `37` status `ready` deltaP `36.6601` edge `1.0681` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.4742` n `37` status `ready` deltaP `36.6601` edge `1.0681` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.7595` n `77` status `ready` deltaP `29.3944` edge `1.0334` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.9834` n `37` status `ready` deltaP `42.1875` edge `0.5507` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.9834` n `37` status `ready` deltaP `42.1875` edge `0.5507` maxDD `0.0`
- `market_context_high->equity_24h` score `9.5778` n `77` status `ready` deltaP `42.1875` edge `0.5169` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.2864` n `69` status `ready` deltaP `24.7962` edge `0.6893` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `6.7195` n `47` status `ready` deltaP `32.0641` edge `0.3917` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.7195` n `47` status `ready` deltaP `32.0641` edge `0.3917` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.3846` n `69` status `ready` deltaP `40.4287` edge `0.3066` maxDD `-0.526`
- `risk_on_high->index_24h` score `5.1344` n `37` status `ready` deltaP `51.539` edge `0.0885` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.1344` n `37` status `ready` deltaP `51.539` edge `0.0885` maxDD `-0.005`
- `market_context_high->index_24h` score `3.3234` n `77` status `ready` deltaP `36.1652` edge `0.0752` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
