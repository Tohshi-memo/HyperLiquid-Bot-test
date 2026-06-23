# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T09:37:29.457358+00:00`
- Price records: `672`
- Market context records: `4503`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `124.7729` n `49` status `ready` deltaP `4.6354` edge `10.5499` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.7729` n `49` status `ready` deltaP `4.6354` edge `10.5499` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `39.5899` n `205` status `ready` deltaP `3.4957` edge `3.4264` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `19.0378` n `205` status `ready` deltaP `2.7439` edge `2.0288` maxDD `-30.1818`
- `risk_on_high->equity_4h` score `5.0525` n `49` status `ready` deltaP `41.6159` edge `0.1436` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0525` n `49` status `ready` deltaP `41.6159` edge `0.1436` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.7928` n `49` status `ready` deltaP `24.1382` edge `0.2217` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.7928` n `49` status `ready` deltaP `24.1382` edge `0.2217` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.5501` n `49` status `ready` deltaP `-12.8755` edge `0.5107` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.5501` n `49` status `ready` deltaP `-12.8755` edge `0.5107` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.1183` n `49` status `ready` deltaP `11.1075` edge `0.1828` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.1183` n `49` status `ready` deltaP `11.1075` edge `0.1828` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.0259` n `49` status `ready` deltaP `15.7634` edge `0.0973` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3567` n `49` status `ready` deltaP `16.0394` edge `0.0404` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3567` n `49` status `ready` deltaP `16.0394` edge `0.0404` maxDD `-0.7415`
- `risk_on_high->index_24h` score `0.8656` n `49` status `ready` deltaP `19.657` edge `-0.0072` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.8656` n `49` status `ready` deltaP `19.657` edge `-0.0072` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6363` n `49` status `ready` deltaP `15.7043` edge `0.0074` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
