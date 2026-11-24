# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T11:37:24.814455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4308`

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

- `market_context_high->unknown_1h` score `32330.4087` n `45` status `ready` deltaP `1.5668` edge `2694.1997` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22169.097` n `45` status `ready` deltaP `2.5678` edge `1847.4215` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1120.8793` n `31` status `ready` deltaP `1.7819` edge `93.4123` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `933.7439` n `31` status `ready` deltaP `3.7864` edge `77.7924` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.0167` n `31` status `ready` deltaP `48.9583` edge `2.675` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.8134` n `31` status `ready` deltaP `41.4931` edge `2.6245` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1645` n `31` status `ready` deltaP `46.7014` edge `2.2857` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.2953` n `31` status `ready` deltaP `41.4091` edge `0.6927` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.01` n `31` status `ready` deltaP `24.1689` edge `0.8434` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.4037` n `31` status `ready` deltaP `32.499` edge `0.6152` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.9091` n `31` status `ready` deltaP `15.4062` edge `0.9248` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.7047` n `31` status `ready` deltaP `56.4684` edge `0.1951` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2106` n `31` status `ready` deltaP `39.0625` edge `0.1738` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5815` n `31` status `ready` deltaP `19.0892` edge `0.1899` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9557` n `45` status `ready` deltaP `35.5759` edge `0.0376` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9` n `31` status `ready` deltaP `31.7369` edge `0.0561` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.627` n `31` status `ready` deltaP `11.6573` edge `0.3052` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6099` n `31` status `ready` deltaP `30.9446` edge `0.0197` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2831` n `31` status `ready` deltaP `11.5076` edge `0.2517` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6591` n `31` status `ready` deltaP `31.3791` edge `0.0314` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
