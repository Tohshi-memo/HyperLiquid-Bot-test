# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T17:22:27.411308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.2597` n `51` status `ready` deltaP `13.5417` edge `3.7647` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2799` n `51` status `ready` deltaP `40.237` edge `0.9315` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8595` n `51` status `ready` deltaP `24.2587` edge `0.9145` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4472` n `51` status `ready` deltaP `48.9481` edge `0.1428` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.9079` n `87` status `ready` deltaP `7.7946` edge `0.3863` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.1014` n `51` status `ready` deltaP `27.995` edge `0.2322` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5742` n `51` status `ready` deltaP `16.4846` edge `0.2184` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3394` n `51` status `ready` deltaP `39.3024` edge `0.0297` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.655` n `130` status `ready` deltaP `19.2964` edge `0.0501` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2949` n `51` status `ready` deltaP `17.5942` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0735` n `51` status `ready` deltaP `15.0735` edge `0.0287` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0044` n `51` status `ready` deltaP `18.6421` edge `0.0409` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.708` n `51` status `ready` deltaP `27.3795` edge `-0.1193` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2746` n `51` status `ready` deltaP `9.1376` edge `-0.0072` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `8.9732` edge `0.0052` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1196` n `130` status `ready` deltaP `10.8678` edge `-0.0166` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0312` n `130` status `ready` deltaP `11.0548` edge `-0.0262` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1146` n `51` status `ready` deltaP `2.1927` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3065` n `51` status `ready` deltaP `5.996` edge `-0.0124` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3991` n `130` status `ready` deltaP `3.1598` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
