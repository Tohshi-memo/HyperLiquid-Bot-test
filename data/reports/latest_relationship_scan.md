# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T05:37:31.035620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8376`

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

- `news_risk_high->crypto_major_24h` score `59.6089` n `59` status `ready` deltaP `35.2342` edge `4.8217` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `53.4873` n `59` status `ready` deltaP `38.0532` edge `4.3415` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.2935` n `149` status `ready` deltaP `-1.683` edge `3.059` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.9399` n `59` status `ready` deltaP `48.2639` edge `0.8399` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.1721` n `52` status `ready` deltaP `-8.9236` edge `0.9297` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.1721` n `52` status `ready` deltaP `-8.9236` edge `0.9297` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.5723` n `75` status `ready` deltaP `27.939` edge `0.6407` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.2676` n `52` status `ready` deltaP `44.9653` edge `0.3892` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2676` n `52` status `ready` deltaP `44.9653` edge `0.3892` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9685` n `149` status `ready` deltaP `38.2539` edge `0.3782` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.8098` n `75` status `ready` deltaP `24.435` edge `0.4387` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.6142` n `59` status `ready` deltaP `38.4004` edge `0.1443` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.283` n `81` status `ready` deltaP `17.1509` edge `0.2058` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6113` n `81` status `ready` deltaP `19.9194` edge `0.1371` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.4744` n `75` status `ready` deltaP `16.2826` edge `0.0362` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.2428` n `59` status `ready` deltaP `6.9857` edge `0.0612` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0402` n `149` status `ready` deltaP `15.4624` edge `0.0213` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
