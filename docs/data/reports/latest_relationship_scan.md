# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T18:07:26.959023+00:00`
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

- `market_context_high->unknown_4h` score `40.6031` n `91` status `ready` deltaP `-6.7978` edge `3.4828` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.042` n `91` status `ready` deltaP `38.4635` edge `0.6233` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3647` n `91` status `ready` deltaP `20.8696` edge `1.3763` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5251` n `91` status `ready` deltaP `10.0578` edge `0.7397` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4757` n `91` status `ready` deltaP `17.554` edge `0.2052` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1961` n `91` status `ready` deltaP `9.8441` edge `0.0484` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1757` n `91` status `ready` deltaP `5.6492` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1431` n `91` status `ready` deltaP `12.1965` edge `0.0913` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1708` n `91` status `ready` deltaP `7.9118` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.2704` n `91` status `ready` deltaP `1.6007` edge `0.0044` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3205` n `91` status `ready` deltaP `3.4481` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4337` n `91` status `ready` deltaP `5.5041` edge `0.0562` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6404` n `91` status `ready` deltaP `-1.1843` edge `-0.0042` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9702` n `91` status `ready` deltaP `-5.3365` edge `-0.0048` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9804` n `91` status `ready` deltaP `-6.3422` edge `0.1099` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9966` n `91` status `ready` deltaP `-6.0758` edge `0.0135` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1703` n `91` status `ready` deltaP `-9.14` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1783` n `91` status `ready` deltaP `-2.2438` edge `0.0306` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2827` n `91` status `ready` deltaP `-10.8651` edge `0.0012` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.318` n `91` status `ready` deltaP `-4.5061` edge `0.008` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
