# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T21:52:53.324364+00:00`
- Price records: `672`
- Market context records: `5289`
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

- `market_context_high->unknown_24h` score `23.5775` n `153` status `ready` deltaP `26.8178` edge `1.795` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.544` n `153` status `ready` deltaP `25.7353` edge `0.8721` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.231` n `179` status `ready` deltaP `16.5852` edge `0.4061` maxDD `-9.46`
- `market_context_high->equity_24h` score `4.2158` n `153` status `ready` deltaP `19.9653` edge `0.7811` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `4.0609` n `179` status `ready` deltaP `16.8381` edge `0.4554` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.0822` n `179` status `ready` deltaP `10.6869` edge `0.1828` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.8908` n `179` status `ready` deltaP `14.6478` edge `0.0788` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5565` n `153` status `ready` deltaP `13.3068` edge `0.0472` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3247` n `189` status `ready` deltaP `4.0071` edge `0.0965` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2638` n `153` status `ready` deltaP `20.8231` edge `0.0585` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1663` n `189` status `ready` deltaP `8.1726` edge `0.0559` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1578` n `189` status `ready` deltaP `5.3544` edge `0.102` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0523` n `189` status `ready` deltaP `5.3568` edge `0.0103` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2779` n `179` status `ready` deltaP `7.3375` edge `0.0272` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3872` n `189` status `ready` deltaP `1.6015` edge `0.0072` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3919` n `189` status `ready` deltaP `-0.1639` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7277` n `179` status `ready` deltaP `1.1889` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3791` n `189` status `ready` deltaP `-2.6004` edge `-0.0058` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7552` n `179` status `ready` deltaP `-4.1372` edge `0.0029` maxDD `-9.3609`
- `market_context_high->crypto_alt_24h` score `-2.9031` n `153` status `ready` deltaP `13.3476` edge `0.3798` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
