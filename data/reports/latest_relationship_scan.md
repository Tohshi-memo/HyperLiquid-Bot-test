# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T22:52:29.595119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8700`

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

- `news_risk_high->crypto_major_24h` score `51.1028` n `72` status `ready` deltaP `27.0833` edge `4.1672` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5292` n `72` status `ready` deltaP `33.507` edge `3.6253` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `18.1837` n `107` status `ready` deltaP `-5.0048` edge `1.572` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.5936` n `72` status `ready` deltaP `36.8055` edge `0.475` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9897` n `107` status `ready` deltaP `39.4389` edge `0.4554` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8394` n `98` status `ready` deltaP `21.9232` edge `0.4614` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5389` n `98` status `ready` deltaP `22.5329` edge `0.3538` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2868` n `98` status `ready` deltaP `18.624` edge `0.1963` maxDD `-2.058`
- `market_context_high->commodity_4h` score `3.1905` n `107` status `ready` deltaP `30.5262` edge `0.0898` maxDD `-0.1946`
- `news_risk_high->crypto_major_1h` score `2.4643` n `98` status `ready` deltaP `20.121` edge `0.1235` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.6978` n `72` status `ready` deltaP `22.3958` edge `0.0766` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5281` n `109` status `ready` deltaP `18.5464` edge `0.0289` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0831` n `107` status `ready` deltaP `20.4254` edge `0.0009` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7455` n `98` status `ready` deltaP `18.2149` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.5671` n `72` status `ready` deltaP `3.8195` edge `0.04` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.4515` n `107` status `ready` deltaP `9.8293` edge `-0.0237` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4306` n `98` status `ready` deltaP `6.816` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.161` n `109` status `ready` deltaP `5.6104` edge `0.0018` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.1641` n `98` status `ready` deltaP `7.6841` edge `0.0795` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
