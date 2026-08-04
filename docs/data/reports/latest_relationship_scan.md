# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T01:37:29.607025+00:00`
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

- `market_context_high->unknown_24h` score `37.4273` n `46` status `ready` deltaP `26.6455` edge `2.9456` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.3078` n `46` status `ready` deltaP `47.9922` edge `0.5564` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `10.2398` n `75` status `ready` deltaP `10.6809` edge `0.8295` maxDD `-1.4578`
- `market_context_high->commodity_24h` score `8.49` n `46` status `ready` deltaP `40.5193` edge `0.4553` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0361` n `31` status `ready` deltaP `12.192` edge `0.0703` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8516` n `31` status `ready` deltaP `18.6401` edge `0.0061` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.8411` n `75` status `ready` deltaP `11.9431` edge `0.0751` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.391` n `75` status `ready` deltaP `18.9187` edge `0.01` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.3892` n `87` status `ready` deltaP `7.22` edge `0.0259` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.3131` n `87` status `ready` deltaP `9.4707` edge `-0.0022` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.0608` n `31` status `ready` deltaP `3.5209` edge `0.0346` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.1778` n `31` status `ready` deltaP `0.6471` edge `-0.0073` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2141` n `31` status `ready` deltaP `9.943` edge `-0.0297` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.2502` n `31` status `ready` deltaP `8.6743` edge `-0.0286` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2731` n `31` status `ready` deltaP `-3.57` edge `0.0391` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3221` n `31` status `ready` deltaP `-1.9123` edge `0.0026` maxDD `-0.1588`
- `market_context_high->metal_1h` score `-0.5063` n `87` status `ready` deltaP `-0.9705` edge `-0.009` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.509` n `31` status `ready` deltaP `-1.3621` edge `-0.0073` maxDD `-1.5766`
- `market_context_high->index_1h` score `-0.6744` n `87` status `ready` deltaP `2.1302` edge `-0.017` maxDD `-1.6054`
- `news_risk_high->equity_4h` score `-0.7456` n `31` status `ready` deltaP `-16.7781` edge `0.1193` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
