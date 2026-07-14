# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T22:37:24.836545+00:00`
- Price records: `672`
- Market context records: `6755`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.0804` n `176` status `ready` deltaP `0.7102` edge `0.509` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0302` n `176` status `ready` deltaP `7.5021` edge `0.0321` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.0958` n `176` status `ready` deltaP `7.9704` edge `0.1257` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.1304` n `176` status `ready` deltaP `5.4981` edge `0.0289` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3804` n `176` status `ready` deltaP `-0.1157` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5819` n `176` status `ready` deltaP `-0.5682` edge `0.0006` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6071` n `176` status `ready` deltaP `-0.1531` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7074` n `176` status `ready` deltaP `-5.1409` edge `-0.0039` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.116` n `176` status `ready` deltaP `3.5554` edge `-0.014` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2104` n `176` status `ready` deltaP `6.7489` edge `-0.0122` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2264` n `176` status `ready` deltaP `7.3864` edge `-0.0001` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4298` n `176` status `ready` deltaP `-1.7738` edge `-0.0225` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.8113` n `176` status `ready` deltaP `-7.3251` edge `-0.012` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.4663` n `176` status `ready` deltaP `4.2683` edge `-0.0132` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.5675` n `176` status `ready` deltaP `3.4368` edge `-0.0119` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6676` n `176` status `ready` deltaP `-6.4718` edge `-0.0128` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.6293` n `176` status `ready` deltaP `-15.8675` edge `0.0399` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.1396` n `176` status `ready` deltaP `3.4645` edge `-0.1269` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2475` n `176` status `ready` deltaP `-7.3548` edge `-0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.3463` n `176` status `ready` deltaP `-12.7683` edge `-0.1364` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
