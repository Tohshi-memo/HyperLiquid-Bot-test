# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T05:07:32.142494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11872`

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

- `risk_on_high->commodity_4h` score `2.1276` n `32` status `ready` deltaP `14.4055` edge `0.0995` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1276` n `32` status `ready` deltaP `14.4055` edge `0.0995` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8817` n `32` status `ready` deltaP `10.1372` edge `0.02` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8817` n `32` status `ready` deltaP `10.1372` edge `0.02` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6039` n `180` status `ready` deltaP `9.032` edge `0.0223` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.394` n `180` status `ready` deltaP `7.9472` edge `0.0437` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3794` n `32` status `ready` deltaP `11.3024` edge `0.0108` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3794` n `32` status `ready` deltaP `11.3024` edge `0.0108` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0733` n `180` status `ready` deltaP `4.8071` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1964` n `180` status `ready` deltaP `4.5122` edge `0.0052` maxDD `-0.504`
- `market_context_high->commodity_24h` score `-0.2346` n `174` status `ready` deltaP `6.7469` edge `0.0158` maxDD `-2.4263`
- `risk_on_high->index_4h` score `-0.3294` n `32` status `ready` deltaP `-0.0762` edge `0.0165` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3294` n `32` status `ready` deltaP `-0.0762` edge `0.0165` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6757` n `32` status `ready` deltaP `-3.3121` edge `-0.0102` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6757` n `32` status `ready` deltaP `-3.3121` edge `-0.0102` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.7777` n `180` status `ready` deltaP `-6.1976` edge `-0.0007` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
