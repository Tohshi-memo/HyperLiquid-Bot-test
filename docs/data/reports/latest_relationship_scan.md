# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T01:37:23.759656+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10761`

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

- `risk_on_high->unknown_24h` score `408.6809` n `101` status `ready` deltaP `26.7361` edge `33.8785` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `408.6809` n `101` status `ready` deltaP `26.7361` edge `33.8785` maxDD `0.0`
- `market_context_high->unknown_1h` score `21.7293` n `249` status `ready` deltaP `-3.0866` edge `1.9038` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `19.916` n `101` status `ready` deltaP `33.6238` edge `1.4872` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.916` n `101` status `ready` deltaP `33.6238` edge `1.4872` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.7807` n `101` status `ready` deltaP `30.2083` edge `0.947` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.7807` n `101` status `ready` deltaP `30.2083` edge `0.947` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7826` n `190` status `ready` deltaP `23.8925` edge `0.6301` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6412` n `190` status `ready` deltaP `23.0903` edge `0.3995` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.8947` n `123` status `ready` deltaP `29.2175` edge `0.3188` maxDD `-1.1222`
- `risk_on_and_context->crypto_alt_4h` score `5.8947` n `123` status `ready` deltaP `29.2175` edge `0.3188` maxDD `-1.1222`
- `risk_on_high->equity_24h` score `5.6536` n `101` status `ready` deltaP `23.0903` edge `0.3172` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.6536` n `101` status `ready` deltaP `23.0903` edge `0.3172` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.1355` n `123` status `ready` deltaP `23.0691` edge `0.2767` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1355` n `123` status `ready` deltaP `23.0691` edge `0.2767` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7551` n `101` status `ready` deltaP `23.4186` edge `0.0777` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7551` n `101` status `ready` deltaP `23.4186` edge `0.0777` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6134` n `190` status `ready` deltaP `21.6521` edge `0.0949` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.8647` n `125` status `ready` deltaP `3.9138` edge `0.0812` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8647` n `125` status `ready` deltaP `3.9138` edge `0.0812` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
