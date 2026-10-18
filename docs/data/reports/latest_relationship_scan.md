# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T22:52:27.342483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8526`

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

- `market_context_high->commodity_24h` score `1.9537` n `100` status `ready` deltaP `16.4783` edge `0.1381` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8295` n `100` status `ready` deltaP `17.3841` edge `0.4591` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `1.1805` n `67` status `ready` deltaP `16.5931` edge `0.2888` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.1805` n `67` status `ready` deltaP `16.5931` edge `0.2888` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0324` n `67` status `ready` deltaP `17.0902` edge `0.0982` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0324` n `67` status `ready` deltaP `17.0902` edge `0.0982` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.5794` n `100` status `ready` deltaP `6.8503` edge `0.1175` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1148` n `67` status `ready` deltaP `7.6532` edge `0.0021` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1148` n `67` status `ready` deltaP `7.6532` edge `0.0021` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.3612` n `67` status `ready` deltaP `-0.8965` edge `-0.0031` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.3612` n `67` status `ready` deltaP `-0.8965` edge `-0.0031` maxDD `-0.3121`
- `market_context_high->index_1h` score `-0.4458` n `100` status `ready` deltaP `2.9069` edge `-0.0017` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.4976` n `100` status `ready` deltaP `0.2395` edge `0.0846` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.5487` n `67` status `ready` deltaP `0.5966` edge `0.0176` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.5487` n `67` status `ready` deltaP `0.5966` edge `0.0176` maxDD `-4.6876`
- `market_context_high->fx_1h` score `-0.6411` n `100` status `ready` deltaP `-4.1502` edge `-0.0024` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.7461` n `67` status `ready` deltaP `8.8723` edge `0.0083` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.7461` n `67` status `ready` deltaP `8.8723` edge `0.0083` maxDD `-5.3696`
- `market_context_high->fx_4h` score `-0.7951` n `100` status `ready` deltaP `-5.6361` edge `-0.0013` maxDD `-0.7115`
- `market_context_high->metal_4h` score `-0.8232` n `100` status `ready` deltaP `-1.8354` edge `0.0404` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
