# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T16:52:29.017342+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7332`

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

- `market_context_high->unknown_24h` score `1381.2885` n `40` status `ready` deltaP `-20.1389` edge `115.278` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `51.4567` n `77` status `ready` deltaP `-7.1389` edge `4.3937` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `11.3521` n `88` status `ready` deltaP `-3.5656` edge `1.0034` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.82` n `40` status `ready` deltaP `27.6736` edge `0.5934` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3856` n `40` status `ready` deltaP `52.4306` edge `0.1826` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3657` n `40` status `ready` deltaP `37.9861` edge `0.0402` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6729` n `40` status `ready` deltaP `-20.5903` edge `0.5915` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7826` n `77` status `ready` deltaP `12.8069` edge `0.0082` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.7104` n `88` status `ready` deltaP `7.0223` edge `0.1158` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.4798` n `77` status `ready` deltaP `11.8982` edge `0.014` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.0374` n `88` status `ready` deltaP `3.9126` edge `0.0054` maxDD `-0.6025`
- `market_context_high->crypto_major_1h` score `-0.0229` n `88` status `ready` deltaP `1.9121` edge `0.0732` maxDD `-3.7778`
- `market_context_high->fx_1h` score `-0.2061` n `88` status `ready` deltaP `0.8914` edge `0.0011` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.2091` n `88` status `ready` deltaP `5.709` edge `0.0034` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.2625` n `77` status `ready` deltaP `2.8687` edge `0.0195` maxDD `-1.1153`
- `market_context_high->index_1h` score `-0.6679` n `88` status `ready` deltaP `-2.7831` edge `-0.002` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.8883` n `77` status `ready` deltaP `-6.8321` edge `0.0017` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-0.9058` n `77` status `ready` deltaP `-3.7892` edge `0.1197` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.0176` n `88` status `ready` deltaP `-6.5868` edge `0.0004` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.017` n `77` status `ready` deltaP `-7.131` edge `0.1353` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
