# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T03:22:30.517870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11273`

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

- `market_context_high->unknown_24h` score `474.6027` n `142` status `ready` deltaP `14.0429` edge `39.4618` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.0785` n `82` status `ready` deltaP `-3.6038` edge `31.9894` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `25.1275` n `90` status `ready` deltaP `43.0555` edge `1.8299` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.1275` n `90` status `ready` deltaP `43.0555` edge `1.8299` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.5216` n `54` status `ready` deltaP `53.8773` edge `1.691` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.8586` n `142` status `ready` deltaP `37.3435` edge `1.572` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `16.5405` n `54` status `ready` deltaP `28.2407` edge `1.2389` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.7035` n `54` status `ready` deltaP `33.2755` edge `0.7633` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.1899` n `90` status `ready` deltaP `36.9792` edge `0.5193` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1899` n `90` status `ready` deltaP `36.9792` edge `0.5193` maxDD `0.0`
- `market_context_high->equity_24h` score `8.8671` n `142` status `ready` deltaP `36.9792` edge `0.4924` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.8423` n `90` status `ready` deltaP `43.8788` edge `0.4815` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8423` n `90` status `ready` deltaP `43.8788` edge `0.4815` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1525` n `54` status `ready` deltaP `51.0417` edge `0.3391` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9178` n `54` status `ready` deltaP `51.1574` edge `0.3281` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `7.8042` n `90` status `ready` deltaP `24.618` edge `1.2432` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.8042` n `90` status `ready` deltaP `24.618` edge `1.2432` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.7707` n `90` status `ready` deltaP `31.8293` edge `0.4379` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7707` n `90` status `ready` deltaP `31.8293` edge `0.4379` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2691` n `90` status `ready` deltaP `51.5278` edge `0.0998` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
