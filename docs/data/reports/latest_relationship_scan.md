# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T01:37:26.443141+00:00`
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

- `news_risk_high->unknown_1h` score `3309.6337` n `31` status `ready` deltaP `1.6322` edge `275.8095` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3174.0283` n `31` status `ready` deltaP `3.4815` edge `264.4848` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.6594` n `31` status `ready` deltaP `27.9029` edge `1.2856` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.2876` n `31` status `ready` deltaP `26.1698` edge `0.8495` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.4497` n `31` status `ready` deltaP `23.9168` edge `0.7947` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.4239` n `31` status `ready` deltaP `19.1384` edge `0.5781` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1853` n `31` status `ready` deltaP `28.8405` edge `0.2879` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7066` n `31` status `ready` deltaP `38.6762` edge `0.1472` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.6857` n `31` status `ready` deltaP `14.0342` edge `0.6489` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.368` n `31` status `ready` deltaP `12.1877` edge `0.2269` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2471` n `31` status `ready` deltaP `27.9259` edge `0.0271` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2385` n `31` status `ready` deltaP `27.5015` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2203` n `31` status `ready` deltaP `14.8976` edge `0.1044` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1644` n `31` status `ready` deltaP `24.6101` edge `0.0163` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.8305` n `31` status `ready` deltaP `5.0705` edge `0.247` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6439` n `31` status `ready` deltaP `8.0645` edge `0.1927` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1247` n `31` status `ready` deltaP `24.4929` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3484` n `31` status `ready` deltaP `8.8267` edge `0.0256` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2521` n `31` status `ready` deltaP `10.2232` edge `0.0199` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3567` n `31` status `ready` deltaP `-2.3614` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
