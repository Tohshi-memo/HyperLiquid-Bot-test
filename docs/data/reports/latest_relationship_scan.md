# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T01:07:20.056749+00:00`
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

- `news_risk_high->unknown_1h` score `2.583` n `38` status `ready` deltaP `29.6802` edge `0.0292` maxDD `-0.2787`
- `news_risk_high->fx_1h` score `1.8942` n `38` status `ready` deltaP `25.0552` edge `0.0078` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.8093` n `135` status `ready` deltaP `6.4638` edge `0.1304` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `1.396` n `135` status `ready` deltaP `21.0106` edge `-0.0024` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `1.153` n `38` status `ready` deltaP `22.723` edge `0.0245` maxDD `-0.9204`
- `news_risk_high->crypto_major_1h` score `0.6144` n `38` status `ready` deltaP `12.9688` edge `0.0525` maxDD `-5.0209`
- `news_risk_high->commodity_1h` score `0.5016` n `38` status `ready` deltaP `15.5768` edge `-0.0087` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1308` n `135` status `ready` deltaP `8.7161` edge `0.0089` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.025` n `38` status `ready` deltaP `4.0656` edge `-0.008` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0548` n `135` status `ready` deltaP `6.2963` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1583` n `135` status `ready` deltaP `1.6634` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3618` n `135` status `ready` deltaP `4.185` edge `0.0327` maxDD `-5.2257`
- `news_risk_high->index_1h` score `-0.4021` n `38` status `ready` deltaP `-2.6316` edge `0.0013` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6273` n `135` status `ready` deltaP `-0.8272` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6663` n `135` status `ready` deltaP `1.1755` edge `0.0103` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8632` n `119` status `ready` deltaP `0.6419` edge `0.0072` maxDD `-2.105`
- `market_context_high->commodity_4h` score `-1.0626` n `135` status `ready` deltaP `-7.3803` edge `-0.002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0752` n `135` status `ready` deltaP `-7.6591` edge `-0.002` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.1595` n `135` status `ready` deltaP `8.5038` edge `-0.0065` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
