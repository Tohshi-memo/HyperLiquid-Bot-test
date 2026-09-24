# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T10:37:31.864062+00:00`
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

- `market_context_high->unknown_1h` score `66.0018` n `47` status `ready` deltaP `10.5651` edge `5.4368` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.2377` n `46` status `ready` deltaP `29.5064` edge `3.3387` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `27.8195` n `46` status `ready` deltaP `24.4792` edge `2.1551` maxDD `0.0`
- `market_context_high->equity_24h` score `24.487` n `46` status `ready` deltaP `26.9022` edge `1.8713` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.4965` n `103` status `ready` deltaP `1.8154` edge `1.6002` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.0595` n `46` status `ready` deltaP `35.93` edge `0.4408` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.5574` n `103` status `ready` deltaP `-0.7635` edge `1.1695` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.3671` n `46` status `ready` deltaP `29.9064` edge `0.1046` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.9801` n `47` status `ready` deltaP `34.0263` edge `0.0369` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.5209` n `114` status `ready` deltaP `13.5466` edge `0.1688` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.4727` n `47` status `ready` deltaP `16.8396` edge `0.1356` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.1165` n `114` status `ready` deltaP `15.4927` edge `0.1166` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7105` n `112` status `ready` deltaP `24.8911` edge `0.0402` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.4754` n `103` status `ready` deltaP `18.3657` edge `0.1184` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `1.3405` n `112` status `ready` deltaP `13.3711` edge `0.1996` maxDD `-11.4961`
- `news_risk_high->fx_24h` score `1.2941` n `103` status `ready` deltaP `30.1847` edge `0.1278` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9966` n `47` status `ready` deltaP `15.0592` edge `0.0105` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9139` n `47` status `ready` deltaP `11.0173` edge `0.043` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8554` n `103` status `ready` deltaP `21.7806` edge `0.1093` maxDD `-7.2536`
- `news_risk_high->crypto_alt_4h` score `0.7873` n `112` status `ready` deltaP `8.5149` edge `0.2462` maxDD `-13.1628`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
