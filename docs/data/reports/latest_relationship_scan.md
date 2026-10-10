# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T11:52:26.248950+00:00`
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

- `market_context_high->unknown_4h` score `40.9817` n `91` status `ready` deltaP `-6.3404` edge `3.5113` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.9324` n `91` status `ready` deltaP `37.4236` edge `0.6211` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.1235` n `91` status `ready` deltaP `20.1764` edge `1.35` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7637` n `91` status `ready` deltaP `10.0578` edge `0.7703` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.385` n `91` status `ready` deltaP `16.3345` edge `0.2017` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2248` n `91` status `ready` deltaP `6.248` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1564` n `91` status `ready` deltaP `9.0956` edge `0.0483` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1318` n `91` status `ready` deltaP `8.3691` edge `0.0079` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.185` n `91` status `ready` deltaP `11.33` edge `0.0917` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.2968` n `91` status `ready` deltaP `1.3013` edge `0.0042` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3217` n `91` status `ready` deltaP `3.4481` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4012` n `91` status `ready` deltaP `6.024` edge `0.0569` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.7009` n `91` status `ready` deltaP `-1.794` edge `-0.0079` maxDD `-1.6002`
- `market_context_high->unknown_1h` score `-0.7829` n `91` status `ready` deltaP `-4.2179` edge `0.0044` maxDD `-0.9885`
- `market_context_high->equity_1h` score `-0.9297` n `91` status `ready` deltaP `-4.588` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9887` n `91` status `ready` deltaP `-5.9234` edge `0.0135` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0003` n `91` status `ready` deltaP `-6.7995` edge `0.1104` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1616` n `91` status `ready` deltaP `-2.0941` edge `0.031` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2489` n `91` status `ready` deltaP `-10.637` edge `-0.003` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.2793` n `91` status `ready` deltaP `-3.8964` edge `0.0089` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
