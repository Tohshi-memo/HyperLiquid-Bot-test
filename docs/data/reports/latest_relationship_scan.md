# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T06:22:26.837263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6958`

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

- `market_context_high->unknown_1h` score `92.2152` n `112` status `ready` deltaP `1.1495` edge `7.7184` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `65.2236` n `100` status `ready` deltaP `3.1585` edge `5.4454` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.3689` n `69` status `ready` deltaP `29.1591` edge `0.6833` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2889` n `65` status `ready` deltaP `32.3992` edge `0.5784` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.3892` n `69` status `ready` deltaP `24.1697` edge `0.5166` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.9046` n `65` status `ready` deltaP `20.2439` edge `0.4915` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.585` n `65` status `ready` deltaP `13.4643` edge `0.219` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3481` n `65` status `ready` deltaP `23.6111` edge `0.1216` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.2664` n `100` status `ready` deltaP `14.0915` edge `0.2486` maxDD `-3.294`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5602` n `65` status `ready` deltaP `20.4245` edge `0.1382` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.518` n `65` status `ready` deltaP `10.3155` edge `0.1766` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0854` n `65` status `ready` deltaP `25.7669` edge `0.017` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9621` n `65` status `ready` deltaP `18.1637` edge `0.084` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3072` n `100` status `ready` deltaP `23.6707` edge `0.0268` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2344` n `65` status `ready` deltaP `3.9705` edge `0.1283` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.7684` n `112` status `ready` deltaP `10.2331` edge `0.0847` maxDD `-3.7778`
- `market_context_high->equity_24h` score `0.5223` n `69` status `ready` deltaP `5.1253` edge `0.0296` maxDD `-0.6196`
- `market_context_high->fx_1h` score `0.5177` n `112` status `ready` deltaP `13.4196` edge `0.0053` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.5131` n `65` status `ready` deltaP `24.391` edge `0.1063` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
