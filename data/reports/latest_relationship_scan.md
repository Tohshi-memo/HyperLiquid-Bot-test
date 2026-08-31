# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T04:37:31.568777+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `risk_on_high->crypto_alt_24h` score `21.3477` n `55` status `ready` deltaP `47.058` edge `1.5133` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.3477` n `55` status `ready` deltaP `47.058` edge `1.5133` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `9.7489` n `95` status `ready` deltaP `28.389` edge `0.666` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.7489` n `95` status `ready` deltaP `28.389` edge `0.666` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `9.1574` n `55` status `ready` deltaP `28.1724` edge `0.7171` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.1574` n `55` status `ready` deltaP `28.1724` edge `0.7171` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `7.4158` n `149` status `ready` deltaP `22.6101` edge `0.5101` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2` n `55` status `ready` deltaP `69.4444` edge `0.0537` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2` n `55` status `ready` deltaP `69.4444` edge `0.0537` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9537` n `98` status `ready` deltaP `35.5158` edge `0.2409` maxDD `-2.1893`
- `market_context_high->crypto_alt_24h` score `4.4158` n `98` status `ready` deltaP `22.123` edge `0.8376` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.3936` n `55` status `ready` deltaP `40.5808` edge `0.1428` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3936` n `55` status `ready` deltaP `40.5808` edge `0.1428` maxDD `-0.7767`
- `market_context_high->crypto_major_24h` score `3.8492` n `98` status `ready` deltaP `19.8236` edge `0.4377` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6589` n `107` status `ready` deltaP `7.7131` edge `0.2278` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6589` n `107` status `ready` deltaP `7.7131` edge `0.2278` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.4347` n `161` status `ready` deltaP `7.5157` edge `0.2158` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0126` n `98` status `ready` deltaP `36.7913` edge `0.0304` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8342` n `55` status `ready` deltaP `9.6528` edge `0.1414` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8342` n `55` status `ready` deltaP `9.6528` edge `0.1414` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
