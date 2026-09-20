# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T18:37:29.526210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9806`

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

- `news_risk_high->crypto_major_24h` score `23.5134` n `98` status `ready` deltaP `10.7072` edge `2.5739` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3463` n `98` status `ready` deltaP `15.0935` edge `2.083` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `17.5161` n `42` status `ready` deltaP `-0.7405` edge `1.4796` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.3696` n `101` status `ready` deltaP `22.4251` edge `0.4189` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.3905` n `42` status `ready` deltaP `37.4854` edge `0.1293` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.1715` n `101` status `ready` deltaP `21.5105` edge `0.33` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.1204` n `31` status `ready` deltaP `17.0475` edge `0.1989` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9153` n `101` status `ready` deltaP `16.6805` edge `0.1783` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1959` n `101` status `ready` deltaP `18.6266` edge `0.1111` maxDD `-2.8494`
- `market_context_high->fx_24h` score `2.1539` n `31` status `ready` deltaP `21.2534` edge `0.042` maxDD `-0.0027`
- `market_context_high->fx_4h` score `2.1071` n `42` status `ready` deltaP `27.5406` edge `0.0135` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.1937` n `52` status `ready` deltaP `13.5882` edge `0.0364` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0549` n `98` status `ready` deltaP `22.775` edge `0.114` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8879` n `52` status `ready` deltaP `12.667` edge `0.007` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6336` n `101` status `ready` deltaP `17.2512` edge `0.0432` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.5578` n `98` status `ready` deltaP `16.3974` edge `0.0781` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3298` n `52` status `ready` deltaP `7.0935` edge `0.0067` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2448` n `101` status `ready` deltaP `5.5137` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1534` n `98` status `ready` deltaP `14.9837` edge `0.0042` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
