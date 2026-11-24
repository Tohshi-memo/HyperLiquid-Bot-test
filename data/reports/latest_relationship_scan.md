# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T03:37:26.863628+00:00`
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

- `market_context_high->unknown_1h` score `32365.7978` n `45` status `ready` deltaP `2.1656` edge `2697.1448` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22222.9894` n `45` status `ready` deltaP `2.8727` edge `1851.9105` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1156.2684` n `31` status `ready` deltaP `2.3807` edge `96.3574` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `987.6363` n `31` status `ready` deltaP `4.0913` edge `82.2814` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.4657` n `31` status `ready` deltaP `42.3611` edge `2.7564` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9754` n `31` status `ready` deltaP `46.0069` edge `2.6079` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7848` n `31` status `ready` deltaP `45.6597` edge `2.261` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8129` n `31` status `ready` deltaP `42.1035` edge `0.7312` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.728` n `31` status `ready` deltaP `24.1689` edge `0.8199` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6467` n `31` status `ready` deltaP `30.8222` edge `0.5633` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.6454` n `31` status `ready` deltaP `14.3391` edge `0.8981` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.6375` n `31` status `ready` deltaP `56.4684` edge `0.1895` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5812` n `31` status `ready` deltaP `39.9306` edge `0.1989` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3164` n `31` status `ready` deltaP `18.3407` edge `0.1728` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1832` n `45` status `ready` deltaP `38.0149` edge `0.0403` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7582` n `31` status `ready` deltaP `30.6698` edge `0.0514` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5904` n `31` status `ready` deltaP `11.3579` edge `0.3025` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4997` n `31` status `ready` deltaP `29.8967` edge `0.0175` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1935` n `31` status `ready` deltaP `10.6094` edge `0.2462` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6038` n `31` status `ready` deltaP `30.6306` edge `0.0293` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
