# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T11:52:28.435727+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2166.8928` n `116` status `ready` deltaP `-6.8427` edge `180.663` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `94.6662` n `98` status `ready` deltaP `-5.493` edge `7.9541` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `51.0825` n `116` status `ready` deltaP `1.435` edge `4.2606` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.3926` n `41` status `ready` deltaP `45.9901` edge `1.1479` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.3267` n `116` status `ready` deltaP `25.856` edge `0.9639` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.0074` n `98` status `ready` deltaP `18.3331` edge `0.4337` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.5816` n `116` status `ready` deltaP `41.9121` edge `0.1207` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8732` n `98` status `ready` deltaP `7.7966` edge `0.1037` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.8079` n `116` status `ready` deltaP `18.6711` edge `0.0356` maxDD `-1.1867`
- `market_context_high->metal_1h` score `0.6133` n `116` status `ready` deltaP `13.7157` edge `0.0162` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.3836` n `116` status `ready` deltaP `5.0588` edge `0.0858` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.3491` n `116` status `ready` deltaP `3.853` edge `0.1584` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `0.2917` n `116` status `ready` deltaP `8.1716` edge `0.0726` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `-0.0301` n `116` status `ready` deltaP `10.2029` edge `0.05` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-0.0388` n `116` status `ready` deltaP `10.7579` edge `0.188` maxDD `-10.5088`
- `market_context_high->fx_1h` score `-0.0464` n `116` status `ready` deltaP `4.5375` edge `-0.0008` maxDD `-0.1655`
- `market_context_high->commodity_1h` score `-0.3132` n `116` status `ready` deltaP `-0.3046` edge `0.0133` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3461` n `116` status `ready` deltaP `2.3286` edge `-0.0019` maxDD `-0.3062`
- `market_context_high->index_1h` score `-0.4721` n `116` status `ready` deltaP `2.2507` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.7395` n `116` status `ready` deltaP `13.2306` edge `0.091` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
