# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T17:52:30.608299+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6186`

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

- `market_context_high->unknown_4h` score `40.5753` n `91` status `ready` deltaP `-6.9502` edge `3.4815` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0384` n `91` status `ready` deltaP `38.4635` edge `0.623` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3601` n `91` status `ready` deltaP `20.8696` edge `1.3757` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5391` n `91` status `ready` deltaP `10.0578` edge `0.7415` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4773` n `91` status `ready` deltaP `17.554` edge `0.2054` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1953` n `91` status `ready` deltaP `9.8441` edge `0.0483` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1637` n `91` status `ready` deltaP `5.4995` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1423` n `91` status `ready` deltaP `12.1965` edge `0.0914` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1708` n `91` status `ready` deltaP `7.9118` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.256` n `91` status `ready` deltaP `1.7504` edge `0.0046` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3325` n `91` status `ready` deltaP `3.2984` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4427` n `91` status `ready` deltaP `5.3308` edge `0.0562` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6396` n `91` status `ready` deltaP `-1.1843` edge `-0.0041` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9702` n `91` status `ready` deltaP `-5.3365` edge `-0.0048` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9758` n `91` status `ready` deltaP `-6.3422` edge `0.1105` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-1.0045` n `91` status `ready` deltaP `-6.2283` edge `0.0135` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.178` n `91` status `ready` deltaP `-9.2897` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1831` n `91` status `ready` deltaP `-2.2438` edge `0.0302` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2835` n `91` status `ready` deltaP `-10.8651` edge `0.0011` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.318` n `91` status `ready` deltaP `-4.5061` edge `0.008` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
