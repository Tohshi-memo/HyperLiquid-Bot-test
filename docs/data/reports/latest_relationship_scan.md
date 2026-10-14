# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T15:52:38.784593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->crypto_alt_4h` score `6.8521` n `117` status `ready` deltaP `17.9839` edge `0.596` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.267` n `54` status `ready` deltaP `32.3478` edge `0.3066` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.267` n `54` status `ready` deltaP `32.3478` edge `0.3066` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0308` n `117` status `ready` deltaP `20.8151` edge `0.5197` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.441` n `54` status `ready` deltaP `20.2631` edge `0.3631` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.441` n `54` status `ready` deltaP `20.2631` edge `0.3631` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.4598` n `54` status `ready` deltaP `33.9205` edge `0.4309` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4598` n `54` status `ready` deltaP `33.9205` edge `0.4309` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7507` n `117` status `ready` deltaP `13.5665` edge `0.1622` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.237` n `117` status `ready` deltaP `5.8115` edge `0.1449` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2762` n `117` status `ready` deltaP `13.6127` edge `0.0368` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.329` n `117` status `ready` deltaP `7.7141` edge `0.0081` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3523` n `54` status `ready` deltaP `1.2531` edge `0.0187` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3523` n `54` status `ready` deltaP `1.2531` edge `0.0187` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.366` n `117` status `ready` deltaP `0.797` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4282` n `54` status `ready` deltaP `2.301` edge `0.0029` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4282` n `54` status `ready` deltaP `2.301` edge `0.0029` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5953` n `54` status `ready` deltaP `3.3101` edge `0.0042` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5953` n `54` status `ready` deltaP `3.3101` edge `0.0042` maxDD `-5.8734`
- `risk_on_high->metal_4h` score `-0.6014` n `54` status `ready` deltaP `1.2195` edge `0.0193` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
