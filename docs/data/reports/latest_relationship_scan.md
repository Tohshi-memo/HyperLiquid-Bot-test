# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T01:22:26.760590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4416`

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

- `market_context_high->unknown_4h` score `120.8425` n `37` status `ready` deltaP `-7.4448` edge `10.1646` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4666` n `37` status `ready` deltaP `37.7348` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1921` n `37` status `ready` deltaP `9.7589` edge `0.2469` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8343` n `37` status `ready` deltaP `24.2213` edge `0.0384` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7432` n `52` status `ready` deltaP `10.6303` edge `0.0965` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.869` n `52` status `ready` deltaP `7.1412` edge `0.1377` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7699` n `37` status `ready` deltaP `9.6011` edge `0.0587` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.435` n `37` status `ready` deltaP `10.7987` edge `0.0653` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2298` n `52` status `ready` deltaP `8.5248` edge `0.0204` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2048` n `52` status `ready` deltaP `6.851` edge `0.1474` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.1979` n `37` status `ready` deltaP `0.7526` edge `0.0385` maxDD `-0.1621`
- `news_risk_high->fx_4h` score `0.1611` n `52` status `ready` deltaP `8.5248` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1459` n `37` status `ready` deltaP `9.4676` edge `0.0102` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0264` n `37` status `ready` deltaP `3.7492` edge `0.0238` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0342` n `37` status `ready` deltaP `1.8005` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0629` n `52` status `ready` deltaP `5.1704` edge `0.0028` maxDD `-0.2931`
- `news_risk_high->fx_1h` score `-0.2795` n `52` status `ready` deltaP `-0.046` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2839` n `52` status `ready` deltaP `-3.5468` edge `0.0422` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7543` n `37` status `ready` deltaP `21.6423` edge `0.087` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
