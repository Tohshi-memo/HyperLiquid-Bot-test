# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T08:37:39.405231+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.1823` n `46` status `ready` deltaP `25.083` edge `2.9356` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.5414` n `46` status `ready` deltaP `43.1311` edge `0.4416` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9606` n `46` status `ready` deltaP `36.5262` edge `0.4378` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.6797` n `88` status `ready` deltaP `1.3581` edge `0.5638` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.198` n `88` status `ready` deltaP `15.3687` edge `0.082` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2836` n `88` status `ready` deltaP `17.0177` edge `0.0089` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2181` n `88` status `ready` deltaP `5.5321` edge `0.0229` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4577` n `88` status `ready` deltaP `1.7284` edge `-0.0168` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5401` n `88` status `ready` deltaP `-1.6195` edge `-0.009` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5827` n `88` status `ready` deltaP `4.4346` edge `0.0192` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9631` n `88` status `ready` deltaP `3.2567` edge `-0.0062` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2851` n `88` status `ready` deltaP `-3.62` edge `-0.0119` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5572` n `88` status `ready` deltaP `5.4641` edge `-0.0825` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.8429` n `46` status `ready` deltaP `-5.7895` edge `0.0056` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8523` n `88` status `ready` deltaP `-9.964` edge `-0.0456` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.4064` n `88` status `ready` deltaP `2.7491` edge `-0.2575` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6331` n `88` status `ready` deltaP `-12.9491` edge `-0.0791` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9192` n `46` status `ready` deltaP `-24.5094` edge `-0.1297` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.657` n `88` status `ready` deltaP `0.3325` edge `-0.3226` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
