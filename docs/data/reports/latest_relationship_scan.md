# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T14:07:35.152094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6668`

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

- `risk_on_high->equity_1h` score `0.599` n `37` status `ready` deltaP `14.8487` edge `0.0201` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.599` n `37` status `ready` deltaP `14.8487` edge `0.0201` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5099` n `37` status `ready` deltaP `13.0523` edge `0.0054` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5099` n `37` status `ready` deltaP `13.0523` edge `0.0054` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3984` n `80` status `ready` deltaP `15.4861` edge `0.0554` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.1261` n `37` status `ready` deltaP `11.1956` edge `0.0213` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1261` n `37` status `ready` deltaP `11.1956` edge `0.0213` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `market_context_high->fx_4h` score `-0.0296` n `87` status `ready` deltaP `7.2242` edge `0.01` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.063` n `37` status `ready` deltaP `1.8498` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.063` n `37` status `ready` deltaP `1.8498` edge `0.006` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1316` n `87` status `ready` deltaP `2.3711` edge `0.0028` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.235` n `37` status `ready` deltaP `7.6014` edge `0.0037` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.235` n `37` status `ready` deltaP `7.6014` edge `0.0037` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.4408` n `87` status `ready` deltaP `3.0181` edge `-0.0032` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.4654` n `87` status `ready` deltaP `0.7296` edge `0.0022` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.5158` n `37` status `ready` deltaP `-3.3218` edge `0.0052` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5158` n `37` status `ready` deltaP `-3.3218` edge `0.0052` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.611` n `87` status `ready` deltaP `2.3006` edge `0.0095` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
