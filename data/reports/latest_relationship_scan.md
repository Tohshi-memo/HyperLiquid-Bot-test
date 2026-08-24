# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T02:37:26.965771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `52.843` n `48` status `ready` deltaP `17.1875` edge `4.289` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.3429` n `48` status `ready` deltaP `45.1389` edge `1.1077` maxDD `-2.0707`
- `news_risk_high->unknown_4h` score `13.0445` n `51` status `ready` deltaP `23.4965` edge `0.935` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.4524` n `48` status `ready` deltaP `54.3403` edge `0.1845` maxDD `-0.0585`
- `risk_on_high->unknown_1h` score `3.9796` n `35` status `ready` deltaP `-12.4808` edge `0.6383` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.9796` n `35` status `ready` deltaP `-12.4808` edge `0.6383` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1433` n `51` status `ready` deltaP `37.0158` edge `0.0286` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.9721` n `51` status `ready` deltaP `24.184` edge `0.1635` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `2.9239` n `51` status `ready` deltaP `15.5864` edge `0.1702` maxDD `-0.7693`
- `news_risk_high->crypto_alt_24h` score `2.7914` n `48` status `ready` deltaP `27.2569` edge `0.0509` maxDD `0.0`
- `risk_on_high->equity_4h` score `2.6512` n `35` status `ready` deltaP `1.9991` edge `0.2506` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.6512` n `35` status `ready` deltaP `1.9991` edge `0.2506` maxDD `-0.773`
- `risk_on_high->metal_4h` score `2.2999` n `35` status `ready` deltaP `30.1873` edge `-0.0008` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2999` n `35` status `ready` deltaP `30.1873` edge `-0.0008` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1296` n `48` status `ready` deltaP `37.5` edge `-0.0683` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.8784` n `145` status `ready` deltaP `21.3194` edge `0.0281` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.6451` n `157` status `ready` deltaP `10.3036` edge `0.1133` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2805` n `51` status `ready` deltaP `17.4445` edge `0.0074` maxDD `-0.0257`
- `risk_on_high->index_4h` score `0.9489` n `35` status `ready` deltaP `12.7439` edge `0.0421` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.9489` n `35` status `ready` deltaP `12.7439` edge `0.0421` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
