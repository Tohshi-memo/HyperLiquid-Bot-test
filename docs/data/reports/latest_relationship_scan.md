# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T06:37:28.336496+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `news_risk_high->crypto_major_24h` score `40.9668` n `81` status `ready` deltaP `17.1103` edge `3.4666` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.379` n `81` status `ready` deltaP `28.6844` edge `3.0616` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.0544` n `76` status `ready` deltaP `36.1477` edge `0.3994` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2914` n `98` status `ready` deltaP `23.4476` edge `0.4889` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.202` n `81` status `ready` deltaP `33.2755` edge `0.3086` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.8768` n `98` status `ready` deltaP `23.1427` edge `0.3779` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8186` n `79` status `ready` deltaP `33.5906` edge `0.1076` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4116` n `98` status `ready` deltaP `18.9234` edge `0.2047` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6333` n `98` status `ready` deltaP `21.1689` edge `0.1306` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3609` n `79` status `ready` deltaP `31.1381` edge `0.0065` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.7314` n `79` status `ready` deltaP `19.4573` edge `0.0356` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4261` n `81` status `ready` deltaP `22.0293` edge `0.0564` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.034` n `76` status `ready` deltaP `14.83` edge `-0.0085` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8966` n `98` status `ready` deltaP `20.0441` edge `0.0465` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7446` n `98` status `ready` deltaP `15.9049` edge `0.0162` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.6865` n `79` status `ready` deltaP `11.8491` edge `0.004` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3468` n `98` status `ready` deltaP `5.7681` edge `0.031` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.3442` n `81` status `ready` deltaP `17.2068` edge `0.06` maxDD `-3.4467`
- `market_context_high->unknown_4h` score `0.1684` n `79` status `ready` deltaP `0.3782` edge `0.0265` maxDD `-0.5326`
- `news_risk_high->fx_4h` score `-0.1183` n `98` status `ready` deltaP `4.7754` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
