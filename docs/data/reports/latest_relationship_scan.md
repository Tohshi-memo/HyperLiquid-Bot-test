# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T11:54:43.661217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11210`

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

- `news_risk_high->unknown_4h` score `396.746` n `78` status `ready` deltaP `-22.4554` edge `33.3012` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.1445` n `78` status `ready` deltaP `46.0337` edge `1.5776` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.0409` n `78` status `ready` deltaP `19.7917` edge `1.7048` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.0104` n `78` status `ready` deltaP `36.7789` edge `1.3194` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1918` n `78` status `ready` deltaP `48.4642` edge `1.1209` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6123` n `78` status `ready` deltaP `61.2446` edge `0.327` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5222` n `78` status `ready` deltaP `38.3146` edge `0.3335` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9515` n `52` status `ready` deltaP `37.6736` edge `0.2448` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9515` n `52` status `ready` deltaP `37.6736` edge `0.2448` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6545` n `137` status `ready` deltaP `30.3743` edge `0.2379` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.5852` n `52` status `ready` deltaP `42.0005` edge `0.023` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.5852` n `52` status `ready` deltaP `42.0005` edge `0.023` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.1882` n `137` status `ready` deltaP `38.8141` edge `0.0285` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.849` n `52` status `ready` deltaP `24.3082` edge `0.027` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.849` n `52` status `ready` deltaP `24.3082` edge `0.027` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7487` n `149` status `ready` deltaP `20.8105` edge `0.0488` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8677` n `149` status `ready` deltaP `13.666` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7217` n `78` status `ready` deltaP `17.5735` edge `0.0382` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2444` n `52` status `ready` deltaP `6.7481` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2444` n `52` status `ready` deltaP `6.7481` edge `0.0106` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
