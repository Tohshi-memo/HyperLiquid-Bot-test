# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T03:07:23.144945+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4428`

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

- `market_context_high->unknown_4h` score `121.0509` n `37` status `ready` deltaP `-6.835` edge `10.1779` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3776` n `37` status `ready` deltaP `36.6678` edge `0.046` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2197` n `37` status `ready` deltaP `10.0583` edge `0.2472` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8745` n `37` status `ready` deltaP `24.6787` edge `0.0387` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7576` n `52` status `ready` deltaP `10.6303` edge `0.0977` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8894` n `52` status `ready` deltaP `7.2936` edge `0.1393` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7699` n `37` status `ready` deltaP `9.6011` edge `0.0587` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4948` n `37` status `ready` deltaP `7.9706` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4413` n `37` status `ready` deltaP `10.7987` edge `0.0661` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2559` n `52` status `ready` deltaP `8.9822` edge `0.0207` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2259` n `52` status `ready` deltaP `6.851` edge `0.1501` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1101` n `37` status `ready` deltaP `8.8688` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.1033` n `52` status `ready` deltaP `7.4578` edge `0.0074` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0707` n `37` status `ready` deltaP `4.5114` edge `0.0244` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0178` n `37` status `ready` deltaP `2.0999` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.266` n `52` status `ready` deltaP `-3.2474` edge `0.0425` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2959` n `52` status `ready` deltaP `-0.3454` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7339` n `37` status `ready` deltaP `21.7947` edge `0.0886` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
