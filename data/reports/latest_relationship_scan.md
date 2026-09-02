# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T10:37:29.843422+00:00`
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

- `risk_on_high->unknown_4h` score `7.3634` n `107` status `ready` deltaP `18.391` edge `0.5528` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3634` n `107` status `ready` deltaP `18.391` edge `0.5528` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3978` n `148` status `ready` deltaP `14.2675` edge `0.4242` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.2893` n `107` status `ready` deltaP `22.6603` edge `0.6228` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.2893` n `107` status `ready` deltaP `22.6603` edge `0.6228` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8324` n `107` status `ready` deltaP `3.3718` edge `0.1879` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8324` n `107` status `ready` deltaP `3.3718` edge `0.1879` maxDD `-1.9475`
- `news_risk_high->equity_24h` score `1.2644` n `59` status `ready` deltaP `8.6099` edge `0.2962` maxDD `-15.5253`
- `market_context_high->equity_24h` score `1.2296` n `148` status `ready` deltaP `18.9283` edge `0.5147` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1221` n `59` status `ready` deltaP `0.8373` edge `0.1226` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.5027` n `148` status `ready` deltaP `1.9826` edge `0.0917` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2554` n `59` status `ready` deltaP `11.4019` edge `0.0046` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.122` n `107` status `ready` deltaP `8.393` edge `0.0042` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.122` n `107` status `ready` deltaP `8.393` edge `0.0042` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.09` n `107` status `ready` deltaP `20.3257` edge `0.0091` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.09` n `107` status `ready` deltaP `20.3257` edge `0.0091` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0547` n `107` status `ready` deltaP `11.1968` edge `0.0036` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0547` n `107` status `ready` deltaP `11.1968` edge `0.0036` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.0989` n `107` status `ready` deltaP `8.1664` edge `0.0158` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.0989` n `107` status `ready` deltaP `8.1664` edge `0.0158` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
