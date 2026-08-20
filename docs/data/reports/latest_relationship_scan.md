# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T18:37:29.488409+00:00`
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

- `market_context_high->equity_4h` score `0.7312` n `105` status `ready` deltaP `8.2463` edge `0.1689` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5678` n `105` status `ready` deltaP `10.067` edge `0.0617` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3838` n `105` status `ready` deltaP `11.0066` edge `0.0073` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0116` n `105` status `ready` deltaP `6.8757` edge `0.0059` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0133` n `105` status `ready` deltaP `9.7314` edge `-0.009` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.0809` n `96` status `ready` deltaP `4.6875` edge `0.1417` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1682` n `105` status `ready` deltaP `3.5372` edge `0.0011` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2263` n `105` status `ready` deltaP `0.4762` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2349` n `105` status `ready` deltaP `6.3429` edge `0.02` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.5177` n `105` status `ready` deltaP `6.882` edge `-0.0663` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.529` n `105` status `ready` deltaP `1.1007` edge `0.005` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7077` n `105` status `ready` deltaP `1.5369` edge `-0.0165` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7347` n `105` status `ready` deltaP `-2.5` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8328` n `105` status `ready` deltaP `-7.2255` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5714` n `105` status `ready` deltaP `4.2814` edge `-0.0325` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9683` n `105` status `ready` deltaP `6.8351` edge `-0.1075` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.3524` n `96` status `ready` deltaP `17.5347` edge `-0.2623` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6022` n `96` status `ready` deltaP `1.0416` edge `-0.052` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8126` n `96` status `ready` deltaP `-21.1805` edge `-0.0182` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9689` n `96` status `ready` deltaP `-21.0069` edge `-0.1662` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
