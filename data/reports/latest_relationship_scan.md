# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T23:22:28.235768+00:00`
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

- `market_context_high->unknown_4h` score `40.0904` n `91` status `ready` deltaP `-7.1026` edge `3.4421` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0667` n `91` status `ready` deltaP `38.5474` edge `0.6248` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3739` n `91` status `ready` deltaP `20.9707` edge `1.3768` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.4873` n `91` status `ready` deltaP `17.4015` edge `0.2077` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.0332` n `91` status `ready` deltaP `10.1534` edge `0.676` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2132` n `91` status `ready` deltaP `9.9938` edge `0.0496` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1649` n `91` status `ready` deltaP `5.4995` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0291` n `91` status `ready` deltaP `10.3508` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.3076` n `91` status `ready` deltaP `9.169` edge `0.0904` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3351` n `91` status `ready` deltaP `0.8522` edge `0.004` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3696` n `91` status `ready` deltaP `2.8493` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3899` n `91` status `ready` deltaP `6.271` edge `0.0567` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6371` n `91` status `ready` deltaP `-1.0318` edge `-0.0048` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9453` n `91` status `ready` deltaP `-4.8874` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.972` n `91` status `ready` deltaP `-5.6185` edge `0.0136` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9875` n `91` status `ready` deltaP `-6.3422` edge `0.109` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.1228` n `91` status `ready` deltaP `-8.2418` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1855` n `91` status `ready` deltaP `-2.3935` edge `0.031` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.1932` n `91` status `ready` deltaP `-9.1883` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2508` n `91` status `ready` deltaP `-3.439` edge `0.0095` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
