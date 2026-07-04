# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T18:46:31.687444+00:00`
- Price records: `672`
- Market context records: `5692`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `1.9932` n `257` status `ready` deltaP `13.0469` edge `0.2375` maxDD `-8.3373`
- `market_context_high->equity_24h` score `1.1579` n `207` status `ready` deltaP `16.1761` edge `0.5485` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.0411` n `257` status `ready` deltaP `10.1346` edge `0.1801` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2254` n `257` status `ready` deltaP `6.5323` edge `0.1391` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `-0.1998` n `269` status `ready` deltaP `3.1348` edge `0.0443` maxDD `-3.8812`
- `market_context_high->crypto_major_1h` score `-0.208` n `269` status `ready` deltaP `4.7865` edge `0.0459` maxDD `-4.6115`
- `market_context_high->fx_1h` score `-0.2636` n `269` status `ready` deltaP `1.8949` edge `0.0012` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.4634` n `269` status `ready` deltaP `1.2911` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5702` n `269` status `ready` deltaP `3.6413` edge `0.0289` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6055` n `269` status `ready` deltaP `0.6923` edge `0.0046` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.6361` n `269` status `ready` deltaP `-0.1809` edge `-0.0038` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.9` n `207` status `ready` deltaP `13.5115` edge `0.0465` maxDD `-3.1571`
- `market_context_high->fx_4h` score `-1.1253` n `257` status `ready` deltaP `4.7956` edge `0.0072` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2944` n `257` status `ready` deltaP `-0.8767` edge `0.0076` maxDD `-3.0835`
- `market_context_high->index_24h` score `-2.7459` n `207` status `ready` deltaP `3.9779` edge `0.0306` maxDD `-17.7323`
- `market_context_high->metal_4h` score `-2.7866` n `257` status `ready` deltaP `-10.0787` edge `-0.0525` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8865` n `257` status `ready` deltaP `-3.4836` edge `-0.0331` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.1323` n `207` status `ready` deltaP `5.5404` edge `0.0644` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.1572` n `207` status `ready` deltaP `-10.145` edge `-0.246` maxDD `-32.5725`
- `market_context_high->commodity_24h` score `-12.1822` n `207` status `ready` deltaP `-11.4584` edge `-0.0779` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
