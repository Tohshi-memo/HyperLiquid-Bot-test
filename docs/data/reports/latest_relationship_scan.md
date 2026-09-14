# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T15:07:39.010077+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11022`

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

- `news_risk_high->unknown_4h` score `395.3044` n `78` status `ready` deltaP `-20.931` edge `33.1709` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7168` n `78` status `ready` deltaP `46.2073` edge `1.5408` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.6119` n `78` status `ready` deltaP `35.0428` edge `1.3811` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.8854` n `78` status `ready` deltaP `37.8739` edge `0.9993` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6648` n `78` status `ready` deltaP `61.7655` edge `0.3279` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1339` n `106` status `ready` deltaP `39.5833` edge `0.3306` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.3371` n `46` status `ready` deltaP `39.5833` edge `0.2642` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3371` n `46` status `ready` deltaP `39.5833` edge `0.2642` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.26` n `78` status `ready` deltaP `37.2729` edge `0.3186` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.8333` n `46` status `ready` deltaP `54.0761` edge `0.0465` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8333` n `46` status `ready` deltaP `54.0761` edge `0.0465` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4147` n `106` status `ready` deltaP `50.5896` edge `0.0522` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9327` n `52` status `ready` deltaP `25.985` edge `0.0228` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9327` n `52` status `ready` deltaP `25.985` edge `0.0228` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.733` n `137` status `ready` deltaP `21.3949` edge `0.0436` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7263` n `137` status `ready` deltaP `12.3629` edge `0.0158` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6437` n `78` status `ready` deltaP `15.7442` edge `0.0404` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2273` n `137` status `ready` deltaP `10.3113` edge `0.008` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2108` n `52` status `ready` deltaP `6.7481` edge `0.0078` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2108` n `52` status `ready` deltaP `6.7481` edge `0.0078` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
