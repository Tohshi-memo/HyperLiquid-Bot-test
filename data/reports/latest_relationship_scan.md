# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T01:07:29.273570+00:00`
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

- `market_context_high->unknown_1h` score `32254.6646` n `45` status `ready` deltaP `1.7165` edge `2687.8867` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22003.1785` n `45` status `ready` deltaP `3.1776` edge `1833.5909` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1019.7096` n `31` status `ready` deltaP `1.9316` edge `84.9805` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `750.231` n `31` status `ready` deltaP `4.3962` edge `62.4956` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.7179` n `31` status `ready` deltaP `50.1736` edge `2.892` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.0403` n `31` status `ready` deltaP `43.9236` edge `2.8772` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.7111` n `31` status `ready` deltaP `48.9583` edge `2.5662` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7079` n `31` status `ready` deltaP `26.6079` edge `0.8853` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1314` n `31` status `ready` deltaP `41.2355` edge `0.6802` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1698` n `31` status `ready` deltaP `34.1759` edge `0.6677` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.1981` n `31` status `ready` deltaP `16.7781` edge `0.9527` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6531` n `31` status `ready` deltaP `42.0139` edge `0.191` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.6299` n `31` status `ready` deltaP `47.7879` edge `0.1634` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6824` n `31` status `ready` deltaP `19.0892` edge `0.1983` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0285` n `31` status `ready` deltaP `32.8039` edge `0.0597` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7135` n `31` status `ready` deltaP `12.4058` edge `0.3113` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6504` n `45` status `ready` deltaP `32.3746` edge `0.0335` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5872` n `31` status `ready` deltaP `30.6452` edge `0.0198` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3868` n `31` status `ready` deltaP `12.4058` edge `0.259` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6264` n `31` status `ready` deltaP `30.6306` edge `0.0322` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
