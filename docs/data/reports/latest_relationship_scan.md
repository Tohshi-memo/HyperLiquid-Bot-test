# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T22:07:34.444548+00:00`
- Price records: `672`
- Market context records: `7396`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `risk_on_high->crypto_major_4h` score `6.195` n `32` status `ready` deltaP `35.747` edge `0.2972` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.195` n `32` status `ready` deltaP `35.747` edge `0.2972` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.8943` n `32` status `ready` deltaP `15.3963` edge `0.3482` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8943` n `32` status `ready` deltaP `15.3963` edge `0.3482` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6529` n `32` status `ready` deltaP `27.2104` edge `0.2307` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6529` n `32` status `ready` deltaP `27.2104` edge `0.2307` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0663` n `32` status `ready` deltaP `18.881` edge `0.0353` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0663` n `32` status `ready` deltaP `18.881` edge `0.0353` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3964` n `32` status `ready` deltaP `5.3491` edge `0.0253` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3964` n `32` status `ready` deltaP `5.3491` edge `0.0253` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1499` n `32` status `ready` deltaP `3.7538` edge `0.0319` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1499` n `32` status `ready` deltaP `3.7538` edge `0.0319` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0706` n `32` status `ready` deltaP `-0.7485` edge `0.033` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0706` n `32` status `ready` deltaP `-0.7485` edge `0.033` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1553` n `132` status `ready` deltaP `4.3817` edge `0.0` maxDD `-0.5967`
- `risk_on_high->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5298` n `132` status `ready` deltaP `-0.9009` edge `-0.0047` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.6618` n `131` status `ready` deltaP `0.3746` edge `0.0095` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.864` n `131` status `ready` deltaP `3.4211` edge `0.1023` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
