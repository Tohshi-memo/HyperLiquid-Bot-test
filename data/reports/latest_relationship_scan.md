# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T02:22:28.489602+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5679`

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

- `market_context_high->unknown_4h` score `39.2582` n `91` status `ready` deltaP `-8.4746` edge `3.3819` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1099` n `91` status `ready` deltaP `38.5474` edge `0.6284` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.5564` n `91` status `ready` deltaP `20.9707` edge `1.4002` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5993` n `91` status `ready` deltaP `18.9259` edge `0.2119` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.9489` n `91` status `ready` deltaP `10.1534` edge `0.6652` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.5349` n `96` status `ready` deltaP `11.5893` edge `0.0562` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1499` n `96` status `ready` deltaP `5.3269` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.094` n `91` status `ready` deltaP `8.8264` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2895` n `91` status `ready` deltaP `9.5162` edge `0.0904` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3084` n `91` status `ready` deltaP `7.6599` edge `0.0579` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3132` n `96` status `ready` deltaP `3.5554` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.4767` n `96` status `ready` deltaP `-0.6175` edge `0.002` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7516` n `91` status `ready` deltaP `-2.7087` edge `-0.0083` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.7735` n `96` status `ready` deltaP `-0.3181` edge `0.0515` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8333` n `96` status `ready` deltaP `-3.0189` edge `-0.0027` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9213` n `91` status `ready` deltaP `-5.58` edge `0.1124` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9807` n `91` status `ready` deltaP `-5.7709` edge `0.0135` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.2239` n `91` status `ready` deltaP `-2.9817` edge `0.0099` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.2257` n `91` status `ready` deltaP `-9.798` edge `0.0014` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7454` n `96` status `ready` deltaP `-8.483` edge `-0.0027` maxDD `-0.5627`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
