# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T17:22:27.368931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `222.5538` n `88` status `ready` deltaP `-21.512` edge `28.9443` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.9177` n `88` status `ready` deltaP `41.3037` edge `0.3902` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.456` n `125` status `ready` deltaP `14.2268` edge `0.0736` maxDD `-0.7687`
- `market_context_high->fx_1h` score `-0.1168` n `125` status `ready` deltaP `1.7521` edge `0.0015` maxDD `-0.2527`
- `market_context_high->commodity_1h` score `-0.131` n `125` status `ready` deltaP `1.6072` edge `0.0195` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.3024` n `125` status `ready` deltaP `4.3598` edge `0.0062` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5183` n `125` status `ready` deltaP `1.6539` edge `-0.0059` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7695` n `125` status `ready` deltaP `-6.5377` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8808` n `125` status `ready` deltaP `8.5902` edge `-0.0128` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3724` n `88` status `ready` deltaP `-6.9761` edge `0.0313` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6713` n `125` status `ready` deltaP `-9.7329` edge `-0.0454` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8633` n `88` status `ready` deltaP `-8.7437` edge `0.0706` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.8789` n `125` status `ready` deltaP `-0.7976` edge `-0.0173` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.0001` n `125` status `ready` deltaP `-4.6994` edge `-0.03` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.0594` n `125` status `ready` deltaP `-12.1756` edge `-0.0092` maxDD `-0.8328`
- `market_context_high->index_24h` score `-2.1141` n `88` status `ready` deltaP `-7.1023` edge `-0.0697` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.6826` n `125` status `ready` deltaP `-1.0854` edge `-0.0639` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.9966` n `88` status `ready` deltaP `-6.0448` edge `-0.0146` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1713` n `125` status `ready` deltaP `0.0024` edge `-0.5519` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.9887` n `125` status `ready` deltaP `-11.7524` edge `-0.0995` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
