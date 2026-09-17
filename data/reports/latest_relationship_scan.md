# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T12:37:30.383245+00:00`
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

- `news_risk_high->unknown_4h` score `384.471` n `83` status `ready` deltaP `-22.2726` edge `32.2772` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.475` n `83` status `ready` deltaP `31.7541` edge `0.9658` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.0205` n `83` status `ready` deltaP `23.8203` edge `1.0424` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.2565` n `52` status `ready` deltaP `49.8264` edge `0.4392` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2565` n `52` status `ready` deltaP `49.8264` edge `0.4392` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.6321` n `83` status `ready` deltaP `33.0531` edge `0.6764` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.9574` n `149` status `ready` deltaP `43.115` edge `0.4282` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6982` n `83` status `ready` deltaP `38.4831` edge `0.2359` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.92` n `83` status `ready` deltaP `31.1224` edge `0.1646` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.7465` n `52` status `ready` deltaP `31.7777` edge `0.052` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7465` n `52` status `ready` deltaP `31.7777` edge `0.052` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6462` n `149` status `ready` deltaP `28.28` edge `0.0738` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.3943` n `52` status `ready` deltaP `31.5838` edge `-0.0068` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3943` n `52` status `ready` deltaP `31.5838` edge `-0.0068` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2594` n `149` status `ready` deltaP `28.8089` edge `0.0178` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1481` n `149` status `ready` deltaP `16.5103` edge `0.0233` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5248` n `52` status `ready` deltaP `9.5924` edge `0.015` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5248` n `52` status `ready` deltaP `9.5924` edge `0.015` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1404` n `83` status `ready` deltaP `8.8396` edge `0.0219` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0883` n `149` status `ready` deltaP `5.2506` edge `0.0021` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
