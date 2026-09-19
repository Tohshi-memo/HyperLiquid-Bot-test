# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T20:37:30.420055+00:00`
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

- `news_risk_high->crypto_major_24h` score `51.11` n `72` status `ready` deltaP `27.0833` edge `4.1678` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.6144` n `72` status `ready` deltaP `33.507` edge `3.6324` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.9277` n `116` status `ready` deltaP `-3.9897` edge `3.0439` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.8163` n `72` status `ready` deltaP `36.9792` edge `0.4924` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8557` n `116` status `ready` deltaP `40.164` edge `0.4394` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5364` n `98` status `ready` deltaP `20.5512` edge `0.4453` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2965` n `98` status `ready` deltaP `21.6183` edge `0.3397` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2208` n `98` status `ready` deltaP `18.4743` edge `0.1918` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.7183` n `116` status `ready` deltaP `27.7912` edge `0.0824` maxDD `-0.292`
- `news_risk_high->crypto_major_1h` score `2.3803` n `98` status `ready` deltaP `19.8216` edge `0.1185` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7237` n `72` status `ready` deltaP `22.5694` edge `0.0776` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4641` n `116` status `ready` deltaP `18.0312` edge `0.027` maxDD `-0.3491`
- `market_context_high->fx_4h` score `0.8593` n `116` status `ready` deltaP `17.8826` edge `-0.0008` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8101` n `98` status `ready` deltaP `18.9771` edge `0.0464` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7075` n `98` status `ready` deltaP `15.4558` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.4701` n `98` status `ready` deltaP `7.2651` edge `0.0313` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.4241` n `72` status `ready` deltaP `2.257` edge `0.0385` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.2735` n `116` status `ready` deltaP `8.3393` edge `-0.0286` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.0341` n `116` status `ready` deltaP `4.1297` edge `0.0011` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0303` n `98` status `ready` deltaP `9.0561` edge `0.0815` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
