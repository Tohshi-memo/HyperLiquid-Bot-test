# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T04:07:23.720917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11182`

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

- `news_risk_high->unknown_4h` score `400.1398` n `78` status `ready` deltaP `-22.303` edge `33.583` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.4473` n `78` status `ready` deltaP `18.5764` edge `1.8301` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9635` n `78` status `ready` deltaP `43.2559` edge `1.4977` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.4388` n `78` status `ready` deltaP `31.7441` edge `1.222` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.3749` n `78` status `ready` deltaP `45.5128` edge `1.0725` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5827` n `78` status `ready` deltaP `60.7238` edge `0.328` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4349` n `78` status `ready` deltaP `37.7938` edge `0.3297` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.2107` n `52` status `ready` deltaP `40.1042` edge `0.2502` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2107` n `52` status `ready` deltaP `40.1042` edge `0.2502` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9138` n `137` status `ready` deltaP `32.8049` edge `0.2433` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1421` n `52` status `ready` deltaP `46.8616` edge `0.037` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1421` n `52` status `ready` deltaP `46.8616` edge `0.037` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7451` n `137` status `ready` deltaP `43.6752` edge `0.0425` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9279` n `52` status `ready` deltaP `25.0703` edge `0.0285` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9279` n `52` status `ready` deltaP `25.0703` edge `0.0285` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7706` n `140` status `ready` deltaP `20.9494` edge `0.0497` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7802` n `149` status `ready` deltaP `12.9175` edge `0.0166` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6495` n `78` status `ready` deltaP `16.2015` edge `0.0381` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2097` n `52` status `ready` deltaP `7.462` edge `0.0077` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2097` n `52` status `ready` deltaP `7.462` edge `0.0077` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
