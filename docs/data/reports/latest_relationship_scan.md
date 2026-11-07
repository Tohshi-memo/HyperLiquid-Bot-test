# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T14:52:25.034483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4119`

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

- `market_context_high->unknown_4h` score `174.9014` n `35` status `ready` deltaP `-4.7953` edge `14.6411` maxDD `-0.721`
- `market_context_high->fx_4h` score `3.4123` n `35` status `ready` deltaP `36.8162` edge `0.0479` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1071` n `37` status `ready` deltaP `8.8607` edge `0.2458` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9464` n `35` status `ready` deltaP `25.4268` edge `0.0397` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.1434` n `55` status `ready` deltaP `4.6622` edge `0.0863` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9178` n `55` status `ready` deltaP `7.4196` edge `0.1421` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.6536` n `37` status `ready` deltaP `8.8526` edge `0.054` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.4546` n `55` status `ready` deltaP `12.6995` edge `0.0214` maxDD `-0.4888`
- `market_context_high->crypto_alt_1h` score `0.3875` n `37` status `ready` deltaP `10.649` edge `0.0602` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2367` n `55` status `ready` deltaP `7.7336` edge `0.1456` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1436` n `37` status `ready` deltaP `9.4676` edge `0.0099` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1217` n `55` status `ready` deltaP `8.6309` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.0253` n `55` status `ready` deltaP `6.1669` edge `0.0062` maxDD `-0.1919`
- `market_context_high->commodity_4h` score `0.0219` n `35` status `ready` deltaP `3.8284` edge `0.0227` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.091` n `37` status `ready` deltaP `0.7526` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1471` n `55` status `ready` deltaP `2.4714` edge `0.0032` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.1513` n `55` status `ready` deltaP `-1.5079` edge `0.0456` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7266` n `35` status `ready` deltaP `23.5235` edge `0.078` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
