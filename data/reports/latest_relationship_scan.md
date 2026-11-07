# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T22:22:27.313416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4366`

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

- `market_context_high->unknown_4h` score `120.6213` n `37` status `ready` deltaP `-7.7496` edge `10.1482` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4666` n `37` status `ready` deltaP `37.7348` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2257` n `37` status `ready` deltaP `10.0583` edge `0.2477` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8721` n `37` status `ready` deltaP `24.6787` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.6979` n `52` status `ready` deltaP `10.1095` edge `0.0962` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8137` n `52` status `ready` deltaP `6.379` edge `0.1357` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7699` n `37` status `ready` deltaP `9.4514` edge `0.0597` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.496` n `37` status `ready` deltaP `7.9706` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4553` n `37` status `ready` deltaP `10.9484` edge `0.0669` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2543` n `52` status `ready` deltaP `8.9822` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2032` n `52` status `ready` deltaP `6.851` edge `0.1472` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1611` n `52` status `ready` deltaP `8.5248` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1163` n `37` status `ready` deltaP `9.0185` edge `0.0094` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0187` n `37` status `ready` deltaP `2.987` edge `0.0231` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0419` n `37` status `ready` deltaP `1.6508` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.2621` n `52` status `ready` deltaP `-3.2474` edge `0.043` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2951` n `52` status `ready` deltaP `-0.3454` edge `0.003` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.8095` n `37` status `ready` deltaP `20.8801` edge `0.085` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
