# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T00:22:28.162823+00:00`
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

- `market_context_high->unknown_4h` score `39.8714` n `91` status `ready` deltaP `-7.5599` edge `3.4269` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0739` n `91` status `ready` deltaP `38.5474` edge `0.6254` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.416` n `91` status `ready` deltaP `20.9707` edge `1.3822` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5283` n `91` status `ready` deltaP `18.0113` edge `0.2089` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.9871` n `91` status `ready` deltaP `10.1534` edge `0.6701` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2514` n `91` status `ready` deltaP `10.5926` edge `0.0505` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1649` n `91` status `ready` deltaP `5.4995` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.0075` n `91` status `ready` deltaP `9.8935` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.3354` n `91` status `ready` deltaP `8.6482` edge `0.0903` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3638` n `91` status `ready` deltaP `0.5528` edge `0.0036` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3809` n `91` status `ready` deltaP `6.4446` edge `0.0567` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3936` n `91` status `ready` deltaP `2.5499` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_4h` score `-0.6813` n `91` status `ready` deltaP `-1.6416` edge `-0.0064` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9111` n `91` status `ready` deltaP `-4.2886` edge `-0.0042` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9582` n `91` status `ready` deltaP `-5.8849` edge `0.1097` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9887` n `91` status `ready` deltaP `-5.9234` edge `0.0135` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1072` n `91` status `ready` deltaP `-7.9424` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1544` n `91` status `ready` deltaP `-2.0941` edge `0.0316` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2178` n `91` status `ready` deltaP `-9.6456` edge `0.0014` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2501` n `91` status `ready` deltaP `-3.439` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
