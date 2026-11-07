# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T17:22:28.665539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4238`

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

- `market_context_high->unknown_4h` score `138.173` n `37` status `ready` deltaP `-8.3594` edge `11.6149` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3898` n `37` status `ready` deltaP `36.8202` edge `0.046` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1454` n `37` status `ready` deltaP `9.1601` edge `0.247` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9879` n `37` status `ready` deltaP `26.0506` edge `0.039` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5959` n `52` status `ready` deltaP `8.8942` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8193` n `52` status `ready` deltaP `6.5314` edge `0.1354` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7483` n `37` status `ready` deltaP `9.4514` edge `0.0579` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4709` n `37` status `ready` deltaP `11.2478` edge `0.0669` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3296` n `52` status `ready` deltaP `10.3541` edge `0.021` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2602` n `37` status `ready` deltaP `1.5011` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.197` n `52` status `ready` deltaP `6.851` edge `0.1464` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1112` n `52` status `ready` deltaP `7.6102` edge `0.0074` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1086` n `37` status `ready` deltaP `8.8688` edge `0.0094` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0186` n `37` status `ready` deltaP `2.0999` edge `0.0164` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0203` n `37` status `ready` deltaP `2.987` edge `0.0229` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0224` n `52` status `ready` deltaP `5.9189` edge `0.003` maxDD `-0.2931`
- `news_risk_high->fx_1h` score `-0.2718` n `52` status `ready` deltaP `0.1037` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3142` n `52` status `ready` deltaP `-4.1456` edge `0.0423` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8039` n `37` status `ready` deltaP `21.0325` edge `0.0847` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
