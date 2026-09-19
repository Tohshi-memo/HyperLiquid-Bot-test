# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T15:52:30.084219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8594`

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

- `news_risk_high->crypto_major_24h` score `52.1299` n `72` status `ready` deltaP `30.3819` edge `4.2308` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.7783` n `72` status `ready` deltaP `35.5903` edge `3.7155` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `41.6278` n `135` status `ready` deltaP `-2.8794` edge `3.5115` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `14.2489` n `45` status `ready` deltaP `-11.7683` edge `1.2884` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `14.2489` n `45` status `ready` deltaP `-11.7683` edge `1.2884` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.8036` n `72` status `ready` deltaP `39.9305` edge `0.555` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.8411` n `45` status `ready` deltaP `47.0486` edge `0.4231` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8411` n `45` status `ready` deltaP `47.0486` edge `0.4231` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3903` n `135` status `ready` deltaP `39.6412` edge `0.4041` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.071` n `96` status `ready` deltaP `23.0183` edge `0.4734` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4668` n `96` status `ready` deltaP `21.9766` edge `0.3515` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3419` n `98` status `ready` deltaP `19.5222` edge `0.1949` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5357` n `135` status `ready` deltaP `27.168` edge `0.072` maxDD `-0.345`
- `risk_on_high->commodity_4h` score `2.5111` n `45` status `ready` deltaP `29.3902` edge `0.0483` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5111` n `45` status `ready` deltaP `29.3902` edge `0.0483` maxDD `-0.1313`
- `news_risk_high->crypto_major_1h` score `2.4594` n `98` status `ready` deltaP `20.7198` edge `0.1191` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7448` n `72` status `ready` deltaP `22.7431` edge `0.0782` maxDD `-2.4203`
- `risk_on_high->commodity_1h` score `1.4859` n `45` status `ready` deltaP `18.5662` edge `0.0186` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.4859` n `45` status `ready` deltaP `18.5662` edge `0.0186` maxDD `-0.1507`
- `market_context_high->commodity_1h` score `1.4817` n `135` status `ready` deltaP `18.5662` edge `0.0249` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
