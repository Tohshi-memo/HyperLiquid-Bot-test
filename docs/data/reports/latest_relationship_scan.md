# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T19:37:27.690941+00:00`
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

- `risk_on_high->unknown_4h` score `7.3511` n `107` status `ready` deltaP `20.0678` edge `0.5406` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3511` n `107` status `ready` deltaP `20.0678` edge `0.5406` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8977` n `151` status `ready` deltaP `16.3604` edge `0.4519` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.9967` n `107` status `ready` deltaP `3.9706` edge `0.1976` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.9967` n `107` status `ready` deltaP `3.9706` edge `0.1976` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.8659` n `151` status `ready` deltaP `3.3331` edge `0.1963` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.2864` n `59` status `ready` deltaP `1.4361` edge `0.1323` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1635` n `59` status `ready` deltaP `10.7922` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1065` n `107` status `ready` deltaP `8.2433` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1065` n `107` status `ready` deltaP `8.2433` edge `0.0032` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_high->commodity_24h` score `0.0826` n `107` status `ready` deltaP `6.5226` edge `0.0622` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.0826` n `107` status `ready` deltaP `6.5226` edge `0.0622` maxDD `-0.5706`
- `risk_on_high->index_4h` score `-0.0055` n `107` status `ready` deltaP `18.9538` edge `0.006` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0055` n `107` status `ready` deltaP `18.9538` edge `0.006` maxDD `-3.6448`
- `market_context_high->commodity_1h` score `-0.1249` n `151` status `ready` deltaP `6.9259` edge `0.0084` maxDD `-1.5315`
- `risk_on_high->equity_1h` score `-0.1527` n `107` status `ready` deltaP `7.867` edge `0.0109` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1527` n `107` status `ready` deltaP `7.867` edge `0.0109` maxDD `-2.3009`
- `risk_on_high->commodity_1h` score `-0.1544` n `107` status `ready` deltaP `3.8251` edge `0.0069` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
