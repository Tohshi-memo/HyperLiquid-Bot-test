# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T07:07:27.694649+00:00`
- Price records: `672`
- Market context records: `5016`
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

- `market_context_high->unknown_1h` score `15.4603` n `93` status `ready` deltaP `4.2673` edge `1.31` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9925` n `93` status `ready` deltaP `21.4496` edge `0.7086` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7475` n `93` status `ready` deltaP `18.0141` edge `0.5173` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3735` n `93` status `ready` deltaP `14.7883` edge `0.4886` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3535` n `93` status `ready` deltaP `14.4587` edge `0.1243` maxDD `-1.9651`
- `market_context_high->unknown_24h` score `1.079` n `74` status `ready` deltaP `27.7309` edge `-0.0607` maxDD `-1.4072`
- `market_context_high->equity_1h` score `0.9471` n `93` status `ready` deltaP `8.9353` edge `0.0767` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8524` n `93` status `ready` deltaP `6.553` edge `0.1191` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5516` n `93` status `ready` deltaP `4.6453` edge `0.1779` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3652` n `93` status `ready` deltaP `6.2536` edge `0.0384` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2147` n `93` status `ready` deltaP `5.5598` edge `0.0927` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0413` n `93` status `ready` deltaP `4.7813` edge `0.0408` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1047` n `74` status `ready` deltaP `8.5164` edge `0.006` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3228` n `93` status `ready` deltaP `1.5582` edge `0.0142` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5071` n `93` status `ready` deltaP `2.8105` edge `0.0131` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7845` n `93` status `ready` deltaP `4.0028` edge `-0.002` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9935` n `93` status `ready` deltaP `-3.9158` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.9461` n `74` status `ready` deltaP `2.9514` edge `0.0199` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.3851` n `74` status `ready` deltaP `3.5379` edge `-0.0749` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
