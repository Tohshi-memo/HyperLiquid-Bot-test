# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T16:36:12.274801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `128.8259` n `131` status `ready` deltaP `-33.1147` edge `11.2475` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7752` n `32` status `ready` deltaP `-46.3542` edge `4.586` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7752` n `32` status `ready` deltaP `-46.3542` edge `4.586` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.9197` n `36` status `ready` deltaP `11.4583` edge `0.7882` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3444` n `36` status `ready` deltaP `38.7195` edge `0.3539` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7462` n `32` status `ready` deltaP `32.1181` edge `0.1814` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7462` n `32` status `ready` deltaP `32.1181` edge `0.1814` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6257` n `131` status `ready` deltaP `27.5379` edge `0.223` maxDD `-0.6891`
- `risk_on_high->commodity_4h` score `2.8582` n `32` status `ready` deltaP `19.8933` edge `0.1238` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8582` n `32` status `ready` deltaP `19.8933` edge `0.1238` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.2796` n `32` status `ready` deltaP `17.7083` edge `0.2898` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2796` n `32` status `ready` deltaP `17.7083` edge `0.2898` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.1894` n `36` status `ready` deltaP `15.2778` edge `0.0806` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7613` n `36` status `ready` deltaP `20.5284` edge `0.0231` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.743` n `36` status `ready` deltaP `8.7326` edge `0.1189` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.6676` n `131` status `ready` deltaP `16.5775` edge `0.0757` maxDD `-0.7797`
- `risk_on_high->commodity_1h` score `1.321` n `32` status `ready` deltaP `13.9596` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.321` n `32` status `ready` deltaP `13.9596` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.123` n `32` status `ready` deltaP `13.3681` edge `0.0229` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.123` n `32` status `ready` deltaP `13.3681` edge `0.0229` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
