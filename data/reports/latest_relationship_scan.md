# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T07:07:26.245595+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `news_risk_high->unknown_4h` score `15.0097` n `50` status `ready` deltaP `26.5061` edge `1.0787` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.046` n `33` status `ready` deltaP `-7.5802` edge `0.7423` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.046` n `33` status `ready` deltaP `-7.5802` edge `0.7423` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.8007` n `51` status `ready` deltaP `20.2272` edge `0.2123` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `3.2193` n `50` status `ready` deltaP `26.628` edge `0.1615` maxDD `-1.9929`
- `news_risk_high->fx_4h` score `2.8109` n `50` status `ready` deltaP `33.7317` edge `0.0228` maxDD `-0.0746`
- `news_risk_high->fx_1h` score `1.2218` n `51` status `ready` deltaP `16.8457` edge `0.0065` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1273` n `135` status `ready` deltaP `6.7632` edge `0.0937` maxDD `-1.5876`
- `news_risk_high->equity_1h` score `0.8664` n `51` status `ready` deltaP `18.6421` edge `0.0233` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.8118` n `50` status `ready` deltaP `12.8963` edge `0.021` maxDD `-0.1462`
- `market_context_high->unknown_4h` score `0.7387` n `124` status `ready` deltaP `22.0545` edge `-0.0683` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.3` n `108` status `ready` deltaP `0.1158` edge `0.1` maxDD `-2.0619`
- `news_risk_high->index_1h` score `0.2558` n `51` status `ready` deltaP `9.7217` edge `0.0033` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2464` n `33` status `ready` deltaP `6.8636` edge `0.0035` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2464` n `33` status `ready` deltaP `6.8636` edge `0.0035` maxDD `-0.0796`
- `news_risk_high->metal_4h` score `0.1937` n `50` status `ready` deltaP `11.1402` edge `-0.0094` maxDD `-0.2316`
- `news_risk_high->commodity_1h` score `0.1356` n `51` status `ready` deltaP `7.94` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1314` n `124` status `ready` deltaP `7.8285` edge `0.009` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.0843` n `51` status `ready` deltaP `2.7915` edge `-0.0071` maxDD `-0.1184`
- `risk_on_high->index_1h` score `-0.1145` n `33` status `ready` deltaP `-0.617` edge `0.0076` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
