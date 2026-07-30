# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T00:22:29.426950+00:00`
- Price records: `672`
- Market context records: `8356`
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

- `news_risk_high->unknown_24h` score `6252.071` n `52` status `ready` deltaP `35.1896` edge `520.8134` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6094` n `52` status `ready` deltaP `26.372` edge `0.518` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9148` n `52` status `ready` deltaP `20.8314` edge `0.1349` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7854` n `52` status `ready` deltaP `23.1707` edge `0.0967` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1518` n `52` status `ready` deltaP `10.1313` edge `0.2777` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7742` n `52` status `ready` deltaP `13.3579` edge `0.1022` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7118` n `52` status `ready` deltaP `11.7112` edge `0.1043` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6504` n `52` status `ready` deltaP `17.6361` edge `0.2332` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8328` n `52` status `ready` deltaP `7.6337` edge `0.0653` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2397` n `52` status `ready` deltaP `4.445` edge `0.0192` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0806` n `52` status `ready` deltaP `5.3432` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2024` n `52` status `ready` deltaP `2.3492` edge `0.0078` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5616` n `52` status `ready` deltaP `2.9784` edge `0.0039` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2184` n `52` status `ready` deltaP `-9.316` edge `-0.0442` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2699` n `52` status `ready` deltaP `-23.0369` edge `-0.0534` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.8067` n `52` status `ready` deltaP `-26.2019` edge `-0.1155` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0241` n `52` status `ready` deltaP `-31.2383` edge `-0.213` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9044` n `52` status `ready` deltaP `-9.3082` edge `-0.336` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0359` n `52` status `ready` deltaP `-24.0785` edge `-0.2922` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.7849` n `52` status `ready` deltaP `-16.9871` edge `-1.333` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
