# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T08:07:29.139003+00:00`
- Price records: `672`
- Market context records: `2847`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.7059` n `142` status `ready` deltaP `4.1642` edge `0.2442` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.3876` n `142` status `ready` deltaP `2.1812` edge `0.5761` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.9152` n `142` status `ready` deltaP `12.4266` edge `0.3028` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8378` n `142` status `ready` deltaP `6.338` edge `0.1329` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.3142` n `142` status `ready` deltaP `5.7243` edge `0.0861` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2654` n `142` status `ready` deltaP `12.3862` edge `0.0356` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0862` n `142` status `ready` deltaP `4.4805` edge `0.0504` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0859` n `142` status `ready` deltaP `4.198` edge `0.0104` maxDD `-1.2855`
- `market_context_high->equity_24h` score `-0.098` n `142` status `ready` deltaP `3.526` edge `0.1687` maxDD `-12.6963`
- `market_context_high->fx_1h` score `-0.6305` n `142` status `ready` deltaP `-1.5855` edge `0.0024` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6428` n `142` status `ready` deltaP `-0.7316` edge `-0.0022` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.685` n `142` status `ready` deltaP `4.7968` edge `0.0562` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7019` n `142` status `ready` deltaP `0.1328` edge `-0.0063` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.886` n `142` status `ready` deltaP `-2.1506` edge `0.0238` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8866` n `142` status `ready` deltaP `3.926` edge `0.0471` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0932` n `142` status `ready` deltaP `1.8099` edge `0.0348` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2285` n `142` status `ready` deltaP `-4.5152` edge `0.0056` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3591` n `142` status `ready` deltaP `13.7281` edge `0.2293` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.3602` n `142` status `ready` deltaP `1.6854` edge `0.0064` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4119` n `142` status `ready` deltaP `-1.8852` edge `-0.0179` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
