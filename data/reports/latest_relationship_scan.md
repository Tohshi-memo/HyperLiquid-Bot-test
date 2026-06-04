# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T22:22:21.513220+00:00`
- Price records: `672`
- Market context records: `2909`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `12.015` n `142` status `ready` deltaP `11.209` edge `1.3182` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.2653` n `142` status `ready` deltaP `13.4218` edge `0.633` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.4727` n `142` status `ready` deltaP `11.6295` edge `0.425` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1898` n `142` status `ready` deltaP `10.2382` edge `0.2123` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7796` n `142` status `ready` deltaP `15.5516` edge `0.354` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4712` n `142` status `ready` deltaP `13.1484` edge `0.0569` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.1977` n `142` status `ready` deltaP `6.2307` edge `0.1129` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.0879` n `142` status `ready` deltaP `4.5087` edge `0.0826` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0687` n `142` status `ready` deltaP `3.7489` edge `0.0156` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3361` n `142` status `ready` deltaP `4.0314` edge `0.0182` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.3733` n `142` status `ready` deltaP `15.1` edge `0.3023` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-0.4747` n `142` status `ready` deltaP `0.0949` edge `0.0431` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4964` n `142` status `ready` deltaP `5.695` edge `0.0744` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.579` n `142` status `ready` deltaP `-0.9867` edge `0.0027` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5921` n `142` status `ready` deltaP `-0.4322` edge `0.0023` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6271` n `142` status `ready` deltaP `5.8721` edge `0.0674` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6723` n `142` status `ready` deltaP `-0.3163` edge `0.0005` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0288` n `142` status `ready` deltaP `-2.2286` edge `0.007` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2339` n `142` status `ready` deltaP `2.4476` edge `0.0175` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2876` n `142` status `ready` deltaP `-1.7116` edge `-0.0087` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
