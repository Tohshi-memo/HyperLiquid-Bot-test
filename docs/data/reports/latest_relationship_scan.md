# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T23:37:24.714908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12819`

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

- `market_context_high->equity_1h` score `0.5342` n `105` status `ready` deltaP `10.067` edge `0.0589` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.5185` n `105` status `ready` deltaP `7.0268` edge `0.1593` maxDD `-8.3685`
- `market_context_high->index_1h` score `0.4185` n `105` status `ready` deltaP `11.4557` edge `0.0072` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.009` n `105` status `ready` deltaP `6.5708` edge `0.0053` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1254` n `96` status `ready` deltaP `4.6875` edge `0.136` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.1499` n `105` status `ready` deltaP `7.7497` edge `-0.0133` maxDD `-1.273`
- `market_context_high->fx_1h` score `-0.1866` n `105` status `ready` deltaP `1.2247` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.191` n `105` status `ready` deltaP `3.3875` edge `0.0002` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2088` n `105` status `ready` deltaP `6.8003` edge `0.0203` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3367` n `105` status `ready` deltaP `8.379` edge `-0.0612` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5602` n `105` status `ready` deltaP `0.8013` edge `0.003` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7014` n `105` status `ready` deltaP `1.3872` edge `-0.0147` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7607` n `105` status `ready` deltaP `-2.8049` edge `0.0062` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8102` n `105` status `ready` deltaP `-6.7764` edge `-0.0021` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5418` n `105` status `ready` deltaP `4.8911` edge `-0.0341` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9046` n `105` status `ready` deltaP `6.9875` edge `-0.1032` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6038` n `96` status `ready` deltaP `1.0416` edge `-0.0522` maxDD `-18.3411`
- `market_context_high->unknown_24h` score `-3.7823` n `96` status `ready` deltaP `14.9305` edge `-0.3641` maxDD `-1.0505`
- `market_context_high->fx_24h` score `-3.8642` n `96` status `ready` deltaP `-21.1805` edge `-0.0225` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9471` n `96` status `ready` deltaP `-21.0069` edge `-0.1634` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
