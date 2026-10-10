# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T03:52:32.686289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8811` n `91` status `ready` deltaP `-6.188` edge `3.5019` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3993` n `91` status `ready` deltaP `33.2641` edge `0.6044` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7058` n `91` status `ready` deltaP `18.4433` edge `1.308` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6561` n `91` status `ready` deltaP `10.0578` edge `0.7565` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5229` n `91` status `ready` deltaP `18.0113` edge `0.2082` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.238` n `91` status `ready` deltaP `6.3977` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2358` n `91` status `ready` deltaP `10.2932` edge `0.0505` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0937` n `91` status `ready` deltaP `11.113` edge `0.0084` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.2956` n `91` status `ready` deltaP `1.451` edge `0.0033` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3469` n `91` status `ready` deltaP `3.1487` edge `0.0013` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3539` n `91` status `ready` deltaP `6.5439` edge `0.0595` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3731` n `91` status `ready` deltaP `7.8638` edge `0.0907` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6523` n `91` status `ready` deltaP `-0.5745` edge `-0.0098` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9064` n `91` status `ready` deltaP `-4.1389` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->unknown_1h` score `-0.9798` n `91` status `ready` deltaP `-3.9185` edge `-0.014` maxDD `-0.9885`
- `market_context_high->metal_4h` score `-1.0219` n `91` status `ready` deltaP `-6.5331` edge `0.0133` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0345` n `91` status `ready` deltaP `-7.5617` edge `0.1111` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1879` n `91` status `ready` deltaP `-2.3935` edge `0.0308` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.21` n `91` status `ready` deltaP `-9.8885` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2304` n `91` status `ready` deltaP `-9.798` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
