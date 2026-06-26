# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T04:22:28.242208+00:00`
- Price records: `672`
- Market context records: `4792`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.6975` n `122` status `ready` deltaP `18.72` edge `0.6377` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.5001` n `122` status `ready` deltaP `12.5798` edge `0.5829` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.1053` n `109` status `ready` deltaP `12.0859` edge `0.1872` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1501` n `122` status `ready` deltaP `5.8309` edge `0.0324` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0597` n `122` status `ready` deltaP `11.8153` edge `0.0461` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.1279` n `122` status `ready` deltaP `8.2342` edge `0.0973` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.367` n `122` status `ready` deltaP `6.9947` edge `0.0132` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4511` n `122` status `ready` deltaP `2.6689` edge `0.002` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7331` n `122` status `ready` deltaP `1.4185` edge `0.0062` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9232` n `122` status `ready` deltaP `-1.3326` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3788` n `122` status `ready` deltaP `-1.3473` edge `-0.0055` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2404` n `109` status `ready` deltaP `19.1323` edge `0.0961` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2532` n `122` status `ready` deltaP `-0.7976` edge `-0.066` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.1556` n `122` status `ready` deltaP `0.8982` edge `-0.045` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.3608` n `109` status `ready` deltaP `-15.4355` edge `-0.0222` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4899` n `122` status `ready` deltaP `0.6847` edge `-0.0697` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.7657` n `122` status `ready` deltaP `4.898` edge `-0.0012` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.9629` n `109` status `ready` deltaP `-6.1147` edge `-0.1094` maxDD `-19.7393`
- `market_context_high->crypto_major_4h` score `-8.059` n `122` status `ready` deltaP `3.6585` edge `-0.1345` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3298` n `122` status `ready` deltaP `6.3825` edge `-0.2864` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
