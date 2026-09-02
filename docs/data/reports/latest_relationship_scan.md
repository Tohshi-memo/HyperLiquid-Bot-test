# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T05:37:24.680572+00:00`
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

- `risk_on_high->unknown_4h` score `7.5753` n `107` status `ready` deltaP `19.9154` edge `0.5603` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5753` n `107` status `ready` deltaP `19.9154` edge `0.5603` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6098` n `148` status `ready` deltaP `15.7919` edge `0.4317` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `2.4804` n `107` status `ready` deltaP `19.1881` edge `0.4952` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `2.4804` n `107` status `ready` deltaP `19.1881` edge `0.4952` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.7245` n `107` status `ready` deltaP `3.0724` edge `0.1809` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7245` n `107` status `ready` deltaP `3.0724` edge `0.1809` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.0142` n `59` status `ready` deltaP `0.5379` edge `0.1156` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.3948` n `148` status `ready` deltaP `1.6832` edge `0.0847` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2168` n `59` status `ready` deltaP `11.2495` edge `0.0024` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1111` n `107` status `ready` deltaP `8.2433` edge `0.0038` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1111` n `107` status `ready` deltaP `8.2433` edge `0.0038` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0905` n `107` status `ready` deltaP `11.7956` edge `0.0042` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0905` n `107` status `ready` deltaP `11.7956` edge `0.0042` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0838` n `107` status `ready` deltaP `20.3257` edge `0.0083` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0838` n `107` status `ready` deltaP `20.3257` edge `0.0083` maxDD `-3.6448`
- `market_context_high->equity_24h` score `0.0538` n `148` status `ready` deltaP `15.4561` edge `0.3871` maxDD `-24.6594`
- `risk_on_high->equity_1h` score `-0.127` n `107` status `ready` deltaP `8.0167` edge `0.0132` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.127` n `107` status `ready` deltaP `8.0167` edge `0.0132` maxDD `-2.3009`
- `market_context_high->commodity_1h` score `-0.1801` n `148` status `ready` deltaP `6.5504` edge `0.0063` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
