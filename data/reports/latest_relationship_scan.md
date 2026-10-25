# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T10:07:27.215831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7592`

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

- `market_context_high->unknown_4h` score `38.4256` n `112` status `ready` deltaP `-0.3049` edge `3.2377` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.714` n `114` status `ready` deltaP `4.3334` edge `0.3295` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.8651` n `47` status `ready` deltaP `17.9559` edge `0.0821` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0177` n `112` status `ready` deltaP `7.818` edge `0.0092` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.065` n `114` status `ready` deltaP `3.5508` edge `0.0029` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.0849` n `47` status `ready` deltaP `3.2801` edge `0.077` maxDD `-5.8084`
- `market_context_high->crypto_alt_24h` score `-0.2501` n `47` status `ready` deltaP `11.3106` edge `0.1755` maxDD `-18.637`
- `market_context_high->commodity_1h` score `-0.4966` n `114` status `ready` deltaP `-0.063` edge `0.0091` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5328` n `114` status `ready` deltaP `5.8173` edge `-0.004` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6285` n `114` status `ready` deltaP `-1.5417` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8766` n `112` status `ready` deltaP `-2.9835` edge `0.0304` maxDD `-1.165`
- `market_context_high->fx_24h` score `-0.9337` n `47` status `ready` deltaP `0.0997` edge `0.0066` maxDD `-1.1576`
- `market_context_high->crypto_major_1h` score `-1.3078` n `114` status `ready` deltaP `2.4609` edge `-0.026` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8907` n `112` status `ready` deltaP `4.7473` edge `-0.0182` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1341` n `112` status `ready` deltaP `-7.4042` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-2.9751` n `114` status `ready` deltaP `-1.5207` edge `-0.0504` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.1825` n `47` status `ready` deltaP `-8.4995` edge `-0.0091` maxDD `-6.9559`
- `market_context_high->equity_1h` score `-3.7012` n `114` status `ready` deltaP `0.5541` edge `-0.0848` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.8938` n `47` status `ready` deltaP `-16.7368` edge `-0.1661` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.9312` n `112` status `ready` deltaP `-12.4347` edge `-0.245` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
