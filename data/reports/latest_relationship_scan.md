# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T03:22:30.617387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11561`

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

- `news_risk_high->unknown_4h` score `365.8562` n `83` status `ready` deltaP `-21.6629` edge `30.7219` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.8632` n `78` status `ready` deltaP `21.1806` edge `3.0974` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.4047` n `78` status `ready` deltaP `47.7698` edge `1.7543` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.8057` n `78` status `ready` deltaP `39.7303` edge `1.616` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9689` n `78` status `ready` deltaP `49.8531` edge `1.1758` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3613` n `78` status `ready` deltaP `59.6821` edge `0.3165` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8372` n `78` status `ready` deltaP `38.4882` edge `0.3586` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.7499` n `52` status `ready` deltaP `37.6736` edge `0.228` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7499` n `52` status `ready` deltaP `37.6736` edge `0.228` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4507` n `149` status `ready` deltaP `30.9622` edge `0.217` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4499` n `52` status `ready` deltaP `32.2783` edge `-0.0068` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4499` n `52` status `ready` deltaP `32.2783` edge `-0.0068` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.315` n `149` status `ready` deltaP `29.5034` edge `0.0178` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.748` n `52` status `ready` deltaP `24.1557` edge `0.0196` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.748` n `52` status `ready` deltaP `24.1557` edge `0.0196` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6477` n `149` status `ready` deltaP `20.658` edge `0.0414` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8078` n `149` status `ready` deltaP `13.3666` edge `0.0159` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7826` n `83` status `ready` deltaP `18.5957` edge `0.0392` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3775` n `52` status `ready` deltaP `10.0024` edge `0.1432` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3775` n `52` status `ready` deltaP `10.0024` edge `0.1432` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
