# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T10:07:23.720397+00:00`
- Price records: `672`
- Market context records: `3062`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.7422` n `92` status `ready` deltaP `11.8207` edge `2.4593` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.4323` n `92` status `ready` deltaP `45.9089` edge `0.9207` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.3797` n `92` status `ready` deltaP `23.362` edge `1.0057` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.4128` n `92` status `ready` deltaP `29.212` edge `0.8527` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.3065` n `92` status `ready` deltaP `24.2904` edge `1.4346` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4425` n `126` status `ready` deltaP `16.703` edge `0.1569` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.2687` n `129` status `ready` deltaP `-0.1845` edge `0.0211` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3229` n `126` status `ready` deltaP `2.5697` edge `0.0613` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5744` n `129` status `ready` deltaP `2.6598` edge `0.0149` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6246` n `129` status `ready` deltaP `-6.1667` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7477` n `129` status `ready` deltaP `3.5847` edge `0.0932` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7906` n `92` status `ready` deltaP `-0.536` edge `-0.0106` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.0069` n `129` status `ready` deltaP `2.6969` edge `-0.0288` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.072` n `129` status `ready` deltaP `0.564` edge `0.0042` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.0939` n `129` status `ready` deltaP `2.2269` edge `0.0712` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2126` n `126` status `ready` deltaP `-9.8336` edge `-0.0057` maxDD `-1.0693`
- `market_context_high->metal_1h` score `-1.3011` n `129` status `ready` deltaP `-3.6752` edge `-0.0055` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3404` n `126` status `ready` deltaP `9.519` edge `0.0556` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.9245` n `126` status `ready` deltaP `18.5758` edge `0.3057` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.4668` n `126` status `ready` deltaP `7.9051` edge `0.0153` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
