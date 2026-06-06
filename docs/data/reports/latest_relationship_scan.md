# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T22:37:22.916436+00:00`
- Price records: `672`
- Market context records: `3119`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

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

- `market_context_high->commodity_24h` score `14.6347` n `97` status `ready` deltaP `46.798` edge `0.9504` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.5262` n `97` status `ready` deltaP `21.9377` edge `0.9464` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `12.4085` n `97` status `ready` deltaP `10.9625` edge `2.3536` maxDD `-58.2016`
- `market_context_high->index_24h` score `10.1597` n `97` status `ready` deltaP `31.3341` edge `0.8932` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.0967` n `97` status `ready` deltaP `13.0585` edge `1.3169` maxDD `-49.3761`
- `market_context_high->commodity_4h` score `2.9898` n `123` status `ready` deltaP `18.2927` edge `0.173` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0045` n `135` status `ready` deltaP `2.2777` edge `0.0267` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4354` n `135` status `ready` deltaP `4.6884` edge `0.0192` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5398` n `97` status `ready` deltaP `4.2723` edge `-0.0007` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7822` n `135` status `ready` deltaP `3.0572` edge `0.0923` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.057` n `135` status `ready` deltaP `0.5201` edge `0.0096` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1122` n `135` status `ready` deltaP `-10.4336` edge `-0.0055` maxDD `-0.736`
- `market_context_high->index_4h` score `-1.3697` n `123` status `ready` deltaP `10.3659` edge `0.0462` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4066` n `123` status `ready` deltaP `-13.4654` edge `-0.0062` maxDD `-1.0829`
- `market_context_high->crypto_major_1h` score `-2.1257` n `135` status `ready` deltaP `-0.5922` edge `0.0531` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2109` n `135` status `ready` deltaP `-5.6665` edge `-0.0071` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.3379` n `123` status `ready` deltaP `2.6931` edge `-0.0049` maxDD `-14.2968`
- `market_context_high->unknown_1h` score `-2.84` n `135` status `ready` deltaP `2.8454` edge `-0.053` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.8139` n `123` status `ready` deltaP `13.0081` edge `0.2288` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.9235` n `123` status `ready` deltaP `7.0122` edge `-0.0192` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
