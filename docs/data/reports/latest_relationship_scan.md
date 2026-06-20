# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T04:52:28.794539+00:00`
- Price records: `672`
- Market context records: `4174`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10140`

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

- `risk_on_high->unknown_4h` score `144.8174` n `40` status `ready` deltaP `-9.7256` edge `12.3148` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.8174` n `40` status `ready` deltaP `-9.7256` edge `12.3148` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.1999` n `202` status `ready` deltaP `0.6417` edge `3.087` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.8183` n `202` status `ready` deltaP `-4.3543` edge `1.3902` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.8957` n `198` status `ready` deltaP `-13.2338` edge `1.2329` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9751` n `40` status `ready` deltaP `31.9512` edge `-0.0437` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9751` n `40` status `ready` deltaP `31.9512` edge `-0.0437` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.8047` n `40` status `ready` deltaP `2.6167` edge `0.3611` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.8047` n `40` status `ready` deltaP `2.6167` edge `0.3611` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.7708` n `40` status `ready` deltaP `14.878` edge `0.0316` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7708` n `40` status `ready` deltaP `14.878` edge `0.0316` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1237` n `40` status `ready` deltaP `9.5732` edge `-0.0144` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1237` n `40` status `ready` deltaP `9.5732` edge `-0.0144` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1023` n `40` status `ready` deltaP `10.2439` edge `0.0039` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1023` n `40` status `ready` deltaP `10.2439` edge `0.0039` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `0.0985` n `40` status `ready` deltaP `9.7156` edge `-0.0176` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0985` n `40` status `ready` deltaP `9.7156` edge `-0.0176` maxDD `-0.7834`
- `risk_on_high->fx_1h` score `0.091` n `40` status `ready` deltaP `5.0` edge `0.0013` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.091` n `40` status `ready` deltaP `5.0` edge `0.0013` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0449` n `40` status `ready` deltaP `9.3114` edge `-0.0021` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
