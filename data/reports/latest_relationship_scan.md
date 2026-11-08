# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T22:07:28.754432+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6515`

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

- `market_context_high->unknown_4h` score `64.6482` n `41` status `ready` deltaP `-3.6585` edge `5.4565` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.89` n `37` status `ready` deltaP `11.2472` edge `0.762` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.2382` n `41` status `ready` deltaP `25.1525` edge `0.0371` maxDD `-0.128`
- `market_context_high->index_4h` score `1.5133` n `41` status `ready` deltaP `20.8841` edge `0.0339` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1651` n `37` status `ready` deltaP `14.6913` edge `0.1145` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8666` n `37` status `ready` deltaP `10.9422` edge `0.0081` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.7126` n `53` status `ready` deltaP `4.3272` edge `0.1429` maxDD `-3.4309`
- `market_context_high->commodity_1h` score `0.2237` n `53` status `ready` deltaP `10.7078` edge `0.0119` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.035` n `53` status `ready` deltaP `3.2793` edge `0.008` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.0439` n `37` status `ready` deltaP `2.7403` edge `0.0956` maxDD `-6.5601`
- `market_context_high->commodity_4h` score `-0.0936` n `41` status `ready` deltaP `1.9817` edge `0.0244` maxDD `-1.633`
- `market_context_high->index_1h` score `-0.234` n `53` status `ready` deltaP `-1.3332` edge `0.0222` maxDD `-0.4645`
- `market_context_high->fx_1h` score `-0.6113` n `53` status `ready` deltaP `-4.5955` edge `0.0068` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `-0.7561` n `53` status `ready` deltaP `3.0081` edge `-0.0018` maxDD `-5.2157`
- `market_context_high->metal_4h` score `-0.9175` n `41` status `ready` deltaP `-5.4878` edge `-0.036` maxDD `-0.9363`
- `market_context_high->crypto_major_1h` score `-1.1351` n `53` status `ready` deltaP `0.6129` edge `-0.0292` maxDD `-5.6328`
- `market_context_high->equity_4h` score `-1.5528` n `41` status `ready` deltaP `19.5122` edge `0.0685` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.606` n `37` status `ready` deltaP `7.5263` edge `-0.1287` maxDD `-1.4245`
- `market_context_high->crypto_alt_4h` score `-2.5101` n `41` status `ready` deltaP `13.2622` edge `-0.0533` maxDD `-17.5435`
- `market_context_high->crypto_major_4h` score `-4.8722` n `41` status `ready` deltaP `0.6097` edge `-0.1851` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
