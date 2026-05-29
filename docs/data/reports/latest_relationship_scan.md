# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T09:52:21.263053+00:00`
- Price records: `672`
- Market context records: `2233`
- Flow alert records: `8322`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.5226` n `33` status `ready` deltaP `56.0922` edge `1.8118` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.3988` n `33` status `ready` deltaP `46.4489` edge `0.9342` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9908` n `131` status `ready` deltaP `37.1695` edge `0.9284` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.3278` n `33` status `ready` deltaP `37.4211` edge `0.8093` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7723` n `131` status `ready` deltaP `42.2129` edge `0.7526` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.3136` n `33` status `ready` deltaP `36.995` edge `0.5521` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.3242` n `33` status `ready` deltaP `18.9394` edge `0.8708` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.8631` n `131` status `ready` deltaP `22.0606` edge `0.3869` maxDD `-1.6306`
- `market_context_high->equity_4h` score `3.9744` n `131` status `ready` deltaP `24.3705` edge `0.2422` maxDD `-3.2111`
- `news_risk_high->commodity_4h` score `3.9536` n `43` status `ready` deltaP `33.2246` edge `0.3525` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.6222` n `131` status `ready` deltaP `27.8754` edge `0.1637` maxDD `-1.1484`
- `market_context_high->crypto_major_1h` score `3.1425` n `143` status `ready` deltaP `17.3831` edge `0.1937` maxDD `-1.817`
- `market_context_high->unknown_24h` score `3.1085` n `129` status `ready` deltaP `24.4509` edge `0.48` maxDD `-26.0504`
- `news_risk_high->fx_24h` score `2.9568` n `33` status `ready` deltaP `31.0606` edge `0.0578` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9303` n `143` status `ready` deltaP `16.2839` edge `0.222` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.3185` n `33` status `ready` deltaP `-2.1149` edge `0.289` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.161` n `43` status `ready` deltaP `27.4319` edge `0.0156` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.9331` n `129` status `ready` deltaP `9.2458` edge `0.2014` maxDD `-3.4888`
- `market_context_high->crypto_major_24h` score `1.4974` n `129` status `ready` deltaP `14.9224` edge `0.8203` maxDD `-52.2242`
- `market_context_high->metal_4h` score `1.4215` n `131` status `ready` deltaP `18.0902` edge `0.1366` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
