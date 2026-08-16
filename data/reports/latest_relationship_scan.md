# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T11:52:25.150583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `199.7466` n `88` status `ready` deltaP `-21.512` edge `26.0203` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5385` n `88` status `ready` deltaP `41.3037` edge `0.3586` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.8358` n `117` status `ready` deltaP `17.8641` edge `0.081` maxDD `-0.7687`
- `market_context_high->fx_4h` score `-0.0761` n `117` status `ready` deltaP `6.4806` edge `0.0075` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.0771` n `125` status `ready` deltaP `2.206` edge `0.02` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5362` n `125` status `ready` deltaP `1.3545` edge `-0.0062` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8022` n `125` status `ready` deltaP `-7.1365` edge `-0.0031` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-1.05` n `117` status `ready` deltaP `5.6807` edge `-0.0151` maxDD `-4.5909`
- `market_context_high->index_4h` score `-1.3014` n `117` status `ready` deltaP `-11.4303` edge `-0.0094` maxDD `-0.8328`
- `market_context_high->fx_24h` score `-1.6271` n `88` status `ready` deltaP `-10.4483` edge `0.0218` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-1.6442` n `88` status `ready` deltaP `-5.4451` edge `0.0767` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-1.7001` n `125` status `ready` deltaP `-10.182` edge `-0.0461` maxDD `-4.9849`
- `market_context_high->index_24h` score `-1.9737` n `88` status `ready` deltaP `-4.6717` edge `-0.0679` maxDD `-2.3194`
- `market_context_high->crypto_major_1h` score `-2.0193` n `125` status `ready` deltaP `-4.6994` edge `-0.0316` maxDD `-5.4277`
- `market_context_high->crypto_alt_1h` score `-2.0263` n `125` status `ready` deltaP `-1.8455` edge `-0.0226` maxDD `-7.0497`
- `market_context_high->crypto_major_4h` score `-2.2849` n `117` status `ready` deltaP `1.8919` edge `-0.0698` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6432` n `88` status `ready` deltaP `-3.267` edge `0.0122` maxDD `-35.189`
- `market_context_high->equity_4h` score `-5.4015` n `117` status `ready` deltaP `-29.0143` edge `-0.1945` maxDD `-15.3661`
- `market_context_high->unknown_1h` score `-7.206` n `125` status `ready` deltaP `-0.4467` edge `-0.5518` maxDD `-1.3246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
