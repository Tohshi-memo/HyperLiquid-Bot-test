# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T23:22:23.498761+00:00`
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

- `market_context_high->unknown_4h` score `120.6779` n `37` status `ready` deltaP `-7.5972` edge `10.1519` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4666` n `37` status `ready` deltaP `37.7348` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1838` n `37` status `ready` deltaP `9.6092` edge `0.2472` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8721` n `37` status `ready` deltaP `24.6787` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.6979` n `52` status `ready` deltaP `10.1095` edge `0.0962` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8469` n `52` status `ready` deltaP `6.8363` edge `0.1369` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.722` n `37` status `ready` deltaP `9.152` edge `0.0577` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.5212` n `37` status `ready` deltaP `8.27` edge `0.0154` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4093` n `37` status `ready` deltaP `10.4993` edge `0.064` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.2614` n `37` status `ready` deltaP `1.5011` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.2543` n `52` status `ready` deltaP `8.9822` edge `0.0205` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2032` n `52` status `ready` deltaP `6.851` edge `0.1472` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1611` n `52` status `ready` deltaP `8.5248` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1163` n `37` status `ready` deltaP `9.0185` edge `0.0094` maxDD `-1.7019`
- `news_risk_high->index_1h` score `-0.0216` n `52` status `ready` deltaP `5.9189` edge `0.0031` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `-0.0282` n `37` status `ready` deltaP `2.8346` edge `0.0229` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0419` n `37` status `ready` deltaP `1.6508` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2788` n `52` status `ready` deltaP `-0.046` edge `0.0031` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2893` n `52` status `ready` deltaP `-3.6965` edge `0.0425` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7764` n `37` status `ready` deltaP `21.3374` edge `0.0862` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
