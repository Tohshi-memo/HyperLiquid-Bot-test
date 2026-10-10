# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T22:22:27.327024+00:00`
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

- `market_context_high->unknown_4h` score `40.2949` n `91` status `ready` deltaP `-6.6453` edge `3.4561` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0667` n `91` status `ready` deltaP `38.5474` edge `0.6248` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3606` n `91` status `ready` deltaP `20.9707` edge `1.3751` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.488` n `91` status `ready` deltaP `17.4015` edge `0.2078` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.1057` n `91` status `ready` deltaP `10.1534` edge `0.6853` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2257` n `91` status `ready` deltaP `10.1435` edge `0.0502` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1398` n `91` status `ready` deltaP `5.2001` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.0209` n `91` status `ready` deltaP `9.7411` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2699` n `91` status `ready` deltaP `9.8634` edge `0.0906` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3674` n `91` status `ready` deltaP `0.5528` edge `0.0033` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3809` n `91` status `ready` deltaP `6.4446` edge `0.0567` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3816` n `91` status `ready` deltaP `2.6996` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_4h` score `-0.6301` n `91` status `ready` deltaP `-1.0318` edge `-0.0039` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9453` n `91` status `ready` deltaP `-4.8874` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9554` n `91` status `ready` deltaP `-5.3136` edge `0.0137` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9993` n `91` status `ready` deltaP `-6.4946` edge `0.1085` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.1228` n `91` status `ready` deltaP `-8.2418` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.1924` n `91` status `ready` deltaP `-9.1883` edge `0.0016` maxDD `-1.1242`
- `market_context_high->crypto_alt_1h` score `-1.1927` n `91` status `ready` deltaP `-2.3935` edge `0.0304` maxDD `-4.7735`
- `market_context_high->equity_4h` score `-1.2501` n `91` status `ready` deltaP `-3.439` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
