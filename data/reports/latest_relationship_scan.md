# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T11:22:30.691462+00:00`
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

- `market_context_high->unknown_1h` score `32333.2563` n `45` status `ready` deltaP `1.5668` edge `2694.437` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22172.0778` n `45` status `ready` deltaP `2.5678` edge `1847.6699` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1123.7269` n `31` status `ready` deltaP `1.7819` edge `93.6496` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `936.7247` n `31` status `ready` deltaP `3.7864` edge `78.0408` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.962` n `31` status `ready` deltaP `48.7847` edge `2.6716` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.8254` n `31` status `ready` deltaP `41.4931` edge `2.6255` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1134` n `31` status `ready` deltaP `46.5278` edge `2.2826` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.3109` n `31` status `ready` deltaP `41.4091` edge `0.694` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9824` n `31` status `ready` deltaP `24.1689` edge `0.8411` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3941` n `31` status `ready` deltaP `32.499` edge `0.6144` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.8982` n `31` status `ready` deltaP `15.4062` edge `0.9234` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.7047` n `31` status `ready` deltaP `56.4684` edge `0.1951` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.2142` n `31` status `ready` deltaP `39.0625` edge `0.1741` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5527` n `31` status `ready` deltaP `18.9395` edge `0.1885` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9569` n `45` status `ready` deltaP `35.5759` edge `0.0377` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8976` n `31` status `ready` deltaP `31.7369` edge `0.0559` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6153` n `31` status `ready` deltaP `11.5076` edge `0.3047` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5968` n `31` status `ready` deltaP `30.7949` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2676` n `31` status `ready` deltaP `11.3579` edge `0.2507` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6676` n `31` status `ready` deltaP `31.5288` edge `0.0315` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
