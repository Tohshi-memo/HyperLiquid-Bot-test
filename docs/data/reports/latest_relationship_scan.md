# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T00:52:27.899426+00:00`
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

- `news_risk_high->unknown_24h` score `44.6815` n `51` status `ready` deltaP `8.3333` edge `3.6679` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0874` n `51` status `ready` deltaP `25.1733` edge `0.9274` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.1423` n `51` status `ready` deltaP `40.237` edge `0.8367` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2204` n `51` status `ready` deltaP `48.9481` edge `0.1239` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.736` n `51` status `ready` deltaP `27.5377` edge `0.2048` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5705` n `51` status `ready` deltaP `16.784` edge `0.2161` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3298` n `51` status `ready` deltaP `39.3024` edge `0.0289` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.883` n `130` status `ready` deltaP `20.211` edge `0.063` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2434` n `51` status `ready` deltaP `16.9954` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0317` n `51` status `ready` deltaP `19.0912` edge `0.0414` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9415` n `51` status `ready` deltaP `14.1589` edge `0.0238` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.289` n `51` status `ready` deltaP `9.1376` edge `-0.006` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2092` n `51` status `ready` deltaP `8.5241` edge `0.0053` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0386` n `130` status `ready` deltaP `10.4105` edge `-0.0203` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0276` n `130` status `ready` deltaP `11.3542` edge `-0.0285` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1847` n `51` status `ready` deltaP `0.9951` edge `-0.008` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.2636` n `51` status `ready` deltaP `22.3448` edge `-0.1667` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.3875` n `51` status `ready` deltaP `5.5387` edge `-0.0161` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4326` n `130` status `ready` deltaP `2.561` edge `0.0007` maxDD `-0.8587`
- `market_context_high->metal_1h` score `-0.4984` n `130` status `ready` deltaP `-2.7153` edge `-0.0081` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
