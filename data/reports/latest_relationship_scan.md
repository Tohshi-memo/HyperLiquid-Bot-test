# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T15:37:31.792531+00:00`
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

- `news_risk_high->unknown_4h` score `395.2622` n `78` status `ready` deltaP `-21.0835` edge `33.1684` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7156` n `78` status `ready` deltaP `46.2073` edge `1.5407` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.4953` n `78` status `ready` deltaP `34.6955` edge `1.3737` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.9492` n `78` status `ready` deltaP `38.2211` edge `1.0023` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6708` n `78` status `ready` deltaP `61.7655` edge `0.3284` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.0737` n `108` status `ready` deltaP `39.2361` edge `0.3279` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3058` n `78` status `ready` deltaP `37.6202` edge `0.3201` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.2997` n `48` status `ready` deltaP `39.2361` edge `0.2634` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2997` n `48` status `ready` deltaP `39.2361` edge `0.2634` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.8103` n `48` status `ready` deltaP `53.8195` edge `0.0463` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8103` n `48` status `ready` deltaP `53.8195` edge `0.0463` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.3893` n `108` status `ready` deltaP `50.3472` edge `0.0517` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9217` n `52` status `ready` deltaP `25.8325` edge `0.0229` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9217` n `52` status `ready` deltaP `25.8325` edge `0.0229` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.722` n `137` status `ready` deltaP `21.2424` edge `0.0437` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7562` n `137` status `ready` deltaP `12.6623` edge `0.0163` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6532` n `78` status `ready` deltaP `15.8966` edge `0.0406` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2408` n `52` status `ready` deltaP `7.0475` edge `0.0083` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2408` n `52` status `ready` deltaP `7.0475` edge `0.0083` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2194` n `137` status `ready` deltaP `10.1589` edge `0.008` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
