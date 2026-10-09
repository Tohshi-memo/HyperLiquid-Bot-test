# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T11:22:30.591796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8370`

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

- `market_context_high->unknown_4h` score `40.1975` n `91` status `ready` deltaP `-4.9685` edge `3.4368` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1831` n `90` status `ready` deltaP `34.1667` edge `0.6637` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.9949` n `90` status `ready` deltaP `22.3611` edge `1.4297` maxDD `-16.7906`
- `market_context_high->crypto_alt_24h` score `3.5259` n `90` status `ready` deltaP `14.0625` edge `0.9521` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.9656` n `91` status `ready` deltaP `18.621` edge `0.2609` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.5748` n `90` status `ready` deltaP `14.5486` edge `0.1252` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3357` n `91` status `ready` deltaP `10.1435` edge `0.0643` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2954` n `91` status `ready` deltaP `7.1462` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0953` n `91` status `ready` deltaP `11.4179` edge `0.0065` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2211` n `91` status `ready` deltaP `4.3463` edge `0.0038` maxDD `-0.7626`
- `market_context_high->crypto_alt_4h` score `-0.3259` n `91` status `ready` deltaP `-6.1897` edge `0.1928` maxDD `-8.7986`
- `market_context_high->index_24h` score `-0.3266` n `90` status `ready` deltaP `7.8125` edge `0.097` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.443` n `91` status `ready` deltaP `0.2534` edge `-0.001` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7957` n `91` status `ready` deltaP `-1.3456` edge `0.0565` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.8209` n `91` status `ready` deltaP `-3.9417` edge `0.0218` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8254` n `91` status `ready` deltaP `-2.4922` edge `-0.0052` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9096` n `91` status `ready` deltaP `-3.166` edge `-0.0255` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2076` n `91` status `ready` deltaP `-9.7388` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3433` n `91` status `ready` deltaP `-11.4748` edge `-0.0025` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3821` n `91` status `ready` deltaP `-4.6586` edge `0.0008` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
