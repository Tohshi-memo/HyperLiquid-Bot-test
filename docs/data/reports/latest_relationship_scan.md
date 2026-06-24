# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T04:07:27.957296+00:00`
- Price records: `672`
- Market context records: `4585`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9993`

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

- `market_context_high->unknown_1h` score `70.4526` n `156` status `ready` deltaP `6.6598` edge `5.8767` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.6766` n `156` status `ready` deltaP `8.3138` edge `0.372` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.6229` n `156` status `ready` deltaP `1.0939` edge `0.0204` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.6351` n `156` status `ready` deltaP `3.8422` edge `0.0012` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.8031` n `156` status `ready` deltaP `-1.1938` edge `-0.0035` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8209` n `156` status `ready` deltaP `2.5406` edge `-0.0099` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8727` n `156` status `ready` deltaP `-2.2033` edge `0.0015` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.1628` n `156` status `ready` deltaP `1.8371` edge `0.0156` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1697` n `156` status `ready` deltaP `3.9595` edge `0.0344` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5975` n `156` status `ready` deltaP `-3.1437` edge `-0.0113` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.4233` n `154` status `ready` deltaP `1.9187` edge `-0.1224` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.8965` n `156` status `ready` deltaP `-3.6734` edge `-0.0817` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.1922` n `154` status `ready` deltaP `-6.6423` edge `-0.0839` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.2688` n `154` status `ready` deltaP `-11.7514` edge `-0.0095` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.4086` n `156` status `ready` deltaP `-1.9039` edge `-0.1093` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.711` n `154` status `ready` deltaP `8.6873` edge `0.0392` maxDD `-33.176`
- `market_context_high->crypto_major_1h` score `-6.6984` n `156` status `ready` deltaP `-5.7923` edge `-0.1443` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0182` n `156` status `ready` deltaP `-3.3537` edge `-0.2681` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1766` n `156` status `ready` deltaP `-7.149` edge `-0.3353` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.9447` n `156` status `ready` deltaP `-3.5999` edge `-0.413` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
