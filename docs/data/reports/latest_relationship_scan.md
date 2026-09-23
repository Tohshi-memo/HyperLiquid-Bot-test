# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T16:37:36.857183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_1h` score `80.6036` n `47` status `ready` deltaP `9.5172` edge `6.6606` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `31.3461` n `46` status `ready` deltaP `17.0064` edge `2.5144` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.739` n `46` status `ready` deltaP `14.4022` edge `1.3923` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.7671` n `46` status `ready` deltaP `11.9792` edge `1.0674` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.6525` n `96` status `ready` deltaP `-5.7291` edge `1.2784` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.0107` n `46` status `ready` deltaP `23.43` edge `0.3534` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.8676` n `103` status `ready` deltaP `15.756` edge `0.275` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.2519` n `103` status `ready` deltaP `10.5731` edge `0.3003` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.1354` n `96` status `ready` deltaP `28.6458` edge `0.1882` maxDD `-2.431`
- `market_context_high->index_4h` score `2.5092` n `46` status `ready` deltaP `29.1092` edge `0.0284` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.2452` n `103` status `ready` deltaP `12.1098` edge `0.1554` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.903` n `103` status `ready` deltaP `15.2535` edge `0.1004` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3351` n `46` status `ready` deltaP `9.6633` edge `0.0775` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2677` n `103` status `ready` deltaP `19.5655` edge `0.0388` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1771` n `96` status `ready` deltaP `28.2986` edge `0.1212` maxDD `-1.7159`
- `news_risk_high->crypto_alt_24h` score `0.8762` n `96` status `ready` deltaP `-7.8125` edge `0.6132` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.684` n `47` status `ready` deltaP `11.4664` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6554` n `103` status `ready` deltaP `15.2026` edge `0.0126` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.5371` n `46` status `ready` deltaP `17.4064` edge `-0.0479` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.4009` n `47` status `ready` deltaP `7.1251` edge `0.0262` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
