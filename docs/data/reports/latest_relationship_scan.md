# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T21:52:29.205982+00:00`
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

- `market_context_high->unknown_4h` score `40.8587` n `91` status `ready` deltaP `-4.9977` edge `3.4921` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6621` n `91` status `ready` deltaP `33.2641` edge `0.6263` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.5139` n `91` status `ready` deltaP `18.4433` edge `1.2834` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6725` n `91` status `ready` deltaP `10.0578` edge `0.7586` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.481` n `91` status `ready` deltaP `18.2415` edge `0.2013` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2619` n `91` status `ready` deltaP `6.6971` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1727` n `91` status `ready` deltaP `9.6944` edge `0.0464` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1121` n `91` status `ready` deltaP `11.3436` edge `0.0084` maxDD `-0.3077`
- `market_context_high->metal_24h` score `-0.0234` n `91` status `ready` deltaP `10.5301` edge `0.0753` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.2714` n `91` status `ready` deltaP `4.0469` edge `0.0016` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3136` n `91` status `ready` deltaP `1.3013` edge `0.0028` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3512` n `91` status `ready` deltaP `7.8638` edge `0.0935` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6458` n `91` status `ready` deltaP `-0.6439` edge `-0.0085` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8815` n `91` status `ready` deltaP `-3.6898` edge `-0.0044` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9365` n `91` status `ready` deltaP `-4.9359` edge `0.0136` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0135` n `91` status `ready` deltaP `-7.3227` edge `0.1122` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.2071` n `91` status `ready` deltaP `-2.3935` edge `0.0292` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2255` n `91` status `ready` deltaP `-10.1879` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2422` n `91` status `ready` deltaP `-10.0256` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2968` n `91` status `ready` deltaP `-4.2634` edge `0.0091` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
