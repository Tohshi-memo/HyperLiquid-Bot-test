# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T01:52:29.762961+00:00`
- Price records: `672`
- Market context records: `4887`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7592`

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

- `market_context_high->unknown_1h` score `16.0099` n `110` status `ready` deltaP `9.5727` edge `1.3121` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5612` n `110` status `ready` deltaP `23.0099` edge `0.6965` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.457` n `110` status `ready` deltaP `21.3609` edge `0.5309` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.2688` n `110` status `ready` deltaP `18.7971` edge `0.5195` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.0434` n `91` status `ready` deltaP `24.0804` edge `0.294` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1199` n `110` status `ready` deltaP `8.0627` edge `0.1058` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8758` n `110` status `ready` deltaP `12.439` edge `0.1675` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5913` n `110` status `ready` deltaP `12.1452` edge `0.0411` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4726` n `110` status `ready` deltaP `6.4698` edge `0.1213` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4082` n `110` status `ready` deltaP `7.8715` edge `0.1021` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1966` n `110` status `ready` deltaP `3.9358` edge `0.0587` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2025` n `110` status `ready` deltaP `0.2449` edge `0.0304` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2246` n `110` status `ready` deltaP `3.2825` edge `0.0153` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5172` n `110` status `ready` deltaP `-0.2885` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6822` n `110` status `ready` deltaP `0.7622` edge `0.0045` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9266` n `110` status `ready` deltaP `5.6624` edge `0.0037` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3226` n `110` status `ready` deltaP `-6.7175` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7125` n `91` status `ready` deltaP `-4.947` edge `-0.0087` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.515` n `91` status `ready` deltaP `-4.8879` edge `-0.1377` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.8386` n `91` status `ready` deltaP `14.4993` edge `0.011` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
