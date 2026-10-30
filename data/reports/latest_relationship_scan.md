# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T19:42:09.889505+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7148`

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

- `market_context_high->unknown_24h` score `1590.2002` n `134` status `ready` deltaP `-5.9158` edge `132.5991` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `120.0378` n `72` status `ready` deltaP `-1.1228` edge `10.0232` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.52` n `134` status `ready` deltaP `0.5688` edge `2.7195` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `5.6397` n `60` status `ready` deltaP `20.2947` edge `0.3983` maxDD `-3.4234`
- `market_context_high->equity_24h` score `5.4581` n `134` status `ready` deltaP `16.6589` edge `0.6195` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5998` n `134` status `ready` deltaP `35.2638` edge `0.0832` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.0965` n `60` status `ready` deltaP `9.4106` edge `0.0624` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.4093` n `134` status `ready` deltaP `11.203` edge `0.0157` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.4038` n `134` status `ready` deltaP `16.1358` edge `0.0338` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3709` n `134` status `ready` deltaP `5.3803` edge `0.0826` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2609` n `134` status `ready` deltaP `13.9379` edge `0.0507` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.2122` n `134` status `ready` deltaP `3.3059` edge `0.1636` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.09` n `134` status `ready` deltaP `7.6146` edge `0.0595` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.0302` n `72` status `ready` deltaP `3.2518` edge `0.0651` maxDD `-3.9659`
- `market_context_high->fx_1h` score `-0.1018` n `134` status `ready` deltaP `3.5794` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2685` n `134` status `ready` deltaP `2.2433` edge `0.0141` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4099` n `72` status `ready` deltaP `-2.6697` edge `0.0155` maxDD `-0.6872`
- `market_context_high->fx_4h` score `-0.5061` n `134` status `ready` deltaP `-0.3208` edge `-0.0029` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.7851` n `134` status `ready` deltaP `-1.6467` edge `0.0014` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-0.8451` n `72` status `ready` deltaP `-5.0649` edge `-0.0045` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
