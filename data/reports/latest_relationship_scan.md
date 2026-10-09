# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T00:07:31.599447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8152` n `91` status `ready` deltaP `-3.5965` edge `3.3958` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.0276` n `49` status `ready` deltaP `42.8354` edge `0.8834` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6162` n `49` status `ready` deltaP `44.2416` edge `0.8465` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.5959` n `49` status `ready` deltaP `27.7119` edge `0.7082` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.2001` n `90` status `ready` deltaP `21.9122` edge `1.3308` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.9274` n `90` status `ready` deltaP `26.9863` edge `0.5236` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7031` n `49` status `ready` deltaP `47.8336` edge `0.2397` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8591` n `49` status `ready` deltaP `32.233` edge `0.2939` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5417` n `49` status `ready` deltaP `45.3677` edge `0.0805` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0282` n `49` status `ready` deltaP `11.7133` edge `0.2098` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.0268` n `90` status `ready` deltaP `13.6145` edge `0.8911` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.5327` n `49` status `ready` deltaP `5.7406` edge `0.2045` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4278` n `49` status `ready` deltaP `29.986` edge `0.0164` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1873` n `49` status `ready` deltaP `29.194` edge `-0.0039` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6512` n `91` status `ready` deltaP `17.554` edge `0.2277` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.2881` n `90` status `ready` deltaP `22.0855` edge `0.1664` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1913` n `49` status `ready` deltaP `18.6007` edge `0.0703` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5685` n `91` status `ready` deltaP `16.4484` edge `0.0124` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4392` n `91` status `ready` deltaP `8.7929` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2569` n `91` status `ready` deltaP `10.1435` edge `0.0542` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
