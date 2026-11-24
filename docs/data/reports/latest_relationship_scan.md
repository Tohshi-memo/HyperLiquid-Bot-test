# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T15:22:31.416949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `market_context_high->unknown_1h` score `32279.5827` n `45` status `ready` deltaP `1.5668` edge `2689.9642` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22111.4922` n `45` status `ready` deltaP `2.5678` edge `1842.6211` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1070.0533` n `31` status `ready` deltaP `1.7819` edge `89.1768` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `876.1391` n `31` status `ready` deltaP `3.7864` edge `72.992` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.8688` n `31` status `ready` deltaP `49.3056` edge `2.7437` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.8045` n `31` status `ready` deltaP `40.4514` edge `2.6307` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.028` n `31` status `ready` deltaP `46.875` edge `2.3565` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0894` n `31` status `ready` deltaP `41.2355` edge `0.6767` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.926` n `31` status `ready` deltaP `24.1689` edge `0.8364` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1611` n `31` status `ready` deltaP `32.3466` edge `0.596` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.717` n `31` status `ready` deltaP `15.1013` edge `0.9022` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.4992` n `31` status `ready` deltaP `54.5587` edge `0.1907` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.11` n `31` status `ready` deltaP `38.1944` edge `0.1712` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3728` n `31` status `ready` deltaP `18.4904` edge `0.1765` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9425` n `45` status `ready` deltaP `35.5759` edge `0.0365` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8794` n `31` status `ready` deltaP `31.5844` edge `0.0554` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5771` n `31` status `ready` deltaP `11.5076` edge `0.2998` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5189` n `31` status `ready` deltaP `30.0464` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2442` n `31` status `ready` deltaP `11.2082` edge `0.2487` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6217` n `31` status `ready` deltaP `30.7803` edge `0.0306` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
