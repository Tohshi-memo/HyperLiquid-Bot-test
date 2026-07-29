# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T08:52:33.642155+00:00`
- Price records: `672`
- Market context records: `8286`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6096.9766` n `53` status `ready` deltaP `35.1382` edge `507.8775` maxDD `-1.4298`
- `news_risk_high->equity_4h` score `7.0205` n `54` status `ready` deltaP `25.9259` edge `0.4719` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9743` n `54` status `ready` deltaP `21.2298` edge `0.1372` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6555` n `54` status `ready` deltaP `22.2674` edge `0.0919` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0202` n `54` status `ready` deltaP `9.7166` edge `0.2636` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8172` n `54` status `ready` deltaP `14.2548` edge `0.0998` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5418` n `54` status `ready` deltaP `10.4569` edge `0.0985` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5412` n `54` status `ready` deltaP `17.2313` edge `0.2219` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.9981` n `54` status `ready` deltaP `9.1294` edge `0.0691` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4136` n `54` status `ready` deltaP `6.4538` edge `0.0203` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1603` n `54` status `ready` deltaP `6.8474` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1227` n `54` status `ready` deltaP `2.8055` edge `0.0114` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4255` n `54` status `ready` deltaP `5.07` edge `0.0074` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0964` n `54` status `ready` deltaP `-8.3611` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.9628` n `53` status `ready` deltaP `-20.4042` edge `-0.0486` maxDD `-5.3152`
- `news_risk_high->metal_24h` score `-5.5661` n `53` status `ready` deltaP `-19.7655` edge `-0.056` maxDD `-10.7521`
- `news_risk_high->commodity_4h` score `-8.7214` n `54` status `ready` deltaP `-30.1999` edge `-0.1947` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.2735` n `53` status `ready` deltaP `-7.6028` edge `-0.2948` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0759` n `53` status `ready` deltaP `-24.2466` edge `-0.3002` maxDD `-27.8917`
- `news_risk_high->crypto_major_24h` score `-32.5125` n `53` status `ready` deltaP `-13.0175` edge `-1.1701` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
