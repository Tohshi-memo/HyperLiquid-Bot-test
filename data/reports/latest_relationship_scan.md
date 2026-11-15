# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T19:52:25.489426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_24h` score `608.1081` n `59` status `ready` deltaP `3.9861` edge `50.6491` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.9021` n `50` status `ready` deltaP `50.565` edge `3.5587` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.9324` n `59` status `ready` deltaP `45.6158` edge `3.2611` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.2762` n `59` status `ready` deltaP `62.8705` edge `2.5449` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.0661` n `50` status `ready` deltaP `45.695` edge `2.7669` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.0606` n `50` status `ready` deltaP `38.3049` edge `0.8627` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5038` n `50` status `ready` deltaP `20.4298` edge `1.5328` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1563` n `59` status `ready` deltaP `49.1614` edge `0.3606` maxDD `-0.0251`
- `market_context_high->crypto_major_24h` score `8.0894` n `59` status `ready` deltaP `14.8136` edge `1.3311` maxDD `-55.7925`
- `market_context_high->metal_24h` score `6.6601` n `59` status `ready` deltaP `63.4667` edge `0.5199` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.6227` n `50` status `ready` deltaP `42.2461` edge `0.3006` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5139` n `50` status `ready` deltaP `42.6343` edge `0.2586` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.0907` n `50` status `ready` deltaP `22.3659` edge `0.4127` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.87` n `50` status `ready` deltaP `44.0793` edge `0.1496` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.4808` n `50` status `ready` deltaP `26.9939` edge `0.337` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0019` n `50` status `ready` deltaP `21.497` edge `0.2532` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6868` n `50` status `ready` deltaP `34.2866` edge `0.104` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5185` n `50` status `ready` deltaP `24.3415` edge `0.0826` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3046` n `50` status `ready` deltaP `17.3473` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
