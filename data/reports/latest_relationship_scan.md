# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T04:52:25.899243+00:00`
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

- `risk_on_high->commodity_4h` score `2.1422` n `32` status `ready` deltaP `14.5579` edge `0.0997` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1422` n `32` status `ready` deltaP `14.5579` edge `0.0997` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0107` n `32` status `ready` deltaP `11.1153` edge `0.0334` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8963` n `32` status `ready` deltaP `10.2896` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8963` n `32` status `ready` deltaP `10.2896` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6039` n `180` status `ready` deltaP `9.032` edge `0.0223` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.4086` n `180` status `ready` deltaP `8.0996` edge `0.0439` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3708` n `32` status `ready` deltaP `11.1527` edge `0.0107` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3708` n `32` status `ready` deltaP `11.1527` edge `0.0107` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1897` n `32` status `ready` deltaP `5.3518` edge `0.0029` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1897` n `32` status `ready` deltaP `5.3518` edge `0.0029` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0811` n `180` status `ready` deltaP `4.6574` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.187` n `180` status `ready` deltaP `4.6646` edge `0.0054` maxDD `-0.504`
- `market_context_high->commodity_24h` score `-0.2136` n `173` status `ready` deltaP `6.8441` edge `0.0169` maxDD `-2.4263`
- `risk_on_high->index_4h` score `-0.3286` n `32` status `ready` deltaP `-0.0762` edge `0.0166` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3286` n `32` status `ready` deltaP `-0.0762` edge `0.0166` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6874` n `32` status `ready` deltaP `-3.4618` edge `-0.0107` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6874` n `32` status `ready` deltaP `-3.4618` edge `-0.0107` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.7862` n `180` status `ready` deltaP `-6.3473` edge `-0.0008` maxDD `-0.948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
