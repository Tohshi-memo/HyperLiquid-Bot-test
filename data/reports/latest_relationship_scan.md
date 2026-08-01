# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T11:37:33.274683+00:00`
- Price records: `672`
- Market context records: `8617`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5192.427` n `60` status `ready` deltaP `34.2345` edge `432.5161` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.3226` n `43` status `ready` deltaP `52.7428` edge `1.215` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1591` n `60` status `ready` deltaP `20.7991` edge `0.4343` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4435` n `60` status `ready` deltaP `20.9513` edge `0.083` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.8186` n `62` status `ready` deltaP `13.2837` edge `0.1587` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.6544` n `60` status `ready` deltaP `14.6308` edge `0.088` maxDD `-2.4803`
- `market_context_high->fx_24h` score `1.3312` n `43` status `ready` deltaP `23.55` edge `0.0651` maxDD `-1.1145`
- `news_risk_high->crypto_major_4h` score `1.0484` n `60` status `ready` deltaP `6.446` edge `0.169` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4475` n `60` status `ready` deltaP `8.483` edge `0.0535` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3434` n `60` status `ready` deltaP `6.517` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->crypto_alt_4h` score `0.3434` n `60` status `ready` deltaP `10.3805` edge `0.114` maxDD `-5.8012`
- `news_risk_high->fx_4h` score `0.3097` n `60` status `ready` deltaP `14.6651` edge `0.0238` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1266` n `60` status `ready` deltaP `5.8982` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0799` n `60` status `ready` deltaP `5.7884` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `0.0754` n `60` status `ready` deltaP `3.3866` edge `0.0347` maxDD `-0.8085`
- `news_risk_high->index_1h` score `-0.024` n `60` status `ready` deltaP `2.9242` edge `0.0091` maxDD `-0.5338`
- `market_context_high->crypto_major_24h` score `-0.1155` n `43` status `ready` deltaP `2.9826` edge `0.4027` maxDD `-27.991`
- `market_context_high->fx_4h` score `-0.1527` n `62` status `ready` deltaP `8.0522` edge `0.0132` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2568` n `62` status `ready` deltaP `2.5111` edge `0.0006` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3309` n `62` status `ready` deltaP `3.8584` edge `-0.0056` maxDD `-2.0038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
