# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T16:07:30.156534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4172`

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

- `market_context_high->unknown_4h` score `143.6506` n `37` status `ready` deltaP `-8.6643` edge `12.0734` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.363` n `37` status `ready` deltaP `36.5153` edge `0.0458` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1706` n `37` status `ready` deltaP `9.4595` edge `0.2471` maxDD `-2.3425`
- `market_context_high->index_4h` score `2.0013` n `37` status `ready` deltaP `26.2031` edge `0.0391` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5959` n `52` status `ready` deltaP `8.8942` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.7688` n `52` status `ready` deltaP `5.7692` edge `0.134` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7579` n `37` status `ready` deltaP `9.6011` edge `0.0577` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4818` n `37` status `ready` deltaP `11.3975` edge `0.0673` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3383` n `52` status `ready` deltaP `10.5066` edge `0.0211` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2602` n `37` status `ready` deltaP `1.5011` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1531` n `52` status `ready` deltaP `6.1566` edge `0.1454` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1436` n `37` status `ready` deltaP `9.4676` edge `0.0099` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0938` n `52` status `ready` deltaP `7.3053` edge `0.0072` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.009` n `37` status `ready` deltaP `3.4443` edge `0.0236` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0224` n `52` status `ready` deltaP `5.9189` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0505` n `37` status `ready` deltaP `1.5011` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2718` n `52` status `ready` deltaP `0.1037` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2979` n `52` status `ready` deltaP `-3.8462` edge `0.0424` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8545` n `37` status `ready` deltaP `20.2703` edge `0.0833` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
