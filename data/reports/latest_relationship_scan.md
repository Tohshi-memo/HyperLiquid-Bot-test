# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T22:22:27.271426+00:00`
- Price records: `672`
- Market context records: `5291`
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

- `market_context_high->unknown_24h` score `23.0734` n `153` status `ready` deltaP `26.4706` edge `1.7553` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5608` n `153` status `ready` deltaP `25.7353` edge `0.8735` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.3454` n `153` status `ready` deltaP `19.9653` edge `0.7919` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `4.144` n `180` status `ready` deltaP `16.0976` edge `0.4021` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0117` n `180` status `ready` deltaP `16.6429` edge `0.4526` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.2487` n `180` status `ready` deltaP `10.8638` edge `0.1955` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.9203` n `180` status `ready` deltaP `14.4918` edge `0.0823` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5529` n `153` status `ready` deltaP `13.3068` edge `0.0469` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3484` n `191` status `ready` deltaP `4.2284` edge `0.097` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2724` n `153` status `ready` deltaP `20.8231` edge `0.0596` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.1755` n `191` status `ready` deltaP `5.5757` edge `0.102` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.1566` n `191` status `ready` deltaP `8.261` edge `0.0545` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0448` n `191` status `ready` deltaP `5.495` edge `0.01` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2793` n `180` status `ready` deltaP `7.3103` edge `0.0272` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3728` n `191` status `ready` deltaP `1.834` edge `0.0075` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3815` n `191` status `ready` deltaP `0.0353` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7293` n `180` status `ready` deltaP `1.1585` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4242` n `191` status `ready` deltaP `-3.1045` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7759` n `180` status `ready` deltaP `-4.3699` edge `0.0018` maxDD `-9.3609`
- `market_context_high->crypto_alt_24h` score `-2.9062` n `153` status `ready` deltaP `13.3476` edge `0.3794` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
