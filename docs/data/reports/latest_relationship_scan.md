# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T13:07:40.290346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->crypto_major_24h` score `3.0079` n `32` status `ready` deltaP `20.6597` edge `0.3635` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.0079` n `32` status `ready` deltaP `20.6597` edge `0.3635` maxDD `-6.2481`
- `risk_on_high->equity_24h` score `2.5776` n `32` status `ready` deltaP `6.9444` edge `0.4621` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `2.5776` n `32` status `ready` deltaP `6.9444` edge `0.4621` maxDD `-11.2348`
- `risk_on_high->commodity_4h` score `2.3249` n `32` status `ready` deltaP `15.7774` edge `0.1068` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3249` n `32` status `ready` deltaP `15.7774` edge `0.1068` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `2.1436` n `32` status `ready` deltaP `19.4444` edge `0.049` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.1436` n `32` status `ready` deltaP `19.4444` edge `0.049` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_high->index_24h` score `1.6129` n `32` status `ready` deltaP `14.0625` edge `0.0711` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.6129` n `32` status `ready` deltaP `14.0625` edge `0.0711` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.1257` n `32` status `ready` deltaP `12.3129` edge `0.035` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1257` n `32` status `ready` deltaP `12.3129` edge `0.035` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0023` n `32` status `ready` deltaP `11.5091` edge `0.0209` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0023` n `32` status `ready` deltaP `11.5091` edge `0.0209` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6901` n `178` status `ready` deltaP `9.855` edge `0.024` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5455` n `178` status `ready` deltaP `9.0007` edge `0.0493` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3109` n `32` status `ready` deltaP `10.1048` edge `0.01` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3109` n `32` status `ready` deltaP `10.1048` edge `0.01` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
