# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T06:36:11.943927+00:00`
- Price records: `672`
- Market context records: `5014`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10194`

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

- `market_context_high->unknown_1h` score `15.4351` n `93` status `ready` deltaP `4.1176` edge `1.3089` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9805` n `93` status `ready` deltaP `21.4496` edge `0.7076` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7305` n `93` status `ready` deltaP `17.8616` edge `0.5169` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3409` n `93` status `ready` deltaP `14.6358` edge `0.4869` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `1.7848` n `74` status `ready` deltaP `28.0781` edge `-0.0042` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3669` n `93` status `ready` deltaP `14.6112` edge `0.1244` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9603` n `93` status `ready` deltaP `9.085` edge `0.0768` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8872` n `93` status `ready` deltaP `6.8524` edge `0.12` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5603` n `93` status `ready` deltaP `4.7978` edge `0.178` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3784` n `93` status `ready` deltaP `6.4033` edge `0.0385` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2014` n `93` status `ready` deltaP `5.4101` edge `0.092` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0291` n `93` status `ready` deltaP `4.9338` edge `0.0408` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1145` n `74` status `ready` deltaP `8.3428` edge `0.0059` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3041` n `93` status `ready` deltaP `1.8576` edge `0.0146` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5191` n `93` status `ready` deltaP `2.6608` edge `0.0131` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7845` n `93` status `ready` deltaP `4.0028` edge `-0.002` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.9805` n `74` status `ready` deltaP `2.6042` edge `0.0178` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.3515` n `74` status `ready` deltaP `3.8851` edge `-0.0729` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
