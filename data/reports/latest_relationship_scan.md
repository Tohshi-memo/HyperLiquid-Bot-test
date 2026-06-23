# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T23:52:34.474475+00:00`
- Price records: `672`
- Market context records: `4567`
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

- `market_context_high->unknown_1h` score `69.939` n `157` status `ready` deltaP `6.7347` edge `5.8334` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.0019` n `157` status `ready` deltaP `7.4549` edge `0.3215` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.4984` n `157` status `ready` deltaP `6.2908` edge `0.0024` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6057` n `157` status `ready` deltaP `1.3988` edge `0.0198` maxDD `-2.0345`
- `market_context_high->equity_1h` score `-0.6793` n `157` status `ready` deltaP `-2.1883` edge `0.0262` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.6811` n `157` status `ready` deltaP `2.1147` edge `0.0755` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.7106` n `157` status `ready` deltaP `-0.0982` edge `-0.0031` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7654` n `157` status `ready` deltaP `3.2633` edge `-0.0076` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1766` n `157` status `ready` deltaP `3.6614` edge `0.0355` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5708` n `157` status `ready` deltaP `-2.8252` edge `-0.0112` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9236` n `157` status `ready` deltaP `-4.1049` edge `-0.0823` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.1674` n `155` status `ready` deltaP `1.5278` edge `-0.1818` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.438` n `157` status `ready` deltaP `-2.3761` edge `-0.1086` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5073` n `155` status `ready` deltaP `-14.0726` edge `-0.0139` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.5982` n `155` status `ready` deltaP `-9.2754` edge `-0.1184` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-5.7549` n `155` status `ready` deltaP `8.3815` edge `0.049` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.6416` n `157` status `ready` deltaP `-5.4874` edge `-0.1416` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.9469` n `157` status `ready` deltaP `-2.8827` edge `-0.2621` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.288` n `157` status `ready` deltaP `-8.8871` edge `-0.338` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.7141` n `157` status `ready` deltaP `-1.7448` edge `-0.3958` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
