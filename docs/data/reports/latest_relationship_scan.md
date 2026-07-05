# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T02:07:26.213082+00:00`
- Price records: `672`
- Market context records: `5726`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9474` n `218` status `ready` deltaP `16.2239` edge `0.5212` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1535` n `276` status `ready` deltaP `7.253` edge `0.1283` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2295` n `285` status `ready` deltaP `2.6363` edge `0.0011` maxDD `-0.5144`
- `market_context_high->crypto_major_4h` score `-0.327` n `276` status `ready` deltaP `8.5078` edge `0.1737` maxDD `-14.2803`
- `market_context_high->metal_1h` score `-0.4549` n `285` status `ready` deltaP `1.4855` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6238` n `285` status `ready` deltaP `3.212` edge `0.0273` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.759` n `285` status `ready` deltaP `-1.7381` edge `-0.005` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.88` n `285` status `ready` deltaP `2.6316` edge `0.0326` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-1.0246` n `285` status `ready` deltaP `0.8867` edge `0.0291` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1302` n `218` status `ready` deltaP `10.6875` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1377` n `276` status `ready` deltaP `1.7961` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2552` n `276` status `ready` deltaP `2.671` edge `0.0058` maxDD `-1.4288`
- `market_context_high->crypto_alt_4h` score `-1.7924` n `276` status `ready` deltaP `6.3539` edge `0.1219` maxDD `-16.7569`
- `market_context_high->metal_4h` score `-2.5922` n `276` status `ready` deltaP `-6.8045` edge `-0.0494` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.9158` n `218` status `ready` deltaP `1.7473` edge `0.029` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8326` n `276` status `ready` deltaP `-3.4398` edge `-0.0289` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3797` n `218` status `ready` deltaP `7.0225` edge `0.0339` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5994` n `218` status `ready` deltaP `-6.7342` edge `-0.2409` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.4265` n `218` status `ready` deltaP `-10.0535` edge `-0.0712` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
