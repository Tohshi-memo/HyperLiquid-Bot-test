# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T13:37:26.327064+00:00`
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

- `market_context_high->unknown_4h` score `40.2715` n `91` status `ready` deltaP `-5.2734` edge `3.445` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1971` n `91` status `ready` deltaP `34.2071` edge `0.6646` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.5145` n `91` status `ready` deltaP `21.6652` edge `1.3902` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.118` n `91` status `ready` deltaP `13.452` edge `0.9213` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9705` n `91` status `ready` deltaP `18.7735` edge `0.2605` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.4591` n `91` status `ready` deltaP `13.3891` edge `0.1181` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3536` n `91` status `ready` deltaP `10.4429` edge `0.0646` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.3074` n `91` status `ready` deltaP `7.2959` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.184` n `91` status `ready` deltaP `12.3325` edge `0.0078` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1619` n `91` status `ready` deltaP `-4.9702` edge `0.2057` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2247` n `91` status `ready` deltaP `4.3463` edge `0.0035` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2683` n `91` status `ready` deltaP `8.6482` edge `0.0989` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4885` n `91` status `ready` deltaP `-0.1957` edge `-0.0018` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7825` n `91` status `ready` deltaP `-1.0462` edge `0.0556` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.7853` n `91` status `ready` deltaP `-3.3319` edge `0.0223` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8761` n `91` status `ready` deltaP `-3.2407` edge `-0.0067` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9055` n `91` status `ready` deltaP `-3.0136` edge `-0.026` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2076` n `91` status `ready` deltaP `-9.7388` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2478` n `91` status `ready` deltaP `-10.1029` edge `0.0006` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2841` n `91` status `ready` deltaP `-4.0488` edge `0.0093` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
