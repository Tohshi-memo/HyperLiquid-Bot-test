# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T06:22:29.815645+00:00`
- Price records: `672`
- Market context records: `4490`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11169`

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

- `risk_on_high->unknown_4h` score `124.2417` n `49` status `ready` deltaP `4.0256` edge `10.5097` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.2417` n `49` status `ready` deltaP `4.0256` edge `10.5097` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `35.436` n `218` status `ready` deltaP `3.2921` edge `3.0816` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.4535` n `218` status `ready` deltaP `2.9397` edge `1.898` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.5485` n `49` status `ready` deltaP `39.7866` edge `0.1138` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.5485` n `49` status `ready` deltaP `39.7866` edge `0.1138` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.8843` n `49` status `ready` deltaP `22.1565` edge `0.1592` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.8843` n `49` status `ready` deltaP `22.1565` edge `0.1592` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.1506` n `49` status `ready` deltaP `13.1909` edge `0.1716` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.1506` n `49` status `ready` deltaP `13.1909` edge `0.1716` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `2.1309` n `49` status `ready` deltaP `-15.1325` edge `0.472` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.1309` n `49` status `ready` deltaP `-15.1325` edge `0.472` maxDD `-4.834`
- `risk_on_high->metal_4h` score `1.75` n `49` status `ready` deltaP `13.9341` edge `0.0865` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.75` n `49` status `ready` deltaP `13.9341` edge `0.0865` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.328` n `49` status `ready` deltaP `15.8897` edge `0.039` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.328` n `49` status `ready` deltaP `15.8897` edge `0.039` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6205` n `49` status `ready` deltaP `15.5519` edge `0.0071` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6205` n `49` status `ready` deltaP `15.5519` edge `0.0071` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.3971` n `49` status `ready` deltaP `17.4001` edge `-0.0312` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.3971` n `49` status `ready` deltaP `17.4001` edge `-0.0312` maxDD `-2.4702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
