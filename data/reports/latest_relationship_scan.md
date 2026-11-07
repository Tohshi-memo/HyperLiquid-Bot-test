# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T19:22:25.982967+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4357`

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

- `market_context_high->unknown_4h` score `120.1788` n `37` status `ready` deltaP `-8.5118` edge `10.1164` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4422` n `37` status `ready` deltaP `37.43` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1394` n `37` status `ready` deltaP `9.1601` edge `0.2465` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9099` n `37` status `ready` deltaP `25.136` edge `0.0386` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.611` n `52` status `ready` deltaP `9.0678` edge `0.0959` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8375` n `52` status `ready` deltaP `6.8363` edge `0.1357` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7376` n `37` status `ready` deltaP `9.3017` edge `0.058` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4155` n `37` status `ready` deltaP `10.649` edge `0.0638` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2789` n `52` status `ready` deltaP `9.4395` edge `0.0206` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2362` n `37` status `ready` deltaP `1.2017` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1986` n `52` status `ready` deltaP `6.851` edge `0.1466` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1452` n `52` status `ready` deltaP `8.22` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1335` n `37` status `ready` deltaP `9.3179` edge `0.0096` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0211` n `37` status `ready` deltaP `2.987` edge `0.0228` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.038` n `52` status `ready` deltaP `5.6195` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0583` n `37` status `ready` deltaP `1.3514` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2795` n `52` status `ready` deltaP `-0.046` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3181` n `52` status `ready` deltaP `-4.1456` edge `0.0418` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7857` n `37` status `ready` deltaP `21.3374` edge `0.085` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
