# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T21:37:00.475170+00:00`
- Price records: `672`
- Market context records: `7394`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14654`

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

- `risk_on_high->crypto_major_4h` score `6.1406` n `32` status `ready` deltaP `35.4421` edge `0.2947` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1406` n `32` status `ready` deltaP `35.4421` edge `0.2947` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.8786` n `32` status `ready` deltaP `15.2439` edge `0.3479` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8786` n `32` status `ready` deltaP `15.2439` edge `0.3479` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6069` n `32` status `ready` deltaP `26.9055` edge `0.2289` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6069` n `32` status `ready` deltaP `26.9055` edge `0.2289` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0757` n `32` status `ready` deltaP `19.0307` edge `0.0355` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0757` n `32` status `ready` deltaP `19.0307` edge `0.0355` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.4085` n `32` status `ready` deltaP `5.4992` edge `0.0253` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4085` n `32` status `ready` deltaP `5.4992` edge `0.0253` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1515` n `32` status `ready` deltaP `3.7538` edge `0.0321` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1515` n `32` status `ready` deltaP `3.7538` edge `0.0321` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0644` n `32` status `ready` deltaP `-0.7485` edge `0.0338` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0644` n `32` status `ready` deltaP `-0.7485` edge `0.0338` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1606` n `32` status `ready` deltaP `-0.3049` edge `0.071` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1606` n `32` status `ready` deltaP `-0.3049` edge `0.071` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1717` n `132` status `ready` deltaP `4.0814` edge `-0.0001` maxDD `-0.5967`
- `market_context_high->commodity_1h` score `-0.522` n `132` status `ready` deltaP `-0.7508` edge `-0.0047` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7106` n `129` status `ready` deltaP `-0.3236` edge `0.0079` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.8718` n `129` status `ready` deltaP `3.1799` edge `0.1029` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
