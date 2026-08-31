# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T08:22:24.123731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `22.065` n `55` status `ready` deltaP `48.7942` edge `1.5615` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `22.065` n `55` status `ready` deltaP `48.7942` edge `1.5615` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.693` n `55` status `ready` deltaP `30.7765` edge `0.8277` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.693` n `55` status `ready` deltaP `30.7765` edge `0.8277` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.07` n `107` status `ready` deltaP `25.4032` edge `0.5648` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.07` n `107` status `ready` deltaP `25.4032` edge `0.5648` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.524` n `159` status `ready` deltaP `22.0998` edge `0.4657` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.4455` n `55` status `ready` deltaP `72.0486` edge `0.0568` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4455` n `55` status `ready` deltaP `72.0486` edge `0.0568` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2444` n `96` status `ready` deltaP `37.1527` edge `0.2502` maxDD `-1.8678`
- `market_context_high->crypto_major_24h` score `4.7537` n `96` status `ready` deltaP `21.875` edge `0.4994` maxDD `-17.2607`
- `market_context_high->crypto_alt_24h` score `4.6319` n `96` status `ready` deltaP `23.2639` edge `0.8577` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.4248` n `55` status `ready` deltaP `40.5808` edge `0.1454` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4248` n `55` status `ready` deltaP `40.5808` edge `0.1454` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.4863` n `107` status `ready` deltaP `6.3658` edge `0.2224` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4863` n `107` status `ready` deltaP `6.3658` edge `0.2224` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2636` n `159` status `ready` deltaP `5.7075` edge `0.2136` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.1321` n `96` status `ready` deltaP `38.7153` edge `0.0329` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `1.0474` n `43` status `ready` deltaP `10.5338` edge `0.0956` maxDD `-1.1904`
- `risk_on_high->equity_24h` score `1.0225` n `55` status `ready` deltaP `20.2778` edge `0.0308` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
