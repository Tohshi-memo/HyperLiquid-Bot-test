# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T20:52:25.109983+00:00`
- Price records: `672`
- Market context records: `3110`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6925`

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

- `market_context_high->crypto_alt_24h` score `15.2017` n `90` status `ready` deltaP `12.8472` edge `2.4832` maxDD `-40.9265`
- `market_context_high->commodity_24h` score `14.8038` n `90` status `ready` deltaP `46.0764` edge `0.9693` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `13.5311` n `90` status `ready` deltaP `22.0486` edge `1.0294` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3676` n `90` status `ready` deltaP `32.2223` edge `0.9046` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.3885` n `90` status `ready` deltaP `15.4514` edge `1.3482` maxDD `-42.2408`
- `market_context_high->commodity_4h` score `2.9894` n `120` status `ready` deltaP `17.9878` edge `0.175` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0721` n `128` status `ready` deltaP `1.4783` edge `0.0264` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.471` n `128` status `ready` deltaP `4.2899` edge `0.0173` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5331` n `90` status `ready` deltaP `4.3403` edge `-0.0006` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.8496` n `128` status `ready` deltaP `-9.4077` edge `-0.0051` maxDD `-0.6216`
- `market_context_high->crypto_alt_1h` score `-0.8509` n `128` status `ready` deltaP `2.6946` edge `0.0859` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0794` n `128` status `ready` deltaP `0.2994` edge `0.0082` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3288` n `120` status `ready` deltaP `-12.4187` edge `-0.0032` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4305` n `120` status `ready` deltaP `9.4817` edge `0.0443` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.8996` n `120` status `ready` deltaP `4.5935` edge `0.0128` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.2654` n `128` status `ready` deltaP `-1.2585` edge `0.0459` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.379` n `128` status `ready` deltaP `-7.3775` edge `-0.0097` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.8358` n `128` status `ready` deltaP `2.2081` edge `-0.0484` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.936` n `120` status `ready` deltaP `12.2053` edge `0.2185` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0648` n `120` status `ready` deltaP `5.9146` edge `-0.03` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
