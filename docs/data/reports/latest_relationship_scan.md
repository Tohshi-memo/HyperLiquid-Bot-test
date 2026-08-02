# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T04:22:32.289462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.8226` n `60` status `ready` deltaP `33.7146` edge `432.2192` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.9606` n `53` status `ready` deltaP `61.257` edge `1.2114` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.6337` n `68` status `ready` deltaP `16.831` edge `0.3503` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7852` n `53` status `ready` deltaP `27.4844` edge `0.2315` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.6752` n `68` status `ready` deltaP `16.3737` edge `0.0685` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.6994` n `53` status `ready` deltaP `9.805` edge `0.12` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6911` n `68` status `ready` deltaP `10.391` edge `0.0706` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.3252` n `53` status `ready` deltaP `15.5402` edge `0.0177` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.2443` n `53` status `ready` deltaP `11.9126` edge `0.0499` maxDD `-2.506`
- `news_risk_high->fx_4h` score `0.1224` n `68` status `ready` deltaP `12.2938` edge `0.024` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1086` n `68` status `ready` deltaP `5.165` edge `0.0271` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0842` n `68` status `ready` deltaP `6.4812` edge `0.0358` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0642` n `53` status `ready` deltaP `8.1008` edge `0.0016` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `0.0081` n `53` status `ready` deltaP `4.7763` edge `0.0233` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.0599` n `68` status `ready` deltaP `2.9676` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.07` n `68` status `ready` deltaP `2.4657` edge `0.0069` maxDD `-0.5845`
- `market_context_high->commodity_4h` score `-0.1106` n `53` status `ready` deltaP `3.7247` edge `0.0485` maxDD `-3.0005`
- `news_risk_high->metal_1h` score `-0.1435` n `68` status `ready` deltaP `2.4657` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2693` n `68` status `ready` deltaP `1.6203` edge `0.0267` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6249` n `68` status `ready` deltaP `3.4167` edge `-0.0249` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
