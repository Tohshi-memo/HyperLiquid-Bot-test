# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T02:37:31.735898+00:00`
- Price records: `672`
- Market context records: `8154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `22.144` n `76` status `ready` deltaP `44.3348` edge `1.6408` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1031` n `77` status `ready` deltaP `37.4089` edge `0.616` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7626` n `76` status `ready` deltaP `39.0625` edge `0.4698` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.4195` n `43` status `ready` deltaP `32.2745` edge `0.507` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `5.1528` n `43` status `ready` deltaP `18.9663` edge `0.3635` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9679` n `77` status `ready` deltaP `35.8113` edge `0.0962` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.9429` n `77` status `ready` deltaP `20.9834` edge `0.209` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.8027` n `43` status `ready` deltaP `29.3796` edge `0.1519` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.7594` n `76` status `ready` deltaP `24.1959` edge `0.219` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.6747` n `43` status `ready` deltaP `22.4014` edge `0.0926` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.5598` n `77` status `ready` deltaP `24.0379` edge `0.1153` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.3947` n `77` status `ready` deltaP `10.4966` edge `0.2413` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.2158` n `77` status `ready` deltaP `12.5634` edge `0.2727` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.1088` n `76` status `ready` deltaP `28.4082` edge `0.0567` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.7741` n `77` status `ready` deltaP `20.8298` edge `0.0286` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.7148` n `76` status `ready` deltaP `32.3373` edge `0.2928` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `1.5657` n `77` status `ready` deltaP `14.7329` edge `0.0733` maxDD `-1.6171`
- `news_risk_high->metal_4h` score `1.4981` n `43` status `ready` deltaP `14.5845` edge `0.0744` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2875` n `43` status `ready` deltaP `5.8836` edge `0.1078` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.1877` n `77` status `ready` deltaP `15.287` edge `0.0349` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
