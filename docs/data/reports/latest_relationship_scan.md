# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T14:07:26.373881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `22.091` n `98` status `ready` deltaP `7.5822` edge `2.4762` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.0461` n `98` status `ready` deltaP `14.7463` edge `2.0603` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `19.3885` n `58` status `ready` deltaP `1.23` edge `1.6225` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.0067` n `101` status `ready` deltaP `23.3398` edge `0.4659` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.0069` n `47` status `ready` deltaP `28.029` edge `0.2829` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.514` n `101` status `ready` deltaP `21.9678` edge `0.3555` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.398` n `58` status `ready` deltaP `38.2832` edge `0.1246` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.1433` n `101` status `ready` deltaP `17.1296` edge `0.1943` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2919` n `101` status `ready` deltaP `18.7763` edge `0.1181` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.7335` n `58` status `ready` deltaP `23.3652` edge `0.0102` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.6689` n `47` status `ready` deltaP `19.2265` edge `0.0151` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.479` n `58` status `ready` deltaP `16.5703` edge `0.0403` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.051` n `98` status `ready` deltaP `22.775` edge `0.1135` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8194` n `58` status `ready` deltaP `12.6007` edge `0.0059` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.6908` n `101` status `ready` deltaP `17.861` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.6749` n `98` status `ready` deltaP `16.571` edge `0.0867` maxDD `-4.941`
- `news_risk_high->metal_1h` score `0.6544` n `101` status `ready` deltaP `14.8974` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.2663` n `98` status `ready` deltaP `15.5046` edge `0.0152` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2376` n `101` status `ready` deltaP `5.364` edge `0.0246` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.2068` n `58` status `ready` deltaP `6.4475` edge `0.0059` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
