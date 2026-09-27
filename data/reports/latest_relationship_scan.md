# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T14:22:24.646393+00:00`
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

- `news_risk_high->unknown_24h` score `769.368` n `136` status `ready` deltaP `1.2153` edge `64.1059` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.4068` n `40` status `ready` deltaP `10.3743` edge `12.9694` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.8653` n `36` status `ready` deltaP `29.6875` edge `4.6593` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.9428` n `36` status `ready` deltaP `35.5903` edge `2.3727` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.6458` n `36` status `ready` deltaP `14.4097` edge `2.4124` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5717` n `36` status `ready` deltaP `32.9861` edge `0.5032` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `5.138` n `40` status `ready` deltaP `20.061` edge `0.3487` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4468` n `36` status `ready` deltaP `39.9306` edge `0.1282` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0371` n `40` status `ready` deltaP `25.3049` edge `0.2012` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2415` n `40` status `ready` deltaP `35.5488` edge `0.0402` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.7011` n `40` status `ready` deltaP `10.7012` edge `0.2442` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.803` n `40` status `ready` deltaP `19.7605` edge `0.0588` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.6444` n `40` status `ready` deltaP `11.512` edge `0.1492` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4898` n `40` status `ready` deltaP `11.8563` edge `0.1309` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0907` n `40` status `ready` deltaP `15.0599` edge `0.01` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9257` n `40` status `ready` deltaP `15.6886` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.903` n `136` status `ready` deltaP `16.6463` edge `0.0338` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4611` n `136` status `ready` deltaP `15.2574` edge `0.1222` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4325` n `40` status `ready` deltaP `7.8354` edge `0.0217` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1007` n `139` status `ready` deltaP `2.6139` edge `0.0032` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
