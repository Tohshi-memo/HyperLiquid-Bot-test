# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T23:37:27.082110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `38.4189` n `45` status `ready` deltaP `26.7709` edge `3.0274` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `12.2895` n `67` status `ready` deltaP `11.822` edge `0.9927` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.3924` n `45` status `ready` deltaP `48.1944` edge `0.5621` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.751` n `45` status `ready` deltaP `41.6667` edge `0.4694` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0397` n `31` status `ready` deltaP `12.192` edge `0.0706` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9038` n `31` status `ready` deltaP `19.3886` edge `0.0078` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.5153` n `67` status `ready` deltaP `8.5457` edge `0.0706` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.4888` n `79` status `ready` deltaP `11.4265` edge `-0.0006` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.4471` n `67` status `ready` deltaP `20.2517` edge `0.0083` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1305` n `79` status `ready` deltaP `4.8113` edge `0.0204` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.09` n `31` status `ready` deltaP `3.9782` edge `0.0353` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.119` n `31` status `ready` deltaP `9.8938` edge `-0.0258` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1521` n `31` status `ready` deltaP `1.0962` edge `-0.007` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2126` n `31` status `ready` deltaP `9.7933` edge `-0.0285` maxDD `-3.1233`
- `news_risk_high->index_4h` score `-0.215` n `31` status `ready` deltaP `-3.1127` edge `0.0409` maxDD `-0.3783`
- `market_context_high->index_1h` score `-0.2644` n `79` status `ready` deltaP `4.4853` edge `-0.0104` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3408` n `31` status `ready` deltaP `-2.2117` edge `0.0022` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.5224` n `31` status `ready` deltaP `-1.5146` edge `-0.008` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.532` n `79` status `ready` deltaP `-1.4629` edge `-0.009` maxDD `-1.6224`
- `news_risk_high->equity_4h` score `-0.5902` n `31` status `ready` deltaP `-16.3208` edge `0.1292` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
