# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T12:22:29.043573+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `780.1188` n `136` status `ready` deltaP `1.2153` edge `65.0018` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.3816` n `40` status `ready` deltaP `10.3743` edge `12.9673` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `56.9677` n `36` status `ready` deltaP `29.6875` edge `4.5845` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.6428` n `36` status `ready` deltaP `35.5903` edge `2.3477` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.5394` n `36` status `ready` deltaP `14.4097` edge `2.3202` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5105` n `36` status `ready` deltaP `32.9861` edge `0.4981` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.5797` n `40` status `ready` deltaP `18.8415` edge `0.3103` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.3021` n `36` status `ready` deltaP `38.5417` edge `0.1254` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9196` n `40` status `ready` deltaP `24.3902` edge `0.1975` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1355` n `40` status `ready` deltaP `34.3293` edge `0.0395` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.3579` n `40` status `ready` deltaP `9.7866` edge `0.2217` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7754` n `40` status `ready` deltaP `19.4611` edge `0.0585` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5868` n `40` status `ready` deltaP `11.512` edge `0.1444` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4167` n `40` status `ready` deltaP `11.5569` edge `0.1268` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0535` n `40` status `ready` deltaP `14.6108` edge `0.0099` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9496` n `40` status `ready` deltaP `15.988` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.8418` n `136` status `ready` deltaP `16.6463` edge `0.0287` maxDD `-2.2287`
- `market_context_high->metal_4h` score `0.3424` n `40` status `ready` deltaP `6.7683` edge `0.0213` maxDD `-0.3647`
- `news_risk_high->metal_24h` score `0.3164` n `136` status `ready` deltaP `13.8685` edge `0.1194` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.1378` n `139` status `ready` deltaP `2.1648` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
