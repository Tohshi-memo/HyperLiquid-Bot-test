# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T17:37:43.051492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6648`

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

- `risk_on_high->equity_1h` score `0.6109` n `37` status `ready` deltaP `15.8966` edge `0.0147` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6109` n `37` status `ready` deltaP `15.8966` edge `0.0147` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4884` n `37` status `ready` deltaP `14.8492` edge `0.0434` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4884` n `37` status `ready` deltaP `14.8492` edge `0.0434` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.1942` n `78` status `ready` deltaP `11.8` edge `0.0538` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1048` n `37` status `ready` deltaP `5.5511` edge `0.0023` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1048` n `37` status `ready` deltaP `5.5511` edge `0.0023` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1737` n `37` status `ready` deltaP `0.0206` edge `0.004` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1737` n `37` status `ready` deltaP `0.0206` edge `0.004` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.4185` n `93` status `ready` deltaP `-1.1912` edge `-0.0015` maxDD `-0.5374`
- `risk_on_high->index_4h` score `-0.447` n `37` status `ready` deltaP `5.0099` edge `-0.0062` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.447` n `37` status `ready` deltaP `5.0099` edge `-0.0062` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.5177` n `93` status `ready` deltaP `-0.3058` edge `0.0024` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5766` n `93` status `ready` deltaP `1.6805` edge `-0.0056` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.6751` n `37` status `ready` deltaP `-4.9685` edge `0.0029` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6751` n `37` status `ready` deltaP `-4.9685` edge `0.0029` maxDD `-0.0831`
- `market_context_high->metal_1h` score `-0.781` n `93` status `ready` deltaP `-6.7993` edge `-0.0088` maxDD `-1.3465`
- `market_context_high->commodity_4h` score `-0.811` n `85` status `ready` deltaP `0.0449` edge `-0.0011` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
