# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T19:07:50.404690+00:00`
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

- `market_context_high->equity_4h` score `0.7784` n `105` status `ready` deltaP `8.5511` edge `0.1708` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.569` n `105` status `ready` deltaP `10.067` edge `0.0618` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3838` n `105` status `ready` deltaP `11.0066` edge `0.0073` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0108` n `105` status `ready` deltaP `6.8757` edge `0.0058` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0243` n `105` status `ready` deltaP `9.579` edge `-0.0094` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.0856` n `96` status `ready` deltaP `4.6875` edge `0.1411` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.185` n `105` status `ready` deltaP `3.3875` edge `0.0007` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2159` n `105` status `ready` deltaP `6.6478` edge `0.0204` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.2271` n `105` status `ready` deltaP `0.4762` edge `0.0036` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4947` n `105` status `ready` deltaP `1.4001` edge `0.0074` maxDD `-2.413`
- `market_context_high->unknown_1h` score `-0.5009` n `105` status `ready` deltaP `7.0317` edge `-0.0659` maxDD `-0.4843`
- `market_context_high->crypto_major_1h` score `-0.6516` n `105` status `ready` deltaP `1.8363` edge `-0.0113` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7561` n `105` status `ready` deltaP `-2.8049` edge `0.0068` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8444` n `105` status `ready` deltaP `-7.3752` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.569` n `105` status `ready` deltaP `4.2814` edge `-0.0323` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9791` n `105` status `ready` deltaP `6.8351` edge `-0.1084` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.5` n `96` status `ready` deltaP `17.5347` edge `-0.2746` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6038` n `96` status `ready` deltaP `1.0416` edge `-0.0522` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8186` n `96` status `ready` deltaP `-21.1805` edge `-0.0187` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9705` n `96` status `ready` deltaP `-21.0069` edge `-0.1664` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
