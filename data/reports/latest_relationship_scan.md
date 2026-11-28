# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T02:37:36.194398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3230`

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

- `news_risk_high->unknown_1h` score `3310.1389` n `31` status `ready` deltaP `1.6322` edge `275.8516` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3174.2131` n `31` status `ready` deltaP `3.4815` edge `264.5002` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.8882` n `31` status `ready` deltaP `28.4229` edge `1.3012` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.3861` n `31` status `ready` deltaP `26.5165` edge `0.8554` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3357` n `31` status `ready` deltaP `23.9168` edge `0.7852` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.1065` n `31` status `ready` deltaP `18.6811` edge `0.5547` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.0214` n `31` status `ready` deltaP `28.2308` edge `0.2783` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.715` n `31` status `ready` deltaP `38.6762` edge `0.1479` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.4146` n `31` status `ready` deltaP `13.4244` edge `0.6182` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3488` n `31` status `ready` deltaP `12.1877` edge `0.2253` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.1899` n `31` status `ready` deltaP `27.3161` edge `0.0264` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.1882` n `31` status `ready` deltaP `26.9027` edge `0.0115` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1632` n `31` status `ready` deltaP `24.6101` edge `0.0162` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1472` n `31` status `ready` deltaP `14.2988` edge `0.1023` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7666` n `31` status `ready` deltaP `4.7711` edge `0.2408` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6119` n `31` status `ready` deltaP `7.9148` edge `0.1896` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0912` n `31` status `ready` deltaP `23.8941` edge `0.0085` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3508` n `31` status `ready` deltaP `8.8267` edge `0.0259` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2111` n `31` status `ready` deltaP `9.6135` edge `0.0187` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3567` n `31` status `ready` deltaP `-2.3614` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
