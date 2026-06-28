# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T07:22:32.432061+00:00`
- Price records: `672`
- Market context records: `5017`
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

- `market_context_high->unknown_1h` score `15.4783` n `93` status `ready` deltaP `4.2673` edge `1.3115` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0117` n `93` status `ready` deltaP `21.4496` edge `0.7102` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7451` n `93` status `ready` deltaP `18.0141` edge `0.5171` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3917` n `93` status `ready` deltaP `14.9407` edge `0.4891` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3523` n `93` status `ready` deltaP `14.4587` edge `0.1242` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9327` n `93` status `ready` deltaP `8.7856` edge `0.0765` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8261` n `93` status `ready` deltaP `6.4033` edge `0.1179` maxDD `-4.6734`
- `market_context_high->unknown_24h` score `0.7459` n `74` status `ready` deltaP `27.5573` edge `-0.0873` maxDD `-1.4072`
- `market_context_high->equity_4h` score `0.5421` n `93` status `ready` deltaP `4.4929` edge `0.1777` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.364` n `93` status `ready` deltaP `6.2536` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2108` n `93` status `ready` deltaP `5.5598` edge `0.0922` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0413` n `93` status `ready` deltaP `4.7813` edge `0.0408` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0949` n `74` status `ready` deltaP `8.69` edge `0.0061` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3322` n `93` status `ready` deltaP `1.4085` edge `0.014` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5203` n `93` status `ready` deltaP `2.6608` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7948` n `93` status `ready` deltaP `3.8503` edge `-0.0023` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9935` n `93` status `ready` deltaP `-3.9158` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7593` n `93` status `ready` deltaP `-11.9986` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.93` n `74` status `ready` deltaP `3.125` edge `0.0208` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.4019` n `74` status `ready` deltaP `3.3643` edge `-0.0759` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
