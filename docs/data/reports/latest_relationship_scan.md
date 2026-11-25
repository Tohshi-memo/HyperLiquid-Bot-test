# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T20:22:29.192312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3732`

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

- `market_context_high->unknown_1h` score `32163.4826` n `45` status `ready` deltaP `1.7165` edge `2680.2882` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21834.8998` n `45` status `ready` deltaP `1.958` edge `1819.5758` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `928.5276` n `31` status `ready` deltaP `1.9316` edge `77.382` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `581.9523` n `31` status `ready` deltaP `3.1766` edge `48.4805` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `300.3479` n `31` status `ready` deltaP `5.7292` edge `24.9908` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3587` n `31` status `ready` deltaP `52.0833` edge `3.516` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4604` n `31` status `ready` deltaP `54.3403` edge `3.1761` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.2273` n `31` status `ready` deltaP `54.1667` edge `2.8245` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9305` n `31` status `ready` deltaP `40.8883` edge `0.7491` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.1209` n `31` status `ready` deltaP `26.4555` edge `0.8374` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7829` n `31` status `ready` deltaP `37.8344` edge `0.6944` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4799` n `31` status `ready` deltaP `53.2986` edge `0.268` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.8954` n `31` status `ready` deltaP `17.6927` edge `0.9078` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4247` n `31` status `ready` deltaP `46.5726` edge `0.1544` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6379` n `31` status `ready` deltaP `19.9874` edge `0.1886` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3654` n `31` status `ready` deltaP `36.31` edge `0.0644` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6542` n `31` status `ready` deltaP `31.5434` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4415` n `31` status `ready` deltaP `10.1603` edge `0.2914` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3741` n `45` status `ready` deltaP `29.3259` edge `0.0308` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2464` n `31` status `ready` deltaP `12.7052` edge `0.239` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
