# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T10:52:30.858326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `1.0629` n `120` status `ready` deltaP `12.5711` edge `0.0894` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.4823` n `120` status `ready` deltaP `7.9491` edge `0.0288` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4287` n `113` status `ready` deltaP `19.175` edge `0.0477` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.2726` n `113` status `ready` deltaP `0.8628` edge `0.1338` maxDD `-2.6802`
- `market_context_high->fx_1h` score `0.1301` n `120` status `ready` deltaP `8.0988` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1807` n `120` status `ready` deltaP `8.6585` edge `0.0051` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6557` n `120` status `ready` deltaP `-3.5728` edge `-0.0108` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8339` n `120` status `ready` deltaP `-3.5928` edge `-0.0119` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9832` n `120` status `ready` deltaP `-2.5249` edge `-0.0117` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2563` n `120` status `ready` deltaP `4.2465` edge `-0.0329` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5085` n `120` status `ready` deltaP `-5.8435` edge `-0.029` maxDD `-4.7021`
- `market_context_high->index_24h` score `-1.8388` n `113` status `ready` deltaP `-0.8923` edge `0.0722` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.8693` n `120` status `ready` deltaP `-2.8659` edge `-0.0132` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0955` n `120` status `ready` deltaP `0.8943` edge `-0.0416` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.7029` n `120` status `ready` deltaP `-6.7515` edge `-0.0429` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.6529` n `113` status `ready` deltaP `-9.8556` edge `-0.0944` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9354` n `120` status `ready` deltaP `0.4979` edge `-0.2354` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-5.9925` n `113` status `ready` deltaP `11.661` edge `0.0305` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5944` n `120` status `ready` deltaP `-7.2561` edge `-0.1633` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.0521` n `120` status `ready` deltaP `1.9212` edge `-0.6391` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
