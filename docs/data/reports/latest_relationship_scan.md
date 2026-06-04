# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T13:07:29.594353+00:00`
- Price records: `672`
- Market context records: `2869`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `market_context_high->crypto_alt_24h` score `6.3554` n `142` status `ready` deltaP `5.6534` edge `0.8836` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.0085` n `142` status `ready` deltaP `7.6364` edge `0.3296` maxDD `-1.7175`
- `market_context_high->equity_24h` score `3.4438` n `142` status `ready` deltaP `6.9982` edge `0.4407` maxDD `-12.6963`
- `market_context_high->index_24h` score `1.7812` n `142` status `ready` deltaP `9.1965` edge `0.1852` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6035` n `142` status `ready` deltaP `15.0308` edge `0.3428` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.926` n `142` status `ready` deltaP `5.8807` edge `0.1433` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6703` n `142` status `ready` deltaP `15.2826` edge `0.0682` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0085` n `142` status `ready` deltaP `4.1811` edge `0.0445` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0454` n `142` status `ready` deltaP `4.4974` edge `0.0136` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1538` n `142` status `ready` deltaP `4.4014` edge `0.0958` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5169` n `142` status `ready` deltaP `14.4903` edge `0.2944` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5773` n `142` status `ready` deltaP `-0.2825` edge `0.0032` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6664` n `142` status `ready` deltaP `-2.0346` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6967` n `142` status `ready` deltaP `4.6471` edge `0.0557` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8152` n `142` status `ready` deltaP `-2.0009` edge `0.0287` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.8204` n `142` status `ready` deltaP `-1.2145` edge `-0.0125` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8726` n `142` status `ready` deltaP `4.2254` edge `0.0469` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1582` n `142` status `ready` deltaP `3.5147` edge `0.0201` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2649` n `142` status `ready` deltaP `-4.8201` edge `0.0046` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3891` n `142` status `ready` deltaP `-1.8852` edge `-0.016` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
