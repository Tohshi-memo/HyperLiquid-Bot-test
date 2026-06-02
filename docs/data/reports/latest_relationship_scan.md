# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T02:22:22.138090+00:00`
- Price records: `672`
- Market context records: `2620`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.7502` n `146` status `ready` deltaP `18.2958` edge `0.5567` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0621` n `146` status `ready` deltaP `24.8914` edge `0.5238` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2683` n `146` status `ready` deltaP `14.1539` edge `0.359` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4168` n `146` status `ready` deltaP `11.73` edge `0.1586` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0807` n `146` status `ready` deltaP `7.6846` edge `0.1438` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.9654` n `146` status `ready` deltaP `9.8435` edge `0.1129` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7892` n `146` status `ready` deltaP `9.1625` edge `0.1241` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.514` n `146` status `ready` deltaP `2.0643` edge `0.6669` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2324` n `146` status `ready` deltaP `8.8227` edge `0.0447` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0796` n `146` status `ready` deltaP `4.3905` edge `0.0135` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3092` n `146` status `ready` deltaP `6.2505` edge `0.0204` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4632` n `146` status `ready` deltaP `1.6508` edge `0.0167` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.6476` n `146` status `ready` deltaP `1.2612` edge `0.0124` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6916` n `146` status `ready` deltaP `-1.134` edge `0.0034` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7845` n `146` status `ready` deltaP `-0.2276` edge `0.02` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-0.9349` n `146` status `ready` deltaP `4.711` edge `0.043` maxDD `-10.2078`
- `market_context_high->metal_4h` score `-0.9378` n `146` status `ready` deltaP `3.4351` edge `0.0377` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9614` n `146` status `ready` deltaP `3.3675` edge `-0.0032` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9859` n `146` status `ready` deltaP `-0.9877` edge `0.0102` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.371` n `146` status `ready` deltaP `1.6497` edge `0.0152` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
