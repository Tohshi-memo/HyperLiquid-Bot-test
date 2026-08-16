# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T21:07:27.914499+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `174.0628` n `83` status `ready` deltaP `-25.1401` edge `22.7517` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.107` n `83` status `ready` deltaP `41.3404` edge `0.3224` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.1694` n `119` status `ready` deltaP `12.6537` edge `0.0602` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `0.003` n `121` status `ready` deltaP `3.2823` edge `0.0195` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2412` n `119` status `ready` deltaP `5.0945` edge `0.0064` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3504` n `121` status `ready` deltaP `0.8685` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5731` n `121` status `ready` deltaP `0.7188` edge `-0.0067` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.6076` n `119` status `ready` deltaP `10.2032` edge `-0.0052` maxDD `-4.5909`
- `market_context_high->index_1h` score `-0.7272` n `121` status `ready` deltaP `-5.7245` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.1653` n `119` status `ready` deltaP `-9.3321` edge `-0.0063` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.3401` n `83` status `ready` deltaP `-0.9852` edge `-0.0584` maxDD `-1.5472`
- `market_context_high->fx_24h` score `-1.7558` n `83` status `ready` deltaP `-11.724` edge `0.0138` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.0392` n `83` status `ready` deltaP `-10.8664` edge `0.0622` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.2257` n `121` status `ready` deltaP `-5.1443` edge `-0.0363` maxDD `-5.8571`
- `market_context_high->crypto_alt_1h` score `-2.3081` n `121` status `ready` deltaP `-4.3178` edge `-0.0296` maxDD `-7.0497`
- `market_context_high->crypto_major_4h` score `-2.4185` n `119` status `ready` deltaP `-0.5726` edge `-0.0425` maxDD `-8.0847`
- `market_context_high->equity_1h` score `-2.691` n `121` status `ready` deltaP `-10.9764` edge `-0.0471` maxDD `-4.9849`
- `market_context_high->crypto_major_24h` score `-3.0474` n `83` status `ready` deltaP `-4.7273` edge `0.0633` maxDD `-25.132`
- `market_context_high->unknown_1h` score `-6.5311` n `121` status `ready` deltaP `3.8031` edge `-0.5299` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-6.8275` n `119` status `ready` deltaP `-9.742` edge `-0.0791` maxDD `-21.326`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
