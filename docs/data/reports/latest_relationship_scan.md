# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T10:07:23.162070+00:00`
- Price records: `672`
- Market context records: `2856`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `3.9183` n `142` status `ready` deltaP `3.5701` edge `0.6944` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.3126` n `142` status `ready` deltaP `5.5531` edge `0.2855` maxDD `-1.7175`
- `market_context_high->equity_24h` score `1.2971` n `142` status `ready` deltaP `4.9149` edge `0.2757` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.2615` n `142` status `ready` deltaP `13.8155` edge `0.3224` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8866` n `142` status `ready` deltaP `6.0331` edge `0.139` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.867` n `142` status `ready` deltaP `7.1132` edge `0.1229` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.3622` n `142` status `ready` deltaP `13.4533` edge `0.0409` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1762` n `142` status `ready` deltaP `4.9296` edge `0.0549` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.075` n `142` status `ready` deltaP `4.198` edge `0.0118` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.5782` n `142` status `ready` deltaP `5.2459` edge `0.0669` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6225` n `142` status `ready` deltaP `-0.5819` edge `-0.0006` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.7084` n `142` status `ready` deltaP `-2.4837` edge `0.0019` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7557` n `142` status `ready` deltaP `-0.466` edge `-0.0092` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.7853` n `142` status `ready` deltaP `4.5248` edge `0.0561` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.8344` n `142` status `ready` deltaP `-2.1506` edge `0.0281` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-0.8506` n `142` status `ready` deltaP `2.877` edge `0.0479` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.0555` n `142` status `ready` deltaP `13.7281` edge `0.2546` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2369` n `142` status `ready` deltaP `-4.5152` edge `0.0049` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2714` n `142` status `ready` deltaP `2.4476` edge `0.0127` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4011` n `142` status `ready` deltaP `-1.8852` edge `-0.017` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
