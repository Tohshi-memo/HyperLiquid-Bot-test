# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T23:37:31.410721+00:00`
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

- `risk_on_high->unknown_4h` score `6.9923` n `107` status `ready` deltaP `19.1532` edge `0.5168` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `6.9923` n `107` status `ready` deltaP `19.1532` edge `0.5168` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.5389` n `151` status `ready` deltaP `15.4458` edge `0.4281` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.884` n `107` status `ready` deltaP `3.3718` edge `0.1922` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.884` n `107` status `ready` deltaP `3.3718` edge `0.1922` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.7532` n `151` status `ready` deltaP `2.7343` edge `0.1909` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.1737` n `59` status `ready` deltaP `0.8373` edge `0.1269` maxDD `-1.1072`
- `risk_on_high->equity_24h` score `0.3002` n `107` status `ready` deltaP `15.0214` edge `0.3413` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `0.3002` n `107` status `ready` deltaP `15.0214` edge `0.3413` maxDD `-19.9806`
- `risk_on_high->metal_1h` score `0.1146` n `107` status `ready` deltaP `12.3944` edge `0.0033` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1146` n `107` status `ready` deltaP `12.3944` edge `0.0033` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `0.0867` n `59` status `ready` deltaP `9.8775` edge `0.0007` maxDD `-0.7461`
- `risk_on_high->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.1178` n `107` status `ready` deltaP `6.5226` edge `0.0455` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.1178` n `107` status `ready` deltaP `6.5226` edge `0.0455` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.1239` n `107` status `ready` deltaP `8.1664` edge `0.0126` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1239` n `107` status `ready` deltaP `8.1664` edge `0.0126` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
