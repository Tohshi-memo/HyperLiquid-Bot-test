# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T03:22:28.565270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10938`

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

- `news_risk_high->unknown_4h` score `400.0508` n `78` status `ready` deltaP `-22.4554` edge `33.5766` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.6981` n `78` status `ready` deltaP `18.5764` edge `1.851` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9599` n `78` status `ready` deltaP `43.2559` edge `1.4974` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.4232` n `78` status `ready` deltaP `31.7441` edge `1.2207` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.2924` n `78` status `ready` deltaP `44.992` edge `1.0691` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5899` n `78` status `ready` deltaP `60.7238` edge `0.3286` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4373` n `78` status `ready` deltaP `37.7938` edge `0.3299` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1547` n `52` status `ready` deltaP `39.5833` edge `0.249` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1547` n `52` status `ready` deltaP `39.5833` edge `0.249` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8577` n `137` status `ready` deltaP `32.284` edge `0.2421` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1445` n `52` status `ready` deltaP `46.8616` edge `0.0372` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7475` n `137` status `ready` deltaP `43.6752` edge `0.0427` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9195` n `52` status `ready` deltaP `25.0703` edge `0.0278` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9195` n `52` status `ready` deltaP `25.0703` edge `0.0278` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7199` n `137` status `ready` deltaP `20.4802` edge `0.0486` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7407` n `149` status `ready` deltaP `12.4684` edge `0.0163` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6827` n `78` status `ready` deltaP `16.6588` edge `0.0393` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1895` n `52` status `ready` deltaP `7.1626` edge `0.0071` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1895` n `52` status `ready` deltaP `7.1626` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
