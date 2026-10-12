# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T01:07:27.921939+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `1131.9075` n `44` status `ready` deltaP `-20.2967` edge `94.4973` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `38.991` n `109` status `ready` deltaP `-9.2247` edge `3.3813` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.2645` n `44` status `ready` deltaP `29.7191` edge `0.6168` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.328` n `44` status `ready` deltaP `52.4306` edge `0.1778` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.2056` n `30` status `ready` deltaP `22.8557` edge `0.3262` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2056` n `30` status `ready` deltaP `22.8557` edge `0.3262` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `3.5178` n `44` status `ready` deltaP `-13.3838` edge `0.6972` maxDD `-17.8526`
- `risk_on_high->crypto_major_4h` score `2.9298` n `30` status `ready` deltaP `25.1829` edge `0.293` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `2.9298` n `30` status `ready` deltaP `25.1829` edge `0.293` maxDD `-4.1548`
- `risk_on_high->metal_4h` score `2.8267` n `30` status `ready` deltaP `25.5996` edge `0.0881` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.8267` n `30` status `ready` deltaP `25.5996` edge `0.0881` maxDD `-0.1896`
- `market_context_high->fx_24h` score `2.1445` n `44` status `ready` deltaP `25.2367` edge `0.0286` maxDD `-0.1175`
- `risk_on_high->crypto_alt_1h` score `1.8305` n `42` status `ready` deltaP `12.1757` edge `0.1269` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.8305` n `42` status `ready` deltaP `12.1757` edge `0.1269` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.5018` n `42` status `ready` deltaP `13.8366` edge `0.0982` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.5018` n `42` status `ready` deltaP `13.8366` edge `0.0982` maxDD `-3.2233`
- `market_context_high->unknown_1h` score `1.3878` n `121` status `ready` deltaP `-3.5297` edge `0.1728` maxDD `-1.0231`
- `risk_on_high->metal_1h` score `1.3488` n `42` status `ready` deltaP `16.5027` edge `0.0263` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.3488` n `42` status `ready` deltaP `16.5027` edge `0.0263` maxDD `-0.2466`
- `risk_on_high->equity_4h` score `0.5814` n `30` status `ready` deltaP `4.3598` edge `0.0836` maxDD `-1.0501`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
