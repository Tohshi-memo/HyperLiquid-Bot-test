# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T22:07:31.351629+00:00`
- Price records: `672`
- Market context records: `4558`
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

- `market_context_high->unknown_1h` score `62.9491` n `157` status `ready` deltaP `6.2856` edge `5.2539` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.3248` n `157` status `ready` deltaP `8.522` edge `0.3413` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5151` n `157` status `ready` deltaP `5.9859` edge `0.0023` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6584` n `157` status `ready` deltaP `0.8` edge `0.0194` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7111` n `157` status `ready` deltaP `1.6574` edge `0.0747` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.7179` n `157` status `ready` deltaP `4.0255` edge `-0.0066` maxDD `-5.9823`
- `market_context_high->fx_1h` score `-0.7226` n `157` status `ready` deltaP `-0.2479` edge `-0.0031` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.7276` n `157` status `ready` deltaP `-2.7871` edge `0.024` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1718` n `157` status `ready` deltaP `3.8139` edge `0.0351` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5588` n `157` status `ready` deltaP `-2.6755` edge `-0.0112` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9587` n `157` status `ready` deltaP `-4.554` edge `-0.0838` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.2142` n `155` status `ready` deltaP `1.5278` edge `-0.1857` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.5051` n `157` status `ready` deltaP `-2.8252` edge `-0.1112` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5917` n `155` status `ready` deltaP `-14.767` edge `-0.0163` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.6925` n `155` status `ready` deltaP `8.3815` edge `0.0542` maxDD `-34.0892`
- `market_context_high->index_24h` score `-5.8159` n `155` status `ready` deltaP `-10.4906` edge `-0.1382` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.6572` n `157` status `ready` deltaP `-5.6371` edge `-0.1419` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.822` n `157` status `ready` deltaP `-1.8156` edge `-0.2532` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3251` n `157` status `ready` deltaP `-9.3444` edge `-0.3397` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.5946` n `157` status `ready` deltaP `-0.6778` edge `-0.3876` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
