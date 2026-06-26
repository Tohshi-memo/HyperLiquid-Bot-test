# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T07:07:32.295281+00:00`
- Price records: `672`
- Market context records: `4804`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7578`

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

- `market_context_high->unknown_1h` score `11.2287` n `119` status `ready` deltaP `11.7119` edge `0.8994` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8317` n `118` status `ready` deltaP `18.3573` edge `0.6513` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2685` n `112` status `ready` deltaP `12.8968` edge `0.1954` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.3944` n `118` status `ready` deltaP `10.4563` edge `0.1262` maxDD `-6.9604`
- `market_context_high->commodity_4h` score `0.0871` n `118` status `ready` deltaP `12.0117` edge `0.0483` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0346` n `119` status `ready` deltaP `5.1527` edge `0.0273` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.2359` n `118` status `ready` deltaP `8.4384` edge `0.0188` maxDD `-5.4242`
- `market_context_high->fx_4h` score `-0.3349` n `118` status `ready` deltaP `4.6946` edge `0.0034` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.621` n `119` status `ready` deltaP `2.6996` edge `0.007` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9193` n `119` status `ready` deltaP `-1.3284` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3572` n `119` status `ready` deltaP `-0.9271` edge `-0.0065` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.141` n `112` status `ready` deltaP `19.5436` edge `0.1061` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2537` n `119` status `ready` deltaP `-0.5221` edge `-0.0679` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7685` n `112` status `ready` deltaP `-11.5328` edge `-0.018` maxDD `-3.1993`
- `market_context_high->crypto_major_1h` score `-2.9529` n `119` status `ready` deltaP `0.5019` edge `-0.0729` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.0473` n `119` status `ready` deltaP `1.4681` edge `-0.0433` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.4193` n `112` status `ready` deltaP `-7.5645` edge `-0.1253` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.4288` n `118` status `ready` deltaP `6.8288` edge `0.0021` maxDD `-43.8998`
- `market_context_high->crypto_major_4h` score `-8.1704` n `118` status `ready` deltaP `3.9634` edge `-0.1541` maxDD `-68.2515`
- `market_context_high->metal_4h` score `-8.4893` n `118` status `ready` deltaP `5.6712` edge `-0.3021` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
