# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T20:22:28.999627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `41.0887` n `91` status `ready` deltaP `-4.3889` edge `3.5072` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7425` n `91` status `ready` deltaP `33.2641` edge `0.633` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.4765` n `91` status `ready` deltaP `18.4433` edge `1.2786` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6896` n `91` status `ready` deltaP `10.0578` edge `0.7608` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.491` n `91` status `ready` deltaP `18.0892` edge `0.2036` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2859` n `91` status `ready` deltaP `6.9965` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2748` n `91` status `ready` deltaP `10.2932` edge `0.0555` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1888` n `91` status `ready` deltaP `12.2569` edge `0.0087` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0211` n `91` status `ready` deltaP `10.5301` edge `0.081` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3158` n `91` status `ready` deltaP `3.5978` edge `0.0009` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3315` n `91` status `ready` deltaP `1.1516` edge `0.0023` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.345` n `91` status `ready` deltaP `7.8638` edge `0.0943` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.7307` n `91` status `ready` deltaP `-1.5571` edge `-0.0133` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8752` n `91` status `ready` deltaP `-3.5401` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.948` n `91` status `ready` deltaP `-1.4953` edge `0.0448` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.9483` n `91` status `ready` deltaP `-5.0881` edge `0.0131` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9533` n `91` status `ready` deltaP `-7.1705` edge `0.1189` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.2107` n `91` status `ready` deltaP `-9.8885` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2343` n `91` status `ready` deltaP `-9.8734` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2968` n `91` status `ready` deltaP `-4.2634` edge `0.0091` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
