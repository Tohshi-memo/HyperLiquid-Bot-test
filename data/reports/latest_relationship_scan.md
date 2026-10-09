# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T12:52:31.801354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8505`

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

- `market_context_high->unknown_4h` score `40.4083` n `91` status `ready` deltaP `-5.2734` edge `3.4564` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1266` n `91` status `ready` deltaP `33.6863` edge `0.6622` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.5676` n `91` status `ready` deltaP `21.6652` edge `1.397` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1492` n `91` status `ready` deltaP `13.452` edge `0.9253` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9939` n `91` status `ready` deltaP `18.7735` edge `0.2635` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.5205` n `91` status `ready` deltaP `13.9099` edge `0.1225` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3224` n `91` status `ready` deltaP `10.1435` edge `0.0626` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.3206` n `91` status `ready` deltaP `7.4456` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.1415` n `91` status `ready` deltaP `11.8752` edge `0.0073` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1964` n `91` status `ready` deltaP `-5.2751` edge `0.2033` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2223` n `91` status `ready` deltaP `4.3463` edge `0.0037` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2911` n `91` status `ready` deltaP `8.3009` edge `0.0983` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4586` n `91` status `ready` deltaP `0.1037` edge `-0.0013` maxDD `-0.3417`
- `market_context_high->metal_4h` score `-0.7719` n `91` status `ready` deltaP `-3.1795` edge `0.023` maxDD `-1.0609`
- `market_context_high->crypto_alt_1h` score `-0.8328` n `91` status `ready` deltaP `-1.4953` edge `0.0544` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8659` n `91` status `ready` deltaP `-3.091` edge `-0.0064` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8929` n `91` status `ready` deltaP `-2.8611` edge `-0.0254` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2154` n `91` status `ready` deltaP `-9.8885` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2794` n `91` status `ready` deltaP `-10.5602` edge `-0.0004` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3186` n `91` status `ready` deltaP `-4.2012` edge `0.0059` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
