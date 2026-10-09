# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T13:22:28.623620+00:00`
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

- `market_context_high->unknown_4h` score `40.3675` n `91` status `ready` deltaP `-5.2734` edge `3.453` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1712` n `91` status `ready` deltaP `34.0335` edge `0.6636` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.5317` n `91` status `ready` deltaP `21.6652` edge `1.3924` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1258` n `91` status `ready` deltaP `13.452` edge `0.9223` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.979` n `91` status `ready` deltaP `18.7735` edge `0.2616` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.4806` n `91` status `ready` deltaP `13.5627` edge `0.1197` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3466` n `91` status `ready` deltaP `10.4429` edge `0.0637` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.3206` n `91` status `ready` deltaP `7.4456` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.1695` n `91` status `ready` deltaP `12.1801` edge `0.0076` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.165` n `91` status `ready` deltaP `-4.9702` edge `0.2053` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2091` n `91` status `ready` deltaP `4.496` edge `0.0038` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2789` n `91` status `ready` deltaP `8.4746` edge `0.0987` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4873` n `91` status `ready` deltaP `-0.1957` edge `-0.0017` maxDD `-0.3417`
- `market_context_high->metal_4h` score `-0.7727` n `91` status `ready` deltaP `-3.1795` edge `0.0229` maxDD `-1.0609`
- `market_context_high->crypto_alt_1h` score `-0.8029` n `91` status `ready` deltaP `-1.1959` edge `0.0549` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8776` n `91` status `ready` deltaP `-3.2407` edge `-0.0069` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9047` n `91` status `ready` deltaP `-3.0136` edge `-0.0259` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2069` n `91` status `ready` deltaP `-9.7388` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2573` n `91` status `ready` deltaP `-10.2553` edge `0.0004` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3006` n `91` status `ready` deltaP `-4.2012` edge `0.0082` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
