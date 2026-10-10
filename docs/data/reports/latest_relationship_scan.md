# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T22:54:45.511365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5511`

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

- `market_context_high->unknown_4h` score `40.2179` n `91` status `ready` deltaP `-6.7978` edge `3.4507` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0655` n `91` status `ready` deltaP `38.5474` edge `0.6247` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3637` n `91` status `ready` deltaP `20.9707` edge `1.3755` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.4865` n `91` status `ready` deltaP `17.4015` edge `0.2076` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.0667` n `91` status `ready` deltaP `10.1534` edge `0.6803` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2226` n `91` status `ready` deltaP `10.1435` edge `0.0498` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1398` n `91` status `ready` deltaP `5.2001` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0047` n `91` status `ready` deltaP `10.0459` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2887` n `91` status `ready` deltaP `9.5162` edge `0.0905` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3662` n `91` status `ready` deltaP `0.5528` edge `0.0034` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3899` n `91` status `ready` deltaP `6.271` edge `0.0567` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3936` n `91` status `ready` deltaP `2.5499` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_4h` score `-0.634` n `91` status `ready` deltaP `-1.0318` edge `-0.0044` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9539` n `91` status `ready` deltaP `-5.0371` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9641` n `91` status `ready` deltaP `-5.4661` edge `0.0136` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9969` n `91` status `ready` deltaP `-6.4946` edge `0.1088` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.1391` n `91` status `ready` deltaP `-8.5412` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1879` n `91` status `ready` deltaP `-2.3935` edge `0.0308` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.1932` n `91` status `ready` deltaP `-9.1883` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2508` n `91` status `ready` deltaP `-3.439` edge `0.0095` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
