# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T02:37:36.534620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10302`

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

- `market_context_high->unknown_24h` score `408.2285` n `75` status `ready` deltaP `2.1944` edge `34.0185` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.1745` n `53` status `ready` deltaP `35.23` edge `2.8503` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.9408` n `75` status `ready` deltaP `29.7708` edge `2.2841` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.935` n `75` status `ready` deltaP `47.5834` edge `1.3455` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.1525` n `53` status `ready` deltaP `42.0434` edge `1.8589` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2198` n `53` status `ready` deltaP `36.2402` edge `0.8064` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.2221` n `53` status `ready` deltaP `41.1458` edge `0.2442` maxDD `0.0`
- `market_context_high->index_24h` score `5.5166` n `75` status `ready` deltaP `31.4653` edge `0.2591` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0649` n `53` status `ready` deltaP `48.2254` edge `0.1382` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.8356` n `53` status `ready` deltaP `29.4778` edge `0.2368` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1941` n `75` status `ready` deltaP `41.3334` edge `0.3513` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.6222` n `53` status `ready` deltaP `20.8957` edge `0.3113` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5792` n `53` status `ready` deltaP `18.7634` edge `0.2362` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0409` n `53` status `ready` deltaP `27.4736` edge `0.0956` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2913` n `53` status `ready` deltaP `26.7879` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0068` n `53` status `ready` deltaP `20.2888` edge `0.0756` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8876` n `53` status `ready` deltaP `25.5838` edge `0.2353` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.8019` n `53` status `ready` deltaP `14.4261` edge `0.5854` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1999` n `53` status `ready` deltaP `16.2778` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7102` n `53` status `ready` deltaP `17.594` edge `0.0717` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
