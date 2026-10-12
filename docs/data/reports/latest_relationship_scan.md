# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T12:07:26.900847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `27.5169` n `42` status `ready` deltaP `32.5893` edge `2.1495` maxDD `-3.8951`
- `market_context_high->crypto_major_24h` score `26.5381` n `42` status `ready` deltaP `44.2212` edge `1.9747` maxDD `-2.6398`
- `risk_on_high->crypto_alt_4h` score `3.8844` n `48` status `ready` deltaP `18.1911` edge `0.2472` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8844` n `48` status `ready` deltaP `18.1911` edge `0.2472` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4792` n `48` status `ready` deltaP `32.6728` edge `0.3135` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4792` n `48` status `ready` deltaP `32.6728` edge `0.3135` maxDD `-4.1548`
- `market_context_high->metal_24h` score `2.9778` n `42` status `ready` deltaP `27.9018` edge `0.0912` maxDD `-0.6586`
- `market_context_high->crypto_major_4h` score `2.5283` n `105` status `ready` deltaP `16.3632` edge `0.2794` maxDD `-8.5569`
- `market_context_high->crypto_alt_4h` score `2.1353` n `105` status `ready` deltaP `10.0363` edge `0.2895` maxDD `-11.2774`
- `market_context_high->crypto_alt_1h` score `1.403` n `105` status `ready` deltaP `11.2646` edge `0.1369` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8484` n `48` status `ready` deltaP `5.7884` edge `0.0918` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8484` n `48` status `ready` deltaP `5.7884` edge `0.0918` maxDD `-2.4421`
- `market_context_high->index_24h` score `0.7278` n `42` status `ready` deltaP `14.7818` edge `0.0755` maxDD `-1.1257`
- `market_context_high->crypto_major_1h` score `0.54` n `105` status `ready` deltaP `3.9321` edge `0.0951` maxDD `-3.4384`
- `market_context_high->unknown_4h` score `0.4233` n `105` status `ready` deltaP `-4.6037` edge `0.1306` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `0.3454` n `48` status `ready` deltaP `4.7655` edge `0.0778` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3454` n `48` status `ready` deltaP `4.7655` edge `0.0778` maxDD `-3.2233`
- `market_context_high->equity_24h` score `0.0971` n `42` status `ready` deltaP `-8.9038` edge `0.2952` maxDD `-12.8715`
- `market_context_high->index_1h` score `-0.0096` n `105` status `ready` deltaP `4.3399` edge `0.0029` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.0768` n `105` status `ready` deltaP `6.7479` edge `0.0047` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
