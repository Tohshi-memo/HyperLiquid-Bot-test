# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T00:07:44.184983+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32259.845` n `45` status `ready` deltaP `1.7165` edge `2688.3184` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22005.2341` n `45` status `ready` deltaP `3.1776` edge `1833.7622` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1024.89` n `31` status `ready` deltaP `1.9316` edge `85.4122` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `752.2866` n `31` status `ready` deltaP `4.3962` edge `62.6669` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6459` n `31` status `ready` deltaP `50.1736` edge `2.886` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.7343` n `31` status `ready` deltaP `43.9236` edge `2.8517` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.5071` n `31` status `ready` deltaP `48.9583` edge `2.5492` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7767` n `31` status `ready` deltaP `26.9128` edge `0.889` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0846` n `31` status `ready` deltaP `41.2355` edge `0.6763` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2226` n `31` status `ready` deltaP `34.1759` edge `0.6721` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2397` n `31` status `ready` deltaP `17.083` edge `0.956` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.7143` n `31` status `ready` deltaP `48.4823` edge `0.1658` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.6056` n `31` status `ready` deltaP `41.8403` edge `0.1882` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.7196` n `31` status `ready` deltaP `19.0892` edge `0.2014` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0321` n `31` status `ready` deltaP `32.8039` edge `0.06` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.726` n `31` status `ready` deltaP `12.4058` edge `0.3129` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.7039` n `45` status `ready` deltaP `32.9844` edge `0.0339` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5932` n `31` status `ready` deltaP `30.6452` edge `0.0203` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3985` n `31` status `ready` deltaP `12.4058` edge `0.2605` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6194` n `31` status `ready` deltaP `30.4809` edge `0.0323` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
