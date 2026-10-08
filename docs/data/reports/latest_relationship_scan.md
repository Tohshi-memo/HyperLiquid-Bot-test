# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T20:37:42.312385+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8908`

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

- `market_context_high->unknown_4h` score `40.1674` n `91` status `ready` deltaP `-2.2246` edge `3.416` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.632` n `49` status `ready` deltaP `44.3598` edge `0.9236` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.1054` n `49` status `ready` deltaP `45.766` edge `0.8771` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.3998` n `49` status `ready` deltaP `25.2856` edge `0.6247` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.7563` n `90` status `ready` deltaP `21.9122` edge `1.2739` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.7313` n `90` status `ready` deltaP `24.56` edge `0.4401` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.3194` n `49` status `ready` deltaP `45.4073` edge `0.2239` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9793` n `49` status `ready` deltaP `32.3855` edge `0.3029` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5951` n `49` status `ready` deltaP `45.8251` edge `0.0819` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1625` n `49` status `ready` deltaP `12.7612` edge `0.214` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.8123` n `90` status `ready` deltaP `13.6145` edge `0.8636` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.667` n `49` status `ready` deltaP `6.6388` edge `0.2097` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.5191` n `49` status `ready` deltaP `30.9271` edge `0.0122` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4278` n `49` status `ready` deltaP `29.986` edge `0.0164` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `1.9691` n `91` status `ready` deltaP `19.0784` edge `0.2583` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4214` n `90` status `ready` deltaP `23.6453` edge `0.1731` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2496` n `49` status `ready` deltaP `19.3629` edge `0.0727` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6197` n `91` status `ready` deltaP `17.0581` edge `0.0126` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4392` n `91` status `ready` deltaP `8.7929` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3441` n `91` status `ready` deltaP `11.1914` edge `0.0584` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
