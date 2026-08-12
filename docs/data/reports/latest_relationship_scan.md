# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T05:22:25.486245+00:00`
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

- `risk_on_high->commodity_4h` score `2.1142` n `32` status `ready` deltaP `14.253` edge `0.0994` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1142` n `32` status `ready` deltaP `14.253` edge `0.0994` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8671` n `32` status `ready` deltaP `9.9848` edge `0.0198` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8671` n `32` status `ready` deltaP `9.9848` edge `0.0198` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6039` n `180` status `ready` deltaP `9.032` edge `0.0223` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3879` n `32` status `ready` deltaP `11.4521` edge `0.0109` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3879` n `32` status `ready` deltaP `11.4521` edge `0.0109` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.3806` n `180` status `ready` deltaP `7.7947` edge `0.0436` maxDD `-2.1077`
- `risk_on_high->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2017` n `32` status `ready` deltaP `5.5015` edge `0.0029` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0733` n `180` status `ready` deltaP `4.8071` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.2059` n `180` status `ready` deltaP `4.3598` edge `0.005` maxDD `-0.504`
- `market_context_high->commodity_24h` score `-0.2556` n `175` status `ready` deltaP `6.6488` edge `0.0147` maxDD `-2.4263`
- `risk_on_high->index_4h` score `-0.3294` n `32` status `ready` deltaP `-0.0762` edge `0.0165` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3294` n `32` status `ready` deltaP `-0.0762` edge `0.0165` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6625` n `32` status `ready` deltaP `-3.1624` edge `-0.0095` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6625` n `32` status `ready` deltaP `-3.1624` edge `-0.0095` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.7691` n `180` status `ready` deltaP `-6.0479` edge `-0.0006` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
