# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T05:07:47.684696+00:00`
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

- `risk_on_high->unknown_4h` score `7.5837` n `107` status `ready` deltaP `19.9154` edge `0.561` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5837` n `107` status `ready` deltaP `19.9154` edge `0.561` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.567` n `149` status `ready` deltaP `15.9324` edge `0.4272` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `2.3122` n `107` status `ready` deltaP `18.8409` edge `0.4835` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `2.3122` n `107` status `ready` deltaP `18.8409` edge `0.4835` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.5781` n `107` status `ready` deltaP `3.0724` edge `0.1687` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.5781` n `107` status `ready` deltaP `3.0724` edge `0.1687` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `0.8678` n `59` status `ready` deltaP `0.5379` edge `0.1034` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.8051` n `149` status `ready` deltaP `1.9371` edge `0.1172` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2023` n `59` status `ready` deltaP `11.0971` edge `0.0022` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1283` n `107` status `ready` deltaP `8.5427` edge `0.004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1283` n `107` status `ready` deltaP `8.5427` edge `0.004` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.1092` n `107` status `ready` deltaP `12.095` edge `0.0046` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1092` n `107` status `ready` deltaP `12.095` edge `0.0046` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0838` n `107` status `ready` deltaP `20.3257` edge `0.0083` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0838` n `107` status `ready` deltaP `20.3257` edge `0.0083` maxDD `-3.6448`
- `market_context_high->equity_24h` score `0.0144` n `149` status `ready` deltaP `15.4036` edge `0.3824` maxDD `-24.6594`
- `risk_on_high->equity_1h` score `-0.1013` n `107` status `ready` deltaP `8.3161` edge `0.0145` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1013` n `107` status `ready` deltaP `8.3161` edge `0.0145` maxDD `-2.3009`
- `news_risk_high->index_1h` score `-0.163` n `59` status `ready` deltaP `3.1412` edge `-0.0065` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
