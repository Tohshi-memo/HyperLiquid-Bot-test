# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T05:22:26.474976+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4443`

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

- `market_context_high->unknown_4h` score `121.2985` n `37` status `ready` deltaP `-5.6155` edge `10.1904` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.324` n `37` status `ready` deltaP `36.058` edge `0.0456` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.294` n `37` status `ready` deltaP `10.8068` edge `0.2484` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9671` n `37` status `ready` deltaP `25.7457` edge `0.0393` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.79` n `52` status `ready` deltaP `10.6303` edge `0.1004` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9635` n `52` status `ready` deltaP `8.2082` edge `0.1427` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7843` n `37` status `ready` deltaP `9.7508` edge `0.0589` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5059` n `37` status `ready` deltaP `11.5472` edge `0.0694` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4457` n `37` status `ready` deltaP `7.3718` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.316` n `52` status `ready` deltaP `10.0492` edge `0.0213` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.3093` n `37` status `ready` deltaP `2.0999` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2602` n `52` status `ready` deltaP `6.851` edge `0.1545` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1288` n `37` status `ready` deltaP `9.1682` edge `0.01` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0684` n `52` status `ready` deltaP `6.848` edge `0.007` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0469` n `37` status `ready` deltaP `4.0541` edge `0.0244` maxDD `-1.633`
- `news_risk_high->index_1h` score `0.0095` n `52` status `ready` deltaP `6.5177` edge `0.0031` maxDD `-0.2931`
- `market_context_high->metal_1h` score `0.0063` n `37` status `ready` deltaP `2.549` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.2177` n `52` status `ready` deltaP `-2.4989` edge `0.0437` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3278` n `52` status `ready` deltaP `-0.9442` edge `0.0028` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6598` n `37` status `ready` deltaP `22.7093` edge `0.092` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
