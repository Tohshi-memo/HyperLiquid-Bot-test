# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T08:07:34.023411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4760`

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

- `market_context_high->unknown_4h` score `125.1664` n `37` status `ready` deltaP `-4.396` edge `10.5046` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2532` n `37` status `ready` deltaP `10.3577` edge `0.248` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.2095` n `37` status `ready` deltaP `34.6861` edge `0.0452` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0304` n `37` status `ready` deltaP `26.5079` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.6486` n `48` status `ready` deltaP `9.0278` edge `0.0993` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.7651` n `37` status `ready` deltaP `9.6011` edge `0.0583` maxDD `-3.0172`
- `news_risk_high->equity_4h` score `0.6541` n `48` status `ready` deltaP `4.6748` edge `0.1266` maxDD `-4.2454`
- `market_context_high->crypto_alt_1h` score `0.5153` n `37` status `ready` deltaP `11.6969` edge `0.0696` maxDD `-3.1881`
- `news_risk_high->fx_4h` score `0.4623` n `48` status `ready` deltaP `10.9248` edge `0.009` maxDD `-0.1309`
- `market_context_high->fx_1h` score `0.4098` n `37` status `ready` deltaP `6.9227` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.3132` n `48` status `ready` deltaP `10.0101` edge `0.0212` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2973` n `37` status `ready` deltaP `1.9502` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_1h` score `0.1613` n `51` status `ready` deltaP `9.4223` edge `0.0032` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->equity_1h` score `0.0365` n `51` status `ready` deltaP `1.8786` edge `0.0471` maxDD `-1.396`
- `market_context_high->commodity_4h` score `0.0208` n `37` status `ready` deltaP `3.5968` edge `0.0241` maxDD `-1.633`
- `news_risk_high->index_24h` score `-0.0321` n `48` status `ready` deltaP `3.6458` edge `0.1384` maxDD `-6.6786`
- `market_context_high->metal_1h` score `-0.0326` n `37` status `ready` deltaP `1.8005` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1873` n `51` status `ready` deltaP `1.6232` edge `0.0037` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6378` n `37` status `ready` deltaP `22.8618` edge `0.0938` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
