# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T14:52:32.238686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11441`

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

- `news_risk_high->unknown_4h` score `368.8246` n `83` status `ready` deltaP `-21.0531` edge `30.9652` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.3739` n `78` status `ready` deltaP `47.7698` edge `1.6684` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.7553` n `78` status `ready` deltaP `39.7303` edge `1.6118` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.4988` n `78` status `ready` deltaP `46.2072` edge `1.0776` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.5277` n `78` status `ready` deltaP `52.2168` edge `0.2968` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.1933` n `78` status `ready` deltaP `35.8841` edge `0.3223` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.467` n `52` status `ready` deltaP `34.7222` edge `0.2241` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.467` n `52` status `ready` deltaP `34.7222` edge `0.2241` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1678` n `149` status `ready` deltaP `28.0108` edge `0.2131` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3681` n `52` status `ready` deltaP `31.9311` edge `-0.0113` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3681` n `52` status `ready` deltaP `31.9311` edge `-0.0113` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2332` n `149` status `ready` deltaP `29.1562` edge `0.0133` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1878` n `52` status `ready` deltaP `28.424` edge `0.0278` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1878` n `52` status `ready` deltaP `28.424` edge `0.0278` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0876` n `149` status `ready` deltaP `24.9263` edge `0.0496` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8916` n `149` status `ready` deltaP `14.1151` edge `0.0179` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4397` n `83` status `ready` deltaP `13.2604` edge `0.0308` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3678` n `52` status `ready` deltaP `9.6975` edge `0.144` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3678` n `52` status `ready` deltaP `9.6975` edge `0.144` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2684` n `52` status `ready` deltaP `7.1972` edge `0.0096` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
