# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T18:22:23.008488+00:00`
- Price records: `672`
- Market context records: `3205`
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

- `market_context_high->crypto_alt_24h` score `16.9619` n `97` status `ready` deltaP `11.9398` edge `2.3315` maxDD `-71.142`
- `market_context_high->commodity_24h` score `13.6895` n `97` status `ready` deltaP `47.4924` edge `0.867` maxDD `-2.0927`
- `market_context_high->index_24h` score `6.0664` n `97` status `ready` deltaP `28.0784` edge `0.846` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5109` n `97` status `ready` deltaP `11.8109` edge `1.3412` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4451` n `127` status `ready` deltaP `22.6943` edge `0.1816` maxDD `-1.9973`
- `market_context_high->unknown_24h` score `1.6491` n `97` status `ready` deltaP `14.9485` edge `0.4723` maxDD `-26.8429`
- `market_context_high->fx_24h` score `0.7769` n `97` status `ready` deltaP `12.9761` edge `0.001` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.6194` n `127` status `ready` deltaP `11.1364` edge `0.1996` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.2913` n `135` status `ready` deltaP `5.4059` edge `0.0305` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.6873` n `135` status `ready` deltaP `6.1621` edge `0.1146` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.7694` n `135` status `ready` deltaP `4.2393` edge `0.0139` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-0.8197` n `135` status `ready` deltaP `5.6099` edge `0.0838` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0861` n `135` status `ready` deltaP `-9.8348` edge `-0.005` maxDD `-0.8278`
- `market_context_high->fx_4h` score `-1.1671` n `127` status `ready` deltaP `-8.3181` edge `-0.0057` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.3016` n `135` status `ready` deltaP `4.0818` edge `0.0129` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.4709` n `127` status `ready` deltaP `15.3795` edge `0.0658` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.0159` n `135` status `ready` deltaP `-3.1836` edge `-0.0074` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6832` n `135` status `ready` deltaP `1.8053` edge `-0.1182` maxDD `-17.0266`
- `market_context_high->crypto_alt_4h` score `-3.0726` n `127` status `ready` deltaP `13.6295` edge `0.3197` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.276` n `127` status `ready` deltaP `7.1791` edge `0.1963` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
