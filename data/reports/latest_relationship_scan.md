# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T22:45:14.377669+00:00`
- Price records: `672`
- Market context records: `4561`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `66.717` n `157` status `ready` deltaP `6.7347` edge `5.5649` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.1479` n `157` status `ready` deltaP `8.0647` edge `0.3296` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5072` n `157` status `ready` deltaP `6.1383` edge `0.0023` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6332` n `157` status `ready` deltaP `1.0994` edge `0.0195` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.6922` n `157` status `ready` deltaP `1.9623` edge `0.0751` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.7042` n `157` status `ready` deltaP `-2.4877` edge `0.025` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.7094` n `157` status `ready` deltaP `-0.0982` edge `-0.003` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7369` n `157` status `ready` deltaP `3.7207` edge `-0.007` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1798` n `157` status `ready` deltaP `3.6614` edge `0.0351` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5588` n `157` status `ready` deltaP `-2.6755` edge `-0.0112` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9369` n `157` status `ready` deltaP `-4.2546` edge `-0.083` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.2226` n `155` status `ready` deltaP `1.5278` edge `-0.1864` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.4812` n `157` status `ready` deltaP `-2.6755` edge `-0.1102` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5821` n `155` status `ready` deltaP `-14.767` edge `-0.0155` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.7165` n `155` status `ready` deltaP `8.3815` edge `0.0522` maxDD `-34.0892`
- `market_context_high->index_24h` score `-5.7225` n `155` status `ready` deltaP `-9.9698` edge `-0.1297` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.644` n `157` status `ready` deltaP `-5.4874` edge `-0.1418` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.8785` n `157` status `ready` deltaP `-2.273` edge `-0.2574` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3117` n `157` status `ready` deltaP `-9.1919` edge `-0.339` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.6418` n `157` status `ready` deltaP `-1.1351` edge `-0.3906` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
