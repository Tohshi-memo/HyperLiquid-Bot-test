# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T01:52:26.879138+00:00`
- Price records: `672`
- Market context records: `4576`
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

- `market_context_high->unknown_1h` score `69.927` n `157` status `ready` deltaP `6.585` edge `5.8334` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.2229` n `157` status `ready` deltaP `7.6074` edge `0.3389` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5571` n `157` status `ready` deltaP `5.2237` edge `0.002` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.644` n `157` status `ready` deltaP `0.9497` edge `0.0196` maxDD `-2.0345`
- `market_context_high->equity_1h` score `-0.7105` n `157` status `ready` deltaP `-2.1883` edge `0.0222` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.7193` n `157` status `ready` deltaP `2.1147` edge `0.0706` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.737` n `157` status `ready` deltaP `-0.3976` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8285` n `157` status `ready` deltaP `2.3487` edge `-0.0096` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1837` n `157` status `ready` deltaP `3.6614` edge `0.0346` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5924` n `157` status `ready` deltaP `-2.9749` edge `-0.012` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.8302` n `155` status `ready` deltaP `1.5278` edge `-0.1537` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9307` n `157` status `ready` deltaP `-4.2546` edge `-0.0822` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.3723` n `155` status `ready` deltaP `-7.8865` edge `-0.0987` maxDD `-29.3321`
- `market_context_high->fx_24h` score `-5.3801` n `155` status `ready` deltaP `-12.8573` edge `-0.0114` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5279` n `157` status `ready` deltaP `-2.8252` edge `-0.1131` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8545` n `155` status `ready` deltaP `8.3815` edge `0.0407` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7758` n `157` status `ready` deltaP `-6.3856` edge `-0.1468` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0663` n `157` status `ready` deltaP `-3.9498` edge `-0.2703` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2351` n `157` status `ready` deltaP `-8.1249` edge `-0.3363` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.8812` n `157` status `ready` deltaP `-2.9644` edge `-0.4091` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
