# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T00:22:27.700722+00:00`
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

- `market_context_high->unknown_4h` score `120.7343` n `37` status `ready` deltaP `-7.5972` edge `10.1566` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.48` n `37` status `ready` deltaP `37.8873` edge `0.0464` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1514` n `37` status `ready` deltaP `9.3098` edge `0.2465` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8599` n `37` status `ready` deltaP `24.5262` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7142` n `52` status `ready` deltaP `10.2831` edge `0.0964` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8579` n `52` status `ready` deltaP `6.9887` edge `0.1373` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.6968` n `37` status `ready` deltaP `9.0023` edge `0.0566` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.508` n `37` status `ready` deltaP `8.1203` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.386` n `37` status `ready` deltaP `10.1999` edge `0.063` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2464` n `52` status `ready` deltaP `8.8297` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2242` n `37` status `ready` deltaP `1.052` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2025` n `52` status `ready` deltaP `6.851` edge `0.1471` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1698` n `52` status `ready` deltaP `8.6773` edge `0.0078` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1366` n `37` status `ready` deltaP `9.3179` edge `0.01` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0029` n `37` status `ready` deltaP `3.2919` edge `0.0231` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0457` n `52` status `ready` deltaP `5.4698` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0575` n `37` status `ready` deltaP `1.3514` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2873` n `52` status `ready` deltaP `-0.1957` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3104` n `52` status `ready` deltaP `-3.9959` edge `0.0418` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7653` n `37` status `ready` deltaP `21.4898` edge `0.0866` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
