# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T00:22:24.278670+00:00`
- Price records: `672`
- Market context records: `5719`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8892`

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

- `market_context_high->crypto_major_4h` score `1.4615` n `269` status `ready` deltaP `9.9771` edge `0.201` maxDD `-7.3245`
- `market_context_high->equity_24h` score `1.0429` n `218` status `ready` deltaP `17.2655` edge `0.5265` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.2436` n `269` status `ready` deltaP `7.72` edge `0.1327` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.072` n `269` status `ready` deltaP `7.1851` edge `0.1426` maxDD `-9.7203`
- `market_context_high->fx_1h` score `-0.1734` n `281` status `ready` deltaP `3.6999` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4382` n `281` status `ready` deltaP `1.7906` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4938` n `281` status `ready` deltaP `2.9317` edge `0.0349` maxDD `-3.9811`
- `market_context_high->index_1h` score `-0.6035` n `281` status `ready` deltaP `0.8359` edge `0.0039` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6101` n `281` status `ready` deltaP `3.2929` edge `0.0279` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7578` n `281` status `ready` deltaP `-1.6409` edge `-0.0055` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.8064` n `281` status `ready` deltaP `0.9856` edge `0.0299` maxDD `-4.6273`
- `market_context_high->fx_24h` score `-1.1121` n `218` status `ready` deltaP `11.0347` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1685` n `269` status `ready` deltaP `1.1889` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2615` n `269` status `ready` deltaP `2.5501` edge `0.0058` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6126` n `269` status `ready` deltaP `-7.1233` edge `-0.0499` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8424` n `218` status `ready` deltaP `2.9626` edge `0.0303` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8737` n `269` status `ready` deltaP `-4.0133` edge `-0.0285` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2878` n `218` status `ready` deltaP `7.1961` edge `0.0404` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5019` n `218` status `ready` deltaP `-5.5189` edge `-0.2365` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3073` n `218` status `ready` deltaP `-9.3591` edge `-0.0659` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
