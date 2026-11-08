# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T17:52:25.386539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5903`

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

- `market_context_high->unknown_4h` score `54.1642` n `39` status `ready` deltaP `-4.6591` edge `4.5895` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.8987` n `37` status `ready` deltaP `13.8514` edge `0.8287` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.4111` n `39` status `ready` deltaP `13.0355` edge `0.2433` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7696` n `39` status `ready` deltaP `29.6826` edge `0.0419` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8845` n `39` status `ready` deltaP `24.789` edge `0.0388` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2137` n `39` status `ready` deltaP `14.3636` edge `0.0869` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1633` n `39` status `ready` deltaP `12.1181` edge `0.0747` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0475` n `37` status `ready` deltaP `12.9552` edge `0.111` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7886` n `37` status `ready` deltaP `10.9422` edge `0.0016` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4824` n `39` status `ready` deltaP `7.9649` edge `0.0142` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.2749` n `37` status `ready` deltaP `3.2611` edge `0.133` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2511` n `39` status `ready` deltaP `3.2282` edge `0.0377` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0613` n `39` status `ready` deltaP `7.9457` edge `0.0095` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0113` n `39` status `ready` deltaP `2.33` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1587` n `39` status `ready` deltaP `0.3401` edge `0.0228` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5915` n `39` status `ready` deltaP `23.1669` edge `0.0977` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9517` n `39` status `ready` deltaP `16.1664` edge `0.0145` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.9477` n `37` status `ready` deltaP `4.5749` edge `-0.1375` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8606` n `39` status `ready` deltaP `1.794` edge `-0.1087` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
