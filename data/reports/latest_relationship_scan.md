# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T17:52:19.790504+00:00`
- Price records: `672`
- Market context records: `3202`
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

- `market_context_high->crypto_alt_24h` score `16.6199` n `97` status `ready` deltaP `11.9398` edge `2.303` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.6559` n `97` status `ready` deltaP `47.4924` edge `0.8642` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.1038` n `97` status `ready` deltaP `28.0784` edge `0.8508` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3596` n `97` status `ready` deltaP `11.8109` edge `1.3218` maxDD `-53.663`
- `market_context_high->unknown_24h` score `3.8461` n `97` status `ready` deltaP `16.6631` edge `0.6253` maxDD `-17.4635`
- `market_context_high->commodity_4h` score `3.5306` n `129` status `ready` deltaP `23.0727` edge `0.1862` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.9621` n `97` status `ready` deltaP `14.6907` edge `0.005` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6253` n `129` status `ready` deltaP `11.3443` edge `0.1987` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3362` n `135` status `ready` deltaP `5.9969` edge `0.0303` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.6101` n `135` status `ready` deltaP `6.7532` edge `0.1171` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.646` n `135` status `ready` deltaP `5.4214` edge `0.0163` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-0.859` n `135` status `ready` deltaP `5.0188` edge `0.0827` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1734` n `135` status `ready` deltaP `5.2639` edge `0.0157` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.1924` n `129` status `ready` deltaP `-8.7883` edge `-0.0058` maxDD `-1.4115`
- `market_context_high->index_4h` score `-1.4305` n `129` status `ready` deltaP `15.5996` edge `0.0677` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7194` n `135` status `ready` deltaP `-10.4258` edge `-0.0051` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-1.9614` n `135` status `ready` deltaP `-2.5926` edge `-0.0068` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6742` n `135` status `ready` deltaP `1.8053` edge `-0.1181` maxDD `-16.9424`
- `market_context_high->crypto_alt_4h` score `-2.8868` n `129` status `ready` deltaP `14.3376` edge `0.3388` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.1102` n `129` status `ready` deltaP `8.058` edge `0.2117` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
