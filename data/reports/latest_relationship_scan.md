# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T01:07:35.394538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.0388` n `83` status `ready` deltaP `-20.9007` edge `31.6487` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.2791` n `83` status `ready` deltaP `39.7402` edge `1.3129` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.8045` n `83` status `ready` deltaP `31.8064` edge `1.3045` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.9806` n `83` status `ready` deltaP `41.0392` edge `0.9022` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.3384` n `52` status `ready` deltaP `41.8403` edge `0.3326` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.3384` n `52` status `ready` deltaP `41.8403` edge `0.3326` maxDD `0.0`
- `news_risk_high->index_24h` score `6.6767` n `83` status `ready` deltaP `46.4692` edge `0.2642` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.0393` n `149` status `ready` deltaP `35.1289` edge `0.3216` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.9167` n `83` status `ready` deltaP `32.5113` edge `0.2384` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4836` n `52` status `ready` deltaP `32.6255` edge `-0.0063` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4836` n `52` status `ready` deltaP `32.6255` edge `-0.0063` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3488` n `149` status `ready` deltaP `29.8506` edge `0.0183` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.345` n `52` status `ready` deltaP `29.3386` edge `0.0348` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.345` n `52` status `ready` deltaP `29.3386` edge `0.0348` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2447` n `149` status `ready` deltaP `25.8409` edge `0.0566` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9959` n `149` status `ready` deltaP `15.163` edge `0.0196` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3753` n `83` status `ready` deltaP `11.8884` edge `0.0317` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.156` n `52` status `ready` deltaP `6.4141` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
