# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T04:07:26.241808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6599`

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

- `market_context_high->equity_24h` score `10.6862` n `32` status `ready` deltaP `17.5347` edge `1.0109` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.7713` n `32` status `ready` deltaP `9.0278` edge `0.2295` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4812` n `32` status `ready` deltaP `17.7083` edge `0.1181` maxDD `-2.3671`
- `market_context_high->metal_1h` score `0.8687` n `72` status `ready` deltaP `10.8117` edge `0.0331` maxDD `-0.6226`
- `market_context_high->equity_1h` score `0.8295` n `72` status `ready` deltaP `3.4847` edge `0.1656` maxDD `-5.5762`
- `market_context_high->metal_4h` score `0.7437` n `60` status `ready` deltaP `10.4674` edge `0.0781` maxDD `-1.2025`
- `market_context_high->fx_24h` score `0.6796` n `32` status `ready` deltaP `10.7639` edge `-0.0063` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.4855` n `60` status `ready` deltaP `3.1606` edge `0.0666` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.2126` n `72` status `ready` deltaP `8.1587` edge `0.0221` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.1644` n `60` status `ready` deltaP `12.7235` edge `0.0291` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.1799` n `72` status `ready` deltaP `3.1853` edge `0.0221` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.6246` n `72` status `ready` deltaP `9.8553` edge `0.0435` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8744` n `72` status `ready` deltaP `-10.3875` edge `-0.0034` maxDD `-0.4893`
- `market_context_high->fx_4h` score `-1.4224` n `60` status `ready` deltaP `-6.5549` edge `-0.0048` maxDD `-1.3754`
- `market_context_high->metal_24h` score `-1.5191` n `32` status `ready` deltaP `1.0417` edge `-0.1464` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.8275` n `72` status `ready` deltaP `2.5033` edge `-0.0411` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.0911` n `60` status `ready` deltaP `8.3537` edge `0.0647` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.6774` n `32` status `ready` deltaP `-4.8611` edge `0.0069` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.7245` n `60` status `ready` deltaP `7.185` edge `-0.1414` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.9314` n `32` status `ready` deltaP `-18.75` edge `-0.1614` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
