# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T18:07:51.923460+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8914`

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

- `market_context_high->unknown_4h` score `40.2094` n `91` status `ready` deltaP `-2.2246` edge `3.4195` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.3714` n `49` status `ready` deltaP `44.2073` edge `0.9029` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.924` n `49` status `ready` deltaP `45.6135` edge `0.863` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.3971` n `49` status `ready` deltaP `23.5525` edge `0.5527` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.0203` n `90` status `ready` deltaP `20.1791` edge `1.1911` maxDD `-16.7906`
- `news_risk_high->index_24h` score `6.0163` n `49` status `ready` deltaP `43.6742` edge `0.2102` maxDD `0.0`
- `market_context_high->equity_24h` score `5.7287` n `90` status `ready` deltaP `22.8269` edge `0.3681` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `5.5842` n `49` status `ready` deltaP `31.166` edge `0.2781` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.4471` n `49` status `ready` deltaP `44.6055` edge `0.0777` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2848` n `49` status `ready` deltaP `13.0606` edge `0.2222` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `2.8582` n `49` status `ready` deltaP `32.6602` edge `0.0289` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.8397` n `49` status `ready` deltaP `7.0879` edge `0.2211` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.423` n `49` status `ready` deltaP `29.986` edge `0.016` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `2.0771` n `90` status `ready` deltaP `11.8814` edge `0.7809` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8512` n `91` status `ready` deltaP `18.9259` edge `0.2442` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4993` n `90` status `ready` deltaP `24.5118` edge `0.1773` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2291` n `49` status `ready` deltaP `19.058` edge `0.0721` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5649` n `91` status `ready` deltaP `16.4484` edge `0.0121` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5146` n `91` status `ready` deltaP `9.6911` edge `0.0025` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.4237` n `91` status `ready` deltaP `11.4908` edge `0.0666` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
