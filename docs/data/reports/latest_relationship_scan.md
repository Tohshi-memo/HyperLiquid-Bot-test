# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T21:37:37.952330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10608`

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

- `news_risk_high->unknown_4h` score `397.004` n `78` status `ready` deltaP `-22.4554` edge `33.3227` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.4879` n `78` status `ready` deltaP `18.9236` edge `1.9145` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.7869` n `78` status `ready` deltaP `46.0337` edge `1.5478` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.3815` n `78` status `ready` deltaP `33.133` edge `1.2913` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.8813` n `78` status `ready` deltaP `42.3878` edge `1.0522` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7327` n `78` status `ready` deltaP `61.9391` edge `0.3324` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4397` n `78` status `ready` deltaP `37.7938` edge `0.3301` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.1985` n `126` status `ready` deltaP `36.1111` edge `0.2758` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.7941` n `52` status `ready` deltaP `36.1111` edge `0.2421` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7941` n `52` status `ready` deltaP `36.1111` edge `0.2421` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.4322` n `52` status `ready` deltaP `49.813` edge `0.0415` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.4322` n `52` status `ready` deltaP `49.813` edge `0.0415` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.081` n `126` status `ready` deltaP `46.9742` edge `0.0485` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1239` n `52` status `ready` deltaP `27.2045` edge `0.0306` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1239` n `52` status `ready` deltaP `27.2045` edge `0.0306` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9242` n `137` status `ready` deltaP `22.6144` edge `0.0514` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7275` n `137` status `ready` deltaP `12.2132` edge `0.0169` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6447` n `78` status `ready` deltaP `16.0491` edge `0.0385` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2121` n `52` status `ready` deltaP `6.5984` edge `0.0089` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2121` n `52` status `ready` deltaP `6.5984` edge `0.0089` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
