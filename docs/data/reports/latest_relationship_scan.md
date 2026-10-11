# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T14:52:25.549969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7318`

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

- `market_context_high->unknown_24h` score `1183.0013` n `42` status `ready` deltaP `-18.2539` edge `98.7415` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `52.8854` n `74` status `ready` deltaP `-7.7291` edge `4.5167` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `10.2675` n `82` status `ready` deltaP `-5.2285` edge `0.9241` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.885` n `42` status `ready` deltaP `29.2658` edge `0.5882` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.82` n `42` status `ready` deltaP `48.1895` edge `0.1736` maxDD `-0.1221`
- `market_context_high->fx_24h` score `3.0837` n `42` status `ready` deltaP `34.9702` edge `0.0375` maxDD `-0.0931`
- `market_context_high->crypto_major_24h` score `2.5766` n `42` status `ready` deltaP `-17.0635` edge `0.6433` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.9758` n `74` status `ready` deltaP `15.0874` edge `0.0091` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.6292` n `74` status `ready` deltaP `13.3899` edge `0.0165` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.0536` n `82` status `ready` deltaP `2.6545` edge `0.0032` maxDD `-0.5546`
- `market_context_high->crypto_alt_1h` score `-0.2638` n `82` status `ready` deltaP `3.4249` edge `0.0586` maxDD `-4.9401`
- `market_context_high->fx_1h` score `-0.2716` n `82` status `ready` deltaP `0.0876` edge `0.001` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.3553` n `82` status `ready` deltaP `4.0018` edge `0.0026` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.4449` n `74` status `ready` deltaP `-0.6098` edge `0.0193` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.8553` n `82` status `ready` deltaP `-0.8982` edge `0.0236` maxDD `-3.7778`
- `market_context_high->index_1h` score `-0.9625` n `82` status `ready` deltaP `-6.9958` edge `-0.0033` maxDD `-0.5437`
- `market_context_high->index_4h` score `-1.0955` n `74` status `ready` deltaP `-10.5266` edge `0.0003` maxDD `-0.9791`
- `market_context_high->equity_1h` score `-1.2734` n `82` status `ready` deltaP `-10.0956` edge `-0.009` maxDD `-2.2898`
- `market_context_high->crypto_major_4h` score `-1.3702` n `74` status `ready` deltaP `-6.1058` edge `0.0756` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.0925` n `74` status `ready` deltaP `-8.7797` edge `0.0461` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
