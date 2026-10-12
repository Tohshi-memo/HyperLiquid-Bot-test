# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T02:52:32.280815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `703.883` n `51` status `ready` deltaP `-17.1772` edge `58.8078` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `35.947` n `116` status `ready` deltaP `-7.6745` edge `3.1173` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.0447` n `51` status `ready` deltaP `28.9522` edge `0.6036` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9605` n `51` status `ready` deltaP `50.6434` edge `0.1634` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.3541` n `37` status `ready` deltaP `30.0964` edge `0.3308` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3541` n `37` status `ready` deltaP `30.0964` edge `0.3308` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.1546` n `37` status `ready` deltaP `23.9577` edge `0.3146` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1546` n `37` status `ready` deltaP `23.9577` edge `0.3146` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `4.0169` n `51` status `ready` deltaP `-3.2986` edge `0.8518` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.2671` n `37` status `ready` deltaP `29.7091` edge `0.0974` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.2671` n `37` status `ready` deltaP `29.7091` edge `0.0974` maxDD `-0.1896`
- `risk_on_high->metal_1h` score `1.5369` n `49` status `ready` deltaP `18.8837` edge `0.0261` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.5369` n `49` status `ready` deltaP `18.8837` edge `0.0261` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.3962` n `49` status `ready` deltaP `12.6665` edge `0.0972` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3962` n `49` status `ready` deltaP `12.6665` edge `0.0972` maxDD `-3.2233`
- `risk_on_high->crypto_alt_1h` score `1.3931` n `49` status `ready` deltaP `9.3731` edge `0.1133` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.3931` n `49` status `ready` deltaP `9.3731` edge `0.1133` maxDD `-2.4421`
- `market_context_high->fx_24h` score `0.6977` n `51` status `ready` deltaP `13.6948` edge `0.018` maxDD `-0.4261`
- `market_context_high->metal_4h` score `0.403` n `116` status `ready` deltaP `11.559` edge `0.0288` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.28` n `116` status `ready` deltaP `6.1448` edge `0.2055` maxDD `-11.1784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
