# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T20:37:41.304848+00:00`
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

- `market_context_high->unknown_24h` score `11187.8034` n `73` status `ready` deltaP `12.7117` edge `932.2374` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `10610.2321` n `33` status `ready` deltaP `15.4514` edge `884.083` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `10610.2321` n `33` status `ready` deltaP `15.4514` edge `884.083` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1004` n `82` status `ready` deltaP `-5.5499` edge `32.0042` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `19.6056` n `72` status `ready` deltaP `42.7084` edge `1.4812` maxDD `-7.903`
- `news_risk_high->crypto_alt_24h` score `17.2904` n `72` status `ready` deltaP `30.7292` edge `1.2848` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `14.3952` n `33` status `ready` deltaP `35.0221` edge `0.9891` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.3952` n `33` status `ready` deltaP `35.0221` edge `0.9891` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.2352` n `73` status `ready` deltaP `28.2558` edge `0.9973` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.1434` n `33` status `ready` deltaP `42.8819` edge `0.5594` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.1434` n `33` status `ready` deltaP `42.8819` edge `0.5594` maxDD `0.0`
- `market_context_high->equity_24h` score `9.685` n `73` status `ready` deltaP `42.8819` edge `0.5212` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.4515` n `72` status `ready` deltaP `22.0486` edge `0.6602` maxDD `-3.8986`
- `news_risk_high->index_24h` score `6.6069` n `72` status `ready` deltaP `44.2708` edge `0.2731` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.9909` n `72` status `ready` deltaP `36.6319` edge `0.2991` maxDD `-0.526`
- `risk_on_high->index_24h` score `5.3717` n `33` status `ready` deltaP `53.7405` edge `0.0936` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3717` n `33` status `ready` deltaP `53.7405` edge `0.0936` maxDD `-0.005`
- `risk_on_high->crypto_alt_4h` score `4.8052` n `47` status `ready` deltaP `24.1632` edge `0.3184` maxDD `-3.3243`
- `risk_on_and_context->crypto_alt_4h` score `4.8052` n `47` status `ready` deltaP `24.1632` edge `0.3184` maxDD `-3.3243`
- `market_context_high->index_24h` score `3.346` n `73` status `ready` deltaP `36.2229` edge `0.0767` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
