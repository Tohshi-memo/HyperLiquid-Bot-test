# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T19:22:34.837039+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8078`

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

- `market_context_high->unknown_4h` score `93.6063` n `153` status `ready` deltaP `1.0172` edge `7.8273` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.6236` n `153` status `ready` deltaP `1.6242` edge `2.4234` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3644` n `112` status `ready` deltaP `25.1485` edge `0.1417` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2674` n `153` status `ready` deltaP `8.2648` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1006` n `153` status `ready` deltaP `9.0198` edge `0.0081` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0066` n `112` status `ready` deltaP `16.3051` edge `0.0143` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1221` n `153` status `ready` deltaP `8.4801` edge `0.007` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1748` n `112` status `ready` deltaP `16.2788` edge `0.0263` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.275` n `153` status `ready` deltaP `2.1526` edge `0.0128` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5673` n `153` status `ready` deltaP `0.3121` edge `-0.0011` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.7264` n `153` status `ready` deltaP `3.9245` edge `0.0362` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9059` n `153` status `ready` deltaP `3.9343` edge `0.0157` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9369` n `153` status `ready` deltaP `7.6648` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7894` n `153` status `ready` deltaP `1.7543` edge `-0.0135` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0045` n `153` status `ready` deltaP `-0.725` edge `-0.0037` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3533` n `153` status `ready` deltaP `-5.7747` edge `-0.0233` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4278` n `112` status `ready` deltaP `-2.6182` edge `-0.0645` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6054` n `153` status `ready` deltaP `-0.4583` edge `-0.0834` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.2063` n `112` status `ready` deltaP `-4.2569` edge `-0.224` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.2579` n `112` status `ready` deltaP `-16.2107` edge `-0.1353` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
