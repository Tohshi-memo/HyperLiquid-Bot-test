# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T20:07:26.655658+00:00`
- Price records: `672`
- Market context records: `6953`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11729`

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

- `market_context_high->fx_1h` score `-0.26` n `237` status `ready` deltaP `2.0345` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3716` n `237` status `ready` deltaP `2.5797` edge `0.0216` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7247` n `237` status `ready` deltaP `-0.2388` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7442` n `237` status `ready` deltaP `-2.3895` edge `-0.0027` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9575` n `235` status `ready` deltaP `11.3279` edge `0.0081` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2269` n `237` status `ready` deltaP `2.8791` edge `0.0138` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2777` n `237` status `ready` deltaP `-2.8241` edge `-0.0155` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5757` n `237` status `ready` deltaP `-1.8312` edge `-0.029` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5858` n `223` status `ready` deltaP `-8.9134` edge `0.3059` maxDD `-18.3163`
- `market_context_high->commodity_4h` score `-1.6558` n `235` status `ready` deltaP `-4.424` edge `-0.0338` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8202` n `235` status `ready` deltaP `7.3644` edge `-0.0148` maxDD `-12.079`
- `market_context_high->equity_1h` score `-2.0334` n `237` status `ready` deltaP `1.9391` edge `-0.0182` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1276` n `235` status `ready` deltaP `3.3828` edge `0.003` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.0529` n `235` status `ready` deltaP `0.0285` edge `-0.023` maxDD `-21.487`
- `market_context_high->unknown_4h` score `-3.2713` n `235` status `ready` deltaP `-8.6021` edge `0.0213` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7058` n `223` status `ready` deltaP `-6.0736` edge `-0.0815` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.706` n `235` status `ready` deltaP `-1.3752` edge `-0.0518` maxDD `-23.466`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6589` n `235` status `ready` deltaP `3.8142` edge `-0.0975` maxDD `-65.7866`
- `market_context_high->metal_24h` score `-9.3668` n `223` status `ready` deltaP `-14.0062` edge `-0.1215` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
