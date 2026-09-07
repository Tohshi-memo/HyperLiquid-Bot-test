# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T10:52:25.879648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10427`

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

- `risk_on_high->unknown_24h` score `419.6782` n `93` status `ready` deltaP `26.5625` edge `34.7961` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `419.6782` n `93` status `ready` deltaP `26.5625` edge `34.7961` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.15` n `241` status `ready` deltaP `-2.5275` edge `2.1018` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.1168` n `93` status `ready` deltaP `37.7184` edge `1.6433` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.1168` n `93` status `ready` deltaP `37.7184` edge `1.6433` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.045` n `93` status `ready` deltaP `31.5972` edge `1.0431` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.045` n `93` status `ready` deltaP `31.5972` edge `1.0431` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.266` n `187` status `ready` deltaP `25.1801` edge `0.6618` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.1734` n `187` status `ready` deltaP `21.0069` edge `0.3744` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.5208` n `117` status `ready` deltaP `29.7204` edge `0.2991` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5208` n `117` status `ready` deltaP `29.7204` edge `0.2991` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.0034` n `93` status `ready` deltaP `21.0069` edge `0.2769` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.0034` n `93` status `ready` deltaP `21.0069` edge `0.2769` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3809` n `117` status `ready` deltaP `24.4567` edge `0.2879` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3809` n `117` status `ready` deltaP `24.4567` edge `0.2879` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4665` n `93` status `ready` deltaP `20.9061` edge `0.0704` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4665` n `93` status `ready` deltaP `20.9061` edge `0.0704` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.2904` n `187` status `ready` deltaP `18.7843` edge `0.0871` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.974` n `117` status `ready` deltaP `4.6958` edge `0.0851` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.974` n `117` status `ready` deltaP `4.6958` edge `0.0851` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
