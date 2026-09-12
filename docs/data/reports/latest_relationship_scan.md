# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T11:22:28.245005+00:00`
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

- `market_context_high->unknown_24h` score `3400.3872` n `110` status `ready` deltaP `13.6332` edge `283.2799` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.1745` n `82` status `ready` deltaP `-3.9032` edge `31.9994` maxDD `-1.7068`
- `risk_on_high->unknown_24h` score `360.5005` n `61` status `ready` deltaP `15.4514` edge `29.9387` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `360.5005` n `61` status `ready` deltaP `15.4514` edge `29.9387` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `24.4034` n `59` status `ready` deltaP `54.505` edge `1.7603` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `20.1942` n `61` status `ready` deltaP `40.4144` edge `1.4364` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1942` n `61` status `ready` deltaP `40.4144` edge `1.4364` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5678` n `59` status `ready` deltaP `29.967` edge `1.313` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `17.1764` n `110` status `ready` deltaP `34.0656` edge `1.287` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2471` n `59` status `ready` deltaP `33.9366` edge `0.8042` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9633` n `61` status `ready` deltaP `37.3264` edge `0.4981` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9633` n `61` status `ready` deltaP `37.3264` edge `0.4981` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6669` n `110` status `ready` deltaP `37.3264` edge `0.4734` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.3873` n `59` status `ready` deltaP `53.6458` edge `0.3413` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.2861` n `61` status `ready` deltaP `42.0706` edge `0.4472` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2861` n `61` status `ready` deltaP `42.0706` edge `0.4472` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9069` n `59` status `ready` deltaP `51.4713` edge `0.3251` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.9263` n `61` status `ready` deltaP `49.9431` edge `0.0818` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9263` n `61` status `ready` deltaP `49.9431` edge `0.0818` maxDD `-0.0051`
- `risk_on_high->crypto_major_4h` score `4.5017` n `61` status `ready` deltaP `23.2357` edge `0.3061` maxDD `-3.8693`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
