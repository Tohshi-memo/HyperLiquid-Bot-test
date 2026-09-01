# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T19:52:30.112330+00:00`
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

- `risk_on_high->unknown_4h` score `7.3221` n `107` status `ready` deltaP `19.9154` edge `0.5392` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3221` n `107` status `ready` deltaP `19.9154` edge `0.5392` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8687` n `151` status `ready` deltaP `16.208` edge `0.4505` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.9691` n `107` status `ready` deltaP `3.9706` edge `0.1953` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.9691` n `107` status `ready` deltaP `3.9706` edge `0.1953` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.8383` n `151` status `ready` deltaP `3.3331` edge `0.194` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.2588` n `59` status `ready` deltaP `1.4361` edge `0.13` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1513` n `59` status `ready` deltaP `10.6397` edge `0.001` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1068` n `107` status `ready` deltaP `12.2447` edge `0.0033` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1068` n `107` status `ready` deltaP `12.2447` edge `0.0033` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0987` n `107` status `ready` deltaP `8.0936` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0987` n `107` status `ready` deltaP `8.0936` edge `0.0032` maxDD `-0.5605`
- `risk_on_high->commodity_24h` score `0.0658` n `107` status `ready` deltaP `6.5226` edge `0.0608` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.0658` n `107` status `ready` deltaP `6.5226` edge `0.0608` maxDD `-0.5706`
- `risk_on_high->index_4h` score `0.0056` n `107` status `ready` deltaP `19.1062` edge `0.0064` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0056` n `107` status `ready` deltaP `19.1062` edge `0.0064` maxDD `-3.6448`
- `market_context_high->commodity_1h` score `-0.1404` n `151` status `ready` deltaP `6.7762` edge `0.0081` maxDD `-1.5315`
- `risk_on_high->equity_1h` score `-0.1636` n `107` status `ready` deltaP `7.7173` edge `0.0105` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1636` n `107` status `ready` deltaP `7.7173` edge `0.0105` maxDD `-2.3009`
- `risk_on_high->commodity_1h` score `-0.1646` n `107` status `ready` deltaP `3.6754` edge `0.0066` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
