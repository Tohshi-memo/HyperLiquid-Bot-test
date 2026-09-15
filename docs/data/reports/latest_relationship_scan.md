# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T13:37:32.417382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11180`

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

- `news_risk_high->unknown_4h` score `396.226` n `78` status `ready` deltaP `-22.7603` edge `33.2599` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.3451` n `78` status `ready` deltaP `20.8333` edge `1.7232` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.3266` n `78` status `ready` deltaP `46.5545` edge `1.5893` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.3349` n `78` status `ready` deltaP `37.8205` edge `1.3395` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1066` n `78` status `ready` deltaP `48.4642` edge `1.1138` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.4731` n `78` status `ready` deltaP `60.0293` edge `0.3235` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4565` n `78` status `ready` deltaP `37.7938` edge `0.3315` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9659` n `52` status `ready` deltaP `37.6736` edge `0.246` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9659` n `52` status `ready` deltaP `37.6736` edge `0.246` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6689` n `137` status `ready` deltaP `30.3743` edge `0.2391` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.4484` n `52` status `ready` deltaP `40.7852` edge `0.0197` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.4484` n `52` status `ready` deltaP `40.7852` edge `0.0197` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.0514` n `137` status `ready` deltaP `37.5988` edge `0.0252` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7888` n `52` status `ready` deltaP `24.1557` edge `0.023` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7888` n `52` status `ready` deltaP `24.1557` edge `0.023` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6885` n `149` status `ready` deltaP `20.658` edge `0.0448` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8066` n `149` status `ready` deltaP `13.2169` edge `0.0168` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7044` n `78` status `ready` deltaP `17.421` edge `0.037` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.1951` n `149` status `ready` deltaP `9.886` edge `0.0067` maxDD `-0.1412`
- `risk_on_high->metal_1h` score `0.1926` n `52` status `ready` deltaP `7.3123` edge `0.0065` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
