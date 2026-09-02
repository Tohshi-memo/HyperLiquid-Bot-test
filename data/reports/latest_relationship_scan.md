# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T10:52:26.364574+00:00`
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

- `risk_on_high->unknown_4h` score `7.3464` n `107` status `ready` deltaP `18.2386` edge `0.5524` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3464` n `107` status `ready` deltaP `18.2386` edge `0.5524` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3809` n `148` status `ready` deltaP `14.1151` edge `0.4238` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.3872` n `107` status `ready` deltaP `22.8339` edge `0.6298` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.3872` n `107` status `ready` deltaP `22.8339` edge `0.6298` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.83` n `107` status `ready` deltaP `3.3718` edge `0.1877` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.83` n `107` status `ready` deltaP `3.3718` edge `0.1877` maxDD `-1.9475`
- `news_risk_high->equity_24h` score `1.3623` n `59` status `ready` deltaP `8.7835` edge `0.3032` maxDD `-15.5253`
- `market_context_high->equity_24h` score `1.2933` n `148` status `ready` deltaP `19.1019` edge `0.5217` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1197` n `59` status `ready` deltaP `0.8373` edge `0.1224` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.5003` n `148` status `ready` deltaP `1.9826` edge `0.0915` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2554` n `59` status `ready` deltaP `11.4019` edge `0.0046` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.122` n `107` status `ready` deltaP `8.393` edge `0.0042` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.122` n `107` status `ready` deltaP `8.393` edge `0.0042` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0995` n `107` status `ready` deltaP `20.4781` edge `0.0093` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0995` n `107` status `ready` deltaP `20.4781` edge `0.0093` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0624` n `107` status `ready` deltaP `11.3465` edge `0.0036` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0624` n `107` status `ready` deltaP `11.3465` edge `0.0036` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.0896` n `107` status `ready` deltaP `8.3161` edge `0.016` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.0896` n `107` status `ready` deltaP `8.3161` edge `0.016` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
