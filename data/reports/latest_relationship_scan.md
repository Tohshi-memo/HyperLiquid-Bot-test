# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T09:37:32.491091+00:00`
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

- `news_risk_high->unknown_24h` score `1212.1644` n `127` status `ready` deltaP `1.2153` edge `101.0056` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.36` n `40` status `ready` deltaP `10.3743` edge `12.9655` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `55.8421` n `36` status `ready` deltaP `29.6875` edge `4.4907` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.2612` n `36` status `ready` deltaP `35.5903` edge `2.3159` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.1714` n `36` status `ready` deltaP `14.4097` edge `2.2062` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.4325` n `36` status `ready` deltaP `32.9861` edge `0.4916` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.5361` n `40` status `ready` deltaP `18.5366` edge `0.3087` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.2473` n `36` status `ready` deltaP `38.0209` edge `0.1243` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.939` n `40` status `ready` deltaP `24.5427` edge `0.1981` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1367` n `40` status `ready` deltaP `34.3293` edge `0.0396` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.3857` n `40` status `ready` deltaP `9.939` edge `0.223` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7383` n `40` status `ready` deltaP `19.012` edge `0.0584` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5916` n `40` status `ready` deltaP `11.6617` edge `0.1438` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4454` n `40` status `ready` deltaP `11.8563` edge `0.1272` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0044` n `40` status `ready` deltaP `14.012` edge `0.0098` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9257` n `40` status `ready` deltaP `15.6886` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.7022` n `127` status `ready` deltaP `15.2915` edge `0.0261` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.3588` n `127` status `ready` deltaP `14.1582` edge `0.121` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.3558` n `40` status `ready` deltaP `6.9207` edge `0.0214` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1869` n `139` status `ready` deltaP `1.566` edge `0.003` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
