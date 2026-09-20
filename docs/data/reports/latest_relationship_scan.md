# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T07:37:31.249442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9238`

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

- `news_risk_high->crypto_major_24h` score `41.1693` n `81` status `ready` deltaP `17.6312` edge `3.48` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3622` n `81` status `ready` deltaP `28.6844` edge `3.0602` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.9275` n `72` status `ready` deltaP `35.4167` edge `0.3937` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2434` n `98` status `ready` deltaP `23.4476` edge `0.4849` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.1072` n `81` status `ready` deltaP `33.2755` edge `0.3007` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.777` n `98` status `ready` deltaP `22.9902` edge `0.3706` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1675` n `75` status `ready` deltaP `36.9329` edge `0.1144` maxDD `-0.0659`
- `market_context_high->unknown_4h` score `3.8475` n `75` status `ready` deltaP `2.4024` edge `0.3196` maxDD `-0.5326`
- `news_risk_high->crypto_alt_1h` score `3.4176` n `98` status `ready` deltaP `18.9234` edge `0.2052` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5985` n `98` status `ready` deltaP `21.0192` edge `0.1287` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3573` n `75` status `ready` deltaP `30.9878` edge `0.0072` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8523` n `75` status `ready` deltaP `20.6387` edge `0.0378` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.3573` n `81` status `ready` deltaP `21.3349` edge `0.0553` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.1149` n `72` status `ready` deltaP `15.4514` edge `-0.0059` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.8601` n `75` status `ready` deltaP `13.9441` edge `0.0045` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.8552` n `98` status `ready` deltaP `19.5868` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.3606` n `81` status `ready` deltaP `17.2068` edge `0.0621` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3096` n `98` status `ready` deltaP `5.4687` edge `0.0299` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0805` n `98` status `ready` deltaP `5.2327` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
