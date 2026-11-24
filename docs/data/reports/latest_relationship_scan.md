# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T03:07:28.249222+00:00`
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

- `market_context_high->unknown_1h` score `32373.4946` n `45` status `ready` deltaP `2.1656` edge `2697.7862` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.4144` n `45` status `ready` deltaP `3.0251` edge `1852.9449` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1163.9652` n `31` status `ready` deltaP `2.3807` edge `96.9988` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.0612` n `31` status `ready` deltaP `4.2437` edge `83.3158` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.7167` n `31` status `ready` deltaP `42.7083` edge `2.775` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.902` n `31` status `ready` deltaP `45.6597` edge `2.6041` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7788` n `31` status `ready` deltaP `45.6597` edge `2.2605` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8767` n `31` status `ready` deltaP `42.4508` edge `0.7342` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6978` n `31` status `ready` deltaP `24.0165` edge `0.8184` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6611` n `31` status `ready` deltaP `30.8222` edge `0.5645` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6315` n `31` status `ready` deltaP `56.4684` edge `0.189` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.614` n `31` status `ready` deltaP `14.1866` edge `0.8951` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.639` n `31` status `ready` deltaP `40.2778` edge `0.2014` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.32` n `31` status `ready` deltaP `18.3407` edge `0.1731` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.21` n `45` status `ready` deltaP `38.3198` edge `0.0405` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7886` n `31` status `ready` deltaP `30.9747` edge `0.0519` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5646` n `31` status `ready` deltaP `11.2082` edge `0.3002` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5009` n `31` status `ready` deltaP `29.8967` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1702` n `31` status `ready` deltaP `10.4597` edge `0.2442` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5999` n `31` status `ready` deltaP `30.6306` edge `0.0288` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
