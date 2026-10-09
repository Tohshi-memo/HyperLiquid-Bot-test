# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T07:52:33.305307+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8870`

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

- `market_context_high->unknown_4h` score `40.6634` n `91` status `ready` deltaP `-3.749` edge `3.4675` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `10.0089` n `90` status `ready` deltaP `22.3611` edge `1.4315` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.8359` n `90` status `ready` deltaP `32.2569` edge `0.6475` maxDD `-1.0977`
- `market_context_high->crypto_alt_24h` score `3.593` n `90` status `ready` deltaP `14.0625` edge `0.9607` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8527` n `91` status `ready` deltaP `17.8588` edge `0.2515` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.8548` n `90` status `ready` deltaP `16.9791` edge `0.1449` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.2966` n `91` status `ready` deltaP `7.1462` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2624` n `91` status `ready` deltaP `9.5447` edge `0.0589` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1707` n `91` status `ready` deltaP `12.1801` edge `0.0077` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2103` n `91` status `ready` deltaP `4.496` edge `0.0037` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3327` n `91` status `ready` deltaP `1.1516` edge `0.0022` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3516` n `90` status `ready` deltaP `7.8125` edge `0.0938` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.4366` n `91` status `ready` deltaP `-7.1044` edge `0.1847` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.7862` n `91` status `ready` deltaP `-3.4844` edge `0.0232` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.8778` n `91` status `ready` deltaP `-3.4709` edge `-0.0194` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8994` n `91` status `ready` deltaP `-3.3904` edge `-0.0087` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.9587` n `91` status `ready` deltaP `-2.2438` edge `0.0489` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2762` n `91` status `ready` deltaP `-10.9364` edge `-0.0045` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3757` n `91` status `ready` deltaP `-11.9322` edge `-0.0036` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3838` n `91` status `ready` deltaP `-4.811` edge `0.0016` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
