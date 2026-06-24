# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T06:52:32.426886+00:00`
- Price records: `672`
- Market context records: `4597`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9905`

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

- `market_context_high->unknown_1h` score `68.4503` n `148` status `ready` deltaP `5.8788` edge `5.7109` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.0858` n `148` status `ready` deltaP `8.2234` edge `0.4067` maxDD `-4.6834`
- `market_context_high->fx_1h` score `-0.5664` n `148` status `ready` deltaP `-1.9583` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.5877` n `148` status `ready` deltaP `0.9629` edge `0.0242` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.728` n `148` status `ready` deltaP `2.2206` edge `0.0001` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9154` n `148` status `ready` deltaP `1.2031` edge `-0.0131` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9794` n `148` status `ready` deltaP `-3.52` edge `-0.0034` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2273` n `148` status `ready` deltaP `3.1971` edge `0.0321` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.6737` n `148` status `ready` deltaP `-0.5191` edge `-0.0342` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7452` n `148` status `ready` deltaP `-4.6448` edge `-0.0136` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.6452` n `146` status `ready` deltaP `2.2046` edge `-0.1428` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0251` n `148` status `ready` deltaP `-4.9604` edge `-0.0896` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.5776` n `146` status `ready` deltaP `11.2847` edge `0.0682` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4515` n `146` status `ready` deltaP `-13.72` edge `-0.0116` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5667` n `148` status `ready` deltaP `-2.3952` edge `-0.1192` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8867` n `148` status `ready` deltaP `-6.5261` edge `-0.1551` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.5168` n `146` status `ready` deltaP `-7.9576` edge `-0.1192` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.112` n `148` status `ready` deltaP `-3.2672` edge `-0.2807` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2911` n `148` status `ready` deltaP `-6.2376` edge `-0.3564` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.264` n `148` status `ready` deltaP `-5.1212` edge `-0.4438` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
