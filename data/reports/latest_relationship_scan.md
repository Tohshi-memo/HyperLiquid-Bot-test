# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T10:52:29.676933+00:00`
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

- `news_risk_high->unknown_24h` score `965.6616` n `132` status `ready` deltaP `1.2153` edge `80.4637` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.4548` n `40` status `ready` deltaP `10.3743` edge `12.9734` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `56.3149` n `36` status `ready` deltaP `29.6875` edge `4.5301` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.434` n `36` status `ready` deltaP `35.5903` edge `2.3303` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.739` n `36` status `ready` deltaP `14.4097` edge `2.2535` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.4661` n `36` status `ready` deltaP `32.9861` edge `0.4944` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.4639` n `40` status `ready` deltaP `18.3841` edge `0.3037` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.2322` n `36` status `ready` deltaP `37.8473` edge `0.1242` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9136` n `40` status `ready` deltaP `24.3902` edge `0.197` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1233` n `40` status `ready` deltaP `34.1768` edge `0.0395` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.3243` n `40` status `ready` deltaP `9.7866` edge `0.2189` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7383` n `40` status `ready` deltaP `19.012` edge `0.0584` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5748` n `40` status `ready` deltaP `11.512` edge `0.1434` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.425` n `40` status `ready` deltaP `11.7066` edge `0.1265` maxDD `-4.8632`
- `market_context_high->index_1h` score `0.9925` n `40` status `ready` deltaP `13.8623` edge `0.0098` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.976` n `40` status `ready` deltaP `16.2874` edge `0.0084` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.7738` n `132` status `ready` deltaP `16.0669` edge `0.0269` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.3369` n `132` status `ready` deltaP `14.1099` edge `0.1195` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.2924` n `40` status `ready` deltaP `6.1585` edge `0.0212` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1989` n `139` status `ready` deltaP `1.4163` edge `0.003` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
