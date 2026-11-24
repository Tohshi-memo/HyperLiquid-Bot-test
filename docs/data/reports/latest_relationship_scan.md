# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T22:37:27.832562+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32270.0546` n `45` status `ready` deltaP `1.4171` edge `2689.1712` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22008.0481` n `45` status `ready` deltaP `3.1776` edge `1833.9967` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1035.0997` n `31` status `ready` deltaP `1.6322` edge `86.265` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `755.1006` n `31` status `ready` deltaP `4.3962` edge `62.9014` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6759` n `31` status `ready` deltaP `50.1736` edge `2.8885` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.4751` n `31` status `ready` deltaP `43.9236` edge `2.8301` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.3787` n `31` status `ready` deltaP `48.9583` edge `2.5385` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8621` n `31` status `ready` deltaP `27.0653` edge `0.8951` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0894` n `31` status `ready` deltaP `41.2355` edge `0.6767` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4234` n `31` status `ready` deltaP `34.4808` edge `0.6868` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3551` n `31` status `ready` deltaP `17.9976` edge `0.9647` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.8456` n `31` status `ready` deltaP `49.524` edge `0.1698` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5912` n `31` status `ready` deltaP `41.8403` edge `0.187` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.698` n `31` status `ready` deltaP `19.0892` edge `0.1996` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0647` n `31` status `ready` deltaP `32.9564` edge `0.0617` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7343` n `45` status `ready` deltaP `33.2893` edge `0.0344` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.7314` n `31` status `ready` deltaP `12.5555` edge `0.3126` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5932` n `31` status `ready` deltaP `30.6452` edge `0.0203` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4164` n `31` status `ready` deltaP `12.5555` edge `0.2618` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6443` n `31` status `ready` deltaP `30.7803` edge `0.0335` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
