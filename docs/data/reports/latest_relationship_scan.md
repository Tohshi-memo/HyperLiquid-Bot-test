# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T15:52:25.728176+00:00`
- Price records: `672`
- Market context records: `5678`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `1.9523` n `201` status `ready` deltaP `16.0474` edge `0.5636` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9175` n `251` status `ready` deltaP `11.7044` edge `0.2212` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4582` n `251` status `ready` deltaP `8.7734` edge `0.1607` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.2027` n `251` status `ready` deltaP `5.7387` edge `0.1425` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2364` n `263` status `ready` deltaP `2.4026` edge `0.0013` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4184` n `263` status `ready` deltaP `2.8187` edge `0.0425` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.4777` n `263` status `ready` deltaP `4.618` edge `0.0301` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5835` n `263` status `ready` deltaP `1.0553` edge `0.005` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6067` n `263` status `ready` deltaP `4.4535` edge `0.0443` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7565` n `263` status `ready` deltaP `0.732` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.8883` n `201` status `ready` deltaP `14.8165` edge `0.0483` maxDD `-3.0213`
- `market_context_high->commodity_1h` score `-0.9171` n `263` status `ready` deltaP `0.5584` edge `-0.0036` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1802` n `251` status `ready` deltaP `3.7849` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2618` n `251` status `ready` deltaP `-0.3899` edge `0.008` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5027` n `201` status `ready` deltaP `6.2863` edge `0.0371` maxDD `-16.9893`
- `market_context_high->metal_4h` score `-2.8945` n `251` status `ready` deltaP `-11.9887` edge `-0.0536` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7682` n `251` status `ready` deltaP `-2.139` edge `-0.0322` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7449` n `201` status `ready` deltaP `4.0475` edge `0.0233` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.331` n `201` status `ready` deltaP `-12.6762` edge `-0.249` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.1749` n `201` status `ready` deltaP `-10.8572` edge `-0.0813` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
