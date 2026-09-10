# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T06:37:29.830944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10940`

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

- `risk_on_high->crypto_alt_24h` score `14.005` n `92` status `ready` deltaP `30.8499` edge `0.9844` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.005` n `92` status `ready` deltaP `30.8499` edge `0.9844` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.1788` n `214` status `ready` deltaP `23.2006` edge `0.7763` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.4192` n `92` status `ready` deltaP `38.0302` edge `0.4019` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.4192` n `92` status `ready` deltaP `38.0302` edge `0.4019` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.4135` n `92` status `ready` deltaP `26.9088` edge `0.3576` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.4135` n `92` status `ready` deltaP `26.9088` edge `0.3576` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0246` n `92` status `ready` deltaP `20.0332` edge `0.7892` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0246` n `92` status `ready` deltaP `20.0332` edge `0.7892` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.8676` n `92` status `ready` deltaP `31.6349` edge `0.0323` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8676` n `92` status `ready` deltaP `31.6349` edge `0.0323` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6895` n `214` status `ready` deltaP `15.7986` edge `0.1188` maxDD `0.0`
- `market_context_high->index_24h` score `2.3929` n `214` status `ready` deltaP `26.4846` edge `0.0622` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.8232` n `92` status `ready` deltaP `17.1271` edge `0.0471` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8232` n `92` status `ready` deltaP `17.1271` edge `0.0471` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.7956` n `92` status `ready` deltaP `25.1657` edge `-0.0072` maxDD `-0.2082`
- `risk_on_and_context->equity_4h` score `1.7956` n `92` status `ready` deltaP `25.1657` edge `-0.0072` maxDD `-0.2082`
- `risk_on_high->equity_1h` score `1.1001` n `92` status `ready` deltaP `17.5541` edge `0.0025` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1001` n `92` status `ready` deltaP `17.5541` edge `0.0025` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.0032` n `92` status `ready` deltaP `3.7556` edge `0.0938` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
