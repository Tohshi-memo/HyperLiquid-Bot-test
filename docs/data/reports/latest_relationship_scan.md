# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T20:07:27.189834+00:00`
- Price records: `672`
- Market context records: `3107`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6923`

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

- `market_context_high->crypto_alt_24h` score `16.3687` n `87` status `ready` deltaP `13.9967` edge `2.5432` maxDD `-34.3699`
- `market_context_high->commodity_24h` score `14.9226` n `87` status `ready` deltaP `45.7316` edge `0.9815` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.2307` n `87` status `ready` deltaP `23.2339` edge `1.0798` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.296` n `87` status `ready` deltaP `31.4177` edge `0.904` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.7432` n `87` status `ready` deltaP `16.6547` edge `1.3514` maxDD `-40.4997`
- `market_context_high->commodity_4h` score `2.9918` n `120` status `ready` deltaP `17.9878` edge `0.1752` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.1328` n `125` status `ready` deltaP `1.0036` edge `0.0245` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5005` n `125` status `ready` deltaP `3.9461` edge `0.0158` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5789` n `87` status `ready` deltaP `3.9033` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.7955` n `125` status `ready` deltaP `-8.4515` edge `-0.0049` maxDD `-0.5931`
- `market_context_high->crypto_alt_1h` score `-0.7963` n `125` status `ready` deltaP `3.4455` edge `0.0879` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.1714` n `125` status `ready` deltaP `-0.9006` edge `0.0044` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3035` n `120` status `ready` deltaP `-11.9613` edge `-0.003` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4494` n `120` status `ready` deltaP `9.1768` edge `0.0439` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.85` n `120` status `ready` deltaP `4.8984` edge `0.0149` maxDD `-13.8046`
- `market_context_high->metal_1h` score `-2.3403` n `125` status `ready` deltaP `-6.7581` edge `-0.0106` maxDD `-7.4828`
- `market_context_high->crypto_major_1h` score `-2.3498` n `125` status `ready` deltaP `-2.0144` edge `0.0439` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-3.2758` n `125` status `ready` deltaP `1.8084` edge `-0.0824` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9344` n `120` status `ready` deltaP `12.2053` edge `0.2187` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0648` n `120` status `ready` deltaP `5.9146` edge `-0.03` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
