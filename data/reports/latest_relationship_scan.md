# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T21:10:13.744151+00:00`
- Price records: `672`
- Market context records: `5286`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `24.236` n `153` status `ready` deltaP `27.3386` edge `1.8464` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.508` n `153` status `ready` deltaP `25.7353` edge `0.8691` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3164` n `177` status `ready` deltaP `16.962` edge `0.4107` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.033` n `177` status `ready` deltaP `16.4152` edge `0.4559` maxDD `-14.0065`
- `market_context_high->equity_24h` score `4.0322` n `153` status `ready` deltaP `19.9653` edge `0.7658` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.0426` n `177` status `ready` deltaP `10.3271` edge `0.1819` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7205` n `177` status `ready` deltaP `14.6497` edge `0.0646` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5613` n `153` status `ready` deltaP `13.3068` edge `0.0476` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.416` n `186` status `ready` deltaP `4.6681` edge `0.0997` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.249` n `153` status `ready` deltaP `20.8231` edge `0.0566` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2431` n `186` status `ready` deltaP `5.8657` edge `0.1057` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.1592` n `186` status `ready` deltaP `7.8746` edge `0.0573` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0488` n `186` status `ready` deltaP `5.3699` edge `0.0105` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2649` n `177` status `ready` deltaP `7.5557` edge `0.0274` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.27` n `186` status `ready` deltaP `2.3952` edge `0.0086` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3464` n `186` status `ready` deltaP `0.6809` edge `0.0` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.716` n `177` status `ready` deltaP `1.4132` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4148` n `186` status `ready` deltaP `-2.9876` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7134` n `177` status `ready` deltaP `-3.6637` edge `0.0051` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.8756` n `186` status `ready` deltaP `7.0376` edge `-0.2224` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
