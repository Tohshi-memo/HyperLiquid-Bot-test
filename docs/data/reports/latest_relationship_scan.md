# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T21:22:22.117944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5538`

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

- `market_context_high->unknown_4h` score `40.3331` n `91` status `ready` deltaP `-6.7978` edge `3.4603` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0691` n `91` status `ready` deltaP `38.5474` edge `0.625` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3559` n `91` status `ready` deltaP `20.9707` edge `1.3745` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5142` n `91` status `ready` deltaP `17.8588` edge `0.2081` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.1899` n `91` status `ready` deltaP `10.1534` edge `0.6961` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.1961` n `91` status `ready` deltaP `9.6944` edge `0.0494` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1038` n `91` status `ready` deltaP `4.751` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.0587` n `91` status `ready` deltaP `9.2837` edge `0.0079` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2314` n `91` status `ready` deltaP `10.5579` edge `0.0909` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3195` n `91` status `ready` deltaP `1.0019` edge `0.0043` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3565` n `91` status `ready` deltaP `2.999` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.399` n `91` status `ready` deltaP `6.0974` edge `0.0567` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6246` n `91` status `ready` deltaP `-1.0318` edge `-0.0032` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9388` n `91` status `ready` deltaP `-5.0088` edge `0.0138` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.9461` n `91` status `ready` deltaP `-4.8874` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-1.0047` n `91` status `ready` deltaP `-6.4946` edge `0.1078` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.1383` n `91` status `ready` deltaP `-8.5412` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.1924` n `91` status `ready` deltaP `-9.1883` edge `0.0016` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2516` n `91` status `ready` deltaP `-3.439` edge `0.0094` maxDD `-5.4217`
- `market_context_high->crypto_alt_1h` score `-1.2574` n `91` status `ready` deltaP `-2.8426` edge `0.028` maxDD `-4.7735`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
