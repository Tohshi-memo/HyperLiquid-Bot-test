# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T00:07:25.351070+00:00`
- Price records: `672`
- Market context records: `4568`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.8922` n `157` status `ready` deltaP `6.585` edge `5.8305` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.9705` n `157` status `ready` deltaP `7.3025` edge `0.3199` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5072` n `157` status `ready` deltaP `6.1383` edge `0.0023` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5925` n `157` status `ready` deltaP `1.5485` edge `0.0199` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.685` n `157` status `ready` deltaP `2.1147` edge `0.075` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.6863` n `157` status `ready` deltaP `-2.1883` edge `0.0253` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.7226` n `157` status `ready` deltaP `-0.2479` edge `-0.0031` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7756` n `157` status `ready` deltaP `3.1109` edge `-0.0079` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1751` n `157` status `ready` deltaP `3.6614` edge `0.0357` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5864` n `157` status `ready` deltaP `-2.9749` edge `-0.0115` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9252` n `157` status `ready` deltaP `-4.1049` edge `-0.0825` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.1554` n `155` status `ready` deltaP `1.5278` edge `-0.1808` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.4608` n `157` status `ready` deltaP `-2.5258` edge `-0.1095` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4899` n `155` status `ready` deltaP `-13.899` edge `-0.0136` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.5697` n `155` status `ready` deltaP `-9.1017` edge `-0.1159` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-5.7645` n `155` status `ready` deltaP `8.3815` edge `0.0482` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.6632` n `157` status `ready` deltaP `-5.6371` edge `-0.1424` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.9611` n `157` status `ready` deltaP `-3.0352` edge `-0.2629` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.288` n `157` status `ready` deltaP `-8.8871` edge `-0.338` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.7314` n `157` status `ready` deltaP `-1.8973` edge `-0.397` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
