# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T12:22:24.428730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0365` n `54` status `ready` deltaP `38.5017` edge `0.3297` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0365` n `54` status `ready` deltaP `38.5017` edge `0.3297` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.3326` n `149` status `ready` deltaP `20.4064` edge `0.4405` maxDD `-5.906`
- `market_context_high->crypto_alt_4h` score `4.6737` n `149` status `ready` deltaP `12.5072` edge `0.5118` maxDD `-9.4562`
- `risk_on_high->crypto_major_4h` score `4.6427` n `75` status `ready` deltaP `25.9634` edge `0.3074` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6427` n `75` status `ready` deltaP `25.9634` edge `0.3074` maxDD `-4.1548`
- `market_context_high->crypto_major_1h` score `0.6646` n `161` status `ready` deltaP `5.5566` edge `0.0989` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4381` n `149` status `ready` deltaP `14.0018` edge `0.0477` maxDD `-1.6961`
- `market_context_high->crypto_alt_1h` score `0.367` n `161` status `ready` deltaP `7.0982` edge `0.1147` maxDD `-5.8485`
- `risk_on_high->crypto_alt_4h` score `0.2774` n `75` status `ready` deltaP `4.0955` edge `0.2131` maxDD `-9.387`
- `risk_on_and_context->crypto_alt_4h` score `0.2774` n `75` status `ready` deltaP `4.0955` edge `0.2131` maxDD `-9.387`
- `risk_on_high->index_1h` score `0.1694` n `87` status `ready` deltaP `6.9794` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1694` n `87` status `ready` deltaP `6.9794` edge `0.006` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1591` n `161` status `ready` deltaP `7.4292` edge `0.0049` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.3148` n `161` status `ready` deltaP `7.8021` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_4h` score `-0.3603` n `149` status `ready` deltaP `14.2079` edge `0.2017` maxDD `-17.4086`
- `risk_on_high->fx_1h` score `-0.3636` n `87` status `ready` deltaP `-0.7767` edge `-0.0034` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3636` n `87` status `ready` deltaP `-0.7767` edge `-0.0034` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.3715` n `161` status `ready` deltaP `9.8316` edge `0.0378` maxDD `-7.0778`
- `risk_on_high->equity_1h` score `-0.3781` n `87` status `ready` deltaP `10.5313` edge `0.0279` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
