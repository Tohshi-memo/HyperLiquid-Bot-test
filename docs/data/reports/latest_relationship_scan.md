# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T16:07:26.610011+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4088`

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

- `news_risk_high->crypto_alt_4h` score `0.5413` n `146` status `ready` deltaP `8.6765` edge `0.2752` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.0871` n `146` status `ready` deltaP `4.7268` edge `0.0801` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6495` n `146` status `ready` deltaP `3.4431` edge `0.0029` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6981` n `146` status `ready` deltaP `-2.5223` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4458` n `146` status `ready` deltaP `-7.4695` edge `-0.0104` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5594` n `146` status `ready` deltaP `-8.8405` edge `-0.0188` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7028` n `146` status `ready` deltaP `1.6037` edge `0.0011` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.0856` n `146` status `ready` deltaP `-3.7917` edge `0.0255` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.2828` n `146` status `ready` deltaP `-16.2909` edge `-0.0132` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.421` n `146` status `ready` deltaP `-9.9746` edge `0.0014` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.5281` n `146` status `ready` deltaP `-4.2634` edge `-0.0097` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9137` n `146` status `ready` deltaP `-12.3382` edge `-0.0071` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6979` n `146` status `ready` deltaP `-13.0847` edge `0.0145` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7437` n `146` status `ready` deltaP `-12.7882` edge `-0.0729` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.897` n `146` status `ready` deltaP `-9.5056` edge `-0.0261` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.8584` n `146` status `ready` deltaP `-11.4869` edge `-0.2201` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.8915` n `146` status `ready` deltaP `-14.5334` edge `0.182` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.7019` n `146` status `ready` deltaP `2.6708` edge `0.0098` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.076` n `146` status `ready` deltaP `9.8198` edge `0.2119` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0285` n `146` status `ready` deltaP `1.8337` edge `-0.3677` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
