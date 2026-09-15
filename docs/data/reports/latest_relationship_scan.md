# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T03:37:30.103413+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11102`

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

- `news_risk_high->unknown_4h` score `400.076` n `78` status `ready` deltaP `-22.4554` edge `33.5787` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.6021` n `78` status `ready` deltaP `18.5764` edge `1.843` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9551` n `78` status `ready` deltaP `43.2559` edge `1.497` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.4232` n `78` status `ready` deltaP `31.7441` edge `1.2207` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.3171` n `78` status `ready` deltaP `45.1656` edge `1.07` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5875` n `78` status `ready` deltaP `60.7238` edge `0.3284` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4349` n `78` status `ready` deltaP `37.7938` edge `0.3297` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1734` n `52` status `ready` deltaP `39.7569` edge `0.2494` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1734` n `52` status `ready` deltaP `39.7569` edge `0.2494` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8764` n `137` status `ready` deltaP `32.4576` edge `0.2425` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7475` n `137` status `ready` deltaP `43.6752` edge `0.0427` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9219` n `52` status `ready` deltaP `25.0703` edge `0.028` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9219` n `52` status `ready` deltaP `25.0703` edge `0.028` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7362` n `138` status `ready` deltaP `20.6389` edge `0.0489` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7539` n `149` status `ready` deltaP `12.6181` edge `0.0164` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6709` n `78` status `ready` deltaP `16.5064` edge `0.0388` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1902` n `52` status `ready` deltaP `7.1626` edge `0.0072` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1902` n `52` status `ready` deltaP `7.1626` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
