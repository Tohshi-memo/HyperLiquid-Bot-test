# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T13:52:40.697918+00:00`
- Price records: `672`
- Market context records: `4097`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10376`

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

- `risk_on_high->unknown_4h` score `144.6759` n `40` status `ready` deltaP `-8.811` edge `12.2967` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6759` n `40` status `ready` deltaP `-8.811` edge `12.2967` maxDD `-10.864`
- `market_context_high->unknown_1h` score `47.2174` n `180` status `ready` deltaP `2.2123` edge `4.0778` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0661` n `144` status `ready` deltaP `-9.2396` edge `3.5533` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.6326` n `177` status `ready` deltaP `-1.9042` edge `1.8577` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.6503` n `40` status `ready` deltaP `36.372` edge `-0.0169` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.6503` n `40` status `ready` deltaP `36.372` edge `-0.0169` maxDD `-0.0446`
- `market_context_high->equity_1h` score `0.6104` n `180` status `ready` deltaP `5.2296` edge `0.0727` maxDD `-2.2022`
- `risk_on_high->equity_1h` score `0.4364` n `40` status `ready` deltaP `11.0629` edge `0.0017` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4364` n `40` status `ready` deltaP `11.0629` edge `0.0017` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0747` n `40` status `ready` deltaP `4.7006` edge `0.0012` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0747` n `40` status `ready` deltaP `4.7006` edge `0.0012` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0145` n `40` status `ready` deltaP `10.509` edge `-0.0177` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0145` n `40` status `ready` deltaP `10.509` edge `-0.0177` maxDD `-2.3372`
- `market_context_high->equity_4h` score `-0.0832` n `177` status `ready` deltaP `11.7534` edge `0.0678` maxDD `-6.9137`
- `market_context_high->index_24h` score `-0.1827` n `144` status `ready` deltaP `13.6915` edge `-0.1065` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `-0.183` n `40` status `ready` deltaP `15.9451` edge `-0.055` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.183` n `40` status `ready` deltaP `15.9451` edge `-0.055` maxDD `-2.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
