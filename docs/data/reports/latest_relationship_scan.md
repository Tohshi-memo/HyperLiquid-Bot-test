# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T00:52:25.471849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `2.4951` n `37` status `ready` deltaP `29.4668` edge `0.0233` maxDD `-0.2787`
- `news_risk_high->fx_1h` score `1.8498` n `37` status `ready` deltaP `24.4862` edge `0.0079` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.8177` n `135` status `ready` deltaP `6.4638` edge `0.1311` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `1.4092` n `135` status `ready` deltaP `21.0106` edge `-0.0013` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `1.1017` n `37` status `ready` deltaP `22.0829` edge `0.0222` maxDD `-0.9204`
- `news_risk_high->commodity_1h` score `0.4557` n `37` status `ready` deltaP `14.7233` edge `-0.0089` maxDD `-0.4666`
- `news_risk_high->crypto_major_1h` score `0.3658` n `37` status `ready` deltaP `12.3362` edge `0.036` maxDD `-5.0209`
- `market_context_high->fx_4h` score `0.1315` n `135` status `ready` deltaP `8.7161` edge `0.009` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.054` n `135` status `ready` deltaP `6.2963` edge `0.0042` maxDD `-0.9144`
- `news_risk_high->metal_1h` score `-0.0848` n `37` status `ready` deltaP `3.0062` edge `-0.0086` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1583` n `135` status `ready` deltaP `1.6634` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.361` n `135` status `ready` deltaP `4.185` edge `0.0328` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `news_risk_high->index_1h` score `-0.4784` n `37` status `ready` deltaP `-4.0541` edge `0.001` maxDD `-0.1583`
- `market_context_high->metal_1h` score `-0.6153` n `135` status `ready` deltaP `-0.6775` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6663` n `135` status `ready` deltaP `1.1755` edge `0.0103` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8518` n `119` status `ready` deltaP `0.8156` edge `0.0075` maxDD `-2.105`
- `market_context_high->commodity_4h` score `-1.0634` n `135` status `ready` deltaP `-7.3803` edge `-0.0021` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.076` n `135` status `ready` deltaP `-7.6591` edge `-0.0021` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.1389` n `135` status `ready` deltaP `8.6563` edge `-0.0058` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
