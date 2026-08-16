# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T17:07:27.559676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11814`

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

- `market_context_high->unknown_24h` score `221.156` n `88` status `ready` deltaP `-21.512` edge `28.7651` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.8937` n `88` status `ready` deltaP `41.3037` edge `0.3882` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4414` n `125` status `ready` deltaP `14.0744` edge `0.0734` maxDD `-0.7687`
- `market_context_high->fx_1h` score `-0.109` n `125` status `ready` deltaP `1.9018` edge `0.0015` maxDD `-0.2527`
- `market_context_high->commodity_1h` score `-0.131` n `125` status `ready` deltaP `1.6072` edge `0.0195` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.3024` n `125` status `ready` deltaP `4.3598` edge `0.0062` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5105` n `125` status `ready` deltaP `1.8036` edge `-0.0059` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7695` n `125` status `ready` deltaP `-6.5377` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8808` n `125` status `ready` deltaP `8.5902` edge `-0.0128` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3755` n `88` status `ready` deltaP `-6.9761` edge `0.0309` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6713` n `125` status `ready` deltaP `-9.7329` edge `-0.0454` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8625` n `88` status `ready` deltaP `-8.7437` edge `0.0707` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.8956` n `125` status `ready` deltaP `-0.9473` edge `-0.0177` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-1.9881` n `125` status `ready` deltaP `-4.5497` edge `-0.03` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.0728` n `125` status `ready` deltaP `-12.328` edge `-0.0093` maxDD `-0.8328`
- `market_context_high->index_24h` score `-2.1035` n `88` status `ready` deltaP `-6.9287` edge `-0.0695` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.6632` n `125` status `ready` deltaP `-0.9329` edge `-0.0633` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.965` n `88` status `ready` deltaP `-5.8712` edge `-0.0117` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1533` n `125` status `ready` deltaP `0.1521` edge `-0.5514` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.9935` n `125` status `ready` deltaP `-11.7524` edge `-0.0999` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
