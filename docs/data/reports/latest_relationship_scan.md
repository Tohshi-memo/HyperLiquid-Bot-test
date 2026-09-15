# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T05:37:29.333597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11204`

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

- `news_risk_high->unknown_4h` score `399.9782` n `78` status `ready` deltaP `-21.9981` edge `33.5675` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.8502` n `78` status `ready` deltaP `18.4028` edge `1.7815` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.0247` n `78` status `ready` deltaP `43.2559` edge `1.5028` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.6103` n `78` status `ready` deltaP `32.6122` edge `1.2305` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.4898` n `78` status `ready` deltaP `46.0336` edge `1.0786` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5683` n `78` status `ready` deltaP `60.7238` edge `0.3268` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4193` n `78` status `ready` deltaP `37.7938` edge `0.3284` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1932` n `52` status `ready` deltaP `39.9306` edge `0.2499` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1932` n `52` status `ready` deltaP `39.9306` edge `0.2499` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8963` n `137` status `ready` deltaP `32.6313` edge `0.243` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.0837` n `52` status `ready` deltaP `46.3408` edge `0.0356` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.0837` n `52` status `ready` deltaP `46.3408` edge `0.0356` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.6867` n `137` status `ready` deltaP `43.1544` edge `0.0411` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9495` n `52` status `ready` deltaP `25.0703` edge `0.0303` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9495` n `52` status `ready` deltaP `25.0703` edge `0.0303` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8783` n `146` status `ready` deltaP `21.8301` edge `0.0528` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.779` n `149` status `ready` deltaP `12.9175` edge `0.0165` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6363` n `78` status `ready` deltaP `16.2015` edge `0.0364` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2346` n `52` status `ready` deltaP `7.9111` edge `0.0079` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2346` n `52` status `ready` deltaP `7.9111` edge `0.0079` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
