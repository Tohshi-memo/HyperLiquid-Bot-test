# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T10:37:36.517618+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.669` n `83` status `ready` deltaP `-21.358` edge `32.2876` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.3853` n `83` status `ready` deltaP `33.143` edge `1.0324` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.6152` n `83` status `ready` deltaP `25.2092` edge `1.0827` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.1356` n `83` status `ready` deltaP `34.442` edge `0.7091` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.9858` n `52` status `ready` deltaP `48.4375` edge `0.4259` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9858` n `52` status `ready` deltaP `48.4375` edge `0.4259` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6867` n `149` status `ready` deltaP `41.7261` edge `0.4149` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.8537` n `83` status `ready` deltaP `39.872` edge `0.2396` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.0426` n `83` status `ready` deltaP `31.4696` edge `0.1725` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.5566` n `52` status `ready` deltaP `30.5582` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5566` n `52` status `ready` deltaP `30.5582` edge `0.0443` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.5306` n `52` status `ready` deltaP `32.9727` edge `-0.0047` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5306` n `52` status `ready` deltaP `32.9727` edge `-0.0047` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.4563` n `149` status `ready` deltaP `27.0605` edge `0.0661` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.3957` n `149` status `ready` deltaP `30.1978` edge `0.0199` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0294` n `149` status `ready` deltaP `15.4624` edge `0.0204` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4062` n `52` status `ready` deltaP `8.5445` edge `0.0121` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4062` n `52` status `ready` deltaP `8.5445` edge `0.0121` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2373` n `83` status `ready` deltaP `10.0591` edge `0.0262` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0548` n `52` status `ready` deltaP `4.9171` edge `0.0048` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
