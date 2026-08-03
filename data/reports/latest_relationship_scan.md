# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T23:52:32.605948+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `37.4076` n `46` status `ready` deltaP `26.8192` edge `2.9428` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `12.0493` n `68` status `ready` deltaP `12.1951` edge `0.9702` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.3493` n `46` status `ready` deltaP `48.1658` edge `0.5587` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.6341` n `46` status `ready` deltaP `41.7346` edge `0.4592` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0421` n `31` status `ready` deltaP `12.192` edge `0.0708` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8937` n `31` status `ready` deltaP `19.2389` edge `0.0075` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.5432` n `68` status `ready` deltaP `9.0297` edge `0.0697` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.4804` n `68` status `ready` deltaP `20.7137` edge `0.0095` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.3455` n `80` status `ready` deltaP `11.9012` edge `-0.0002` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.1773` n `80` status `ready` deltaP `5.247` edge `0.0214` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0813` n `31` status `ready` deltaP `3.8257` edge `0.0352` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.1336` n `31` status `ready` deltaP `9.7413` edge `-0.026` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1622` n `31` status `ready` deltaP `0.9465` edge `-0.0073` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.204` n `31` status `ready` deltaP `9.943` edge `-0.0284` maxDD `-3.1233`
- `news_risk_high->index_4h` score `-0.2344` n `31` status `ready` deltaP `-3.2651` edge `0.0403` maxDD `-0.3783`
- `market_context_high->index_1h` score `-0.2419` n `80` status `ready` deltaP `4.8578` edge `-0.01` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3408` n `31` status `ready` deltaP `-2.2117` edge `0.0022` maxDD `-0.1588`
- `market_context_high->metal_1h` score `-0.5053` n `80` status `ready` deltaP `-0.9955` edge `-0.0087` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.5193` n `31` status `ready` deltaP `-1.5146` edge `-0.0076` maxDD `-1.5766`
- `news_risk_high->equity_4h` score `-0.6372` n `31` status `ready` deltaP `-16.4732` edge `0.1263` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
