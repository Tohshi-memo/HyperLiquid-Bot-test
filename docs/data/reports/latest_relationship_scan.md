# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T22:22:30.665459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10273`

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

- `risk_on_high->unknown_24h` score `4086.9486` n `116` status `ready` deltaP `21.0069` edge `340.439` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4086.9486` n `116` status `ready` deltaP `21.0069` edge `340.439` maxDD `0.0`
- `market_context_high->unknown_24h` score `1909.432` n `233` status `ready` deltaP `20.1485` edge `158.9902` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.9481` n `116` status `ready` deltaP `26.2392` edge `0.6659` maxDD `-0.2789`
- `risk_on_and_context->crypto_alt_24h` score `9.9481` n `116` status `ready` deltaP `26.2392` edge `0.6659` maxDD `-0.2789`
- `market_context_high->crypto_alt_24h` score `5.7887` n `233` status `ready` deltaP `21.1038` edge `0.3992` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7824` n `117` status `ready` deltaP `30.635` edge `0.3148` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7824` n `117` status `ready` deltaP `30.635` edge `0.3148` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.7712` n `116` status `ready` deltaP `21.7194` edge `0.9795` maxDD `-23.0855`
- `risk_on_and_context->crypto_major_24h` score `5.7712` n `116` status `ready` deltaP `21.7194` edge `0.9795` maxDD `-23.0855`
- `risk_on_high->crypto_major_4h` score `4.8337` n `117` status `ready` deltaP `25.6762` edge `0.3175` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8337` n `117` status `ready` deltaP `25.6762` edge `0.3175` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.8261` n `233` status `ready` deltaP `13.0208` edge `0.1487` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.0269` n `116` status `ready` deltaP `13.0208` edge `0.0821` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0269` n `116` status `ready` deltaP `13.0208` edge `0.0821` maxDD `0.0`
- `risk_on_high->index_24h` score `1.6071` n `116` status `ready` deltaP `14.9485` edge `0.0385` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6071` n `116` status `ready` deltaP `14.9485` edge `0.0385` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9645` n `117` status `ready` deltaP `4.3964` edge `0.0863` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9645` n `117` status `ready` deltaP `4.3964` edge `0.0863` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.8825` n `233` status `ready` deltaP `9.8094` edge `0.0475` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
