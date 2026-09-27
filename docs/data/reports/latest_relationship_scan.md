# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T10:07:28.428872+00:00`
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

- `news_risk_high->unknown_24h` score `1111.2432` n `129` status `ready` deltaP `1.2153` edge `92.5955` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.3672` n `40` status `ready` deltaP `10.3743` edge `12.9661` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `56.0173` n `36` status `ready` deltaP `29.6875` edge `4.5053` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.3284` n `36` status `ready` deltaP `35.5903` edge `2.3215` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.3682` n `36` status `ready` deltaP `14.4097` edge `2.2226` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.4457` n `36` status `ready` deltaP `32.9861` edge `0.4927` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.4903` n `40` status `ready` deltaP `18.3841` edge `0.3059` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.2322` n `36` status `ready` deltaP `37.8473` edge `0.1242` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9208` n `40` status `ready` deltaP `24.3902` edge `0.1976` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1367` n `40` status `ready` deltaP `34.3293` edge `0.0396` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.3483` n `40` status `ready` deltaP `9.7866` edge `0.2209` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7251` n `40` status `ready` deltaP `18.8623` edge `0.0583` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.5676` n `40` status `ready` deltaP `11.512` edge `0.1428` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4226` n `40` status `ready` deltaP `11.7066` edge `0.1263` maxDD `-4.8632`
- `market_context_high->index_1h` score `0.9925` n `40` status `ready` deltaP `13.8623` edge `0.0098` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9389` n `40` status `ready` deltaP `15.8383` edge `0.0083` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.7312` n `129` status `ready` deltaP `15.6089` edge `0.0264` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.3914` n `129` status `ready` deltaP `14.656` edge `0.1204` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.3302` n `40` status `ready` deltaP `6.6159` edge `0.0213` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1989` n `139` status `ready` deltaP `1.4163` edge `0.003` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
