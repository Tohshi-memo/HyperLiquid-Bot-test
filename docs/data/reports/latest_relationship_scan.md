# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T04:22:32.529625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8757`

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

- `market_context_high->equity_24h` score `2.3045` n `78` status `ready` deltaP `3.0323` edge `1.0907` maxDD `-55.843`
- `risk_on_high->equity_24h` score `1.6946` n `45` status `ready` deltaP `-15.942` edge `0.8263` maxDD `-33.9708`
- `risk_on_and_context->equity_24h` score `1.6946` n `45` status `ready` deltaP `-15.942` edge `0.8263` maxDD `-33.9708`
- `market_context_high->crypto_major_24h` score `1.3701` n `78` status `ready` deltaP `4.6875` edge `0.7541` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.2356` n `78` status `ready` deltaP `13.8171` edge `0.096` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7416` n `45` status `ready` deltaP `14.7148` edge `0.0236` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.7416` n `45` status `ready` deltaP `14.7148` edge `0.0236` maxDD `-2.1255`
- `market_context_high->crypto_major_4h` score `0.5994` n `78` status `ready` deltaP `5.82` edge `0.3785` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5249` n `45` status `ready` deltaP `11.1112` edge `0.0006` maxDD `-0.4746`
- `risk_on_and_context->index_1h` score `0.5249` n `45` status `ready` deltaP `11.1112` edge `0.0006` maxDD `-0.4746`
- `market_context_high->crypto_major_1h` score `0.3705` n `79` status `ready` deltaP `4.798` edge `0.1044` maxDD `-3.7781`
- `risk_on_high->equity_4h` score `-0.0925` n `45` status `ready` deltaP `5.9123` edge `0.1021` maxDD `-5.9378`
- `risk_on_and_context->equity_4h` score `-0.0925` n `45` status `ready` deltaP `5.9123` edge `0.1021` maxDD `-5.9378`
- `risk_on_high->fx_1h` score `-0.1267` n `45` status `ready` deltaP `2.7327` edge `0.0002` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.1267` n `45` status `ready` deltaP `2.7327` edge `0.0002` maxDD `-0.1065`
- `risk_on_high->fx_4h` score `-0.1709` n `45` status `ready` deltaP `1.0296` edge `0.0053` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1709` n `45` status `ready` deltaP `1.0296` edge `0.0053` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.4284` n `45` status `ready` deltaP `9.971` edge `-0.0224` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.4284` n `45` status `ready` deltaP `9.971` edge `-0.0224` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.4512` n `45` status `ready` deltaP `6.2997` edge `0.0089` maxDD `-1.08`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
