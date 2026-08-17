# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T14:39:54.308089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11819`

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

- `risk_on_high->unknown_1h` score `7.1152` n `35` status `ready` deltaP `1.7408` edge `0.6208` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.1152` n `35` status `ready` deltaP `1.7408` edge `0.6208` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.4502` n `89` status `ready` deltaP `7.6115` edge `0.2858` maxDD `-5.2554`
- `market_context_high->index_24h` score `1.2403` n `89` status `ready` deltaP `18.9236` edge `-0.0228` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2303` n `35` status `ready` deltaP `16.8946` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2303` n `35` status `ready` deltaP `16.8946` edge `0.004` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0516` n `35` status `ready` deltaP `11.9589` edge `0.0385` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0516` n `35` status `ready` deltaP `11.9589` edge `0.0385` maxDD `-1.1144`
- `market_context_high->equity_24h` score `0.8565` n `89` status `ready` deltaP `14.3375` edge `-0.0138` maxDD `-0.1657`
- `risk_on_high->equity_1h` score `0.8533` n `35` status `ready` deltaP `13.2079` edge `0.0374` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8533` n `35` status `ready` deltaP `13.2079` edge `0.0374` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7914` n `35` status `ready` deltaP `13.6442` edge `0.0125` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7914` n `35` status `ready` deltaP `13.6442` edge `0.0125` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.4284` n `136` status `ready` deltaP `13.0291` edge `0.0531` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4235` n `35` status `ready` deltaP `2.6089` edge `0.0808` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4235` n `35` status `ready` deltaP `2.6089` edge `0.0808` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.3923` n `89` status `ready` deltaP `18.5588` edge `0.1099` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0796` n `35` status `ready` deltaP `4.5851` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0796` n `35` status `ready` deltaP `4.5851` edge `0.0024` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `0.0265` n `35` status `ready` deltaP `1.5418` edge `0.0643` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
