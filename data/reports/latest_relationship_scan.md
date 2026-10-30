# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T19:22:33.209426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7136`

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

- `market_context_high->unknown_24h` score `1592.9614` n `134` status `ready` deltaP `-5.9158` edge `132.8292` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `120.985` n `71` status `ready` deltaP `-1.2989` edge `10.1033` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `30.6432` n `134` status `ready` deltaP `0.5688` edge `2.5631` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `5.8981` n `59` status `ready` deltaP `21.5094` edge `0.4086` maxDD `-3.1722`
- `market_context_high->equity_24h` score `5.3453` n `134` status `ready` deltaP `16.6589` edge `0.6101` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5902` n `134` status `ready` deltaP `35.2638` edge `0.0824` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.178` n `59` status `ready` deltaP `10.2186` edge `0.0638` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.4179` n `134` status `ready` deltaP `11.3527` edge `0.0158` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.4023` n `134` status `ready` deltaP `16.1358` edge `0.0336` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3997` n `134` status `ready` deltaP `5.53` edge `0.084` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2451` n `134` status `ready` deltaP `13.7855` edge `0.0504` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.2067` n `134` status `ready` deltaP `3.3059` edge `0.1629` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.096` n `134` status `ready` deltaP `7.6146` edge `0.06` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `-0.0387` n `71` status `ready` deltaP `2.6777` edge `0.0601` maxDD `-3.9659`
- `market_context_high->fx_1h` score `-0.094` n `134` status `ready` deltaP `3.7291` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.284` n `134` status `ready` deltaP `2.0936` edge `0.0138` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5053` n `134` status `ready` deltaP `-0.3208` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5718` n `71` status `ready` deltaP `-2.1738` edge `0.0171` maxDD `-0.6872`
- `market_context_high->index_1h` score `-0.7839` n `134` status `ready` deltaP `-1.6467` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.847` n `134` status `ready` deltaP `3.2979` edge `0.0559` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
