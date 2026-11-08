# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T03:52:26.429919+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4428`

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

- `market_context_high->unknown_4h` score `121.0945` n `37` status `ready` deltaP `-6.5301` edge `10.1795` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.363` n `37` status `ready` deltaP `36.5153` edge `0.0458` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2197` n `37` status `ready` deltaP `10.0583` edge `0.2472` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8891` n `37` status `ready` deltaP `24.8311` edge `0.0389` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.766` n `52` status `ready` deltaP `10.6303` edge `0.0984` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9067` n `52` status `ready` deltaP `7.446` edge `0.1405` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7639` n `37` status `ready` deltaP `9.6011` edge `0.0582` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.4709` n `37` status `ready` deltaP `7.6712` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4491` n `37` status `ready` deltaP `10.7987` edge `0.0671` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2654` n `52` status `ready` deltaP `9.1346` edge `0.0209` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2352` n `52` status `ready` deltaP `6.851` edge `0.1513` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1366` n `37` status `ready` deltaP `9.3179` edge `0.01` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0938` n `52` status `ready` deltaP `7.3053` edge `0.0072` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0897` n `37` status `ready` deltaP `4.8163` edge `0.0248` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0178` n `37` status `ready` deltaP `2.0999` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.266` n `52` status `ready` deltaP `-3.2474` edge `0.0425` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3115` n `52` status `ready` deltaP `-0.6448` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7166` n `37` status `ready` deltaP `21.9471` edge `0.0898` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
