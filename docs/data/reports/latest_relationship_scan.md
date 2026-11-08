# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T05:07:26.609702+00:00`
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

- `market_context_high->unknown_4h` score `121.2623` n `37` status `ready` deltaP `-5.7679` edge `10.1884` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3362` n `37` status `ready` deltaP `36.2105` edge `0.0456` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2928` n `37` status `ready` deltaP `10.8068` edge `0.2483` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9537` n `37` status `ready` deltaP `25.5933` edge `0.0392` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7864` n `52` status `ready` deltaP `10.6303` edge `0.1001` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9619` n `52` status `ready` deltaP `8.2082` edge `0.1425` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7711` n `37` status `ready` deltaP `9.6011` edge `0.0588` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.4966` n `37` status `ready` deltaP `11.3975` edge `0.0692` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4457` n `37` status `ready` deltaP `7.3718` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.3073` n `52` status `ready` deltaP `9.8968` edge `0.0212` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2973` n `37` status `ready` deltaP `1.9502` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2555` n `52` status `ready` deltaP `6.851` edge `0.1539` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1288` n `37` status `ready` deltaP `9.1682` edge `0.01` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0764` n `52` status `ready` deltaP `7.0005` edge `0.007` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0548` n `37` status `ready` deltaP `4.2065` edge `0.0244` maxDD `-1.633`
- `news_risk_high->index_1h` score `0.0017` n `52` status `ready` deltaP `6.368` edge `0.0031` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0015` n `37` status `ready` deltaP `2.3993` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.2185` n `52` status `ready` deltaP `-2.4989` edge `0.0436` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3278` n `52` status `ready` deltaP `-0.9442` edge `0.0028` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6613` n `37` status `ready` deltaP `22.7093` edge `0.0918` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
