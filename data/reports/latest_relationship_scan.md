# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T01:37:29.462884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->equity_1h` score `0.4108` n `105` status `ready` deltaP `9.1688` edge `0.0546` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.361` n `105` status `ready` deltaP `10.8569` edge `0.0064` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.3333` n `105` status `ready` deltaP `5.8072` edge `0.152` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0028` n `105` status `ready` deltaP `6.7232` edge `0.0058` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1355` n `96` status `ready` deltaP `4.6875` edge `0.1347` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.1532` n `105` status `ready` deltaP `9.1275` edge `-0.0509` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.192` n `105` status `ready` deltaP `1.075` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2233` n `105` status `ready` deltaP `6.6826` edge `-0.0156` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2605` n `105` status `ready` deltaP `2.7887` edge `-0.0016` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2728` n `105` status `ready` deltaP `5.7332` edge `0.0192` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.5719` n `105` status `ready` deltaP `0.8013` edge `0.0015` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7346` n `105` status `ready` deltaP `-2.3476` edge `0.0065` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7552` n `105` status `ready` deltaP `1.0878` edge `-0.0196` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8211` n `105` status `ready` deltaP `-6.9261` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.8278` n `105` status `ready` deltaP `3.6716` edge `-0.0498` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.1797` n `105` status `ready` deltaP `5.768` edge `-0.118` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5999` n `96` status `ready` deltaP `1.0416` edge `-0.0517` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8527` n `96` status `ready` deltaP `-21.0069` edge `-0.0227` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.3566` n `96` status `ready` deltaP `13.5416` edge `-0.4027` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9408` n `96` status `ready` deltaP `-21.0069` edge `-0.1626` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
