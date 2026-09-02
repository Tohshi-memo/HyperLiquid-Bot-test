# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T11:29:45.608302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.3392` n `107` status `ready` deltaP `18.2386` edge `0.5518` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3392` n `107` status `ready` deltaP `18.2386` edge `0.5518` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3737` n `148` status `ready` deltaP `14.1151` edge `0.4232` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.5722` n `107` status `ready` deltaP `23.1812` edge `0.6429` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.5722` n `107` status `ready` deltaP `23.1812` edge `0.6429` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8228` n `107` status `ready` deltaP `3.3718` edge `0.1871` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8228` n `107` status `ready` deltaP `3.3718` edge `0.1871` maxDD `-1.9475`
- `news_risk_high->equity_24h` score `1.5473` n `59` status `ready` deltaP `9.1308` edge `0.3163` maxDD `-15.5253`
- `market_context_high->equity_24h` score `1.4135` n `148` status `ready` deltaP `19.4492` edge `0.5348` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1125` n `59` status `ready` deltaP `0.8373` edge `0.1218` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.4931` n `148` status `ready` deltaP `1.9826` edge `0.0909` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2578` n `59` status `ready` deltaP `11.4019` edge `0.0048` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1306` n `107` status `ready` deltaP `8.5427` edge `0.0043` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1306` n `107` status `ready` deltaP `8.5427` edge `0.0043` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1208` n `107` status `ready` deltaP `20.783` edge `0.01` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1208` n `107` status `ready` deltaP `20.783` edge `0.01` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0601` n `107` status `ready` deltaP `11.3465` edge `0.0033` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0601` n `107` status `ready` deltaP `11.3465` edge `0.0033` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.0771` n `107` status `ready` deltaP `8.4658` edge `0.0166` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.0771` n `107` status `ready` deltaP `8.4658` edge `0.0166` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
