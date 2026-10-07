# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T04:07:25.419590+00:00`
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

- `market_context_high->unknown_24h` score `1278.0283` n `115` status `ready` deltaP `11.0809` edge `106.4665` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.0043` n `115` status `ready` deltaP `-0.5328` edge `2.5578` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.75` n `62` status `ready` deltaP `34.9233` edge `0.6` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1057` n `62` status `ready` deltaP `21.2579` edge `0.5015` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.2143` n `115` status `ready` deltaP `16.0313` edge `0.2574` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.0909` n `62` status `ready` deltaP `21.7014` edge `0.1129` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6862` n `62` status `ready` deltaP `30.1731` edge `0.0489` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1135` n `62` status `ready` deltaP `7.7796` edge `0.1598` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.8928` n `62` status `ready` deltaP `2.9234` edge `0.1482` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.8869` n `62` status `ready` deltaP `23.9763` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6636` n `62` status `ready` deltaP `16.0996` edge `0.0911` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2427` n `62` status `ready` deltaP `17.8943` edge `0.0816` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.1354` n `115` status `ready` deltaP `7.0652` edge `0.3449` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `1.057` n `115` status `ready` deltaP `0.4865` edge `0.2572` maxDD `-7.1222`
- `news_risk_high->crypto_alt_1h` score `0.9691` n `62` status `ready` deltaP `2.7091` edge `0.1146` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.8928` n `62` status `ready` deltaP `28.9315` edge `0.0782` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8448` n `115` status `ready` deltaP `19.0906` edge `0.0188` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.752` n `115` status `ready` deltaP `12.9081` edge `0.005` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5345` n `115` status `ready` deltaP `12.4112` edge `0.0318` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2677` n `115` status `ready` deltaP `7.5696` edge `0.0115` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
