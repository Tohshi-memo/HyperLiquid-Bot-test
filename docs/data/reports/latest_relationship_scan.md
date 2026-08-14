# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T04:37:29.048698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `90.4291` n `150` status `ready` deltaP `-29.625` edge `8.0245` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.2382` n `32` status `ready` deltaP `-43.75` edge `4.628` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.2382` n `32` status `ready` deltaP `-43.75` edge `4.628` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.8962` n `36` status `ready` deltaP `10.0694` edge `0.7955` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.9394` n `36` status `ready` deltaP `37.3476` edge `0.3293` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7721` n `32` status `ready` deltaP `32.2917` edge `0.1824` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7721` n `32` status `ready` deltaP `32.2917` edge `0.1824` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9796` n `32` status `ready` deltaP `20.9604` edge `0.1268` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9796` n `32` status `ready` deltaP `20.9604` edge `0.1268` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.845` n `150` status `ready` deltaP `22.2917` edge `0.1688` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2935` n `36` status `ready` deltaP `14.5833` edge `0.0939` maxDD `0.0`
- `news_risk_high->index_4h` score `1.6557` n `36` status `ready` deltaP `19.6138` edge `0.0204` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.618` n `150` status `ready` deltaP `17.5021` edge `0.082` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.5272` n `36` status `ready` deltaP `7.535` edge `0.1089` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3617` n `32` status `ready` deltaP `14.4087` edge `0.0407` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3617` n `32` status `ready` deltaP `14.4087` edge `0.0407` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2636` n `32` status `ready` deltaP `14.9306` edge `0.0242` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2636` n `32` status `ready` deltaP `14.9306` edge `0.0242` maxDD `-0.1418`
- `risk_on_high->crypto_major_24h` score `1.0538` n `32` status `ready` deltaP `10.5903` edge `0.1801` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.0538` n `32` status `ready` deltaP `10.5903` edge `0.1801` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
