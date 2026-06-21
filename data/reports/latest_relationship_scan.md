# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T19:59:02.324231+00:00`
- Price records: `672`
- Market context records: `4346`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11234`

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

- `risk_on_high->unknown_4h` score `131.1079` n `44` status `ready` deltaP `-0.3742` edge `11.11` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.1079` n `44` status `ready` deltaP `-0.3742` edge `11.11` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.5056` n `223` status `ready` deltaP `3.0478` edge `2.7631` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.7313` n `220` status `ready` deltaP `2.3531` edge `1.5049` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.0804` n `44` status `ready` deltaP `34.0078` edge `0.0347` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.0804` n `44` status `ready` deltaP `34.0078` edge `0.0347` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.6347` n `44` status `ready` deltaP `-18.1344` edge `0.5201` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.6347` n `44` status `ready` deltaP `-18.1344` edge `0.5201` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.9878` n `44` status `ready` deltaP `21.0069` edge `0.0256` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9878` n `44` status `ready` deltaP `21.0069` edge `0.0256` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6471` n `44` status `ready` deltaP `17.0871` edge `0.0899` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6471` n `44` status `ready` deltaP `17.0871` edge `0.0899` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4973` n `44` status `ready` deltaP `9.0909` edge `0.0038` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4973` n `44` status `ready` deltaP `9.0909` edge `0.0038` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4414` n `44` status `ready` deltaP `6.638` edge `0.0459` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4414` n `44` status `ready` deltaP `6.638` edge `0.0459` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.4185` n `44` status `ready` deltaP `19.2708` edge `-0.0936` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4185` n `44` status `ready` deltaP `19.2708` edge `-0.0936` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2988` n `44` status `ready` deltaP `8.5738` edge `0.0067` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2988` n `44` status `ready` deltaP `8.5738` edge `0.0067` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
