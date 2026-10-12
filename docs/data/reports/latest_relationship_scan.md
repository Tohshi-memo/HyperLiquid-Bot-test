# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T00:07:29.066550+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9204`

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

- `market_context_high->unknown_24h` score `1458.2049` n `40` status `ready` deltaP `-22.5694` edge `121.7039` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `41.6035` n `105` status `ready` deltaP `-7.8034` edge `3.5812` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8032` n `40` status `ready` deltaP `27.6736` edge `0.592` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4264` n `40` status `ready` deltaP `52.4306` edge `0.186` maxDD `0.0`
- `market_context_high->fx_24h` score `2.9561` n `40` status `ready` deltaP `33.6458` edge `0.035` maxDD `-0.0374`
- `market_context_high->unknown_1h` score `2.5796` n `117` status `ready` deltaP `-2.6114` edge `0.266` maxDD `-1.0231`
- `risk_on_high->crypto_alt_1h` score `2.4419` n `38` status `ready` deltaP `16.1125` edge `0.1516` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.4419` n `38` status `ready` deltaP `16.1125` edge `0.1516` maxDD `-2.4421`
- `market_context_high->crypto_major_24h` score `1.3372` n `40` status `ready` deltaP `-21.1111` edge `0.567` maxDD `-17.8526`
- `risk_on_high->crypto_major_1h` score `1.2058` n `38` status `ready` deltaP `10.5263` edge `0.0956` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.2058` n `38` status `ready` deltaP `10.5263` edge `0.0956` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.0617` n `38` status `ready` deltaP `13.6937` edge `0.0211` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.0617` n `38` status `ready` deltaP `13.6937` edge `0.0211` maxDD `-0.2466`
- `risk_on_high->commodity_1h` score `0.4328` n `38` status `ready` deltaP `15.9628` edge `-0.0182` maxDD `-1.285`
- `risk_on_and_context->commodity_1h` score `0.4328` n `38` status `ready` deltaP `15.9628` edge `-0.0182` maxDD `-1.285`
- `market_context_high->commodity_4h` score `0.3198` n `105` status `ready` deltaP `10.8725` edge `0.0075` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.2876` n `117` status `ready` deltaP `6.5984` edge `0.0963` maxDD `-4.9401`
- `risk_on_high->equity_1h` score `0.2422` n `38` status `ready` deltaP `1.757` edge `0.033` maxDD `-0.296`
- `risk_on_and_context->equity_1h` score `0.2422` n `38` status `ready` deltaP `1.757` edge `0.033` maxDD `-0.296`
- `market_context_high->metal_4h` score `0.0135` n `105` status `ready` deltaP `7.9805` edge `0.0202` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
