# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T14:37:33.709822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4779`

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

- `market_context_high->unknown_4h` score `43.3674` n `38` status `ready` deltaP `-4.5892` edge `3.6893` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1365` n `37` status `ready` deltaP `15.4139` edge `0.8381` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3404` n `39` status `ready` deltaP `12.287` edge `0.2424` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.9789` n `38` status `ready` deltaP `32.0443` edge `0.0436` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0097` n `38` status `ready` deltaP `26.2035` edge `0.0398` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2664` n `39` status `ready` deltaP `14.9624` edge `0.0873` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1848` n `39` status `ready` deltaP `12.5672` edge `0.0735` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8932` n `37` status `ready` deltaP `10.8718` edge `0.1051` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.731` n `37` status `ready` deltaP `10.9422` edge `-0.0032` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.5779` n `37` status `ready` deltaP `5.5181` edge `0.1568` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2254` n `39` status `ready` deltaP `2.7791` edge `0.0374` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0738` n `39` status `ready` deltaP `8.0954` edge `0.0101` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0362` n `39` status `ready` deltaP `1.8809` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1781` n `38` status `ready` deltaP `0.1926` edge `0.0213` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6385` n `38` status `ready` deltaP `22.7294` edge `0.0946` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7663` n `38` status `ready` deltaP `-2.6717` edge `-0.0354` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.7934` n `38` status `ready` deltaP `17.6508` edge `0.0249` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.2326` n `37` status `ready` deltaP `2.318` edge `-0.1462` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-4.0502` n `38` status `ready` deltaP `0.8344` edge `-0.1181` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
