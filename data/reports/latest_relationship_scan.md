# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T11:22:26.325516+00:00`
- Price records: `672`
- Market context records: `4202`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10050`

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

- `risk_on_high->unknown_4h` score `145.4794` n `40` status `ready` deltaP `-8.2012` edge `12.3598` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.4794` n `40` status `ready` deltaP `-8.2012` edge `12.3598` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.693` n `209` status `ready` deltaP `1.7807` edge `2.8705` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.4802` n `202` status `ready` deltaP `-2.8299` edge `1.4352` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.227` n `198` status `ready` deltaP `-12.4879` edge `1.1722` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4271` n `40` status `ready` deltaP `4.8319` edge `0.3982` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4271` n `40` status `ready` deltaP `4.8319` edge `0.3982` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.2613` n `40` status `ready` deltaP `32.4085` edge `-0.0229` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2613` n `40` status `ready` deltaP `32.4085` edge `-0.0229` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.816` n `40` status `ready` deltaP `14.5732` edge `0.0374` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.816` n `40` status `ready` deltaP `14.5732` edge `0.0374` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1813` n `40` status `ready` deltaP `9.7156` edge `-0.0107` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1813` n `40` status `ready` deltaP `9.7156` edge `-0.0107` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.1661` n `40` status `ready` deltaP `8.9634` edge `-0.0049` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1661` n `40` status `ready` deltaP `8.9634` edge `-0.0049` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0579` n `40` status `ready` deltaP `9.3293` edge `0.0043` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0579` n `40` status `ready` deltaP `9.3293` edge `0.0043` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `0.0465` n `40` status `ready` deltaP `9.1617` edge `-0.0009` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0465` n `40` status `ready` deltaP `9.1617` edge `-0.0009` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `0.0334` n `40` status `ready` deltaP `3.9521` edge `0.0009` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
