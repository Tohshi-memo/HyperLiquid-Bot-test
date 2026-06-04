# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T02:52:21.668030+00:00`
- Price records: `672`
- Market context records: `2825`
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

- `market_context_high->unknown_24h` score `2.3495` n `142` status `ready` deltaP `2.9489` edge `0.2226` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.911` n `142` status `ready` deltaP `6.338` edge `0.139` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.8509` n `142` status `ready` deltaP `12.253` edge `0.2986` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.3186` n `142` status `ready` deltaP `-0.5966` edge `0.4222` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.2879` n `142` status `ready` deltaP `13.1484` edge `0.0334` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1198` n `142` status `ready` deltaP `4.7799` edge `0.0512` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0828` n `142` status `ready` deltaP `4.198` edge `0.0108` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5564` n `142` status `ready` deltaP `0.466` edge `0.0009` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5622` n `142` status `ready` deltaP `-0.837` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6024` n `142` status `ready` deltaP `5.2459` edge `0.0638` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7292` n `142` status `ready` deltaP `-0.0169` edge `-0.0088` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8749` n `142` status `ready` deltaP `3.926` edge `0.0486` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9494` n `142` status `ready` deltaP `-2.8991` edge `0.0235` maxDD `-2.6634`
- `market_context_high->index_24h` score `-1.079` n `142` status `ready` deltaP `2.0785` edge `-0.0057` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.1204` n `142` status `ready` deltaP `2.1148` edge `0.0305` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1957` n `142` status `ready` deltaP `-4.2103` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2973` n `142` status `ready` deltaP `2.2951` edge `0.0104` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6886` n `142` status `ready` deltaP `-4.4894` edge `-0.0236` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.8699` n `142` status `ready` deltaP `13.1183` edge `0.1908` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.4491` n `142` status `ready` deltaP `-1.6854` edge `-0.0477` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
