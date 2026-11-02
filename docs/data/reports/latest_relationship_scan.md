# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T04:52:38.521679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8080`

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

- `market_context_high->unknown_24h` score `7023.5479` n `41` status `ready` deltaP `1.3889` edge `585.2864` maxDD `0.0`
- `market_context_high->unknown_4h` score `487.8273` n `44` status `ready` deltaP `9.1463` edge `40.5913` maxDD `0.0`
- `market_context_high->unknown_1h` score `87.0404` n `46` status `ready` deltaP `6.5738` edge `7.2206` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0019` n `41` status `ready` deltaP `42.1791` edge `1.3259` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.8718` n `94` status `ready` deltaP `34.2605` edge `1.0632` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.9237` n `41` status `ready` deltaP `44.3937` edge `0.3121` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.7278` n `44` status `ready` deltaP `29.3514` edge `0.3944` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.5166` n `41` status `ready` deltaP `49.1319` edge `0.2155` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.3185` n `44` status `ready` deltaP `28.1597` edge `0.2891` maxDD `-1.6901`
- `market_context_high->equity_4h` score `4.63` n `44` status `ready` deltaP `7.4002` edge `0.4067` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.8557` n `44` status `ready` deltaP `29.6979` edge `0.0657` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2312` n `126` status `ready` deltaP `8.8608` edge `0.2655` maxDD `-7.4246`
- `market_context_high->equity_1h` score `1.8119` n `46` status `ready` deltaP `3.8987` edge `0.1775` maxDD `-1.5336`
- `market_context_high->crypto_alt_24h` score `1.3821` n `41` status `ready` deltaP `-10.4463` edge `0.3366` maxDD `-8.8096`
- `market_context_high->fx_1h` score `1.0652` n `46` status `ready` deltaP `14.6186` edge `0.0089` maxDD `-0.0736`
- `market_context_high->crypto_alt_1h` score `1.0604` n `46` status `ready` deltaP `2.3236` edge `0.1341` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.0248` n `46` status `ready` deltaP `3.8987` edge `0.1103` maxDD `-1.4048`
- `market_context_high->metal_4h` score `0.9334` n `44` status `ready` deltaP `17.0038` edge `0.0488` maxDD `-0.7323`
- `market_context_high->crypto_major_24h` score `0.4301` n `41` status `ready` deltaP `-1.5583` edge `0.1332` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.2475` n `46` status `ready` deltaP `6.3655` edge `0.015` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
