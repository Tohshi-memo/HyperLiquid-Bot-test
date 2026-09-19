# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T21:52:29.388248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `news_risk_high->crypto_major_24h` score `51.0896` n `72` status `ready` deltaP `27.0833` edge `4.1661` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5556` n `72` status `ready` deltaP `33.507` edge `3.6275` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `23.6622` n `111` status `ready` deltaP `-4.5333` edge `2.0254` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.6939` n `72` status `ready` deltaP `36.9792` edge `0.4822` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.923` n `111` status `ready` deltaP `39.7757` edge `0.4476` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6994` n `98` status `ready` deltaP `21.3134` edge `0.4538` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4243` n `98` status `ready` deltaP `22.0756` edge `0.3473` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3012` n `98` status `ready` deltaP `18.7737` edge `0.1965` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.8667` n `111` status `ready` deltaP `28.9882` edge `0.0863` maxDD `-0.2528`
- `news_risk_high->crypto_major_1h` score `2.4511` n `98` status `ready` deltaP `20.121` edge `0.1224` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7014` n `72` status `ready` deltaP `22.3958` edge `0.0769` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5921` n `113` status `ready` deltaP `19.4359` edge `0.0283` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0281` n `111` status `ready` deltaP `19.8418` edge `0.0002` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7455` n `98` status `ready` deltaP `18.2149` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.5031` n `72` status `ready` deltaP `3.125` edge `0.0393` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4438` n `98` status `ready` deltaP `6.9657` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.3795` n `111` status `ready` deltaP `9.1685` edge `-0.0253` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.2715` n `113` status `ready` deltaP `7.0068` edge `0.0017` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.1057` n `98` status `ready` deltaP `8.2939` edge `0.0803` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
