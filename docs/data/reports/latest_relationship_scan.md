# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T00:37:17.067905+00:00`
- Price records: `672`
- Market context records: `1170`
- Flow alert records: `5271`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.8435` n `139` status `ready` deltaP `45.907` edge `1.5441` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1162` n `139` status `ready` deltaP `22.1473` edge `0.897` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.645` n `139` status `ready` deltaP `21.9736` edge `0.5836` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.7198` n `139` status `ready` deltaP `20.5848` edge `0.3952` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5468` n `139` status `ready` deltaP `-3.5772` edge `0.6528` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5061` n `153` status `ready` deltaP `12.8657` edge `0.1894` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1746` n `153` status `ready` deltaP `9.3575` edge `0.1038` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.7085` n `139` status `ready` deltaP `2.9414` edge `0.3124` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.5499` n `153` status `ready` deltaP `8.1777` edge `0.023` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3075` n `153` status `ready` deltaP `3.0586` edge `0.043` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1498` n `153` status `ready` deltaP `8.6484` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0901` n `153` status `ready` deltaP `8.1699` edge `0.1492` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0513` n `153` status `ready` deltaP `6.3735` edge `0.0275` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.1334` n `153` status `ready` deltaP `6.0358` edge `0.0703` maxDD `-6.7322`
- `market_context_high->metal_1h` score `-0.4813` n `153` status `ready` deltaP `5.4646` edge `-0.0155` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4955` n `153` status `ready` deltaP `1.8277` edge `0.0308` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8327` n `153` status `ready` deltaP `-3.2954` edge `-0.004` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0165` n `153` status `ready` deltaP `-3.8976` edge `-0.0047` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3361` n `153` status `ready` deltaP `3.795` edge `0.0999` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9365` n `153` status `ready` deltaP `4.5802` edge `-0.0834` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
