# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T04:22:31.631738+00:00`
- Price records: `672`
- Market context records: `5005`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.3235` n `93` status `ready` deltaP `4.1176` edge `1.2996` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.3785` n `93` status `ready` deltaP `22.6691` edge `0.8993` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7061` n `93` status `ready` deltaP `17.5568` edge `0.5169` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2372` n `93` status `ready` deltaP `14.1785` edge `0.4813` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `4.869` n `74` status `ready` deltaP `29.6406` edge `0.2424` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3157` n `93` status `ready` deltaP `14.0014` edge `0.1242` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8644` n `93` status `ready` deltaP `8.0371` edge `0.0758` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8129` n `93` status `ready` deltaP `6.2536` edge `0.1178` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5002` n `93` status `ready` deltaP `3.7307` edge `0.1774` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3233` n `93` status `ready` deltaP `5.8045` edge `0.0379` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1352` n `93` status `ready` deltaP `4.6616` edge `0.0885` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0803` n `93` status `ready` deltaP `4.324` edge `0.0406` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.153` n `74` status `ready` deltaP `7.6483` edge `0.0056` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2691` n `93` status `ready` deltaP `2.4564` edge `0.0151` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5694` n `93` status `ready` deltaP `2.062` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.797` n `93` status `ready` deltaP `4.0028` edge `-0.0036` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7342` n `93` status `ready` deltaP `-11.6992` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.1055` n `74` status `ready` deltaP `1.0417` edge `0.0122` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.1946` n `74` status `ready` deltaP `5.4476` edge `-0.0632` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
