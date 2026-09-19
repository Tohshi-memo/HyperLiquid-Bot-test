# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T21:37:33.466967+00:00`
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

- `news_risk_high->crypto_major_24h` score `51.0872` n `72` status `ready` deltaP `27.0833` edge `4.1659` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5616` n `72` status `ready` deltaP `33.507` edge `3.628` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `25.7773` n `112` status `ready` deltaP `-4.4207` edge `2.2009` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.7167` n `72` status `ready` deltaP `36.9792` edge `0.4841` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9127` n `112` status `ready` deltaP `39.8561` edge `0.4462` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6668` n `98` status `ready` deltaP `21.161` edge `0.4521` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3953` n `98` status `ready` deltaP `21.9232` edge `0.3459` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2928` n `98` status `ready` deltaP `18.7737` edge `0.1958` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.875` n `112` status `ready` deltaP `29.1812` edge `0.0857` maxDD `-0.2528`
- `news_risk_high->crypto_major_1h` score `2.4427` n `98` status `ready` deltaP `20.121` edge `0.1217` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7026` n `72` status `ready` deltaP `22.3958` edge `0.077` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.6509` n `113` status `ready` deltaP `20.1712` edge `0.0283` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0301` n `112` status `ready` deltaP `19.8824` edge `0.0001` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7589` n `98` status `ready` deltaP `18.3673` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.4868` n `72` status `ready` deltaP `2.9514` edge `0.0391` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4558` n `98` status `ready` deltaP `7.1154` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.3578` n `112` status `ready` deltaP `9.0029` edge `-0.026` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.2115` n `113` status `ready` deltaP `6.2715` edge `0.0016` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0911` n `98` status `ready` deltaP `8.4463` edge `0.0805` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
