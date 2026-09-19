# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T21:08:11.489702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8478`

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

- `news_risk_high->crypto_major_24h` score `51.0884` n `72` status `ready` deltaP `27.0833` edge `4.166` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5712` n `72` status `ready` deltaP `33.507` edge `3.6288` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `29.8736` n `114` status `ready` deltaP `-4.2014` edge `2.5408` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.7647` n `72` status `ready` deltaP `36.9792` edge `0.4881` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8844` n `114` status `ready` deltaP `40.0128` edge `0.4428` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5932` n `98` status `ready` deltaP `20.8561` edge `0.448` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3569` n `98` status `ready` deltaP `21.9232` edge `0.3427` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2628` n `98` status `ready` deltaP `18.7737` edge `0.1933` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.8279` n `114` status `ready` deltaP `28.8324` edge `0.0841` maxDD `-0.2528`
- `news_risk_high->crypto_major_1h` score `2.4187` n `98` status `ready` deltaP `20.121` edge `0.1197` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7201` n `72` status `ready` deltaP `22.5694` edge `0.0773` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5442` n `114` status `ready` deltaP `18.9568` edge `0.0275` maxDD `-0.3491`
- `market_context_high->fx_4h` score `0.9718` n `114` status `ready` deltaP `19.2287` edge `-0.0004` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7845` n `98` status `ready` deltaP `18.6722` edge `0.0463` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.4555` n `72` status `ready` deltaP `2.6042` edge `0.0388` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4438` n `98` status `ready` deltaP `6.9657` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.3169` n `114` status `ready` deltaP `8.6714` edge `-0.0272` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.12` n `114` status `ready` deltaP `5.1581` edge `0.0014` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0607` n `98` status `ready` deltaP `8.7512` edge `0.081` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
