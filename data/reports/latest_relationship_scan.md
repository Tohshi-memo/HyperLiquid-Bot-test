# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T05:52:36.450796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32360.2814` n `45` status `ready` deltaP `1.8662` edge `2696.6871` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22196.4095` n `45` status `ready` deltaP `1.958` edge `1849.7016` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.7521` n `31` status `ready` deltaP `2.0813` edge `95.8997` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `961.0563` n `31` status `ready` deltaP `3.1766` edge `80.0725` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.4842` n `31` status `ready` deltaP `41.4931` edge `2.6804` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9267` n `31` status `ready` deltaP `45.8333` edge `2.605` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4769` n `31` status `ready` deltaP `44.2708` edge `2.2446` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6049` n `31` status `ready` deltaP `41.4091` edge `0.7185` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5528` n `31` status `ready` deltaP `23.2543` edge `0.8114` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5987` n `31` status `ready` deltaP `30.8222` edge `0.5593` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6711` n `31` status `ready` deltaP `56.4684` edge `0.1923` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5928` n `31` status `ready` deltaP `14.0342` edge `0.8934` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3846` n `31` status `ready` deltaP `39.0625` edge `0.1883` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1378` n `31` status `ready` deltaP `17.1431` edge `0.1659` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1296` n `45` status `ready` deltaP `37.4051` edge `0.0399` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.6938` n `31` status `ready` deltaP `30.06` edge `0.0501` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4695` n `31` status `ready` deltaP `10.6094` edge `0.292` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4087` n `31` status `ready` deltaP `28.8488` edge `0.0169` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.0719` n `31` status `ready` deltaP `10.0106` edge `0.2346` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.631` n `31` status `ready` deltaP `31.0797` edge `0.0298` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
