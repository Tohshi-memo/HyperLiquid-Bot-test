# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T10:07:33.518441+00:00`
- Price records: `672`
- Market context records: `4713`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.94` n `144` status `ready` deltaP `14.0137` edge `6.36` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0221` n `144` status `ready` deltaP `13.7026` edge `0.4482` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.8991` n `135` status `ready` deltaP `15.1389` edge `0.233` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3147` n `144` status `ready` deltaP `2.258` edge `0.0242` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6988` n `144` status `ready` deltaP `4.3191` edge `-0.0061` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9321` n `144` status `ready` deltaP `9.1294` edge `0.0304` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9398` n `144` status `ready` deltaP `-1.5074` edge `-0.0022` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-1.1138` n `144` status `ready` deltaP `2.7947` edge `0.0155` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1989` n `144` status `ready` deltaP `-1.7423` edge `0.0104` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.3212` n `144` status `ready` deltaP `-5.435` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6301` n `144` status `ready` deltaP `-3.7841` edge `-0.0102` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1901` n `144` status `ready` deltaP `-0.9398` edge `-0.074` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.6966` n `144` status `ready` deltaP `-1.1311` edge `-0.0911` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3847` n `135` status `ready` deltaP `17.1065` edge `0.071` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4341` n `144` status `ready` deltaP `-5.4766` edge `-0.0762` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7985` n `135` status `ready` deltaP `-13.044` edge `-0.0169` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0802` n `144` status `ready` deltaP `-2.4899` edge `-0.1536` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4023` n `135` status `ready` deltaP `-10.6366` edge `-0.0918` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.5804` n `144` status `ready` deltaP `3.6585` edge `-0.2391` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.8321` n `144` status `ready` deltaP `-2.8794` edge `-0.2795` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
