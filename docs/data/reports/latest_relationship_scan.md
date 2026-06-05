# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T23:07:21.763889+00:00`
- Price records: `672`
- Market context records: `3015`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `21.2496` n `98` status `ready` deltaP `8.9357` edge `2.1029` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.9296` n `98` status `ready` deltaP `43.3355` edge `0.7996` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.6347` n `98` status `ready` deltaP `21.1735` edge `0.9582` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.3502` n `98` status `ready` deltaP `19.9086` edge `1.0135` maxDD `-12.6963`
- `market_context_high->index_24h` score `7.077` n `98` status `ready` deltaP `19.5189` edge `0.5577` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.409` n `106` status `ready` deltaP `18.0396` edge `0.1452` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6725` n `106` status `ready` deltaP `13.7799` edge `0.1748` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2072` n `106` status `ready` deltaP `17.1997` edge `0.0966` maxDD `-10.4423`
- `market_context_high->crypto_alt_4h` score `-0.1453` n `106` status `ready` deltaP `22.6301` edge `0.3853` maxDD `-38.7172`
- `market_context_high->commodity_1h` score `-0.1722` n `118` status `ready` deltaP `1.0961` edge `0.0206` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.2638` n `118` status `ready` deltaP `4.3337` edge `0.0451` maxDD `-5.6254`
- `market_context_high->index_1h` score `-0.3476` n `118` status `ready` deltaP `4.9858` edge `0.0236` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5449` n `118` status `ready` deltaP `6.7797` edge `0.0979` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.6383` n `118` status `ready` deltaP `-2.5931` edge `0.0007` maxDD `-0.2615`
- `market_context_high->unknown_1h` score `-0.8898` n `118` status `ready` deltaP `4.0851` edge `-0.0283` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0438` n `118` status `ready` deltaP `4.3895` edge `0.0632` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1607` n `118` status `ready` deltaP `-2.04` edge `-0.0034` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.1801` n `106` status `ready` deltaP `-10.6823` edge `-0.0011` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.7235` n `106` status `ready` deltaP `-2.7439` edge `-0.02` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7548` n `98` status `ready` deltaP `-5.0914` edge `-0.0251` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
