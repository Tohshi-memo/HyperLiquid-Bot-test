# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T11:37:25.640276+00:00`
- Price records: `672`
- Market context records: `7560`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `-0.1058` n `177` status `ready` deltaP `6.974` edge `0.0207` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1245` n `177` status `ready` deltaP `5.4309` edge `0.0074` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2861` n `177` status `ready` deltaP `3.7792` edge `0.0009` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.3245` n `177` status `ready` deltaP `3.5564` edge `0.0116` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.3308` n `177` status `ready` deltaP `12.6843` edge `0.1089` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.4543` n `177` status `ready` deltaP `2.8146` edge `0.0006` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.6092` n `154` status `ready` deltaP `11.4983` edge `0.0166` maxDD `-3.8554`
- `market_context_high->commodity_24h` score `-0.6211` n `154` status `ready` deltaP `10.1837` edge `0.0387` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `-0.9136` n `177` status `ready` deltaP `0.9972` edge `0.0211` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9527` n `177` status `ready` deltaP `5.3334` edge `0.0261` maxDD `-7.6171`
- `market_context_high->index_4h` score `-0.9974` n `177` status `ready` deltaP `8.8374` edge `0.0196` maxDD `-6.1776`
- `market_context_high->metal_1h` score `-1.0097` n `177` status `ready` deltaP `1.7313` edge `0.0147` maxDD `-1.4971`
- `market_context_high->fx_4h` score `-1.2036` n `177` status `ready` deltaP `1.3139` edge `0.0054` maxDD `-2.1439`
- `market_context_high->metal_4h` score `-1.4283` n `177` status `ready` deltaP `2.2013` edge `0.0504` maxDD `-4.8549`
- `market_context_high->equity_1h` score `-1.4794` n `177` status `ready` deltaP `3.8861` edge `0.0255` maxDD `-14.6193`
- `market_context_high->crypto_alt_4h` score `-1.6751` n `177` status `ready` deltaP `1.8069` edge `0.0475` maxDD `-15.2776`
- `market_context_high->unknown_24h` score `-1.796` n `155` status `ready` deltaP `3.3065` edge `0.0226` maxDD `-9.9917`
- `market_context_high->crypto_major_4h` score `-2.2459` n `177` status `ready` deltaP `5.5645` edge `0.0644` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-4.3762` n `177` status `ready` deltaP `0.9744` edge `0.1186` maxDD `-41.8913`
- `market_context_high->metal_24h` score `-4.6724` n `155` status `ready` deltaP `-9.7491` edge `0.0304` maxDD `-18.4879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
