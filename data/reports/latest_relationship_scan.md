# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T03:07:30.820947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10882`

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

- `news_risk_high->unknown_4h` score `400.0568` n `78` status `ready` deltaP `-22.4554` edge `33.5771` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.826` n `78` status `ready` deltaP `18.75` edge `1.8605` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9707` n `78` status `ready` deltaP `43.2559` edge `1.4983` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.4419` n `78` status `ready` deltaP `31.9178` edge `1.2211` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.2689` n `78` status `ready` deltaP `44.8184` edge `1.0683` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5935` n `78` status `ready` deltaP `60.7238` edge `0.3289` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4397` n `78` status `ready` deltaP `37.7938` edge `0.3301` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.136` n `52` status `ready` deltaP `39.4097` edge `0.2486` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.136` n `52` status `ready` deltaP `39.4097` edge `0.2486` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.839` n `137` status `ready` deltaP `32.1104` edge `0.2417` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7475` n `137` status `ready` deltaP `43.6752` edge `0.0427` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9159` n `52` status `ready` deltaP `25.0703` edge `0.0275` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9159` n `52` status `ready` deltaP `25.0703` edge `0.0275` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7163` n `137` status `ready` deltaP `20.4802` edge `0.0483` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7237` n `148` status `ready` deltaP `12.2552` edge `0.0163` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6945` n `78` status `ready` deltaP `16.8113` edge `0.0398` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1902` n `52` status `ready` deltaP `7.1626` edge `0.0072` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1902` n `52` status `ready` deltaP `7.1626` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
