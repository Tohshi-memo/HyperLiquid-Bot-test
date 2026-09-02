# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T04:07:23.894818+00:00`
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

- `risk_on_high->unknown_4h` score `7.6389` n `107` status `ready` deltaP `19.9154` edge `0.5656` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6389` n `107` status `ready` deltaP `19.9154` edge `0.5656` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.5817` n `150` status `ready` deltaP `16.0711` edge `0.4275` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `1.9422` n `107` status `ready` deltaP `18.1464` edge `0.4573` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `1.9422` n `107` status `ready` deltaP `18.1464` edge `0.4573` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.4365` n `107` status `ready` deltaP `2.9227` edge `0.1579` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.4365` n `107` status `ready` deltaP `2.9227` edge `0.1579` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.2775` n `150` status `ready` deltaP `2.038` edge `0.1559` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `0.7262` n `59` status `ready` deltaP `0.3882` edge `0.0926` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1987` n `59` status `ready` deltaP `11.0971` edge `0.0019` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1442` n `107` status `ready` deltaP `12.6938` edge `0.0051` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1442` n `107` status `ready` deltaP `12.6938` edge `0.0051` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.1111` n `107` status `ready` deltaP `8.2433` edge `0.0038` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1111` n `107` status `ready` deltaP `8.2433` edge `0.0038` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0815` n `107` status `ready` deltaP `20.3257` edge `0.008` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0815` n `107` status `ready` deltaP `20.3257` edge `0.008` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1231` n `107` status `ready` deltaP `8.0167` edge `0.0137` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1231` n `107` status `ready` deltaP `8.0167` edge `0.0137` maxDD `-2.3009`
- `news_risk_high->index_1h` score `-0.1802` n `59` status `ready` deltaP `2.8418` edge `-0.0067` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.1896` n `150` status `ready` deltaP `6.4471` edge `0.0062` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
