# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T05:52:26.424420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3218.7013` n `31` status `ready` deltaP `1.6322` edge `268.2318` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3184.8994` n `31` status `ready` deltaP `3.7864` edge `265.3887` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.8074` n `31` status `ready` deltaP `32.1181` edge `1.6865` maxDD `0.0`
- `news_risk_high->equity_24h` score `20.4306` n `31` status `ready` deltaP `31.5972` edge `1.4919` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.3248` n `31` status `ready` deltaP `31.25` edge `1.2354` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.156` n `31` status `ready` deltaP `23.2543` edge `0.695` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.1896` n `31` status `ready` deltaP `32.8039` edge `0.4285` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.8786` n `31` status `ready` deltaP `16.1683` edge `0.7876` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.7077` n `31` status `ready` deltaP `19.5341` edge `0.3729` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.7105` n `31` status `ready` deltaP `39.2809` edge `0.1435` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.6272` n `31` status `ready` deltaP `33.1597` edge `0.0812` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7062` n `31` status `ready` deltaP `31.2795` edge `0.043` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6461` n `31` status `ready` deltaP `16.3946` edge `0.1299` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3715` n `31` status `ready` deltaP `28.6991` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0815` n `31` status `ready` deltaP `6.8669` edge `0.2672` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8684` n `31` status `ready` deltaP `9.8609` edge `0.2095` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1862` n `31` status `ready` deltaP `25.5408` edge `0.0097` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.456` n `31` status `ready` deltaP `12.5098` edge `0.0308` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0303` n `31` status `ready` deltaP `6.3877` edge `-0.0067` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6551` n `31` status `ready` deltaP `-4.9063` edge `0.0043` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
