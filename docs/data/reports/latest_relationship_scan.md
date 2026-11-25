# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T01:37:46.867928+00:00`
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

- `market_context_high->unknown_1h` score `32251.5542` n `45` status `ready` deltaP `1.8662` edge `2687.6265` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21996.5653` n `45` status `ready` deltaP `3.1776` edge `1833.0398` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.5992` n `31` status `ready` deltaP `2.0813` edge `84.7203` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `743.6178` n `31` status `ready` deltaP `4.3962` edge `61.9445` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.7947` n `31` status `ready` deltaP `50.1736` edge `2.8984` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.2119` n `31` status `ready` deltaP `43.9236` edge `2.8915` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.8371` n `31` status `ready` deltaP `48.9583` edge `2.5767` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7297` n `31` status `ready` deltaP `26.7604` edge `0.8861` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1566` n `31` status `ready` deltaP `41.2355` edge `0.6823` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.177` n `31` status `ready` deltaP `34.1759` edge `0.6683` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2373` n `31` status `ready` deltaP `17.083` edge `0.9557` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6874` n `31` status `ready` deltaP `42.1875` edge `0.1927` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.5913` n `31` status `ready` deltaP `47.4407` edge `0.1625` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6189` n `31` status `ready` deltaP `18.7898` edge `0.195` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0431` n `31` status `ready` deltaP `32.9564` edge `0.0599` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7174` n `31` status `ready` deltaP `12.4058` edge `0.3118` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.637` n `45` status `ready` deltaP `32.2222` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5584` n `31` status `ready` deltaP `30.3458` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3852` n `31` status `ready` deltaP `12.4058` edge `0.2588` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6124` n `31` status `ready` deltaP `30.4809` edge `0.0314` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
