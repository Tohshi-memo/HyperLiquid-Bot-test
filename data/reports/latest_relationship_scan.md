# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T11:37:27.204885+00:00`
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

- `market_context_high->unknown_4h` score `41.0011` n `91` status `ready` deltaP `-6.188` edge `3.5119` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.9066` n `91` status `ready` deltaP `37.2503` edge `0.6201` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.0911` n `91` status `ready` deltaP `20.0031` edge `1.347` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.745` n `91` status `ready` deltaP `10.0578` edge `0.7679` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3755` n `91` status `ready` deltaP `16.182` edge `0.2015` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2248` n `91` status `ready` deltaP `6.248` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1564` n `91` status `ready` deltaP `9.0956` edge `0.0483` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1318` n `91` status `ready` deltaP `8.3691` edge `0.0079` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.1948` n `91` status `ready` deltaP `11.1567` edge `0.0916` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.298` n `91` status `ready` deltaP `1.3013` edge `0.0041` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3217` n `91` status `ready` deltaP `3.4481` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4012` n `91` status `ready` deltaP `6.024` edge `0.0569` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.712` n `91` status `ready` deltaP `-1.9465` edge `-0.0083` maxDD `-1.6002`
- `market_context_high->unknown_1h` score `-0.7529` n `91` status `ready` deltaP `-4.0682` edge `0.0059` maxDD `-0.9885`
- `market_context_high->equity_1h` score `-0.929` n `91` status `ready` deltaP `-4.588` edge `-0.0045` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9887` n `91` status `ready` deltaP `-5.9234` edge `0.0135` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0058` n `91` status `ready` deltaP `-6.7995` edge `0.1097` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1724` n `91` status `ready` deltaP `-2.0941` edge `0.0301` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2489` n `91` status `ready` deltaP `-10.637` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2779` n `91` status `ready` deltaP `-10.7127` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
