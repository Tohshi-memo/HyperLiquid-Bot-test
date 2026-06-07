# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T18:07:30.238953+00:00`
- Price records: `672`
- Market context records: `3203`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10906`

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

- `market_context_high->crypto_alt_24h` score `16.8287` n `97` status `ready` deltaP `11.9398` edge `2.3204` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.6715` n `97` status `ready` deltaP `47.4924` edge `0.8655` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.0913` n `97` status `ready` deltaP `28.0784` edge `0.8492` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4344` n `97` status `ready` deltaP `11.8109` edge `1.3314` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4832` n `128` status `ready` deltaP `22.8849` edge `0.1835` maxDD `-1.9973`
- `market_context_high->unknown_24h` score `2.722` n `97` status `ready` deltaP `15.8058` edge `0.5457` maxDD `-22.1678`
- `market_context_high->fx_24h` score `0.8719` n `97` status `ready` deltaP `13.8334` edge `0.0032` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6339` n `128` status `ready` deltaP `11.2424` edge `0.2001` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.2865` n `135` status `ready` deltaP `5.4059` edge `0.0301` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.6137` n `135` status `ready` deltaP `6.7532` edge `0.1168` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.7041` n `135` status `ready` deltaP `4.8303` edge `0.0154` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-0.8166` n `135` status `ready` deltaP `5.6099` edge `0.0842` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1842` n `128` status `ready` deltaP `-8.6318` edge `-0.0058` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.2339` n `135` status `ready` deltaP `4.6729` edge `0.0146` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.4511` n `128` status `ready` deltaP `15.4916` edge `0.0667` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.671` n `135` status `ready` deltaP `-9.8348` edge `-0.005` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-1.9626` n `135` status `ready` deltaP `-2.5926` edge `-0.0069` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.684` n `135` status `ready` deltaP `1.8053` edge `-0.1183` maxDD `-17.0266`
- `market_context_high->crypto_alt_4h` score `-2.9713` n `128` status `ready` deltaP `13.9863` edge `0.3303` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.1867` n `128` status `ready` deltaP `7.622` edge `0.2048` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
