# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T13:07:25.815689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11392`

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

- `news_risk_high->unknown_24h` score `50.2046` n `56` status `ready` deltaP `15.501` edge `4.1349` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.6867` n `56` status `ready` deltaP `37.1032` edge `2.0305` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `9.0127` n `108` status `ready` deltaP `18.8079` edge `0.6989` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3643` n `80` status `ready` deltaP `11.5854` edge `0.5121` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.2333` n `108` status `ready` deltaP `31.8287` edge `0.2425` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.8448` n `56` status `ready` deltaP `24.4792` edge `0.3907` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.6799` n `80` status `ready` deltaP `5.8234` edge `0.2202` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.4939` n `113` status `ready` deltaP `17.1164` edge `0.1369` maxDD `-0.788`
- `news_risk_high->crypto_major_24h` score `2.4921` n `56` status `ready` deltaP `20.8333` edge `0.4205` maxDD `-16.524`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `1.8244` n `56` status `ready` deltaP `37.8472` edge `0.053` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.4977` n `56` status `ready` deltaP `20.7589` edge `0.0284` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0532` n `125` status `ready` deltaP `8.7234` edge `0.0788` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4096` n `80` status `ready` deltaP `11.9012` edge `0.0052` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3123` n `113` status `ready` deltaP `6.5225` edge `0.0082` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5119` n `80` status `ready` deltaP `2.2256` edge `-0.0163` maxDD `-1.7996`
- `market_context_high->commodity_1h` score `-0.548` n `125` status `ready` deltaP `-0.9988` edge `0.0074` maxDD `-1.6796`
- `market_context_high->crypto_major_4h` score `-0.5823` n `113` status `ready` deltaP `15.4571` edge `0.1935` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
