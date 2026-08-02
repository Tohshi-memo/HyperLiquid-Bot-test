# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T04:52:28.790454+00:00`
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

- `news_risk_high->unknown_24h` score `5188.8075` n `60` status `ready` deltaP `33.5413` edge `432.2191` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `19.0158` n `53` status `ready` deltaP `61.257` edge `1.216` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.5805` n `68` status `ready` deltaP `16.5261` edge `0.3479` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.8024` n `53` status `ready` deltaP `27.4844` edge `0.2337` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.6448` n `68` status `ready` deltaP `16.0688` edge `0.068` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.6861` n `53` status `ready` deltaP `9.805` edge `0.1183` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6635` n `68` status `ready` deltaP `10.0916` edge `0.0703` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.326` n `53` status `ready` deltaP `15.5402` edge `0.0178` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.267` n `53` status `ready` deltaP `12.2592` edge `0.0505` maxDD `-2.506`
- `news_risk_high->fx_4h` score `0.1236` n `68` status `ready` deltaP `12.2938` edge `0.0241` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1047` n `68` status `ready` deltaP `5.165` edge `0.0266` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0835` n `68` status `ready` deltaP `6.4812` edge `0.0357` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0654` n `53` status `ready` deltaP `8.1008` edge `0.0017` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.009` n `53` status `ready` deltaP `4.4769` edge `0.0231` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.0591` n `68` status `ready` deltaP `2.9676` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0692` n `68` status `ready` deltaP `2.4657` edge `0.007` maxDD `-0.5845`
- `market_context_high->commodity_4h` score `-0.0872` n `53` status `ready` deltaP `3.7247` edge `0.0515` maxDD `-3.0005`
- `news_risk_high->metal_1h` score `-0.1435` n `68` status `ready` deltaP `2.4657` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2669` n `68` status `ready` deltaP `1.6203` edge `0.027` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.6277` n `53` status `ready` deltaP `-4.1182` edge `0.0097` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
