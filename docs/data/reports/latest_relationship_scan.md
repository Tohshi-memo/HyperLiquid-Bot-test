# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T09:07:26.353776+00:00`
- Price records: `672`
- Market context records: `5129`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `29.9604` n `62` status `ready` deltaP `28.7635` edge `2.3392` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.6404` n `127` status `ready` deltaP `9.4323` edge `0.7213` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.32` n `118` status `ready` deltaP `19.8326` edge `0.58` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.9234` n `118` status `ready` deltaP `14.1148` edge `0.4761` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4564` n `118` status `ready` deltaP `11.8773` edge `0.4381` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.5775` n `62` status `ready` deltaP `21.2365` edge `0.1581` maxDD `-4.7946`
- `market_context_high->equity_1h` score `0.7091` n `127` status `ready` deltaP `7.7408` edge `0.0668` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.6681` n `118` status `ready` deltaP `7.7615` edge `0.1678` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6317` n `127` status `ready` deltaP `4.214` edge `0.1207` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.561` n `127` status `ready` deltaP `6.5703` edge `0.1275` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.1045` n `127` status `ready` deltaP `6.4595` edge `0.0218` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.003` n `127` status `ready` deltaP `5.2678` edge `0.015` maxDD `-1.0296`
- `market_context_high->metal_24h` score `-0.1762` n `62` status `ready` deltaP `1.5569` edge `0.1988` maxDD `-12.909`
- `market_context_high->index_4h` score `-0.5434` n `118` status `ready` deltaP `4.7927` edge `0.0345` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5451` n `127` status `ready` deltaP `1.1033` edge `-0.0003` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.6118` n `118` status `ready` deltaP `1.6044` edge `0.0519` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6707` n `127` status `ready` deltaP `-2.9834` edge `-0.002` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.9834` n `118` status `ready` deltaP `-2.8473` edge `0.0002` maxDD `-1.9169`
- `market_context_high->crypto_alt_24h` score `-1.254` n `62` status `ready` deltaP `13.6369` edge `0.4996` maxDD `-54.1021`
- `market_context_high->fx_24h` score `-1.2575` n `62` status `ready` deltaP `-0.6944` edge `-0.0074` maxDD `-1.0879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
