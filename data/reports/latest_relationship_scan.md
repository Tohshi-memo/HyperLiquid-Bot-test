# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T06:52:26.032118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_4h` score `125.0976` n `37` status `ready` deltaP `-4.7009` edge `10.5009` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.3059` n `37` status `ready` deltaP `10.9565` edge `0.2484` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.2728` n `37` status `ready` deltaP `35.4483` edge `0.0454` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0061` n `37` status `ready` deltaP `26.2031` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.8104` n `52` status `ready` deltaP `10.6303` edge `0.1021` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9713` n `52` status `ready` deltaP `8.2082` edge `0.1437` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.8154` n `37` status `ready` deltaP `10.0502` edge `0.0595` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5215` n `37` status `ready` deltaP `11.6969` edge `0.0704` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4338` n `37` status `ready` deltaP `7.2221` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.3414` n `52` status `ready` deltaP `10.5066` edge `0.0215` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.3225` n `37` status `ready` deltaP `2.2496` edge `0.0389` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2883` n `52` status `ready` deltaP `6.851` edge `0.1581` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1452` n `37` status `ready` deltaP `9.4676` edge `0.0101` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1451` n `55` status `ready` deltaP `9.08` edge `0.0034` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0556` n `37` status `ready` deltaP `4.2065` edge `0.0245` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.0352` n `52` status `ready` deltaP `6.2383` edge `0.0068` maxDD `-0.1771`
- `market_context_high->metal_1h` score `-0.0092` n `37` status `ready` deltaP `2.2496` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.1314` n `55` status `ready` deltaP `-1.2303` edge `0.0463` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2016` n `55` status `ready` deltaP `1.4235` edge `0.0032` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.652` n `37` status `ready` deltaP `22.7093` edge `0.093` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
