# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T06:22:26.718981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3702`

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

- `news_risk_high->unknown_1h` score `3355.3645` n `31` status `ready` deltaP `1.4825` edge `279.6214` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3213.7245` n `31` status `ready` deltaP `3.634` edge `267.7918` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.9682` n `31` status `ready` deltaP `31.0225` edge `1.4572` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.9662` n `31` status `ready` deltaP `28.9428` edge `0.9709` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.6703` n `31` status `ready` deltaP `24.7834` edge `0.8073` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7471` n `31` status `ready` deltaP `20.3579` edge `0.5969` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.15` n `31` status `ready` deltaP `28.3832` edge `0.288` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.7921` n `31` status `ready` deltaP `14.3391` edge `0.6605` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.7534` n `31` status `ready` deltaP `38.6762` edge `0.1511` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.4553` n `31` status `ready` deltaP `13.0542` edge `0.2284` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2852` n `31` status `ready` deltaP `28.1003` edge `0.0116` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2433` n `31` status `ready` deltaP `27.7734` edge `0.0278` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2432` n `31` status `ready` deltaP `25.13` edge `0.0194` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.14` n `31` status `ready` deltaP `14.4485` edge `0.1007` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7829` n `31` status `ready` deltaP `5.5196` edge `0.2379` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6758` n `31` status `ready` deltaP `8.813` edge `0.1918` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1146` n `31` status `ready` deltaP `24.3432` edge `0.0085` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.3138` n `30` status `ready` deltaP `6.517` edge `0.0041` maxDD `-0.0451`
- `news_risk_high->commodity_4h` score `0.2914` n `31` status `ready` deltaP `7.7596` edge `0.0254` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2655` n `31` status `ready` deltaP `10.3757` edge `0.0206` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
