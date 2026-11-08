# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T20:22:27.523690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6461`

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

- `market_context_high->unknown_4h` score `70.1926` n `39` status `ready` deltaP `-4.6591` edge `5.9252` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.3542` n `37` status `ready` deltaP `12.1153` edge `0.7949` maxDD `-31.3588`
- `market_context_high->equity_1h` score `2.9497` n `46` status `ready` deltaP `11.3187` edge `0.2163` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.6782` n `39` status `ready` deltaP `28.6156` edge `0.0414` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.7762` n `39` status `ready` deltaP `23.5694` edge `0.0379` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1212` n `37` status `ready` deltaP `13.9968` edge `0.1135` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8318` n `37` status `ready` deltaP `10.9422` edge `0.0052` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.7584` n `46` status `ready` deltaP `9.2879` edge `0.0828` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `0.5784` n `46` status `ready` deltaP `6.8927` edge `0.0608` maxDD `-3.0172`
- `market_context_high->index_1h` score `0.4926` n `46` status `ready` deltaP `5.246` edge `0.0331` maxDD `-0.1621`
- `market_context_high->metal_1h` score `0.2915` n `46` status `ready` deltaP `6.5217` edge `0.0136` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.0981` n `37` status `ready` deltaP `3.0875` edge `0.1115` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.0405` n `46` status `ready` deltaP `7.8756` edge `0.0073` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0678` n `39` status `ready` deltaP `1.7121` edge `0.0253` maxDD `-1.633`
- `market_context_high->fx_1h` score `-0.123` n `46` status `ready` deltaP `0.9828` edge `0.0103` maxDD `-0.1681`
- `market_context_high->equity_4h` score `-0.6924` n `39` status `ready` deltaP `21.9473` edge `0.0929` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8157` n `39` status `ready` deltaP `-3.6664` edge `-0.0351` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9846` n `39` status `ready` deltaP `16.014` edge `0.0113` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.7392` n `37` status `ready` deltaP `6.311` edge `-0.1317` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8738` n `39` status `ready` deltaP `1.794` edge `-0.1098` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
