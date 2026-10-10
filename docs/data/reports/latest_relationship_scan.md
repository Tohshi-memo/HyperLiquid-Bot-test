# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T08:37:28.259910+00:00`
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

- `market_context_high->unknown_4h` score `40.8727` n `91` status `ready` deltaP `-6.188` edge `3.5012` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6262` n `91` status `ready` deltaP `35.1706` edge `0.6106` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9065` n `91` status `ready` deltaP `19.4832` edge `1.3268` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6194` n `91` status `ready` deltaP `10.0578` edge `0.7518` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3179` n `91` status `ready` deltaP `15.4198` edge `0.1992` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2236` n `91` status `ready` deltaP `6.248` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.161` n `91` status `ready` deltaP `9.2453` edge `0.0479` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1062` n `91` status `ready` deltaP `8.674` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.301` n `91` status `ready` deltaP `9.2502` edge `0.0907` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3098` n `91` status `ready` deltaP `3.5978` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3558` n `91` status `ready` deltaP `6.7172` edge `0.0581` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.4022` n `91` status `ready` deltaP `0.2534` edge `0.0024` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.771` n `91` status `ready` deltaP `-2.5562` edge `-0.0118` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.922` n `91` status `ready` deltaP `-4.4383` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9245` n `91` status `ready` deltaP `-4.7039` edge `0.0136` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-0.9533` n `91` status `ready` deltaP `-4.0682` edge `-0.0108` maxDD `-0.9885`
- `market_context_high->crypto_alt_1h` score `-1.1244` n `91` status `ready` deltaP `-1.7947` edge `0.0321` maxDD `-4.7735`
- `market_context_high->crypto_alt_4h` score `-1.1913` n `91` status `ready` deltaP `-8.4763` edge `0.0971` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.2248` n `91` status `ready` deltaP `-10.1879` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2874` n `91` status `ready` deltaP `-10.8651` edge `0.0006` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
