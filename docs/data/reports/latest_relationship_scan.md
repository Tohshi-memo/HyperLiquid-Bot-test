# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T03:07:24.058367+00:00`
- Price records: `672`
- Market context records: `3032`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.86` n `99` status `ready` deltaP `10.8112` edge `2.2246` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.9499` n `99` status `ready` deltaP `22.7589` edge `0.9739` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.7685` n `99` status `ready` deltaP `42.3769` edge `0.8056` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.9582` n `99` status `ready` deltaP `21.9855` edge `1.1489` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.7243` n `99` status `ready` deltaP `21.5752` edge `0.6254` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8408` n `122` status `ready` deltaP `19.3122` edge `0.1727` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0553` n `129` status `ready` deltaP `2.5902` edge `0.0296` maxDD `-1.7142`
- `market_context_high->index_4h` score `-0.1847` n `122` status `ready` deltaP `14.5242` edge `0.0851` maxDD `-12.1152`
- `market_context_high->unknown_4h` score `-0.3021` n `122` status `ready` deltaP `2.0792` edge `0.0663` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `-0.354` n `122` status `ready` deltaP `20.5068` edge `0.3727` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.3897` n `129` status `ready` deltaP `4.0872` edge `0.0242` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4653` n `129` status `ready` deltaP `3.7182` edge `0.0371` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.533` n `129` status `ready` deltaP `-4.7394` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5646` n `129` status `ready` deltaP `6.3861` edge `0.098` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8453` n `129` status `ready` deltaP `3.7715` edge `-0.0225` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9981` n `129` status `ready` deltaP `4.2798` edge `0.0698` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0669` n `122` status `ready` deltaP `-8.0443` edge `-0.0024` maxDD `-0.7932`
- `market_context_high->metal_1h` score `-1.138` n `129` status `ready` deltaP `-1.7987` edge `-0.0021` maxDD `-6.8783`
- `market_context_high->equity_4h` score `-1.1461` n `122` status `ready` deltaP `11.438` edge `0.1034` maxDD `-23.4606`
- `market_context_high->fx_24h` score `-1.537` n `99` status `ready` deltaP `-3.0145` edge `-0.0208` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
