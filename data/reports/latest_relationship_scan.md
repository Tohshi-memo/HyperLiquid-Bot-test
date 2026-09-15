# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T03:52:30.876176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11164`

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

- `news_risk_high->unknown_4h` score `400.082` n `78` status `ready` deltaP `-22.4554` edge `33.5792` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.4989` n `78` status `ready` deltaP `18.5764` edge `1.8344` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9599` n `78` status `ready` deltaP `43.2559` edge `1.4974` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.4316` n `78` status `ready` deltaP `31.7441` edge `1.2214` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.3466` n `78` status `ready` deltaP `45.3392` edge `1.0713` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5851` n `78` status `ready` deltaP `60.7238` edge `0.3282` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4349` n `78` status `ready` deltaP `37.7938` edge `0.3297` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1932` n `52` status `ready` deltaP `39.9306` edge `0.2499` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1932` n `52` status `ready` deltaP `39.9306` edge `0.2499` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8963` n `137` status `ready` deltaP `32.6313` edge `0.243` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7475` n `137` status `ready` deltaP `43.6752` edge `0.0427` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9255` n `52` status `ready` deltaP `25.0703` edge `0.0283` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9255` n `52` status `ready` deltaP `25.0703` edge `0.0283` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7547` n `139` status `ready` deltaP `20.7953` edge `0.0494` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7683` n `149` status `ready` deltaP `12.7678` edge `0.0166` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6598` n `78` status `ready` deltaP `16.354` edge `0.0384` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1996` n `52` status `ready` deltaP `7.3123` edge `0.0074` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1996` n `52` status `ready` deltaP `7.3123` edge `0.0074` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
