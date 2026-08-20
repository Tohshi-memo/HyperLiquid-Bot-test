# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T18:22:28.362681+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11818`

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

- `market_context_high->equity_4h` score `0.7034` n `105` status `ready` deltaP `8.0938` edge `0.1676` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5463` n `105` status `ready` deltaP `9.9173` edge `0.0609` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3694` n `105` status `ready` deltaP `10.8569` edge `0.0071` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0123` n `105` status `ready` deltaP `6.8757` edge `0.006` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0022` n `105` status `ready` deltaP `9.8839` edge `-0.0086` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.0786` n `96` status `ready` deltaP `4.6875` edge `0.142` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1682` n `105` status `ready` deltaP `3.5372` edge `0.0011` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2185` n `105` status `ready` deltaP `0.6259` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2444` n `105` status `ready` deltaP `6.1905` edge `0.0198` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.5129` n `105` status `ready` deltaP `6.882` edge `-0.0659` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5509` n `105` status `ready` deltaP `0.951` edge `0.0032` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7245` n `105` status `ready` deltaP `-2.3476` edge `0.0078` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7412` n `105` status `ready` deltaP `1.3872` edge `-0.0198` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8234` n `105` status `ready` deltaP `-7.0758` edge `-0.0018` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5654` n `105` status `ready` deltaP `4.2814` edge `-0.032` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9527` n `105` status `ready` deltaP `6.8351` edge `-0.1062` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.2816` n `96` status `ready` deltaP `17.5347` edge `-0.2564` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6022` n `96` status `ready` deltaP `1.0416` edge `-0.052` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8102` n `96` status `ready` deltaP `-21.1805` edge `-0.018` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9666` n `96` status `ready` deltaP `-21.0069` edge `-0.1659` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
