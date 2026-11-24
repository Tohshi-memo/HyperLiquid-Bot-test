# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T16:07:28.486858+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4302`

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

- `market_context_high->unknown_1h` score `32299.2194` n `45` status `ready` deltaP `1.7165` edge `2691.5996` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22116.5597` n `45` status `ready` deltaP `2.5678` edge `1843.0434` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1064.2644` n `31` status `ready` deltaP `1.9316` edge `88.6934` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `863.6122` n `31` status `ready` deltaP `3.7864` edge `71.9481` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.2403` n `31` status `ready` deltaP `49.4792` edge `2.7735` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.0382` n `31` status `ready` deltaP `40.9722` edge `2.6467` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.3899` n `31` status `ready` deltaP `47.0486` edge `2.3855` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0918` n `31` status `ready` deltaP `41.2355` edge `0.6769` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.0138` n `31` status `ready` deltaP `24.3214` edge `0.8427` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.281` n `31` status `ready` deltaP `32.6515` edge `0.6038` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.7874` n `31` status `ready` deltaP `15.4062` edge `0.9092` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.4359` n `31` status `ready` deltaP `54.0379` edge `0.1889` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.1828` n `31` status `ready` deltaP `38.7153` edge `0.1738` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4797` n `31` status `ready` deltaP `18.7898` edge `0.1834` maxDD `-0.1621`
- `market_context_high->fx_4h` score `2.9279` n `45` status `ready` deltaP `35.4234` edge `0.0363` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9024` n `31` status `ready` deltaP `31.7369` edge `0.0563` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6122` n `31` status `ready` deltaP `11.807` edge `0.3023` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5512` n `31` status `ready` deltaP `30.3458` edge `0.0188` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2769` n `31` status `ready` deltaP `11.3579` edge `0.2519` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6373` n `31` status `ready` deltaP `30.7803` edge `0.0326` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
