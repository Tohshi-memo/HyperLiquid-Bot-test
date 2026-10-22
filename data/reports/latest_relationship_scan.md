# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T18:07:32.998349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6680`

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

- `risk_on_high->equity_1h` score `0.6078` n `37` status `ready` deltaP `15.8966` edge `0.0143` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6078` n `37` status `ready` deltaP `15.8966` edge `0.0143` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4792` n `37` status `ready` deltaP `14.7008` edge `0.0432` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4792` n `37` status `ready` deltaP `14.7008` edge `0.0432` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.284` n `76` status `ready` deltaP `13.136` edge `0.0564` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0884` n `37` status `ready` deltaP `5.2517` edge `0.0022` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0884` n `37` status `ready` deltaP `5.2517` edge `0.0022` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1935` n `37` status `ready` deltaP `-0.2843` edge `0.0035` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1935` n `37` status `ready` deltaP `-0.2843` edge `0.0035` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3226` n `91` status `ready` deltaP `2.5942` edge `-0.005` maxDD `-0.9588`
- `market_context_high->fx_1h` score `-0.3364` n `91` status `ready` deltaP `-0.4508` edge `-0.0009` maxDD `-0.4708`
- `risk_on_high->index_4h` score `-0.4415` n `37` status `ready` deltaP `5.0099` edge `-0.0055` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4415` n `37` status `ready` deltaP `5.0099` edge `-0.0055` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.5247` n `91` status `ready` deltaP `-0.3964` edge `0.0021` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.6895` n `37` status `ready` deltaP `-5.1182` edge `0.0027` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6895` n `37` status `ready` deltaP `-5.1182` edge `0.0027` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.7173` n `84` status `ready` deltaP `1.5607` edge `0.0008` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.8017` n `91` status `ready` deltaP `-7.1972` edge `-0.0088` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
