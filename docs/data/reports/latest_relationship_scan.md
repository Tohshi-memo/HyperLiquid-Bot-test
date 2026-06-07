# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T22:22:23.980957+00:00`
- Price records: `672`
- Market context records: `3221`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->commodity_24h` score `13.8706` n `102` status `ready` deltaP `49.5609` edge `0.8683` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.8459` n `102` status `ready` deltaP `16.6361` edge `2.5263` maxDD `-70.5576`
- `market_context_high->index_24h` score `9.5721` n `102` status `ready` deltaP `30.9334` edge `0.8469` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.9472` n `102` status `ready` deltaP `16.7076` edge `1.4927` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4447` n `128` status `ready` deltaP `23.5137` edge `0.1761` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.3668` n `140` status `ready` deltaP `6.5441` edge `0.0292` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.8124` n `102` status `ready` deltaP `0.674` edge `-0.014` maxDD `-1.5717`
- `market_context_high->crypto_major_24h` score `-0.8839` n `102` status `ready` deltaP `18.2291` edge `1.95` maxDD `-159.1216`
- `market_context_high->unknown_4h` score `-0.889` n `128` status `ready` deltaP `6.9741` edge `0.0661` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.8962` n `140` status `ready` deltaP `3.3747` edge `0.0091` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-1.0041` n `140` status `ready` deltaP `3.2592` edge `0.075` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-1.0875` n `140` status `ready` deltaP `3.4303` edge `0.064` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.6248` n `140` status `ready` deltaP `2.6262` edge `0.004` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.7902` n `140` status `ready` deltaP `-11.2104` edge `-0.0054` maxDD `-0.8572`
- `market_context_high->fx_4h` score `-1.89` n `128` status `ready` deltaP `-9.1082` edge `-0.0083` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.9755` n `128` status `ready` deltaP `11.5473` edge `0.0493` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.3456` n `140` status `ready` deltaP `-4.5509` edge `-0.0156` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.9703` n `140` status `ready` deltaP `0.9581` edge `-0.1393` maxDD `-17.8311`
- `market_context_high->crypto_alt_4h` score `-4.5894` n `128` status `ready` deltaP `7.6792` edge `0.1649` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-5.0545` n `128` status `ready` deltaP `2.8963` edge `0.1235` maxDD `-54.2659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
