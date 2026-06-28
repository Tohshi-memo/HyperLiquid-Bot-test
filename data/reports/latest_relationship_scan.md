# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T03:07:27.288255+00:00`
- Price records: `672`
- Market context records: `5000`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.6907` n `93` status `ready` deltaP `4.2673` edge `1.3292` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `5.9076` n `88` status `ready` deltaP `17.2256` edge `0.5359` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `5.8777` n `74` status `ready` deltaP `29.8142` edge `0.3253` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.0589` n `88` status `ready` deltaP `12.0704` edge `0.4805` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `2.8746` n `88` status `ready` deltaP `21.3553` edge `0.1994` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1455` n `88` status `ready` deltaP `11.5577` edge `0.1263` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8764` n `93` status `ready` deltaP `6.7027` edge `0.1201` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.8752` n `93` status `ready` deltaP `8.1868` edge `0.0757` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6644` n `88` status `ready` deltaP `5.7788` edge `0.1848` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.3781` n `88` status `ready` deltaP `6.25` edge `0.0432` maxDD `-0.935`
- `market_context_high->metal_1h` score `0.3736` n `93` status `ready` deltaP `6.4033` edge `0.0381` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1882` n `93` status `ready` deltaP `5.2604` edge `0.0913` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2012` n `74` status `ready` deltaP `6.7803` edge `0.0052` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3026` n `93` status `ready` deltaP `2.0073` edge `0.0138` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5682` n `93` status `ready` deltaP `2.062` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8334` n `88` status `ready` deltaP `3.617` edge `-0.0057` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.8389` n `88` status `ready` deltaP `-1.4413` edge `-0.0009` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.1143` n `74` status `ready` deltaP `6.3157` edge `-0.0587` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.16` n `74` status `ready` deltaP `0.1736` edge `0.011` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
