# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T06:07:29.466186+00:00`
- Price records: `672`
- Market context records: `4799`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7516`

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

- `market_context_high->unknown_1h` score `10.3785` n `123` status `ready` deltaP `12.5603` edge `0.8229` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.7583` n `122` status `ready` deltaP `19.3298` edge `0.6387` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.459` n `116` status `ready` deltaP `13.9128` edge `0.2045` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.118` n `123` status `ready` deltaP `5.775` edge `0.0301` maxDD `-2.0345`
- `market_context_high->equity_4h` score `0.0389` n `122` status `ready` deltaP `8.9964` edge `0.1136` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `0.0228` n `122` status `ready` deltaP `11.5104` edge `0.0434` maxDD `-4.377`
- `market_context_high->index_4h` score `-0.2923` n `122` status `ready` deltaP `7.7569` edge `0.0177` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.3981` n `122` status `ready` deltaP `3.5836` edge `0.0027` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6436` n `123` status `ready` deltaP `2.2674` edge `0.008` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8781` n `123` status `ready` deltaP `-0.8142` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3139` n `123` status `ready` deltaP `-0.6414` edge `-0.0048` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-1.9777` n `116` status `ready` deltaP `20.9291` edge `0.1178` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.1775` n `123` status `ready` deltaP `-0.0451` edge `-0.0613` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.0814` n `123` status `ready` deltaP `1.0905` edge `-0.0401` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.0909` n `116` status `ready` deltaP `-12.6017` edge `-0.0186` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.413` n `123` status `ready` deltaP `0.897` edge `-0.0647` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.6527` n `122` status `ready` deltaP `5.6602` edge `0.0082` maxDD `-46.0617`
- `market_context_high->index_24h` score `-7.252` n `116` status `ready` deltaP `-9.381` edge `-0.1357` maxDD `-24.4873`
- `market_context_high->crypto_major_4h` score `-7.9493` n `122` status `ready` deltaP `4.2683` edge `-0.1245` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2065` n `122` status `ready` deltaP `7.4495` edge `-0.2777` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
