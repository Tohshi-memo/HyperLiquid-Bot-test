# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T10:22:30.046648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11960`

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

- `news_risk_high->unknown_24h` score `1061.9556` n `130` status `ready` deltaP `1.2153` edge `88.4882` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.372` n `40` status `ready` deltaP `10.3743` edge `12.9665` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `56.1145` n `36` status `ready` deltaP `29.6875` edge `4.5134` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.3632` n `36` status `ready` deltaP `35.5903` edge `2.3244` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.4858` n `36` status `ready` deltaP `14.4097` edge `2.2324` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.4529` n `36` status `ready` deltaP `32.9861` edge `0.4933` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.4759` n `40` status `ready` deltaP `18.3841` edge `0.3047` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.2334` n `36` status `ready` deltaP `37.8473` edge `0.1243` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9184` n `40` status `ready` deltaP `24.3902` edge `0.1974` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1355` n `40` status `ready` deltaP `34.3293` edge `0.0395` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.3363` n `40` status `ready` deltaP `9.7866` edge `0.2199` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7251` n `40` status `ready` deltaP `18.8623` edge `0.0583` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5484` n `40` status `ready` deltaP `11.3623` edge `0.1422` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4023` n `40` status `ready` deltaP `11.5569` edge `0.1256` maxDD `-4.8632`
- `market_context_high->index_1h` score `0.9793` n `40` status `ready` deltaP `13.7126` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9508` n `40` status `ready` deltaP `15.988` edge `0.0083` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.746` n `130` status `ready` deltaP `15.7639` edge `0.0266` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4152` n `130` status `ready` deltaP `14.984` edge `0.1202` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.3168` n `40` status `ready` deltaP `6.4634` edge `0.0212` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.2121` n `139` status `ready` deltaP `1.2666` edge `0.0029` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
