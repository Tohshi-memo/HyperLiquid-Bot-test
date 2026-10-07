# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T06:37:04.579477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1100.9826` n `112` status `ready` deltaP `10.6151` edge `91.7158` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.8369` n `112` status `ready` deltaP `-1.0453` edge `2.6306` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8816` n `62` status `ready` deltaP `34.6184` edge `0.613` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5471` n `62` status `ready` deltaP `22.0201` edge `0.5332` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.7076` n `112` status `ready` deltaP `17.6829` edge `0.2875` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.2754` n `62` status `ready` deltaP `23.4375` edge `0.1167` maxDD `0.0`
- `news_risk_high->index_4h` score `2.825` n `62` status `ready` deltaP `31.6975` edge `0.0503` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.1004` n `62` status `ready` deltaP `4.1387` edge `0.1574` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0644` n `62` status `ready` deltaP `7.4802` edge `0.1577` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9397` n `62` status `ready` deltaP `24.5751` edge `0.0128` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7942` n `62` status `ready` deltaP `16.8618` edge `0.0969` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.691` n `112` status `ready` deltaP `1.9164` edge `0.3005` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3578` n `62` status `ready` deltaP `19.4187` edge `0.0862` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.1369` n `112` status `ready` deltaP `7.9861` edge `0.3899` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9739` n `62` status `ready` deltaP `2.5594` edge `0.116` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8972` n `112` status `ready` deltaP `19.7299` edge `0.0189` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.8164` n `112` status `ready` deltaP `13.6976` edge `0.0051` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.6997` n `62` status `ready` deltaP `27.5426` edge `0.0627` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.364` n `112` status `ready` deltaP `10.6707` edge `0.0292` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.195` n `112` status `ready` deltaP `9.0355` edge `0.0449` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
