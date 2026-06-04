# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T14:52:28.023453+00:00`
- Price records: `672`
- Market context records: `2876`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `7.5362` n `142` status `ready` deltaP `6.8687` edge `0.9739` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.4873` n `142` status `ready` deltaP `8.8517` edge `0.3614` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.291` n `142` status `ready` deltaP `8.2135` edge `0.5032` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.164` n `142` status `ready` deltaP `10.4118` edge `0.209` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7064` n `142` status `ready` deltaP `15.5516` edge `0.3479` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8326` n `142` status `ready` deltaP `6.0331` edge `0.1345` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7601` n `142` status `ready` deltaP `15.435` edge `0.0787` maxDD `-2.3986`
- `market_context_high->index_1h` score `0.0006` n `142` status `ready` deltaP `4.6471` edge `0.0185` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.0458` n `142` status `ready` deltaP `4.4014` edge `0.1048` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.0745` n `142` status `ready` deltaP `4.0314` edge `0.04` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4941` n `142` status `ready` deltaP `14.4903` edge `0.2963` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5804` n `142` status `ready` deltaP `-0.4322` edge `0.0038` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6784` n `142` status `ready` deltaP `-2.1843` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.7038` n `142` status `ready` deltaP `4.7968` edge `0.0538` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7128` n `142` status `ready` deltaP `-0.6157` edge `-0.0027` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7504` n `142` status `ready` deltaP `-2.0009` edge `0.0341` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8337` n `142` status `ready` deltaP `4.6745` edge `0.0489` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.104` n `142` status `ready` deltaP `3.972` edge `0.024` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.3039` n `142` status `ready` deltaP `-5.2774` edge `0.0044` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3903` n `142` status `ready` deltaP `-1.8852` edge `-0.0161` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
