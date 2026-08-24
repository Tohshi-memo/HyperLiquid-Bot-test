# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T18:02:08.659438+00:00`
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

- `news_risk_high->unknown_24h` score `45.9889` n `51` status `ready` deltaP `13.0208` edge `3.7456` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1623` n `51` status `ready` deltaP `40.237` edge `0.9217` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8631` n `51` status `ready` deltaP `24.2587` edge `0.9148` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4244` n `51` status `ready` deltaP `48.9481` edge `0.1409` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.8431` n `90` status `ready` deltaP `7.4652` edge `0.3831` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.0096` n `51` status `ready` deltaP `27.5377` edge `0.2276` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.561` n `51` status `ready` deltaP `16.3349` edge `0.2183` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3406` n `51` status `ready` deltaP `39.3024` edge `0.0298` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6586` n `130` status `ready` deltaP `19.2964` edge `0.0504` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2829` n `51` status `ready` deltaP `17.4445` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0431` n `51` status `ready` deltaP `14.7686` edge `0.0282` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0208` n `51` status `ready` deltaP `18.7918` edge `0.042` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.6207` n `51` status `ready` deltaP `26.8586` edge `-0.1231` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.2914` n `51` status `ready` deltaP `9.2873` edge `-0.0068` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2325` n `51` status `ready` deltaP `8.9732` edge `0.0053` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1268` n `130` status `ready` deltaP `10.8678` edge `-0.016` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0181` n `130` status `ready` deltaP `10.9051` edge `-0.0263` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1131` n `51` status `ready` deltaP `2.1927` edge `-0.0068` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2993` n `51` status `ready` deltaP `5.996` edge `-0.0118` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4069` n `130` status `ready` deltaP `3.0101` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
