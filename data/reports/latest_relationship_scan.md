# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T00:07:24.016601+00:00`
- Price records: `672`
- Market context records: `8355`
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

- `news_risk_high->unknown_24h` score `6252.0614` n `52` status `ready` deltaP `35.1896` edge `520.8126` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6238` n `52` status `ready` deltaP `26.372` edge `0.5192` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.916` n `52` status `ready` deltaP `20.8314` edge `0.135` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7902` n `52` status `ready` deltaP `23.1707` edge `0.0971` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1714` n `52` status `ready` deltaP `10.2838` edge `0.2792` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7694` n `52` status `ready` deltaP `13.3579` edge `0.1018` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7094` n `52` status `ready` deltaP `11.7112` edge `0.1041` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6716` n `52` status `ready` deltaP `17.7885` edge `0.2349` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.834` n `52` status `ready` deltaP `7.6337` edge `0.0654` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2385` n `52` status `ready` deltaP `4.445` edge `0.0191` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0798` n `52` status `ready` deltaP `5.3432` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.218` n `52` status `ready` deltaP `2.1995` edge `0.0075` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5608` n `52` status `ready` deltaP `2.9784` edge `0.004` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2352` n `52` status `ready` deltaP `-9.4657` edge `-0.0446` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2699` n `52` status `ready` deltaP `-23.0369` edge `-0.0534` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.7724` n `52` status `ready` deltaP `-26.0283` edge `-0.1138` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0435` n `52` status `ready` deltaP `-31.3907` edge `-0.2136` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9068` n `52` status `ready` deltaP `-9.3082` edge `-0.3362` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0455` n `52` status `ready` deltaP `-24.0785` edge `-0.293` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.7513` n `52` status `ready` deltaP `-16.9871` edge `-1.3302` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
