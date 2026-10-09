# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T18:07:31.792422+00:00`
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

- `market_context_high->unknown_4h` score `40.9231` n `91` status `ready` deltaP `-4.3587` edge `3.4932` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.9838` n `91` status `ready` deltaP `33.6863` edge `0.6503` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.6972` n `91` status `ready` deltaP `19.5818` edge `1.2993` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.0963` n `91` status `ready` deltaP `11.3687` edge `0.8042` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.6056` n `91` status `ready` deltaP `18.0113` edge `0.2188` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.299` n `91` status `ready` deltaP `10.4429` edge `0.0576` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2859` n `91` status `ready` deltaP `6.9965` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2216` n `91` status `ready` deltaP `12.6374` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0908` n `91` status `ready` deltaP `10.6113` edge `0.0894` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3208` n `91` status `ready` deltaP `7.9537` edge `0.0968` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3301` n `91` status `ready` deltaP `3.4481` edge `0.0007` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.4406` n `91` status `ready` deltaP `0.2534` edge `-0.0008` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.6218` n `91` status `ready` deltaP `-6.4946` edge `0.1569` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-0.8293` n `91` status `ready` deltaP `-1.1959` edge `0.0527` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8425` n `91` status `ready` deltaP `-3.091` edge `-0.0034` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8711` n `91` status `ready` deltaP `-2.8611` edge `-0.0226` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9694` n `91` status `ready` deltaP `-5.3136` edge `0.0119` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1695` n `91` status `ready` deltaP `-9.14` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2193` n `91` status `ready` deltaP `-9.6456` edge `0.0012` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2377` n `91` status `ready` deltaP `-3.5915` edge `0.0122` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
