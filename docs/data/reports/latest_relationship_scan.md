# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T15:14:54.044421+00:00`
- Price records: `672`
- Market context records: `4839`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.6741` n `109` status `ready` deltaP `10.2703` edge `1.1128` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.0194` n `99` status `ready` deltaP `22.8228` edge `0.7906` maxDD `-3.9578`
- `market_context_high->unknown_24h` score `4.0534` n `95` status `ready` deltaP `20.8206` edge `0.2546` maxDD `-2.116`
- `market_context_high->crypto_alt_4h` score `1.0567` n `99` status `ready` deltaP `14.0937` edge `0.2213` maxDD `-11.3825`
- `market_context_high->index_4h` score `0.3723` n `99` status `ready` deltaP `7.2894` edge `0.0291` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.3096` n `109` status `ready` deltaP `3.8098` edge `0.062` maxDD `-2.928`
- `market_context_high->crypto_major_4h` score `0.2546` n `99` status `ready` deltaP `10.4152` edge `0.1965` maxDD `-15.9968`
- `market_context_high->commodity_4h` score `-0.0578` n `99` status `ready` deltaP `12.2244` edge `0.0283` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.0754` n `99` status `ready` deltaP `9.2526` edge `0.0668` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `-0.0892` n `109` status `ready` deltaP `2.9652` edge `0.0253` maxDD `-1.1869`
- `market_context_high->fx_4h` score `-0.1003` n `99` status `ready` deltaP `7.023` edge `0.0085` maxDD `-0.788`
- `market_context_high->index_1h` score `-0.8752` n `109` status `ready` deltaP `-1.3569` edge `0.0116` maxDD `-0.7054`
- `market_context_high->metal_4h` score `-1.1971` n `99` status `ready` deltaP `9.4805` edge `-0.0061` maxDD `-13.5126`
- `market_context_high->fx_1h` score `-1.3133` n `109` status `ready` deltaP `-5.8905` edge `-0.0053` maxDD `-0.8563`
- `market_context_high->crypto_alt_1h` score `-1.3361` n `109` status `ready` deltaP `4.09` edge `-0.0062` maxDD `-12.7225`
- `market_context_high->fx_24h` score `-1.9603` n `95` status `ready` deltaP `-7.4598` edge `-0.0126` maxDD `-2.749`
- `market_context_high->crypto_major_1h` score `-1.9629` n `109` status `ready` deltaP `2.8155` edge `-0.0129` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.1309` n `109` status `ready` deltaP `0.0632` edge `-0.0633` maxDD `-13.4916`
- `market_context_high->commodity_24h` score `-3.2043` n `95` status `ready` deltaP `12.5055` edge `0.0167` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.5993` n `95` status `ready` deltaP `-7.6334` edge `-0.1377` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
