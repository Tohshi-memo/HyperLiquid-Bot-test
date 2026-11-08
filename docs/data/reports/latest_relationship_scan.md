# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T08:37:31.266507+00:00`
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

- `market_context_high->unknown_4h` score `125.1882` n `37` status `ready` deltaP `-4.2436` edge `10.5054` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2532` n `37` status `ready` deltaP `10.3577` edge `0.248` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1961` n `37` status `ready` deltaP `34.5336` edge `0.0451` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0304` n `37` status `ready` deltaP `26.5079` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5401` n `46` status `ready` deltaP `8.122` edge `0.0963` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.7687` n `37` status `ready` deltaP `9.6011` edge `0.0586` maxDD `-3.0172`
- `news_risk_high->fx_4h` score `0.5865` n `46` status `ready` deltaP `11.6781` edge `0.01` maxDD `-0.1183`
- `market_context_high->crypto_alt_1h` score `0.5254` n `37` status `ready` deltaP `11.8466` edge `0.0699` maxDD `-3.1881`
- `news_risk_high->equity_4h` score `0.4709` n `46` status `ready` deltaP `2.5915` edge `0.117` maxDD `-4.2454`
- `market_context_high->fx_1h` score `0.4098` n `37` status `ready` deltaP `6.9227` edge `0.0151` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2961` n `37` status `ready` deltaP `1.9502` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.2324` n `46` status `ready` deltaP `8.4703` edge `0.0211` maxDD `-0.4888`
- `market_context_high->commodity_1h` score `0.1249` n `37` status `ready` deltaP `9.1682` edge `0.0095` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0724` n `49` status `ready` deltaP `7.7417` edge `0.003` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0018` n `37` status `ready` deltaP `3.2919` edge `0.0237` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0482` n `37` status `ready` deltaP `1.5011` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0863` n `49` status `ready` deltaP `-0.1222` edge `0.0447` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1385` n `49` status `ready` deltaP `1.9034` edge `0.0039` maxDD `-0.0807`
- `news_risk_high->index_24h` score `-0.2097` n `46` status `ready` deltaP `1.8342` edge `0.1277` maxDD `-6.6786`
- `market_context_high->equity_4h` score `-0.6378` n `37` status `ready` deltaP `22.8618` edge `0.0938` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
