# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T11:52:40.930052+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6614`

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

- `risk_on_high->equity_1h` score `0.585` n `37` status `ready` deltaP `14.699` edge `0.0193` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.585` n `37` status `ready` deltaP `14.699` edge `0.0193` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5107` n `37` status `ready` deltaP `13.0523` edge `0.0055` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5107` n `37` status `ready` deltaP `13.0523` edge `0.0055` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.1457` n `73` status `ready` deltaP `13.2063` edge `0.0382` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.0921` n `37` status `ready` deltaP `11.022` edge `0.0181` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0921` n `37` status `ready` deltaP `11.022` edge `0.0181` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1271` n `37` status `ready` deltaP `0.7827` edge `0.0049` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1271` n `37` status `ready` deltaP `0.7827` edge `0.0049` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1282` n `87` status `ready` deltaP `6.1571` edge `0.0089` maxDD `-0.5168`
- `market_context_high->fx_1h` score `-0.1316` n `87` status `ready` deltaP `2.3711` edge `0.0028` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.2594` n `37` status `ready` deltaP `7.2965` edge `0.0026` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2594` n `37` status `ready` deltaP `7.2965` edge `0.0026` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.4396` n `87` status `ready` deltaP `3.0181` edge `-0.0031` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.4631` n `87` status `ready` deltaP `0.7296` edge `0.0025` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.5146` n `37` status `ready` deltaP `-3.3218` edge `0.0053` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5146` n `37` status `ready` deltaP `-3.3218` edge `0.0053` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.5738` n `87` status `ready` deltaP `2.9103` edge `0.0102` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
