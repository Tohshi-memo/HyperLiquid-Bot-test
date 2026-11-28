# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T03:37:25.525503+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3248`

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

- `news_risk_high->unknown_1h` score `3312.7489` n `31` status `ready` deltaP `1.6322` edge `276.0691` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3178.4781` n `31` status `ready` deltaP `3.634` edge `264.8546` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.2269` n `31` status `ready` deltaP `29.1161` edge `1.3248` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.5717` n `31` status `ready` deltaP `27.0364` edge `0.8674` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.2853` n `31` status `ready` deltaP `23.9168` edge `0.781` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.0501` n `31` status `ready` deltaP `18.6811` edge `0.55` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.933` n `31` status `ready` deltaP `27.621` edge `0.275` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7258` n `31` status `ready` deltaP `38.6762` edge `0.1488` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.3496` n `31` status `ready` deltaP `13.1196` edge `0.6119` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3428` n `31` status `ready` deltaP `12.1877` edge `0.2248` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.169` n `31` status `ready` deltaP `26.753` edge `0.0109` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1632` n `31` status `ready` deltaP `24.6101` edge `0.0162` maxDD `0.0`
- `news_risk_high->index_4h` score `2.1631` n `31` status `ready` deltaP `27.0112` edge `0.0262` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.0368` n `31` status `ready` deltaP `13.9994` edge `0.0951` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6309` n `31` status `ready` deltaP `4.7711` edge `0.2234` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.4957` n `31` status `ready` deltaP `7.9148` edge `0.1747` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0585` n `31` status `ready` deltaP `23.445` edge `0.0073` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3523` n `31` status `ready` deltaP `8.8267` edge `0.0261` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2008` n `31` status `ready` deltaP `9.461` edge `0.0184` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3998` n `31` status `ready` deltaP `-2.8105` edge `0.0116` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
