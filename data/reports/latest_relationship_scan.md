# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T11:52:26.713207+00:00`
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

- `risk_on_high->unknown_4h` score `7.3198` n `107` status `ready` deltaP `18.0861` edge `0.5512` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3198` n `107` status `ready` deltaP `18.0861` edge `0.5512` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3543` n `148` status `ready` deltaP `13.9626` edge `0.4226` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.7404` n `107` status `ready` deltaP `23.5284` edge `0.6546` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.7404` n `107` status `ready` deltaP `23.5284` edge `0.6546` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.7809` n `107` status `ready` deltaP `3.0724` edge `0.1856` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7809` n `107` status `ready` deltaP `3.0724` edge `0.1856` maxDD `-1.9475`
- `news_risk_high->equity_24h` score `1.7154` n `59` status `ready` deltaP `9.478` edge `0.328` maxDD `-15.5253`
- `market_context_high->equity_24h` score `1.5228` n `148` status `ready` deltaP `19.7964` edge `0.5465` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.0706` n `59` status `ready` deltaP `0.5379` edge `0.1203` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.4512` n `148` status `ready` deltaP `1.6832` edge `0.0894` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2724` n `59` status `ready` deltaP `11.5544` edge `0.005` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.139` n `107` status `ready` deltaP `21.0879` edge `0.0103` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.139` n `107` status `ready` deltaP `21.0879` edge `0.0103` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.1283` n `107` status `ready` deltaP `8.5427` edge `0.004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1283` n `107` status `ready` deltaP `8.5427` edge `0.004` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0375` n `107` status `ready` deltaP `11.0471` edge `0.0024` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0375` n `107` status `ready` deltaP `11.0471` edge `0.0024` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.1021` n `107` status `ready` deltaP `8.1664` edge `0.0154` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1021` n `107` status `ready` deltaP `8.1664` edge `0.0154` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
