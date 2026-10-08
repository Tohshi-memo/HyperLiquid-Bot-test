# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T23:37:27.738784+00:00`
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

- `market_context_high->unknown_4h` score `39.7982` n `91` status `ready` deltaP `-3.749` edge `3.3954` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.047` n `49` status `ready` deltaP `42.9878` edge `0.884` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6332` n `49` status `ready` deltaP `44.394` edge `0.8469` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.4158` n `49` status `ready` deltaP `27.3653` edge `0.6955` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.1213` n `90` status `ready` deltaP `21.9122` edge `1.3207` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.7473` n `90` status `ready` deltaP `26.6397` edge `0.5109` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.6478` n `49` status `ready` deltaP `47.487` edge `0.2374` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8773` n `49` status `ready` deltaP `32.3855` edge `0.2944` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5551` n `49` status `ready` deltaP `45.5202` edge `0.0806` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `2.9911` n `49` status `ready` deltaP `11.4139` edge `0.2087` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.973` n `90` status `ready` deltaP `13.6145` edge `0.8842` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.5124` n `49` status `ready` deltaP `5.5909` edge `0.2038` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4266` n `49` status `ready` deltaP `29.986` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.2275` n `49` status `ready` deltaP `29.3673` edge `-0.0017` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6622` n `91` status `ready` deltaP `17.7064` edge `0.2281` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3162` n `90` status `ready` deltaP `22.4321` edge `0.1677` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2165` n `49` status `ready` deltaP `18.9055` edge `0.0715` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5819` n `91` status `ready` deltaP `16.6008` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4643` n `91` status `ready` deltaP `9.0923` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2327` n `91` status `ready` deltaP `9.8441` edge `0.0531` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
