# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T15:07:47.320400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4793`

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

- `market_context_high->unknown_4h` score `30.1466` n `39` status `ready` deltaP `-4.3543` edge `2.586` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1509` n `37` status `ready` deltaP `15.4139` edge `0.8393` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3524` n `39` status `ready` deltaP `12.4367` edge `0.2424` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7952` n `39` status `ready` deltaP `29.9875` edge `0.042` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8625` n `39` status `ready` deltaP `24.4841` edge `0.039` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2448` n `39` status `ready` deltaP `14.8127` edge `0.0865` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1692` n `39` status `ready` deltaP `12.4175` edge `0.0732` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9092` n `37` status `ready` deltaP `11.0455` edge `0.106` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7406` n `37` status `ready` deltaP `10.9422` edge `-0.0024` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.5341` n `37` status `ready` deltaP `5.1708` edge `0.1535` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.234` n `39` status `ready` deltaP `2.9288` edge `0.0375` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0816` n `39` status `ready` deltaP `8.2451` edge `0.0101` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0362` n `39` status `ready` deltaP `1.8809` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1144` n `39` status `ready` deltaP `1.1023` edge `0.0234` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5876` n `39` status `ready` deltaP `23.1669` edge `0.0982` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8165` n `39` status `ready` deltaP `-3.6664` edge `-0.0352` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9026` n `39` status `ready` deltaP `16.1664` edge `0.0208` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.1941` n `37` status `ready` deltaP `2.6652` edge `-0.1453` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8064` n `39` status `ready` deltaP `1.9465` edge `-0.1052` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
