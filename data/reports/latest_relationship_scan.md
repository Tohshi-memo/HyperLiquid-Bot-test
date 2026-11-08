# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T19:07:27.992605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5608`

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

- `market_context_high->unknown_4h` score `69.4798` n `39` status `ready` deltaP `-4.6591` edge `5.8658` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.6672` n `37` status `ready` deltaP `12.9833` edge `0.8152` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.5409` n `41` status `ready` deltaP `14.1631` edge `0.2466` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7038` n `39` status `ready` deltaP `28.9204` edge `0.0415` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.831` n `39` status `ready` deltaP `24.1792` edge `0.0384` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.5431` n `41` status `ready` deltaP `15.766` edge `0.105` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.3583` n `41` status `ready` deltaP `13.5205` edge `0.0816` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0961` n `37` status `ready` deltaP `13.6496` edge `0.1126` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8114` n `37` status `ready` deltaP `10.9422` edge `0.0035` maxDD `-0.0397`
- `market_context_high->index_1h` score `0.5249` n `41` status `ready` deltaP `5.0058` edge `0.0374` maxDD `-0.1621`
- `market_context_high->fx_1h` score `0.2633` n `41` status `ready` deltaP `5.4367` edge `0.0128` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.1824` n `37` status `ready` deltaP `3.0875` edge `0.1223` maxDD `-6.5601`
- `market_context_high->metal_1h` score `0.1296` n `41` status `ready` deltaP `4.2573` edge `0.0152` maxDD `-0.6226`
- `market_context_high->commodity_1h` score `-0.1065` n `41` status `ready` deltaP `5.3929` edge `0.005` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.1089` n `39` status `ready` deltaP `1.1023` edge `0.0241` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6404` n `39` status `ready` deltaP `22.5571` edge `0.0955` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7896` n `39` status `ready` deltaP `-3.2091` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9972` n `39` status `ready` deltaP `15.8615` edge `0.0107` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.8386` n `37` status `ready` deltaP `5.443` edge `-0.1342` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8872` n `39` status `ready` deltaP `1.6416` edge `-0.1099` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
