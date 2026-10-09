# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T13:52:34.935636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8613`

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

- `market_context_high->unknown_4h` score `40.2595` n `91` status `ready` deltaP `-5.2734` edge `3.444` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.2302` n `91` status `ready` deltaP `34.3807` edge `0.6662` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.495` n `91` status `ready` deltaP `21.6652` edge `1.3877` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1079` n `91` status `ready` deltaP `13.452` edge `0.92` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9595` n `91` status `ready` deltaP `18.7735` edge `0.2591` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.4368` n `91` status `ready` deltaP `13.2155` edge `0.1164` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3559` n `91` status `ready` deltaP `10.4429` edge `0.0649` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2954` n `91` status `ready` deltaP `7.1462` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.1974` n `91` status `ready` deltaP `12.485` edge `0.0079` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1564` n `91` status `ready` deltaP `-4.9702` edge `0.2064` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2415` n `91` status `ready` deltaP `4.1966` edge `0.0031` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.257` n `91` status `ready` deltaP `8.8218` edge `0.0992` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4897` n `91` status `ready` deltaP `-0.1957` edge `-0.0019` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7633` n `91` status `ready` deltaP `-0.8965` edge `0.0562` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.7994` n `91` status `ready` deltaP `-3.4844` edge `0.0215` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8698` n `91` status `ready` deltaP `-3.2407` edge `-0.0059` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9063` n `91` status `ready` deltaP `-3.0136` edge `-0.0261` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2069` n `91` status `ready` deltaP `-9.7388` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2375` n `91` status `ready` deltaP `-9.9505` edge `0.0009` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.266` n `91` status `ready` deltaP `-3.8964` edge `0.0106` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
