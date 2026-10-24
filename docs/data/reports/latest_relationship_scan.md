# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T19:07:30.561175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7582`

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

- `market_context_high->unknown_4h` score `14.2198` n `106` status `ready` deltaP `-2.1571` edge `1.2329` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.896` n `78` status `ready` deltaP `15.8654` edge `0.0598` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5543` n `34` status `ready` deltaP `16.8545` edge `0.001` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5543` n `34` status `ready` deltaP `16.8545` edge `0.001` maxDD `-0.7172`
- `risk_on_high->fx_1h` score `0.526` n `34` status `ready` deltaP `12.2666` edge `0.0032` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.526` n `34` status `ready` deltaP `12.2666` edge `0.0032` maxDD `-0.0698`
- `risk_on_high->index_1h` score `0.4409` n `34` status `ready` deltaP `12.2666` edge `0.0018` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4409` n `34` status `ready` deltaP `12.2666` edge `0.0018` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.3704` n `34` status `ready` deltaP `12.6226` edge `0.0267` maxDD `-1.4019`
- `risk_on_and_context->commodity_24h` score `0.3704` n `34` status `ready` deltaP `12.6226` edge `0.0267` maxDD `-1.4019`
- `market_context_high->commodity_4h` score `0.3538` n `106` status `ready` deltaP `9.5691` edge `0.0358` maxDD `-1.942`
- `risk_on_high->fx_4h` score `0.1214` n `34` status `ready` deltaP `5.3354` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.1214` n `34` status `ready` deltaP `5.3354` edge `0.0064` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1694` n `112` status `ready` deltaP `1.6574` edge `0.0027` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.348` n `112` status `ready` deltaP `2.5075` edge `0.0054` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.4492` n `106` status `ready` deltaP `-0.325` edge `0.0052` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.6258` n `34` status `ready` deltaP `2.5466` edge `-0.0127` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.6258` n `34` status `ready` deltaP `2.5466` edge `-0.0127` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.6393` n `34` status `ready` deltaP `-5.0282` edge `0.0062` maxDD `-0.0765`
- `risk_on_and_context->metal_1h` score `-0.6393` n `34` status `ready` deltaP `-5.0282` edge `0.0062` maxDD `-0.0765`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
