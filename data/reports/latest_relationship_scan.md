# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T01:52:31.548331+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_major_4h` score `5.0733` n `58` status `ready` deltaP `27.6808` edge `0.27` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `5.0733` n `58` status `ready` deltaP `27.6808` edge `0.27` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.679` n `104` status `ready` deltaP `34.415` edge `0.2624` maxDD `-3.1535`
- `risk_on_high->unknown_4h` score `4.1229` n `58` status `ready` deltaP `20.8684` edge `0.2473` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `4.1229` n `58` status `ready` deltaP `20.8684` edge `0.2473` maxDD `-1.0945`
- `risk_on_high->crypto_alt_4h` score `3.5709` n `58` status `ready` deltaP `19.9275` edge `0.3639` maxDD `-1.115`
- `risk_on_and_context->crypto_alt_4h` score `3.5709` n `58` status `ready` deltaP `19.9275` edge `0.3639` maxDD `-1.115`
- `market_context_high->unknown_4h` score `3.3518` n `160` status `ready` deltaP `18.1098` edge `0.2056` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `2.6` n `58` status `ready` deltaP `22.8606` edge `0.0892` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6` n `58` status `ready` deltaP `22.8606` edge `0.0892` maxDD `-0.3281`
- `news_risk_high->unknown_1h` score `2.3877` n `42` status `ready` deltaP `-13.0097` edge `0.3214` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `2.1691` n `58` status `ready` deltaP `26.4035` edge `0.0301` maxDD `-0.0289`
- `risk_on_and_context->metal_4h` score `2.1691` n `58` status `ready` deltaP `26.4035` edge `0.0301` maxDD `-0.0289`
- `risk_on_high->unknown_1h` score `1.8014` n `66` status `ready` deltaP `3.0077` edge `0.174` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.8014` n `66` status `ready` deltaP `3.0077` edge `0.174` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.7691` n `58` status `ready` deltaP `25.042` edge `0.0114` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7691` n `58` status `ready` deltaP `25.042` edge `0.0114` maxDD `-0.1405`
- `news_risk_high->crypto_alt_24h` score `1.7387` n `40` status `ready` deltaP `15.625` edge `0.3783` maxDD `-22.3391`
- `market_context_high->unknown_1h` score `1.7135` n `168` status `ready` deltaP `9.0142` edge `0.1308` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.1908` n `66` status `ready` deltaP `17.0024` edge `0.0073` maxDD `-0.0463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
