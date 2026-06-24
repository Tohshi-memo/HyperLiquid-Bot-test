# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T05:59:16.540637+00:00`
- Price records: `672`
- Market context records: `4593`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `67.7364` n `149` status `ready` deltaP `5.9016` edge `5.6554` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.9823` n `149` status `ready` deltaP `7.845` edge `0.4006` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.5555` n `149` status `ready` deltaP `1.3212` edge `0.0245` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.7065` n `149` status `ready` deltaP `2.5607` edge `0.0006` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.8446` n `149` status `ready` deltaP `-1.6678` edge `-0.0038` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.9064` n `149` status `ready` deltaP `1.3453` edge `-0.0129` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9919` n `149` status `ready` deltaP `-3.7013` edge `-0.0038` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2169` n `149` status `ready` deltaP `3.412` edge `0.032` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.6483` n `149` status `ready` deltaP `-0.2108` edge `-0.033` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7581` n `149` status `ready` deltaP `-4.8216` edge `-0.0135` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.7306` n `147` status `ready` deltaP `1.8283` edge `-0.1474` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9996` n `149` status `ready` deltaP `-4.8015` edge `-0.0874` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.5977` n `147` status `ready` deltaP `10.9446` edge `0.0688` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4713` n `147` status `ready` deltaP `-13.9066` edge `-0.012` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6068` n `149` status `ready` deltaP `-2.7308` edge `-0.1203` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.9134` n `149` status `ready` deltaP `-6.83` edge `-0.1553` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4904` n `147` status `ready` deltaP `-7.7771` edge `-0.1182` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1034` n `149` status `ready` deltaP `-3.5982` edge `-0.2774` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2372` n `149` status `ready` deltaP `-5.8909` edge `-0.3518` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.1841` n `149` status `ready` deltaP `-4.4535` edge `-0.438` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
