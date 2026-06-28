# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T12:22:28.234072+00:00`
- Price records: `672`
- Market context records: `5039`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `market_context_high->unknown_1h` score `12.9126` n `98` status `ready` deltaP `3.1559` edge `1.1051` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0633` n `93` status `ready` deltaP `22.3642` edge `0.7084` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4599` n `93` status `ready` deltaP `16.4897` edge `0.5035` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3068` n `93` status `ready` deltaP `14.1785` edge `0.4871` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2026` n `93` status `ready` deltaP `12.7819` edge `0.1229` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8155` n `98` status `ready` deltaP `8.1908` edge `0.0707` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.72` n `98` status `ready` deltaP `6.0827` edge `0.1112` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3742` n `93` status `ready` deltaP `2.3587` edge `0.1704` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3058` n `98` status `ready` deltaP `5.8108` edge `0.0364` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1946` n `98` status `ready` deltaP `5.2792` edge `0.092` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0012` n `74` status `ready` deltaP `10.2525` edge `0.0077` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2324` n `93` status `ready` deltaP `2.6472` edge `0.0391` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.2426` n `98` status `ready` deltaP `2.8168` edge `0.0161` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4056` n `98` status `ready` deltaP `1.4695` edge `0.0123` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7641` n `93` status `ready` deltaP `4.1552` edge `-0.0004` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0173` n `93` status `ready` deltaP `-4.3732` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.5862` n `98` status `ready` deltaP `-9.8497` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.6283` n `74` status `ready` deltaP `6.4236` edge `0.0375` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6956` n `74` status `ready` deltaP `-0.108` edge `-0.0904` maxDD `-27.5371`
- `market_context_high->unknown_24h` score `-5.9678` n `74` status `ready` deltaP `27.0364` edge `-0.6433` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
