# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T18:22:24.073015+00:00`
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
- `market_context_high->equity_24h` score `10.0444` n `91` status `ready` deltaP `38.4635` edge `0.6235` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3663` n `91` status `ready` deltaP `20.8696` edge `1.3765` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5032` n `91` status `ready` deltaP `10.0578` edge `0.7369` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4773` n `91` status `ready` deltaP `17.554` edge `0.2054` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.2039` n `91` status `ready` deltaP `9.9938` edge `0.0484` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1769` n `91` status `ready` deltaP `5.6492` edge `0.0013` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1521` n `91` status `ready` deltaP `12.0232` edge `0.0913` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1586` n `91` status `ready` deltaP `8.0642` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.2704` n `91` status `ready` deltaP `1.6007` edge `0.0044` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3086` n `91` status `ready` deltaP `3.5978` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4329` n `91` status `ready` deltaP `5.5041` edge `0.0563` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6411` n `91` status `ready` deltaP `-1.1843` edge `-0.0043` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9617` n `91` status `ready` deltaP `-5.1868` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9867` n `91` status `ready` deltaP `-6.3422` edge `0.1091` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9879` n `91` status `ready` deltaP `-5.9234` edge `0.0136` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1625` n `91` status `ready` deltaP `-8.9903` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1795` n `91` status `ready` deltaP `-2.2438` edge `0.0305` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2748` n `91` status `ready` deltaP `-10.7127` edge `0.0012` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.318` n `91` status `ready` deltaP `-4.5061` edge `0.008` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
