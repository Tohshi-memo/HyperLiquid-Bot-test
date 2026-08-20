# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T23:52:24.322575+00:00`
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
- `market_context_high->equity_4h` score `0.4979` n `105` status `ready` deltaP `6.8743` edge `0.1586` maxDD `-8.3685`
- `market_context_high->index_1h` score `0.4197` n `105` status `ready` deltaP `11.4557` edge `0.0073` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.009` n `105` status `ready` deltaP `6.5708` edge `0.0053` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1277` n `96` status `ready` deltaP `4.6875` edge `0.1357` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.1601` n `105` status `ready` deltaP `7.5973` edge `-0.0136` maxDD `-1.273`
- `market_context_high->fx_1h` score `-0.1944` n `105` status `ready` deltaP `1.075` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2053` n `105` status `ready` deltaP `3.2378` edge `0.0` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2088` n `105` status `ready` deltaP `6.8003` edge `0.0203` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3115` n `105` status `ready` deltaP `8.5287` edge `-0.0601` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5618` n `105` status `ready` deltaP `0.8013` edge `0.0028` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7038` n `105` status `ready` deltaP `1.3872` edge `-0.015` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.752` n `105` status `ready` deltaP `-2.6524` edge `0.0063` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8016` n `105` status `ready` deltaP `-6.6267` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5792` n `105` status `ready` deltaP `4.7387` edge `-0.0362` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9347` n `105` status `ready` deltaP `6.8351` edge `-0.1047` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.603` n `96` status `ready` deltaP `1.0416` edge `-0.0521` maxDD `-18.3411`
- `market_context_high->unknown_24h` score `-3.8538` n `96` status `ready` deltaP `14.7569` edge `-0.3689` maxDD `-1.0505`
- `market_context_high->fx_24h` score `-3.8654` n `96` status `ready` deltaP `-21.1805` edge `-0.0226` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9471` n `96` status `ready` deltaP `-21.0069` edge `-0.1634` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
