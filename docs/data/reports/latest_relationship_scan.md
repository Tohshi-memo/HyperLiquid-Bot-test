# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T06:22:25.050947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10428`

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

- `market_context_high->unknown_24h` score `439.5881` n `75` status `ready` deltaP `2.1944` edge `36.6318` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.0169` n `53` status `ready` deltaP `35.23` edge `2.9205` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.7832` n `75` status `ready` deltaP `29.7708` edge `2.3543` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.5594` n `75` status `ready` deltaP `47.5834` edge `1.3142` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.4411` n `53` status `ready` deltaP `42.0434` edge `1.8959` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3032` n `53` status `ready` deltaP `36.6975` edge `0.8103` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.5084` n `53` status `ready` deltaP `43.75` edge `0.2507` maxDD `0.0`
- `market_context_high->index_24h` score `5.8114` n `75` status `ready` deltaP `34.0695` edge `0.2663` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.1304` n `53` status `ready` deltaP `32.082` edge `0.244` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0757` n `53` status `ready` deltaP `48.2254` edge `0.1391` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3009` n `75` status `ready` deltaP `41.3334` edge `0.365` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.224` n `53` status `ready` deltaP `22.2676` edge `0.3523` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5637` n `53` status `ready` deltaP `18.6137` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0775` n `53` status `ready` deltaP `27.9309` edge `0.0956` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2817` n `53` status `ready` deltaP `26.6382` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1943` n `53` status `ready` deltaP `22.4229` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0964` n `53` status `ready` deltaP `26.1936` edge `0.258` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.5578` n `53` status `ready` deltaP `14.4261` edge `0.5541` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2131` n `53` status `ready` deltaP `16.4275` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7247` n `53` status `ready` deltaP `17.8934` edge `0.0788` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
