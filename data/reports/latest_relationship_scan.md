# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T08:22:25.039432+00:00`
- Price records: `672`
- Market context records: `2848`
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

- `market_context_high->unknown_24h` score `2.7726` n `142` status `ready` deltaP `4.3378` edge `0.2486` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.5707` n `142` status `ready` deltaP `2.3548` edge `0.5902` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `0.9555` n `142` status `ready` deltaP `12.6002` edge `0.305` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8172` n `142` status `ready` deltaP `6.1856` edge `0.1322` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.3809` n `142` status `ready` deltaP `5.8979` edge `0.0905` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2662` n `142` status `ready` deltaP `12.3862` edge `0.0357` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0862` n `142` status `ready` deltaP `4.4805` edge `0.0504` maxDD `-3.1801`
- `market_context_high->equity_24h` score `0.0731` n `142` status `ready` deltaP `3.6996` edge `0.1818` maxDD `-12.6963`
- `market_context_high->index_1h` score `-0.0836` n `142` status `ready` deltaP `4.198` edge `0.0107` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.6437` n `142` status `ready` deltaP `-1.7352` edge `0.0023` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6529` n `142` status `ready` deltaP `-0.8813` edge `-0.0025` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6765` n `142` status `ready` deltaP `4.7968` edge `0.0573` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7027` n `142` status `ready` deltaP `0.1328` edge `-0.0064` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8788` n `142` status `ready` deltaP `3.926` edge `0.0481` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.8788` n `142` status `ready` deltaP `-2.1506` edge `0.0244` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.0836` n `142` status `ready` deltaP `1.8099` edge `0.0356` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2297` n `142` status `ready` deltaP `-4.5152` edge `0.0055` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3087` n `142` status `ready` deltaP `13.7281` edge `0.2335` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.3563` n `142` status `ready` deltaP `1.6854` edge `0.0069` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4107` n `142` status `ready` deltaP `-1.8852` edge `-0.0178` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
