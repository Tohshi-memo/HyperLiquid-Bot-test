# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T20:37:24.372262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6469`

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

- `market_context_high->unknown_4h` score `76.3006` n `39` status `ready` deltaP `-4.6591` edge `6.4342` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.2815` n `37` status `ready` deltaP `11.9417` edge `0.79` maxDD `-31.3588`
- `market_context_high->equity_1h` score `2.6997` n `47` status `ready` deltaP `10.1733` edge `0.2031` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.6904` n `39` status `ready` deltaP `28.768` edge `0.0414` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.7896` n `39` status `ready` deltaP `23.7219` edge `0.038` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.131` n `37` status `ready` deltaP `14.1705` edge `0.1136` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8354` n `37` status `ready` deltaP `10.9422` edge `0.0055` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.6167` n `47` status `ready` deltaP `8.2813` edge `0.0777` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `0.4035` n `47` status `ready` deltaP `5.8861` edge `0.0571` maxDD `-3.0172`
- `market_context_high->index_1h` score `0.3904` n `47` status `ready` deltaP `4.2394` edge `0.0313` maxDD `-0.1621`
- `market_context_high->metal_1h` score `0.1965` n `47` status `ready` deltaP `5.4688` edge `0.0127` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.081` n `37` status `ready` deltaP `3.0875` edge `0.1093` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.0799` n `47` status `ready` deltaP `8.5584` edge `0.0078` maxDD `-1.7019`
- `market_context_high->fx_1h` score `-0.0634` n `47` status `ready` deltaP `1.7582` edge `0.0101` maxDD `-0.1681`
- `market_context_high->commodity_4h` score `-0.0671` n `39` status `ready` deltaP `1.7121` edge `0.0254` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6821` n `39` status `ready` deltaP `22.0998` edge `0.0932` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8142` n `39` status `ready` deltaP `-3.6664` edge `-0.0349` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9673` n `39` status `ready` deltaP `16.1664` edge `0.0125` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.7205` n `37` status `ready` deltaP `6.4847` edge `-0.1313` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8484` n `39` status `ready` deltaP `1.9465` edge `-0.1087` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
