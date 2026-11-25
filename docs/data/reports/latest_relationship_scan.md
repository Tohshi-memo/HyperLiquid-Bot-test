# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T02:22:29.503583+00:00`
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

- `market_context_high->unknown_1h` score `32251.3513` n `45` status `ready` deltaP `2.0159` edge `2687.6086` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21990.6421` n `45` status `ready` deltaP `3.1776` edge `1832.5462` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.3964` n `31` status `ready` deltaP `2.231` edge `84.7024` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `737.6946` n `31` status `ready` deltaP `4.3962` edge `61.4509` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.9207` n `31` status `ready` deltaP `50.1736` edge `2.9089` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.521` n `31` status `ready` deltaP `44.0972` edge `2.9161` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.0423` n `31` status `ready` deltaP `48.9583` edge `2.5938` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8203` n `31` status `ready` deltaP `27.2177` edge `0.8906` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1866` n `31` status `ready` deltaP `41.2355` edge `0.6848` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.306` n `31` status `ready` deltaP `34.6332` edge `0.676` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3282` n `31` status `ready` deltaP `17.5403` edge `0.9643` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7651` n `31` status `ready` deltaP `42.7083` edge `0.1957` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.5329` n `31` status `ready` deltaP `46.9198` edge `0.1611` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6476` n `31` status `ready` deltaP `18.9395` edge `0.1964` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0941` n `31` status `ready` deltaP `33.4137` edge `0.0611` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7525` n `31` status `ready` deltaP `12.5555` edge `0.3153` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6114` n `45` status `ready` deltaP `31.9173` edge `0.0333` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5872` n `31` status `ready` deltaP `30.6452` edge `0.0198` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4008` n `31` status `ready` deltaP `12.5555` edge `0.2598` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5765` n `31` status `ready` deltaP `30.0318` edge `0.0298` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
