# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T05:52:28.594610+00:00`
- Price records: `672`
- Market context records: `5011`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10274`

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

- `market_context_high->unknown_1h` score `15.3752` n `93` status `ready` deltaP `3.6685` edge `1.3069` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6075` n `93` status `ready` deltaP `21.9069` edge `0.7568` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6833` n `93` status `ready` deltaP `17.5568` edge `0.515` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2552` n `93` status `ready` deltaP `14.1785` edge `0.4828` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `2.844` n `74` status `ready` deltaP `28.5989` edge `0.0806` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3547` n `93` status `ready` deltaP `14.4587` edge `0.1244` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9447` n `93` status `ready` deltaP `8.9353` edge `0.0765` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8548` n `93` status `ready` deltaP `6.553` edge `0.1193` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5437` n `93` status `ready` deltaP `4.4929` edge `0.1779` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3772` n `93` status `ready` deltaP `6.4033` edge `0.0384` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1617` n `93` status `ready` deltaP `4.961` edge `0.0899` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0547` n `93` status `ready` deltaP `4.6289` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1243` n `74` status `ready` deltaP `8.1691` edge `0.0058` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.294` n `93` status `ready` deltaP `2.0073` edge `0.0149` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5455` n `93` status `ready` deltaP `2.3614` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.79` n `93` status `ready` deltaP `4.0028` edge `-0.0027` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7461` n `93` status `ready` deltaP `-11.8489` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.0287` n `74` status `ready` deltaP `2.0833` edge `0.0151` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.2979` n `74` status `ready` deltaP `4.4059` edge `-0.0695` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
