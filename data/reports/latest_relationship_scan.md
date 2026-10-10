# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T23:37:28.970130+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5511`

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

- `market_context_high->unknown_4h` score `39.9942` n `91` status `ready` deltaP `-7.2551` edge `3.4351` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0679` n `91` status `ready` deltaP `38.5474` edge `0.6249` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3817` n `91` status `ready` deltaP `20.9707` edge `1.3778` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.4991` n `91` status `ready` deltaP `17.554` edge `0.2082` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.0183` n `91` status `ready` deltaP `10.1534` edge `0.6741` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2233` n `91` status `ready` deltaP `10.1435` edge `0.0499` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1649` n `91` status `ready` deltaP `5.4995` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0169` n `91` status `ready` deltaP `10.1984` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.3076` n `91` status `ready` deltaP `9.169` edge `0.0904` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3231` n `91` status `ready` deltaP `1.0019` edge `0.004` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3696` n `91` status `ready` deltaP `2.8493` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3899` n `91` status `ready` deltaP `6.271` edge `0.0567` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6482` n `91` status `ready` deltaP `-1.1843` edge `-0.0052` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9367` n `91` status `ready` deltaP `-4.7377` edge `-0.0045` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9772` n `91` status `ready` deltaP `-6.1897` edge `0.1093` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9799` n `91` status `ready` deltaP `-5.7709` edge `0.0136` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.115` n `91` status `ready` deltaP `-8.0921` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1699` n `91` status `ready` deltaP `-2.2438` edge `0.0313` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.1932` n `91` status `ready` deltaP `-9.1883` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2501` n `91` status `ready` deltaP `-3.439` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
