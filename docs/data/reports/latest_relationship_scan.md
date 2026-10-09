# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T19:52:29.200427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7791`

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

- `market_context_high->unknown_4h` score `40.9063` n `91` status `ready` deltaP `-4.3889` edge `3.492` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7701` n `91` status `ready` deltaP `33.2641` edge `0.6353` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.4835` n `91` status `ready` deltaP `18.4433` edge `1.2795` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.733` n `91` status `ready` deltaP `10.2311` edge `0.7652` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5121` n `91` status `ready` deltaP `18.0892` edge `0.2063` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.299` n `91` status `ready` deltaP `7.1462` edge `0.0015` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.285` n `91` status `ready` deltaP `10.2932` edge `0.0568` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2022` n `91` status `ready` deltaP `12.4091` edge `0.0088` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0343` n `91` status `ready` deltaP `10.5301` edge `0.0827` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3301` n `91` status `ready` deltaP `3.4481` edge `0.0007` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3327` n `91` status `ready` deltaP `1.1516` edge `0.0022` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3427` n `91` status `ready` deltaP `7.8638` edge `0.0946` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.7606` n `91` status `ready` deltaP `-1.8616` edge `-0.0151` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.876` n `91` status `ready` deltaP `-3.5401` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.8857` n `91` status `ready` deltaP `-1.3456` edge `0.049` maxDD `-4.7735`
- `market_context_high->crypto_alt_4h` score `-0.9042` n `91` status `ready` deltaP `-7.1705` edge `0.1252` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9594` n `91` status `ready` deltaP `-5.2403` edge `0.0127` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2107` n `91` status `ready` deltaP `-9.8885` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2343` n `91` status `ready` deltaP `-9.8734` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2945` n `91` status `ready` deltaP `-4.2634` edge `0.0094` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
