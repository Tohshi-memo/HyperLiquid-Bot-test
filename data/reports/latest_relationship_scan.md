# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T03:52:21.604811+00:00`
- Price records: `672`
- Market context records: `1806`
- Flow alert records: `7096`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->crypto_alt_4h` score `6.9823` n `186` status `ready` deltaP `22.6691` edge `0.5452` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8868` n `181` status `ready` deltaP `27.8698` edge `0.6307` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5149` n `30` status `ready` deltaP `29.563` edge `0.4113` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.1747` n `186` status `ready` deltaP `26.385` edge `0.4897` maxDD `-6.0833`
- `market_context_high->unknown_4h` score `4.3535` n `186` status `ready` deltaP `16.924` edge `0.4656` maxDD `-10.2508`
- `market_context_high->index_24h` score `3.3996` n `181` status `ready` deltaP `16.4902` edge `0.2962` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2878` n `30` status `ready` deltaP `24.8703` edge `0.1399` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9694` n `186` status `ready` deltaP `16.0504` edge `0.2499` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.6349` n `181` status `ready` deltaP `18.2272` edge `0.5879` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.9036` n `181` status `ready` deltaP `12.3715` edge `0.6082` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9073` n `30` status `ready` deltaP `21.6362` edge `-0.0007` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.835` n `186` status `ready` deltaP `11.8772` edge `0.0993` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4278` n `188` status `ready` deltaP `6.2651` edge `0.0925` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3712` n `30` status `ready` deltaP `9.8272` edge `0.0544` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3438` n `188` status `ready` deltaP `6.9627` edge `0.0936` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1627` n `188` status `ready` deltaP `3.768` edge `0.0407` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.4222` n `181` status `ready` deltaP `17.8954` edge `0.7041` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4466` n `181` status `ready` deltaP `9.0729` edge `0.0072` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4546` n `30` status `ready` deltaP `-4.8303` edge `0.0001` maxDD `-0.0948`
- `market_context_high->index_1h` score `-0.4662` n `188` status `ready` deltaP `1.6085` edge `0.0136` maxDD `-1.7205`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
