# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T04:52:25.981157+00:00`
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

- `market_context_high->unknown_4h` score `121.2309` n `37` status `ready` deltaP `-5.9204` edge `10.1868` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3362` n `37` status `ready` deltaP `36.2105` edge `0.0456` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2784` n `37` status `ready` deltaP `10.6571` edge `0.2481` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9415` n `37` status `ready` deltaP `25.4409` edge `0.0392` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7828` n `52` status `ready` deltaP `10.6303` edge `0.0998` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9509` n `52` status `ready` deltaP `8.0558` edge `0.1421` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7531` n `37` status `ready` deltaP `9.4514` edge `0.0583` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.4841` n `37` status `ready` deltaP `11.2478` edge `0.0686` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4457` n `37` status `ready` deltaP `7.3718` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.2994` n `52` status `ready` deltaP `9.7444` edge `0.0212` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2508` n `52` status `ready` deltaP `6.851` edge `0.1533` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1374` n `37` status `ready` deltaP `9.3179` edge `0.0101` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0764` n `52` status `ready` deltaP `7.0005` edge `0.007` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0628` n `37` status `ready` deltaP `4.359` edge `0.0244` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0022` n `37` status `ready` deltaP `2.3993` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.006` n `52` status `ready` deltaP `6.2183` edge `0.0031` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2278` n `52` status `ready` deltaP `-2.6486` edge `0.0434` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3278` n `52` status `ready` deltaP `-0.9442` edge `0.0028` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6724` n `37` status `ready` deltaP `22.5569` edge `0.0914` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
