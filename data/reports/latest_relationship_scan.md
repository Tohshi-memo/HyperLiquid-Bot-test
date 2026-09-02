# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T12:22:30.319501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.2896` n `107` status `ready` deltaP `17.9337` edge `0.5497` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2896` n `107` status `ready` deltaP `17.9337` edge `0.5497` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3715` n `147` status `ready` deltaP `13.6677` edge `0.426` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.881` n `107` status `ready` deltaP `23.8756` edge `0.664` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.881` n `107` status `ready` deltaP `23.8756` edge `0.664` maxDD `-19.9806`
- `news_risk_high->equity_24h` score `1.856` n `59` status `ready` deltaP `9.8252` edge `0.3374` maxDD `-15.5253`
- `risk_on_high->unknown_1h` score `1.7569` n `107` status `ready` deltaP `2.9227` edge `0.1846` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7569` n `107` status `ready` deltaP `2.9227` edge `0.1846` maxDD `-1.9475`
- `market_context_high->equity_24h` score `1.5074` n `147` status `ready` deltaP `19.8448` edge `0.5442` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.132` n `61` status `ready` deltaP `1.6664` edge `0.1179` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.4282` n `147` status `ready` deltaP `1.2761` edge `0.0902` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2748` n `59` status `ready` deltaP `11.5544` edge `0.0052` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.1088` n `107` status `ready` deltaP `8.2433` edge `0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1088` n `107` status `ready` deltaP `8.2433` edge `0.0035` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0251` n `107` status `ready` deltaP `10.8974` edge `0.0018` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0251` n `107` status `ready` deltaP `10.8974` edge `0.0018` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0657` n `61` status `ready` deltaP `4.3978` edge `-0.0024` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.1152` n `147` status `ready` deltaP `7.0461` edge `0.0084` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
