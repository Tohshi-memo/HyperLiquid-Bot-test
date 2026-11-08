# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T17:37:31.452496+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5773`

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

- `market_context_high->unknown_4h` score `48.1064` n `39` status `ready` deltaP `-4.8116` edge `4.0857` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.933` n `37` status `ready` deltaP `14.025` edge `0.8304` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.4242` n `39` status `ready` deltaP `13.1852` edge `0.2434` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.783` n `39` status `ready` deltaP `29.8351` edge `0.042` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8857` n `39` status `ready` deltaP `24.789` edge `0.0389` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2125` n `39` status `ready` deltaP `14.3636` edge `0.0868` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1633` n `39` status `ready` deltaP `12.1181` edge `0.0747` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0354` n `37` status `ready` deltaP `12.7816` edge `0.1106` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.785` n `37` status `ready` deltaP `10.9422` edge `0.0013` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4944` n `39` status `ready` deltaP `8.1146` edge `0.0142` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.3011` n `37` status `ready` deltaP `3.4347` edge `0.1352` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2589` n `39` status `ready` deltaP `3.3779` edge `0.0377` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0613` n `39` status `ready` deltaP `7.9457` edge `0.0095` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0105` n `39` status `ready` deltaP `2.33` edge `0.0159` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1587` n `39` status `ready` deltaP `0.3401` edge `0.0228` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5907` n `39` status `ready` deltaP `23.1669` edge `0.0978` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9494` n `39` status `ready` deltaP `16.1664` edge `0.0148` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.9712` n `37` status `ready` deltaP `4.4013` edge `-0.1383` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8594` n `39` status `ready` deltaP `1.794` edge `-0.1086` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
