# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T15:52:28.757655+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7887`

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

- `market_context_high->unknown_4h` score `40.2811` n `91` status `ready` deltaP `-5.2734` edge `3.4458` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.3168` n `91` status `ready` deltaP `34.728` edge `0.6711` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.2371` n `91` status `ready` deltaP `21.1443` edge `1.3581` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.8616` n `91` status `ready` deltaP `12.9312` edge `0.8919` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.8119` n `91` status `ready` deltaP `18.4686` edge `0.2422` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3902` n `91` status `ready` deltaP `10.892` edge `0.0663` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2847` n `91` status `ready` deltaP `6.9965` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2704` n `91` status `ready` deltaP `13.2472` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.257` n `91` status `ready` deltaP `11.8266` edge `0.1026` maxDD `-3.5466`
- `market_context_high->crypto_alt_4h` score `-0.2033` n `91` status `ready` deltaP `-5.1227` edge `0.2014` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2367` n `91` status `ready` deltaP `4.1966` edge `0.0035` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2417` n `91` status `ready` deltaP `8.9954` edge `0.1` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.546` n `91` status `ready` deltaP `-0.6448` edge `-0.0036` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.6878` n `91` status `ready` deltaP `-0.5971` edge `0.0605` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.7818` n `91` status `ready` deltaP `-2.4922` edge `0.0004` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9104` n `91` status `ready` deltaP `-4.7039` edge `0.0154` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.9188` n `91` status `ready` deltaP `-3.0136` edge `-0.0277` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.1485` n `91` status `ready` deltaP `-8.8406` edge `-0.0021` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.1899` n `91` status `ready` deltaP `-3.2866` edge `0.0163` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.1964` n `91` status `ready` deltaP `-9.3407` edge `0.0021` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
