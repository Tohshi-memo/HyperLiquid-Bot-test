# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T12:34:15.518348+00:00`
- Price records: `672`
- Market context records: `7984`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11790`

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

- `market_context_high->equity_24h` score `16.0953` n `84` status `ready` deltaP `24.5039` edge `1.3121` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0194` n `84` status `ready` deltaP `35.9375` edge `0.4287` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4222` n `100` status `ready` deltaP `25.75` edge `0.4528` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4763` n `84` status `ready` deltaP `26.5129` edge `0.2662` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6592` n `100` status `ready` deltaP `27.8537` edge `0.0719` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5887` n `100` status `ready` deltaP `23.6646` edge `0.1202` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6931` n `104` status `ready` deltaP `14.5267` edge `0.126` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1759` n `84` status `ready` deltaP `9.7471` edge `0.1528` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1018` n `84` status `ready` deltaP `24.7768` edge `0.0354` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9384` n `104` status `ready` deltaP `15.0622` edge `0.0208` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9326` n `100` status `ready` deltaP `11.1037` edge `0.1755` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.9167` n `100` status `ready` deltaP `8.3415` edge `0.1325` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7416` n `104` status `ready` deltaP `10.6403` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5708` n `104` status `ready` deltaP `11.0894` edge `0.0403` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.066` n `104` status `ready` deltaP `0.4491` edge `0.0318` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2963` n `104` status `ready` deltaP `-0.3397` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.5279` n `100` status `ready` deltaP `4.061` edge `0.0037` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5412` n `104` status `ready` deltaP `-0.3858` edge `-0.0045` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.0488` n `100` status `ready` deltaP `0.4085` edge `-0.0018` maxDD `-4.8305`
- `market_context_high->unknown_1h` score `-1.9538` n `104` status `ready` deltaP `6.7538` edge `-0.1655` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
