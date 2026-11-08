# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T13:52:28.834831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `57.1951` n `37` status `ready` deltaP `-5.1582` edge `4.8454` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1317` n `37` status `ready` deltaP `15.4139` edge `0.8377` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3368` n `39` status `ready` deltaP `12.287` edge `0.2421` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1595` n `37` status `ready` deltaP `34.0763` edge `0.0451` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.1644` n `37` status `ready` deltaP `28.0323` edge `0.0405` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2316` n `39` status `ready` deltaP `14.8127` edge `0.0854` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1261` n `39` status `ready` deltaP `12.1181` edge `0.0716` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8732` n `37` status `ready` deltaP `10.6982` edge `0.1037` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7142` n `37` status `ready` deltaP `10.9422` edge `-0.0046` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.6315` n `37` status `ready` deltaP `6.0389` edge `0.1602` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.4956` n `39` status `ready` deltaP `8.1146` edge `0.0143` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2091` n `39` status `ready` deltaP `2.4797` edge `0.0373` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0652` n `39` status `ready` deltaP `7.9457` edge `0.01` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0362` n `39` status `ready` deltaP `1.8809` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0781` n `37` status `ready` deltaP `1.92` edge `0.0226` maxDD `-1.633`
- `market_context_high->crypto_alt_4h` score `-0.6863` n `37` status `ready` deltaP `19.2156` edge `0.0282` maxDD `-17.5435`
- `market_context_high->metal_4h` score `-0.7042` n `37` status `ready` deltaP `-1.4626` edge `-0.0355` maxDD `-0.9363`
- `market_context_high->equity_4h` score `-0.7197` n `37` status `ready` deltaP `21.9471` edge `0.0894` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-2.2501` n `37` status `ready` deltaP `2.1444` edge `-0.1465` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-4.3169` n `37` status `ready` deltaP `-0.3544` edge `-0.1324` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
