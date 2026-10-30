# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T19:52:31.891178+00:00`
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

- `market_context_high->unknown_24h` score `1591.675` n `134` status `ready` deltaP `-5.9158` edge `132.722` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `119.2055` n `73` status `ready` deltaP `-0.9516` edge `9.9527` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.3884` n `134` status `ready` deltaP `0.5688` edge `2.8752` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `5.625` n `61` status `ready` deltaP `20.6067` edge `0.395` maxDD `-3.4234`
- `market_context_high->equity_24h` score `5.5673` n `134` status `ready` deltaP `16.6589` edge `0.6286` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.6106` n `134` status `ready` deltaP `35.2638` edge `0.0841` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `0.9996` n `61` status `ready` deltaP `8.634` edge `0.0595` maxDD `-0.7008`
- `market_context_high->metal_4h` score `0.4031` n `134` status `ready` deltaP `16.1358` edge `0.0337` maxDD `-1.8344`
- `market_context_high->metal_1h` score `0.4` n `134` status `ready` deltaP `11.0533` edge `0.0155` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.3457` n `134` status `ready` deltaP `5.3803` edge `0.0805` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2779` n `134` status `ready` deltaP `14.0903` edge `0.0511` maxDD `-1.0837`
- `news_risk_high->crypto_alt_1h` score `0.2504` n `73` status `ready` deltaP `3.8061` edge `0.0784` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.2122` n `134` status `ready` deltaP `3.3059` edge `0.1636` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.06` n `134` status `ready` deltaP `7.4649` edge `0.058` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1104` n `134` status `ready` deltaP `3.4297` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2661` n `134` status `ready` deltaP `2.2433` edge `0.0143` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4681` n `73` status `ready` deltaP `-3.2975` edge `0.0129` maxDD `-0.7413`
- `market_context_high->fx_4h` score `-0.5061` n `134` status `ready` deltaP `-0.3208` edge `-0.0029` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.7887` n `134` status `ready` deltaP `-1.6467` edge `0.0011` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-0.8135` n `73` status `ready` deltaP `-4.4726` edge `-0.0044` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
