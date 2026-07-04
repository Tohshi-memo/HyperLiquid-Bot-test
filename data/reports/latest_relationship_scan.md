# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T18:37:25.729049+00:00`
- Price records: `672`
- Market context records: `5691`
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

- `market_context_high->crypto_major_4h` score `1.8385` n `257` status `ready` deltaP `12.8102` edge `0.2346` maxDD `-9.0101`
- `market_context_high->equity_24h` score `1.1555` n `207` status `ready` deltaP `16.1761` edge `0.5482` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.9802` n `257` status `ready` deltaP `9.8979` edge `0.1766` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2266` n `257` status `ready` deltaP `6.5323` edge `0.1392` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `-0.2082` n `269` status `ready` deltaP `3.1348` edge `0.0436` maxDD `-3.8812`
- `market_context_high->fx_1h` score `-0.2636` n `269` status `ready` deltaP `1.8949` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_major_1h` score `-0.3066` n `269` status `ready` deltaP `4.7865` edge `0.0455` maxDD `-5.2367`
- `market_context_high->metal_1h` score `-0.4642` n `269` status `ready` deltaP `1.2911` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5714` n `269` status `ready` deltaP `3.6413` edge `0.0288` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6063` n `269` status `ready` deltaP `0.6923` edge `0.0045` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.6238` n `269` status `ready` deltaP `0.0412` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-0.8996` n `207` status `ready` deltaP `13.5115` edge `0.0464` maxDD `-3.1452`
- `market_context_high->fx_4h` score `-1.1245` n `257` status `ready` deltaP `4.7956` edge `0.0073` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2921` n `257` status `ready` deltaP `-0.8767` edge `0.0075` maxDD `-3.0516`
- `market_context_high->index_24h` score `-2.7109` n `207` status `ready` deltaP `4.2874` edge `0.032` maxDD `-17.6504`
- `market_context_high->metal_4h` score `-2.7989` n `257` status `ready` deltaP `-10.3154` edge `-0.0525` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.864` n `257` status `ready` deltaP `-3.2469` edge `-0.0328` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2651` n `207` status `ready` deltaP `5.2309` edge `0.0554` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.1773` n `207` status `ready` deltaP `-10.4544` edge `-0.2463` maxDD `-32.5901`
- `market_context_high->commodity_24h` score `-12.1442` n `207` status `ready` deltaP `-11.1489` edge `-0.0768` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
