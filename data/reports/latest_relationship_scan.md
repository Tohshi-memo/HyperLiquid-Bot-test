# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T05:37:23.434518+00:00`
- Price records: `672`
- Market context records: `2837`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.3929` n `142` status `ready` deltaP `3.2961` edge `0.2239` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `0.9215` n `142` status `ready` deltaP `0.4451` edge `0.4655` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.898` n `142` status `ready` deltaP `6.4904` edge `0.1369` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6997` n `142` status `ready` deltaP `11.0377` edge `0.2941` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3412` n `142` status `ready` deltaP `13.4533` edge `0.0382` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.037` n `142` status `ready` deltaP `4.3308` edge `0.0473` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1171` n `142` status `ready` deltaP `3.7489` edge `0.0094` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.325` n `142` status `ready` deltaP `3.9882` edge `0.0444` maxDD `-2.5127`
- `market_context_high->fx_1h` score `-0.5898` n `142` status `ready` deltaP `-1.1364` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6085` n `142` status `ready` deltaP `-0.2825` edge `-0.0008` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7464` n `142` status `ready` deltaP `-0.3163` edge `-0.009` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7638` n `142` status `ready` deltaP `4.4974` edge `0.0481` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.989` n `142` status `ready` deltaP `-3.0488` edge `0.0212` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9965` n `142` status `ready` deltaP `3.4769` edge `0.036` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.021` n `142` status `ready` deltaP `1.9624` edge `0.0398` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1567` n `142` status `ready` deltaP `-3.753` edge `0.0065` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3381` n `142` status `ready` deltaP `1.9903` edge `0.0072` maxDD `-10.0279`
- `market_context_high->crypto_alt_4h` score `-1.4623` n `142` status `ready` deltaP `13.7281` edge `0.2207` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5336` n `142` status `ready` deltaP `-2.9269` edge `-0.0211` maxDD `-0.6418`
- `market_context_high->equity_24h` score `-1.8017` n `142` status `ready` deltaP `1.7899` edge `0.0383` maxDD `-12.6963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
