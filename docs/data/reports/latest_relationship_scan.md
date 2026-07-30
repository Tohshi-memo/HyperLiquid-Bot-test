# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T00:37:27.113145+00:00`
- Price records: `672`
- Market context records: `8357`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.0806` n `52` status `ready` deltaP `35.1896` edge `520.8142` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.5962` n `52` status `ready` deltaP `26.372` edge `0.5169` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.916` n `52` status `ready` deltaP `20.8314` edge `0.135` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7842` n `52` status `ready` deltaP `23.1707` edge `0.0966` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1353` n `52` status `ready` deltaP `9.9789` edge `0.2766` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7922` n `52` status `ready` deltaP `13.5076` edge `0.1027` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7309` n `52` status `ready` deltaP `11.8609` edge `0.1049` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.63` n `52` status `ready` deltaP `17.4836` edge `0.2316` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.834` n `52` status `ready` deltaP `7.6337` edge `0.0654` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.254` n `52` status `ready` deltaP `4.5947` edge `0.0194` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0806` n `52` status `ready` deltaP `5.3432` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1869` n `52` status `ready` deltaP `2.4989` edge `0.0081` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5616` n `52` status `ready` deltaP `2.9784` edge `0.0039` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2052` n `52` status `ready` deltaP `-9.1663` edge `-0.0441` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2711` n `52` status `ready` deltaP `-23.0369` edge `-0.0535` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.8386` n `52` status `ready` deltaP `-26.3755` edge `-0.117` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0059` n `52` status `ready` deltaP `-31.0858` edge `-0.2125` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9008` n `52` status `ready` deltaP `-9.3082` edge `-0.3357` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0275` n `52` status `ready` deltaP `-24.0785` edge `-0.2915` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.8173` n `52` status `ready` deltaP `-16.9871` edge `-1.3357` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
