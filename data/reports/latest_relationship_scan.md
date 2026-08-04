# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T01:52:29.978109+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.4074` n `46` status `ready` deltaP `26.4719` edge `2.9451` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.2736` n `46` status `ready` deltaP `47.8186` edge `0.5547` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `9.877` n `76` status `ready` deltaP `9.716` edge `0.8057` maxDD `-1.4578`
- `market_context_high->commodity_24h` score `8.4702` n `46` status `ready` deltaP `40.3457` edge `0.4548` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0337` n `31` status `ready` deltaP `12.192` edge `0.0701` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.8804` n `76` status `ready` deltaP `12.2994` edge `0.076` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8509` n `31` status `ready` deltaP `18.6401` edge `0.006` maxDD `-0.6947`
- `market_context_high->fx_4h` score `0.3494` n `76` status `ready` deltaP `18.1643` edge `0.0097` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.3401` n `88` status `ready` deltaP `9.7782` edge `-0.002` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.3272` n `88` status `ready` deltaP `6.58` edge `0.025` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.06` n `31` status `ready` deltaP `3.5209` edge `0.0345` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.1887` n `31` status `ready` deltaP `0.4974` edge `-0.0077` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.218` n `31` status `ready` deltaP `9.943` edge `-0.0302` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.2648` n `31` status `ready` deltaP `8.5218` edge `-0.0288` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2901` n `31` status `ready` deltaP `-3.7225` edge `0.0387` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3307` n `31` status `ready` deltaP `-2.062` edge `0.0025` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4078` n `88` status `ready` deltaP `2.4769` edge `-0.0154` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.4723` n `88` status `ready` deltaP `-0.5716` edge `-0.0073` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.5098` n `31` status `ready` deltaP `-1.3621` edge `-0.0074` maxDD `-1.5766`
- `news_risk_high->equity_4h` score `-0.777` n `31` status `ready` deltaP `-16.9305` edge `0.1177` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
