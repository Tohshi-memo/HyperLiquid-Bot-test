# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T06:37:28.049816+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4786`

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

- `market_context_high->unknown_4h` score `122.9363` n `37` status `ready` deltaP `-4.8533` edge `10.3218` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.3059` n `37` status `ready` deltaP `10.9565` edge `0.2484` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.285` n `37` status `ready` deltaP `35.6007` edge `0.0454` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.9939` n `37` status `ready` deltaP `26.0506` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.808` n `52` status `ready` deltaP `10.6303` edge `0.1019` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9705` n `52` status `ready` deltaP `8.2082` edge `0.1436` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.8011` n `37` status `ready` deltaP `9.9005` edge `0.0593` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.52` n `37` status `ready` deltaP `11.6969` edge `0.0702` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4338` n `37` status `ready` deltaP `7.2221` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.3335` n `52` status `ready` deltaP `10.3541` edge `0.0215` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.3213` n `37` status `ready` deltaP `2.2496` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2836` n `52` status `ready` deltaP `6.851` edge `0.1575` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1529` n `37` status `ready` deltaP `9.6173` edge `0.0101` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1443` n `55` status `ready` deltaP `9.08` edge `0.0033` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0636` n `37` status `ready` deltaP `4.359` edge `0.0245` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.0431` n `52` status `ready` deltaP `6.3907` edge `0.0068` maxDD `-0.1771`
- `market_context_high->metal_1h` score `-0.017` n `37` status `ready` deltaP `2.0999` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.1314` n `55` status `ready` deltaP `-1.2303` edge `0.0463` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2016` n `55` status `ready` deltaP `1.4235` edge `0.0032` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6528` n `37` status `ready` deltaP `22.7093` edge `0.0929` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
