# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T12:20:27.499638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `71.5638` n `47` status `ready` deltaP `10.2657` edge `5.9023` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.5037` n `46` status `ready` deltaP `30.7216` edge `3.4361` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `29.3268` n `46` status `ready` deltaP `25.6944` edge `2.2726` maxDD `0.0`
- `market_context_high->equity_24h` score `25.0823` n `46` status `ready` deltaP `28.1175` edge `1.9128` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.7625` n `103` status `ready` deltaP `3.0306` edge `1.6976` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.222` n `46` status `ready` deltaP `36.9716` edge `0.4474` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `7.0647` n `103` status `ready` deltaP `0.4517` edge `1.287` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5951` n `46` status `ready` deltaP `31.1217` edge `0.1155` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.076` n `47` status `ready` deltaP `34.941` edge `0.0388` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6659` n `47` status `ready` deltaP `17.7542` edge `0.1456` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.3457` n `117` status `ready` deltaP `12.557` edge `0.1608` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0109` n `117` status `ready` deltaP `14.6528` edge `0.1134` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6705` n `114` status `ready` deltaP `24.5561` edge `0.0391` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3292` n `103` status `ready` deltaP `17.4976` edge `0.112` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.3219` n `103` status `ready` deltaP `30.3584` edge `0.1302` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0302` n `47` status `ready` deltaP `15.3586` edge `0.0113` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `1.0036` n `103` status `ready` deltaP `22.9959` edge `0.1202` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.9475` n `47` status `ready` deltaP `11.167` edge `0.0448` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.8486` n `114` status `ready` deltaP `13.091` edge `0.1966` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.7961` n `117` status `ready` deltaP `16.3916` edge `0.0164` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
